"""Precompute the tokenizations used by the Week 5 practice page (What Counts as a Word?).

The browser cannot run jieba, so the page shows tokens computed here. All texts are invented.
Run: python scripts/make_week05_practice_data.py   (needs: pip install jieba)
Writes practice/src/week05/tokens.json, which scripts/build_practice.py inlines into the page.
"""
import json
import os
import re

import jieba

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "practice", "src", "week05", "tokens.json")

TEXTS = [
    {"id": "t1", "lang": "en", "text": "AI isn't replacing teachers, it's changing homework."},
    {"id": "t2", "lang": "en", "text": "New York-based startup launches #AI tutor for $5/month"},
    {"id": "t3", "lang": "zh", "text": "新加坡推出人工智能學習計劃"},
    {"id": "t4", "lang": "zh", "text": "香港大學生如何使用生成式人工智慧"},
    {"id": "t5", "lang": "mixed", "text": "Singapore 學生 use ChatGPT 寫功課"},
]


def spaces(t):
    return t.split()


def words(t):
    return re.findall(r"\w+", t.lower())


def chars(t):
    return [c for c in t if not c.isspace()]


def segment(t):
    return [w for w in jieba.lcut(t) if w.strip()]


if __name__ == "__main__":
    out = []
    for d in TEXTS:
        t = d["text"]
        out.append({**d, "tokens": {"spaces": spaces(t), "words": words(t), "chars": chars(t), "jieba": segment(t)}})
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    for d in out:
        print(d["id"], {k: len(v) for k, v in d["tokens"].items()}, d["tokens"]["jieba"])
