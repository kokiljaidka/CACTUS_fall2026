"""Remove links and tokens that are not needed from saved SerpAPI responses.

Saved responses contain archive links back to serpapi.com, Google pagination and
topic tokens, and thumbnail URLs. None of that is used in the course, and long
random-looking strings trigger secret scanners (false alarms). This keeps the
search parameters and all the result text and links.

Usage:
    python scripts/serp_scrub.py                  # scrub data/week01/serp_cache in place and rezip
    python scripts/serp_scrub.py path/to/folder   # scrub another folder

cache_week1.py calls this automatically after saving.
"""
import json
import os
import shutil
import sys

DROP_TOP = {"search_metadata", "pagination", "serpapi_pagination"}
DROP_KEYS = {"thumbnail", "favicon"}


def _drop(key, value):
    if key.startswith("serpapi_") or key.endswith("_token") or key in DROP_KEYS:
        return True
    return isinstance(value, str) and "serpapi.com/" in value


def scrub(node, top=True):
    if isinstance(node, dict):
        return {k: scrub(v, False) for k, v in node.items()
                if not (top and k in DROP_TOP) and not _drop(k, v)}
    if isinstance(node, list):
        return [scrub(v, False) for v in node]
    return node


def scrub_dir(folder):
    before = after = 0
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".json"):
            continue
        path = os.path.join(folder, name)
        before += os.path.getsize(path)
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(scrub(data), f, ensure_ascii=False, indent=2)
        after += os.path.getsize(path)
    return before, after


def rezip(folder):
    parent, base = os.path.dirname(folder), os.path.basename(folder)
    shutil.make_archive(os.path.join(parent, base), "zip", root_dir=parent, base_dir=base)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    folder = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(here, "..", "data", "week01", "serp_cache")
    folder = os.path.normpath(folder)
    b, a = scrub_dir(folder)
    rezip(folder)
    print(f"scrubbed {folder}: {b // 1024} KB -> {a // 1024} KB, rezipped")
