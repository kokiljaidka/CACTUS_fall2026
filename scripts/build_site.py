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
    "project/getting_data_access.md": "access.md",
    "data/README.md": "data.md",
    "schedule/week01.md": "weeks/week01.md",
    "schedule/week02.md": "weeks/week02.md",
    "schedule/week03.md": "weeks/week03.md",
    "schedule/week04.md": "weeks/week04.md",
    "schedule/week05.md": "weeks/week05.md",
    "schedule/midpoint.md": "weeks/midpoint.md",
    "schedule/week06.md": "weeks/week06.md",
    "schedule/week07.md": "weeks/week07.md",
    "schedule/week08.md": "weeks/week08.md",
    "project/rerun_report.md": "rerun-report.md",
    "project/ethics_checklist.md": "ethics.md",
    "facilitators/README.md": "facilitators/index.md",
    "facilitators/week_by_week.md": "facilitators/weeks.md",
    "facilitators/practice_pages_guide.md": "facilitators/practice-pages.md",
    "facilitators/running_this_together.md": "facilitators/community.md",
    "testing/ra_checklist.md": "facilitators/testing.md",
}

# per-week links added to each week page
WEEKS = {
    "weeks/week01.md": {
        "notebook": "week01_first_api_calls.ipynb",
        "slides": ("Lecture slides", "week01_define_your_problem"),
        "practice": ("Cactus Code Garden (puzzle page)", "week01_cactus_code_garden.html"),
        "practice_in": "s2",
        "downloads": [("Saved searches (serp_cache.zip)", "data/week01/serp_cache.zip")],
    },
    "weeks/week03.md": {
        "notebook": "week03_verify_and_analyze.ipynb",
        "slides": ("Lecture slides", "week03_verify_and_analyze"),
        "practice": ("Planted-Effect Lab (practice page)", "week03_planted_effect_lab.html"),
        "downloads": [
            ("Experiment data (week03_experiment.csv)", "data/week03_experiment.csv"),
            ("Survey data (week03_survey.csv)", "data/week03_survey.csv"),
        ],
    },
    "weeks/week04.md": {
        "notebook": "week04_collect_your_own_data.ipynb",
        "slides": ("Lecture slides", "week04_collect_your_own_data"),
        "practice": ("Before You Collect (practice page)", "week04_before_you_collect.html"),
        "downloads": [],
    },
    "weeks/week05.md": {
        "notebook": "week05_analyze_text.ipynb",
        "slides": ("Lecture slides", "week05_analyze_text"),
        "practice": ("What Counts as a Word? (practice page)", "week05_what_counts_as_a_word.html"),
        "downloads": [],
    },
    "weeks/week06.md": {
        "notebook": "week06_ai_as_annotator.ipynb",
        "slides": ("Lecture slides", "week06_ai_as_annotator"),
        "practice": ("Can You Trust the Labeler? (practice page)", "week06_trust_the_labeler.html"),
        "downloads": [],
    },
    "weeks/week07.md": {
        "s1_title": "Session 1 (Tue Jan 12): the shared core",
        "s2_title": "Session 2 (Thu Jan 14, tentative): your track",
        "notebooks": [
            ("Session 1 notebook: the shared core", "week07_core_nested_data.ipynb", "s1"),
            ("Track A: networks", "week07_track_a_networks.ipynb", "s2"),
            ("Track B: images and memes", "week07_track_b_images.ipynb", "s2"),
            ("Track C: mock feed or experiment", "week07_track_c_experiment.ipynb", "s2"),
        ],
        "slides": ("Lecture slides", "week07_applying_statistics"),
        "practice": ("Plant It, Find It (practice page)", "week07_plant_it_find_it.html"),
        "downloads": [
            ("Comments in posts (week07_comments.csv)", "data/week07_comments.csv", "s1"),
            ("Posts (week07_posts.csv)", "data/week07_posts.csv", "s1"),
            ("Track C: experiment (week07_experiment.csv)", "data/week07_experiment.csv", "s2"),
            ("Track A: network edges (week07_edges.csv)", "data/week07_edges.csv", "s2"),
            ("Track B: memes (week07_memes.zip)", "data/week07_memes.zip", "s2"),
        ],
    },
    "weeks/week08.md": {
        "s1_title": "Before presentation day: the reproducibility exercise",
        "slides": ("Lecture slides", "week08_reproduce_and_present"),
        "practice": ("Run It from Scratch (practice page, optional)", "week08_run_it_from_scratch.html"),
        "extra": [("Rerun report (template for your partner)", "rerun-report.md", "s1")],
    },
    "weeks/week02.md": {
        "notebook": "week02_clean_and_chart.ipynb",
        "slides": ("Lecture slides", "week02_clean_it_chart_it"),
        "practice": ("Silent Changes (practice page)", "week02_silent_changes.html"),
        "downloads": [
            ("Starbucks comments (starbucks_sea_comments.csv)", "data/starbucks_sea_comments.csv"),
            ("Toy café table (week02_toy_cafe.csv)", "data/week02_toy_cafe.csv"),
        ],
    },
}
COPY_FILES = [  # published as downloads
    "data/starbucks_sea_comments.csv", "data/lululemon_instagram.csv", "data/week02_toy_cafe.csv",
    "data/week03_experiment.csv", "data/week03_survey.csv",
    "data/week01/serp_cache.zip",
    "data/week07_comments.csv", "data/week07_posts.csv", "data/week07_experiment.csv",
    "data/week07_edges.csv", "data/week07_memes.zip",
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
    """Links for each week, grouped by session: Session 1 (learning) and Session 2 (coding).

    Default: slides and the practice page go with Session 1; notebooks and data with Session 2.
    A week can set cfg["practice_in"] = "s2", and tag a notebook or download with "s1" or "s2".
    """
    here = posixpath.dirname(dest)
    s1, s2 = [], []

    def add(group, line):
        (s1 if group == "s1" else s2).append(line)

    if cfg.get("slides") and os.path.exists(os.path.join(ROOT, "slides", cfg["slides"][1] + ".html")):
        stitle, sname = cfg["slides"]
        base = posixpath.relpath("slides/" + sname, here)
        add("s1", f"[{stitle}]({base}.html){{ .md-button target=_blank }}")
        add("s1", f"[Slides as PDF]({base}.pdf){{ .md-button target=_blank }}")
    if cfg.get("practice"):
        ptitle, pfile = cfg["practice"]
        add(cfg.get("practice_in", "s1"), f"[{ptitle}]({posixpath.relpath('practice/' + pfile, here)}){{ .md-button target=_blank }}")
    notebooks = cfg.get("notebooks") or ([(None, cfg["notebook"], "s2")] if cfg.get("notebook") else [])
    first = True
    for item in notebooks:
        label, nb = item[0], item[1]
        group = item[2] if len(item) > 2 else "s2"
        style = " .md-button--primary" if first else ""
        first = False
        add(group, f"[{label or 'Open the notebook in Colab'}]({COLAB}{nb}){{ .md-button{style} target=_blank }}")
    for label, page, group in cfg.get("extra", []):
        add(group, f"[{label}]({posixpath.relpath(page, here)}){{ .md-button target=_blank }}")
    d1, d2 = [], []
    for item in cfg.get("downloads", []):
        label, rel = item[0], item[1]
        group = item[2] if len(item) > 2 else "s2"
        if os.path.exists(os.path.join(ROOT, rel)):
            line = f"- [{label}]({posixpath.relpath('downloads/' + posixpath.basename(rel), here)})"
        else:
            line = f"- {label}: your facilitator will share this"
        (d1 if group == "s1" else d2).append(line)
    out = ["## Your links", ""]
    for title, buttons, downloads in ((cfg.get("s1_title", "Session 1: learning session"), s1, d1), (cfg.get("s2_title", "Session 2: coding session"), s2, d2)):
        if not buttons and not downloads:
            continue
        out.append(f"### {title}")
        out.append("")
        out.extend(buttons)
        out.append("")
        out.extend(downloads)
        if downloads:
            out.append("")
    return "\n".join(out) + "\n"


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
