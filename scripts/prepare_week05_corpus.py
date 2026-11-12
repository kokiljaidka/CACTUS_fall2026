"""Build the Week 5 shared corpora from data you hold locally.

Two files are written to data/private/ (gitignored: share them with students
through a private channel, such as the class drive, not the public repository):

  week05_reddit_sample.csv   posts from three less-personal subreddits
                             (jobs, personalfinance, mildlyinfuriating), scrubbed
  week05_news_corpus.csv     news and web results about AI from Singapore, Hong Kong and
                             Taiwan, built from the saved Week 1 searches (English and Chinese)

Usage:
    python scripts/prepare_week05_corpus.py --haps "path/to/haps_vignette_references.csv"

Scrubbing: links, email addresses, phone-like numbers and u/handles are replaced with
placeholders; post URLs and exact dates are dropped (dates become year-month); deleted or
very short posts are removed. This lowers re-identification risk but does not remove it,
so keep the files private and tell students not to try to identify anyone.
"""
import argparse
import glob
import json
import os
import re
import sys

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
OUT = os.path.join(ROOT, "data", "private")
SUBREDDITS = ["jobs", "personalfinance", "mildlyinfuriating"]

PATTERNS = [
    (re.compile(r"https?://\S+|www\.\S+"), "[link]"),
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"), "[email]"),
    (re.compile(r"\b\d{3}[-. ]\d{3,4}[-. ]\d{4}\b"), "[phone]"),
    (re.compile(r"(?<!\w)/?u/[A-Za-z0-9_-]{3,}"), "[user]"),
]


def scrub(text):
    text = "" if pd.isna(text) else str(text)
    for pat, repl in PATTERNS:
        text = pat.sub(repl, text)
    return re.sub(r"\s+", " ", text).strip()


def reddit(haps_path):
    d = pd.read_csv(haps_path, encoding_errors="replace", low_memory=False)
    d = d[d["subreddit"].isin(SUBREDDITS)].copy()
    d["title"] = d["title"].map(scrub)
    d["text"] = d["selftext"].map(scrub)
    d = d[~d["text"].str.lower().isin(["[removed]", "[deleted]"])]
    d = d[(d["title"].str.len() + d["text"].str.len()) >= 60]
    d["month"] = pd.to_datetime(d["created_utc"], errors="coerce").dt.strftime("%Y-%m")
    d = d.drop_duplicates(["title", "text"]).reset_index(drop=True)
    d.insert(0, "post_id", [f"r{i + 1:04d}" for i in range(len(d))])
    return d[["post_id", "subreddit", "month", "title", "text", "score", "num_comments"]]


def news():
    sys.path.insert(0, HERE)
    import cactus_serp  # noqa: E402
    places = {"sg": ("Singapore", "en"), "hk": ("Hong Kong", "zh-Hant"), "tw": ("Taiwan", "zh-Hant")}
    rows = []
    for path in sorted(glob.glob(os.path.join(ROOT, "data", "week01", "serp_cache", "*.json"))):
        name = os.path.basename(path)
        engine = "google_news" if name.startswith("google_news") else "google"
        gl = name.replace("google_news_", "").replace("google_", "")[:2]
        place, lang = places[gl]
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        t = cactus_serp.results_table(data, engine, place)
        for _, r in t.iterrows():
            title = scrub(r["title"])
            snippet = scrub(r["snippet"])
            rows.append({"place": place, "language": lang, "engine": engine, "source": r["source"],
                         "date": r["date"], "title": title, "snippet": snippet,
                         "text": (title + ". " + snippet).strip(". ").strip()})
    d = pd.DataFrame(rows)
    d = d[d["text"].str.len() >= 15].drop_duplicates(["place", "text"]).reset_index(drop=True)
    d.insert(0, "doc_id", [f"n{i + 1:04d}" for i in range(len(d))])
    return d


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--haps", required=True, help="path to haps_vignette_references.csv")
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    r = reddit(a.haps)
    r.to_csv(os.path.join(OUT, "week05_reddit_sample.csv"), index=False, encoding="utf-8-sig")
    print("week05_reddit_sample.csv:", len(r), "posts", r["subreddit"].value_counts().to_dict())
    n = news()
    n.to_csv(os.path.join(OUT, "week05_news_corpus.csv"), index=False, encoding="utf-8-sig")
    print("week05_news_corpus.csv:", len(n), "texts", n.groupby(["place", "language"]).size().to_dict())
