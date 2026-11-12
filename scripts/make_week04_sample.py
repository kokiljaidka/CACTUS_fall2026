"""Make the invented raw-response sample for Week 4 (Route B).

Everything here is invented: the people, handles, threads, and comments. It is safe to keep
in the public repository. It has the shape of a real platform API response so students can
practice saving raw data, parsing it, counting, and anonymizing.

Planted, on purpose (all things real collections do):
  - 4 pages of 25 entries, but the last item of each page is repeated at the top of the next,
    so 100 entries contain 97 unique items
  - 4 deleted items (text and author are null)
  - 6 items with no like count
  - @handles and links inside the comment text
  - exact timestamps, and a profile link and display name on each author
  - one reply whose parent is not in the sample

Run: python scripts/make_week04_sample.py   (writes data/week04/sample/page_001.json ... page_004.json)
"""
import json
import os
import random

SEED = 4
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "data", "week04", "sample")

THREADS = [
    ("t01", "Using AI chatbots for school assignments: good or bad?"),
    ("t02", "A hawker stall owner tries an AI ordering assistant"),
    ("t03", "AI-generated art on local event posters"),
    ("t04", "Should newsrooms use AI to write headlines?"),
    ("t05", "我們該不該讓孩子用AI寫功課？"),
]
HANDLES = [
    ("kopi_and_code", "Kopi & Code"), ("mei_reads", "Mei"), ("tan_the_teacher", "Mr Tan"), ("noodle_notes", "Noodle Notes"),
    ("ravi_builds", "Ravi"), ("sunrise_studio", "Sunrise Studio"), ("amy_in_hk", "Amy"), ("taipei_tom", "Tom Lin"),
    ("lah_but_why", "Lah But Why"), ("old_school_ong", "Ong"), ("clara_codes", "Clara"), ("mrt_commuter", "MRT Commuter"),
    ("bao_and_books", "Bao"), ("night_owl_nina", "Nina"), ("zhi_wei_w", "Zhi Wei"), ("coffee_chat_cc", "CC"),
    ("daily_dim_sum", "Dim Sum Daily"), ("student_of_life", "Student"), ("grace_g", "Grace"), ("kelvin_k", "Kelvin"),
    ("hui_ling", "Hui Ling"), ("papaya_pete", "Pete"), ("lena_l", "Lena"), ("min_the_maker", "Min"),
]
EN = [
    "I use it to check my grammar, not to write my essays.",
    "Honestly it saves me hours, but I still read everything it gives me.",
    "My students hand in work that sounds the same. That worries me.",
    "It got the dish names wrong again. Humans still needed.",
    "Great idea, but who is responsible when it makes a mistake?",
    "The poster looks nice but the words are garbled. Please proofread!",
    "I would rather pay a local artist than a machine.",
    "As long as we label it clearly, I do not mind.",
    "My kid asked it to explain fractions and it did a better job than me.",
    "It is fast, but fast is not the same as right.",
    "We tried it at the stall for a week. Fewer wrong orders, more confused customers.",
    "Headlines written by AI all sound the same after a while.",
    "The real question is what we do with the time it saves.",
    "I do not trust anything it says without a second source.",
    "Can someone explain how it decides what to say? Genuinely curious.",
    "This is the future, like it or not.",
    "My boss wants us to use it for everything. I have doubts.",
    "It helped me practice for my interview. Very useful.",
    "Not impressed. It gave me a confident wrong answer yesterday.",
    "Good discussion. Thanks for sharing your experience.",
    "Cheaper than hiring someone, but that is also the problem.",
    "It should help teachers, not replace them.",
    "I tried it for translation and it made up a word.",
    "Everyone is talking about it but few people have read the terms.",
]
ZH = [
    "我覺得可以用，但是一定要自己檢查。",
    "孩子用AI寫功課，老師看得出來嗎？",
    "有時候很方便，有時候亂講，要小心。",
    "我比較相信真人的判斷。",
    "學校應該教學生怎麼正確使用它。",
    "這個海報的字有錯，要請人校對。",
    "科技進步很快，我們要跟上。",
    "如果標示清楚，我可以接受。",
]


def make_items():
    rnd = random.Random(SEED)
    items, used = [], 0
    for n in range(1, 98):
        thread_id, _ = THREADS[(n - 1) % len(THREADS)] if rnd.random() < 0.55 else rnd.choice(THREADS)
        handle, display = rnd.choice(HANDLES)
        zh = thread_id == "t05" or rnd.random() < 0.08
        text = rnd.choice(ZH if zh else EN)
        r = rnd.random()
        if r < 0.12 and items:
            text = f"@{rnd.choice(HANDLES)[0]} " + text
        elif r < 0.20:
            text += f" More here: https://example.com/post/{rnd.randint(1000, 9999)}"
        parent = None
        if items and rnd.random() < 0.35:
            parent = rnd.choice(items)["id"]
        day, hour, minute, sec = rnd.randint(1, 28), rnd.randint(7, 23), rnd.randint(0, 59), rnd.randint(0, 59)
        items.append({
            "id": f"c{n:04d}",
            "parent_id": parent,
            "thread_id": thread_id,
            "created": f"2026-10-{day:02d}T{hour:02d}:{minute:02d}:{sec:02d}Z",
            "author": {"handle": "@" + handle, "display_name": display, "profile_url": f"https://example.com/u/{handle}"},
            "text": text,
            "likes": rnd.choice([0, 0, 1, 2, 3, 5, 8, 12, 20, 41]),
            "lang": "zh-Hant" if zh else "en",
        })
        used += 1
    items.sort(key=lambda i: i["created"])
    for k, it in enumerate(items, 1):          # renumber in time order so ids run in order
        old = it["id"]
        it["_old"] = old
    remap = {it["_old"]: f"c{k:04d}" for k, it in enumerate(items, 1)}
    for it in items:
        it["id"] = remap[it["_old"]]
        it["parent_id"] = remap.get(it["parent_id"]) if it["parent_id"] else None
        # a parent must come earlier in time, or it is a reply to something outside the sample
        if it["parent_id"] and it["parent_id"] >= it["id"]:
            it["parent_id"] = None
        del it["_old"]
    # one reply whose parent is not in the sample
    items[40]["parent_id"] = "c9999"
    # 4 deleted items, 6 items with no like count
    for k in (12, 33, 58, 80):
        items[k]["text"] = None
        items[k]["author"] = None
    for k in (5, 19, 44, 60, 71, 90):
        items[k]["likes"] = None
    return items


def make_pages(items):
    pages, i = [], 0
    for p in range(4):
        start = i - 1 if p else 0
        chunk = items[start:start + 25]
        i = start + 25
        pages.append({
            "query": "AI",
            "page": p + 1,
            "page_size": 25,
            "next_cursor": f"cur_{p + 2}" if p < 3 else None,
            "retrieved": "2026-11-01T09:00:00Z",
            "items": chunk,
        })
    return pages


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    items = make_items()
    pages = make_pages(items)
    for pg in pages:
        with open(os.path.join(OUT, f"page_{pg['page']:03d}.json"), "w", encoding="utf-8") as f:
            json.dump(pg, f, ensure_ascii=False, indent=2)
    entries = sum(len(p["items"]) for p in pages)
    unique = len({it["id"] for p in pages for it in p["items"]})
    print(f"wrote {len(pages)} pages: {entries} entries, {unique} unique items")
