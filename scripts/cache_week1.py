"""Instructor script: save the Week 1 searches so students can run without a key.

Usage (6 API calls):
    export SERPAPI_KEY="your key"
    python3 scripts/cache_week1.py

Writes JSON files to data/week01/serp_cache/ and zips them to
data/week01/serp_cache.zip. Give students the zip; the Week 1 notebook unpacks it.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import cactus_serp  # noqa: E402

# Keep these in sync with PLACES in the Week 1 notebook.
PLACES = [
    ("Singapore", "sg", "en", "artificial intelligence"),
    ("Hong Kong", "hk", "zh-TW", "人工智能"),
    ("Taiwan", "tw", "zh-TW", "人工智慧"),
]
ENGINES = ["google", "google_news"]

if not cactus_serp.API_KEY:
    sys.exit("Set SERPAPI_KEY first: export SERPAPI_KEY='your key'")

cactus_serp.CACHE_DIR = os.path.join(HERE, "..", "data", "week01", "serp_cache")

for place, gl, hl, q in PLACES:
    for engine in ENGINES:
        data = cactus_serp.search(q, gl, hl, engine)
        table = cactus_serp.results_table(data, engine, place)
        print(f"{place:10} {engine:12} {len(table):3} results")
        if table.empty:
            print("  WARNING: no results parsed. Check the raw JSON keys.")

import serp_scrub  # noqa: E402

# Drop links and tokens the course does not use (they look like secrets to scanners).
serp_scrub.scrub_dir(cactus_serp.CACHE_DIR)

week_dir = os.path.join(HERE, "..", "data", "week01")
shutil.make_archive(os.path.join(week_dir, "serp_cache"), "zip", root_dir=week_dir, base_dir="serp_cache")
print("Wrote data/week01/serp_cache.zip")
