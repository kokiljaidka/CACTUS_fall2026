"""Build the lecture slides into viewable web pages and PDFs.

Sources: slides/src/weekNN/deck.json (slide order and title) and
slides/src/weekNN/slides/<id>.html (one <section> per slide, 1920x1080).
These are copies of the decks kept as Artifacts; speaker notes (<aside>) stay in
the sources and are removed from the published pages.

Outputs (committed, copied into the site by build_site.py):
    slides/<name>.html   self-contained viewer (arrow keys, swipe, #3 jumps to slide 3)
    slides/<name>.pdf    one slide per page (needs Microsoft Edge; skipped if absent)
    slides/<name>_presenter.html   viewer with the speaker notes beside the slide (N toggles)
    slides/<name>_handout.pdf      slides with notes, A4, for the facilitator team

Usage: python scripts/build_slides.py [--no-pdf]
"""
import html
import json
import os
import re
import subprocess
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SLIDES = os.path.join(ROOT, "slides")

DECKS = {
    "week01": "week01_define_your_problem",
    "week02": "week02_clean_it_chart_it",
}

FONTS = ("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700"
         "&family=Figtree:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap")

CSS = """
*{box-sizing:border-box}
html,body{margin:0;height:100%;background:#0e1814;color:#e4efe6;font-family:'Figtree',Arial,sans-serif}
#view{position:fixed;inset:0 0 56px 0;overflow:hidden}
.s{position:absolute;left:50%;top:50%;width:1920px;height:1080px;transform:translate(-50%,-50%) scale(var(--k,.5));transform-origin:center;display:none;overflow:hidden;background:#fff}
.s.on{display:block}
.s section{width:1920px;height:1080px;position:relative;overflow:hidden}
.s section *{margin:0}
.s h1{font-size:96px;font-weight:600;line-height:1.1}
.s h2{font-size:64px;font-weight:600;line-height:1.15}
.s h3{font-size:44px;font-weight:600;line-height:1.2}
.s p{font-size:32px;line-height:1.4}
.s ul,.s ol{padding-left:1.2em}
.s table{border-collapse:collapse;width:100%}
.s th,.s td{padding:.35em .6em;text-align:left;border-bottom:1px solid #c6d1c4;vertical-align:top}
.s th{font-weight:600}
.s aside{display:none}
#bar{position:fixed;left:0;right:0;bottom:0;height:56px;display:flex;align-items:center;justify-content:center;gap:16px;background:#14241c;border-top:1px solid #2b4036;font-size:16px}
#bar button{font:inherit;color:#e4efe6;background:#23382e;border:1px solid #2b4036;border-radius:8px;padding:6px 16px;cursor:pointer}
#bar button:disabled{opacity:.4;cursor:default}
#bar a{color:#9fd0b0}
#ct{min-width:70px;text-align:center;font-variant-numeric:tabular-nums}
@page{size:1920px 1080px;margin:0}
@media print{
 html,body{background:#fff;height:auto}
 #view{position:static;overflow:visible}
 #bar{display:none}
 .s{display:block!important;position:relative;left:0;top:0;transform:none;break-after:page;page-break-after:always}
}
"""

JS = r"""
(function(){
var slides=[].slice.call(document.querySelectorAll('.s')),i=0,view=document.getElementById('view');
var ct=document.getElementById('ct'),pv=document.getElementById('pv'),nx=document.getElementById('nx');
function fit(){var k=Math.min(view.clientWidth/1920,view.clientHeight/1080);slides.forEach(function(s){s.style.setProperty('--k',k)});}
function show(n){i=Math.max(0,Math.min(slides.length-1,n));slides.forEach(function(s,j){s.classList.toggle('on',j===i)});
 ct.textContent=(i+1)+' / '+slides.length;pv.disabled=i===0;nx.disabled=i===slides.length-1;
 try{history.replaceState(null,'','#'+(i+1))}catch(e){}}
pv.onclick=function(){show(i-1)};nx.onclick=function(){show(i+1)};
document.addEventListener('keydown',function(e){
 if(e.key==='ArrowRight'||e.key==='PageDown'||e.key===' '){e.preventDefault();show(i+1)}
 else if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();show(i-1)}
 else if(e.key==='Home')show(0);else if(e.key==='End')show(slides.length-1)});
var x0=null;view.addEventListener('touchstart',function(e){x0=e.touches[0].clientX},{passive:true});
view.addEventListener('touchend',function(e){if(x0===null)return;var d=e.changedTouches[0].clientX-x0;if(Math.abs(d)>50)show(i+(d<0?1:-1));x0=null});
view.addEventListener('click',function(e){if(e.target.closest('a'))return;show(i+(e.clientX>view.clientWidth/2?1:-1))});
window.addEventListener('resize',fit);fit();
var m=/^#(\d+)$/.exec(location.hash);show(m?parseInt(m[1],10)-1:0);
})();
"""


KNOWN = ("TIME", "SAY", "DO", "IF", "WATCH", "NEXT", "NOTE", "SIGN-OFF", "AT", "CLOSE")

PRESENTER_CSS = """
#view{right:360px}
#notes{position:fixed;top:0;right:0;bottom:56px;width:360px;overflow:auto;padding:16px 18px;background:#14241c;border-left:1px solid #2b4036;font-size:15px;line-height:1.5}
#notes p{margin:0 0 10px}
#notes b{color:#e8b13a}
body.nonotes #notes{display:none}
body.nonotes #view{right:0}
@media (max-width:900px){#notes{display:none}#view{right:0}}
@media print{#notes{display:none}}
"""

HANDOUT_CSS = """
@page{size:A4;margin:12mm}
html,body{background:#fff;color:#14241c;height:auto}
h1{font:600 18pt 'Bricolage Grotesque',Georgia,serif;margin:0 0 4mm}
.item{display:flex;gap:16px;align-items:flex-start;break-inside:avoid;page-break-inside:avoid;padding:0 0 12px;margin:0 0 12px;border-bottom:1px solid #c6d1c4}
.thumb{width:300px;height:169px;flex:none;position:relative;overflow:hidden;border:1px solid #c6d1c4}
.thumb .s{display:block!important;position:static!important;transform:none!important;zoom:.15625}
.n{flex:1;font-size:10.5pt;line-height:1.45;min-width:0}
.n p{margin:0 0 6px}
.n b{color:#237a4b}
.num{font-weight:700;color:#237a4b;margin:0 0 4px}
"""


def notes_html(text):
    out = []
    for line in text.split("\n"):
        if not line.strip():
            continue
        head, sep, rest = line.partition(": ")
        if sep and head.split()[0].rstrip(":") in KNOWN:
            out.append("<p><b>" + html.escape(head) + "</b> " + html.escape(rest) + "</p>")
        else:
            out.append("<p>" + html.escape(line) + "</p>")
    return "".join(out)


def build(key, name, pdf):
    src = os.path.join(SLIDES, "src", key)
    deck = json.load(open(os.path.join(src, "deck.json"), encoding="utf-8"))
    notes_path = os.path.join(src, "notes.json")
    notes = json.load(open(notes_path, encoding="utf-8")) if os.path.exists(notes_path) else {}
    parts, own = [], []
    for sid in deck["order"]:
        text = open(os.path.join(src, "slides", sid + ".html"), encoding="utf-8").read()
        m = re.search(r"<aside>(.*?)</aside>", text, flags=re.S)
        own.append(html.unescape(m.group(1)).strip() if m else "")
        text = re.sub(r"<aside>.*?</aside>", "", text, flags=re.S)
        parts.append('<div class="s">' + text.strip() + "</div>")
    note_texts = [notes.get(sid) or own[k] for k, sid in enumerate(deck["order"])]
    title = html.escape(deck["title"])
    head = (
        "<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
        f"<title>{{t}}</title><link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">"
        f"<link rel=\"stylesheet\" href=\"{FONTS}\"><style>{{css}}</style></head><body>"
    )
    bar = ("<div id=\"bar\"><button id=\"pv\" type=\"button\">Previous</button><span id=\"ct\"></span>"
           "<button id=\"nx\" type=\"button\">Next</button>{extra}</div>")

    # 1. student viewer (no notes)
    page = (head.format(t=title, css=CSS) + f"<div id=\"view\">{''.join(parts)}</div>"
            + bar.format(extra=f"<a href=\"{name}.pdf\">PDF</a>") + f"<script>{JS}</script></body></html>\n")
    write(os.path.join(SLIDES, name + ".html"), page)

    # 2. presenter view (with notes, N toggles the panel)
    hook = ("window.__onshow=function(i){document.getElementById('notes').innerHTML=NOTES[i]||''};"
            "document.addEventListener('keydown',function(e){if(e.key==='n'||e.key==='N')document.body.classList.toggle('nonotes')});")
    pjs = JS.replace("ct.textContent=", "if(window.__onshow)window.__onshow(i);ct.textContent=", 1)
    notes_js = "var NOTES=" + json.dumps([notes_html(t) for t in note_texts]).replace("</", "<" + chr(92) + "/") + ";" + hook
    ppage = (head.format(t=title + " (presenter)", css=CSS + PRESENTER_CSS)
             + f"<div id=\"view\">{''.join(parts)}</div><div id=\"notes\"></div>"
             + bar.format(extra="<span>Press N to hide or show notes</span>")
             + f"<script>{notes_js}{pjs}</script></body></html>\n")
    write(os.path.join(SLIDES, name + "_presenter.html"), ppage)

    # 3. handout (slides with notes, A4), printed to PDF
    items = []
    for k, t in enumerate(note_texts):
        items.append(f"<div class=\"item\"><div class=\"thumb\">{parts[k]}</div>"
                     f"<div class=\"n\"><p class=\"num\">Slide {k + 1}</p>{notes_html(t)}</div></div>")
    base = CSS.split("@page")[0]
    hpage = (head.format(t=title + " (handout)", css=base + HANDOUT_CSS)
             + f"<h1>{title}</h1>{''.join(items)}</body></html>\n")
    print(f"built {name} ({len(deck['order'])} slides)")
    if pdf:
        tmp = os.path.join(SLIDES, "_handout_tmp.html")
        write(tmp, hpage, quiet=True)
        make_pdf(os.path.join(SLIDES, name + ".html"), os.path.join(SLIDES, name + ".pdf"))
        make_pdf(tmp, os.path.join(SLIDES, name + "_handout.pdf"))
        os.remove(tmp)


def write(path, text, quiet=False):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    if not quiet:
        print("wrote", os.path.relpath(path, ROOT))


def make_pdf(html_path, pdf_path):
    edge = next((p for p in (r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                             r"C:\Program Files\Microsoft\Edge\Application\msedge.exe") if os.path.exists(p)), None)
    if not edge:
        print("  (no Microsoft Edge found, skipped PDF)")
        return
    url = "file:///" + html_path.replace("\\", "/")
    subprocess.run([edge, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000",
                    f"--print-to-pdf={pdf_path}", url], check=False, capture_output=True)
    print("  wrote", os.path.relpath(pdf_path, ROOT) if os.path.exists(pdf_path) else "(PDF failed)")


if __name__ == "__main__":
    pdf = "--no-pdf" not in sys.argv
    for key, name in DECKS.items():
        build(key, name, pdf)
