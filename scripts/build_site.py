"""Assemble the student-facing site into docs/ (then run `mkdocs build`).

Single source of truth: the Markdown files in README.md, schedule/, project/ and
data/. Anything between
    <!-- facilitator:start -->  and  <!-- facilitator:end -->
is removed from the site. Links to files that are not published become plain
text. Practice pages and the small shared datasets are copied in as downloads.

Release a week by adding its page to NAVIGABLE below (and to nav in mkdocs.yml).
docs/ and site/ are generated and not committed.
"""
import os
import posixpath
import re
import shutil

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
DOCS = os.path.join(ROOT, "docs")
REPO = "kokiljaidka/CACTUS_fall2026"
COLAB = f"https://colab.research.google.com/github/{REPO}/blob/main/notebooks/"

FAC = re.compile(r"<!-- facilitator:start -->.*?<!-- facilitator:end -->\n?", re.S)
LINK = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)")

# source file -> page on the site
PAGES = {
    "README.md": "index.md",
    "project/designing_your_project.md": "project.md",
    "data/README.md": "data.md",
    "schedule/week01.md": "weeks/week01.md",
    "schedule/week02.md": "weeks/week02.md",
}

# per-week links added to each week page
WEEKS = {
    "weeks/week01.md": {
        "notebook": "week01_first_api_calls.ipynb",
        "slides": ("Lecture slides (Session 1)", "week01_define_your_problem"),
        "practice": ("Cactus Code Garden (puzzle page)", "week01_cactus_code_garden.html"),
        "downloads": [("Saved searches (serp_cache.zip)", "data/week01/serp_cache.zip")],
    },
    "weeks/week02.md": {
        "notebook": "week02_clean_and_chart.ipynb",
        "slides": ("Lecture slides (learning session)", "week02_clean_it_chart_it"),
        "practice": ("Silent Changes (practice page)", "week02_silent_changes.html"),
        "downloads": [
            ("Starbucks comments (starbucks_sea_comments.csv)", "data/starbucks_sea_comments.csv"),
            ("Toy café table (week02_toy_cafe.csv)", "data/week02_toy_cafe.csv"),
        ],
    },
}
COPY_FILES = [  # published as downloads
    "data/starbucks_sea_comments.csv", "data/lululemon_instagram.csv", "data/week02_toy_cafe.csv",
    "data/week01/serp_cache.zip",
]


def rewrite(text, src, dest):
    def fix(m):
        label, target = m.group(1), m.group(2)
        if re.match(r"^(https?:|mailto:|#)", target):
            return m.group(0)
        path, _, frag = target.partition("#")
        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(src), path))
        if resolved in PAGES:
            rel = posixpath.relpath(PAGES[resolved], posixpath.dirname(dest))
            return f"[{label}]({rel}{'#' + frag if frag else ''})"
        if resolved in COPY_FILES and os.path.exists(os.path.join(ROOT, resolved)):
            rel = posixpath.relpath("downloads/" + posixpath.basename(resolved), posixpath.dirname(dest))
            return f"[{label}]({rel})"
        return label  # not published: keep the words, drop the link
    return LINK.sub(fix, text)


NL, TAB = chr(10), chr(9)
LIST_ITEM = re.compile(r"^\s*([-*]|\d+\.)\s")


def blank_before_lists(text):
    """Python-Markdown needs a blank line before a list; GitHub does not."""
    out, prev = [], ""
    for line in text.split(NL):
        if LIST_ITEM.match(line) and prev.strip() and not LIST_ITEM.match(prev) and not prev.startswith((" ", TAB)):
            out.append("")
        out.append(line)
        prev = line
    return NL.join(out)


def write(dest, text):
    out = os.path.join(DOCS, dest)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def links_block(dest, cfg):
    lines = ["## Your links", ""]
    lines.append(f"[Open the notebook in Colab]({COLAB}{cfg['notebook']}){{ .md-button .md-button--primary target=_blank }}")
    title, fname = cfg["practice"]
    lines.append(f"[{title}]({posixpath.relpath('practice/' + fname, posixpath.dirname(dest))}){{ .md-button target=_blank }}")
    if cfg.get("slides") and os.path.exists(os.path.join(ROOT, "slides", cfg["slides"][1] + ".html")):
        stitle, sname = cfg["slides"]
        base = posixpath.relpath("slides/" + sname, posixpath.dirname(dest))
        lines.append(f"[{stitle}]({base}.html){{ .md-button target=_blank }}")
        lines.append(f"[Slides as PDF]({base}.pdf){{ .md-button target=_blank }}")
    lines.append("")
    for label, rel in cfg["downloads"]:
        if os.path.exists(os.path.join(ROOT, rel)):
            lines.append(f"- [{label}]({posixpath.relpath('downloads/' + posixpath.basename(rel), posixpath.dirname(dest))})")
        else:
            lines.append(f"- {label}: your facilitator will share this")
    return "\n".join(lines) + "\n\n"


def main():
    if os.path.isdir(DOCS):
        shutil.rmtree(DOCS)
    os.makedirs(DOCS)
    for src, dest in PAGES.items():
        text = open(os.path.join(ROOT, src), encoding="utf-8").read()
        text = FAC.sub("", text)
        text = rewrite(text, src, dest)
        text = blank_before_lists(text)
        if dest in WEEKS:
            text = text.replace("## Objectives", links_block(dest, WEEKS[dest]) + "## Objectives", 1)
        write(dest, text)
    for rel in COPY_FILES:
        p = os.path.join(ROOT, rel)
        if os.path.exists(p):
            os.makedirs(os.path.join(DOCS, "downloads"), exist_ok=True)
            shutil.copy(p, os.path.join(DOCS, "downloads", os.path.basename(rel)))
        else:
            print("skipped (not found):", rel)
    pdir = os.path.join(ROOT, "practice")
    os.makedirs(os.path.join(DOCS, "practice"), exist_ok=True)
    for f in os.listdir(pdir):
        if f.endswith(".html"):
            shutil.copy(os.path.join(pdir, f), os.path.join(DOCS, "practice", f))
    sdir = os.path.join(ROOT, "slides")
    os.makedirs(os.path.join(DOCS, "slides"), exist_ok=True)
    for f in os.listdir(sdir):
        if f.endswith((".html", ".pdf")):
            shutil.copy(os.path.join(sdir, f), os.path.join(DOCS, "slides", f))
    print("docs/ ready")


if __name__ == "__main__":
    main()
