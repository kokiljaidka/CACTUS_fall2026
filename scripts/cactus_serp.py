"""SerpAPI helpers for CACTUS Week 1.

This file is the single source for the helper code. The Week 1 notebook embeds
a copy (see build_week01_notebook.py), and cache_week1.py imports it directly.

Every search is saved to serp_cache/ as raw JSON. A repeated search reads the
saved file instead of calling the API, which saves quota and lets students work
from instructor-provided files without a key.
"""
import hashlib
import json
import os
from urllib.parse import urlparse

import pandas as pd
import requests

# --- key (set per environment) ---
API_KEY = os.environ.get("SERPAPI_KEY")
# --- end key ---

CACHE_DIR = "serp_cache"


def _cache_path(q, gl, hl, engine):
    digest = hashlib.md5(q.encode("utf-8")).hexdigest()[:8]
    return os.path.join(CACHE_DIR, f"{engine}_{gl}_{hl}_{digest}.json")


def search(q, gl, hl, engine="google"):
    """Run one SerpAPI search and return the raw JSON as a dict.

    q       the search text
    gl      country code, e.g. "sg", "hk", "tw"
    hl      interface language, e.g. "en", "zh-TW"
    engine  "google" (web results) or "google_news"
    """
    os.makedirs(CACHE_DIR, exist_ok=True)
    path = _cache_path(q, gl, hl, engine)

    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)

    if not API_KEY:
        raise RuntimeError(
            "No saved result for this search and no API key found. "
            "Check Step 1 (your key), or ask the instructor for the saved files."
        )

    params = {"engine": engine, "q": q, "gl": gl, "hl": hl, "api_key": API_KEY}
    response = requests.get("https://serpapi.com/search.json", params=params, timeout=60)
    data = response.json()
    if "error" in data:
        raise RuntimeError(f"SerpAPI said: {data['error']}")

    # Never write the key to disk.
    if isinstance(data.get("search_parameters"), dict):
        data["search_parameters"].pop("api_key", None)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return data


def results_table(data, engine, place):
    """Turn raw SerpAPI JSON into a tidy table, one row per result."""
    key = "news_results" if engine == "google_news" else "organic_results"
    rows = []
    for item in data.get(key, []):
        source = item.get("source")
        if isinstance(source, dict):
            source = source.get("name")
        link = item.get("link", "")
        rows.append(
            {
                "place": place,
                "engine": engine,
                "position": item.get("position"),
                "title": item.get("title"),
                "source": source or urlparse(link).netloc,
                "date": item.get("date"),
                "snippet": item.get("snippet"),
                "link": link,
            }
        )
    return pd.DataFrame(rows)
