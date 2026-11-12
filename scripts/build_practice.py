"""Build the practice pages in practice/ from practice/shared and practice/src.

Each page is one self-contained HTML file (theme, engine, and page code inlined).
Re-run after editing anything under practice/shared or practice/src.
Week 2 also needs scripts/week02_toy_data.py (the toy table the page and the
notebook both use).
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "practice")
sys.path.insert(0, HERE)

PAGES = {
    "week01": "week01_cactus_code_garden.html",
    "week02": "week02_silent_changes.html",
    "week03": "week03_planted_effect_lab.html",
}


def read(*parts):
    path = os.path.join(ROOT, *parts)
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read().strip()


def build(name, out_name):
    page_js = read("src", name, "page.js")
    if not page_js:
        return None
    if "/*__TOY_JSON__*/" in page_js:
        import week02_toy_data
        page_js = page_js.replace("/*__TOY_JSON__*/", json.dumps(week02_toy_data.as_records(), ensure_ascii=False))
    css = read("shared", "theme.css") + "\n" + read("src", name, "page.css")
    html = (
        read("src", name, "head.html") + "\n<style>\n" + css + "\n</style>\n"
        + read("src", name, "body.html") + "\n<script>\n" + read("shared", "engine.js") + "\n" + page_js + "\n</script>\n"
    )
    out = os.path.join(ROOT, out_name)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    return out


if __name__ == "__main__":
    for name, out_name in PAGES.items():
        out = build(name, out_name)
        print("wrote" if out else "skipped (no src)", out_name)
