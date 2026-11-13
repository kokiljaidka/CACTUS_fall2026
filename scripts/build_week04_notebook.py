"""Build notebooks/week04_collect_your_own_data.ipynb. Re-run after editing.

Route A: an export the student already has (Twitter/X, Instagram, Facebook, Reddit, Bluesky, or another source).
Route B: the invented sample made by scripts/make_week04_sample.py. Needs no key.
"""
import os

import nbformat as nbf

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "notebooks", "week04_collect_your_own_data.ipynb")
cells = []


def md(t):
    cells.append(nbf.v4.new_markdown_cell(t.strip()))


def code(t):
    cells.append(nbf.v4.new_code_cell(t.strip()))


md("""
# Week 4: Collect your own data

**CACTUS Fall 2026 · Coding session**

You decide what data exists. Today you collect posts, **save the raw response first**, turn it into a table, **check that nothing was lost without a reason**, remove what identifies people, and write down what you did.

**Goals today**
- start from data you collected or exported, and save the raw data untouched
- log what you collected, when, and how
- parse it into one standard table, and compare counts at every step
- anonymize, and check that it worked
- write a data card for your own project

**Choose a route at the start (pairs can use different routes)**
- **Route A: an export you already have.** Data you collected or downloaded for your own project (for example from Twitter/X, Instagram, Facebook, Reddit, or Bluesky). The facilitators can help you with each of these. Aim to be on this route.
- **Route B: the saved example.** An invented example that looks like a real API response. No key needed. Use it if you do not have data yet, and talk to the facilitators about getting some.

**Rules**
- Predict before you run. Never accept AI code you have not read.
- **Never paste an API key, a password, or real people's data into an AI chat.**
- Keys go in Colab Secrets only. Never in a cell, a notebook, or a repository.
- Public does not mean free to use. If a rule is unclear, ask before you collect.
- Do not try to identify anyone.

**Run cells one at a time**, not "Run all". Some cells are for you to fill in.
""")

md("""
## How this session runs

- There is **no lecture** in the coding session. You will be in a breakout room with a partner, ideally someone on the same platform, and the facilitators visit the rooms.
- **Stuck?** Try these, in order, for no more than 5 minutes:
  1. Read the last line of any error message. What is it telling you?
  2. Re-read the instructions for the step. Did you skip a part?
  3. Ask your partner, then ask an AI assistant to explain the message (never paste keys or real people's data).
  4. Still stuck? Click **Ask for help** in Zoom or message the facilitators in the main chat. Say what you expected, what happened, and what you already tried.
""")

code("""
import datetime
import glob
import json
import os
import re
import time

import pandas as pd
import requests

RAW_DIR = "raw"          # raw responses go here, untouched
os.makedirs(RAW_DIR, exist_ok=True)

BASE = "https://raw.githubusercontent.com/kokiljaidka/CACTUS_fall2026/main/data/week04/sample/"
CURSORS = {None: "page_001.json", "cur_2": "page_002.json", "cur_3": "page_003.json", "cur_4": "page_004.json"}


def sample_api(cursor=None):
    # Stands in for a real platform (Route B). It returns one page of the saved sample and a cursor to the next page.
    name = CURSORS[cursor]
    if os.path.exists(name):
        with open(name, encoding="utf-8") as f:
            return json.load(f)
    return requests.get(BASE + name, timeout=30).json()


STANDARD = ["item_id", "parent_id", "thread_id", "created_at", "author_id", "text", "like_count",
            "platform", "source", "query", "collected_on"]
print("ready")
""")

md("""
---
## Warm-up: a collection stub (about 15 min)

**Everyone does this warm-up on the saved example**, whichever route you are on. The practice page gave you a stub that **saves the raw response before anything else** and writes a log. Paste it below, then change the one function that talks to the platform. For the example, that function is `sample_api`.

On a real platform you would replace `sample_api` with that platform's request. The habit is the same for an export: keep the original untouched, and write a log.

**Predict:** if you collect 3 pages, how many files will be in `raw/`, and what will the log say?

> My prediction:
""")

code("""
# Paste the stub from the practice page here, or use this one.
log = {"query": "AI", "tool": "sample_api (invented sample)", "collected_on": str(datetime.date.today()),
       "page_size": 25, "pause_seconds": 1, "pages": 0, "items": 0}

cursor, n = None, 0
while n < 3:
    page = sample_api(cursor)                                     # <- change this line for your platform
    with open(f"{RAW_DIR}/page_{n + 1:03d}.json", "w", encoding="utf-8") as f:
        json.dump(page, f, ensure_ascii=False, indent=2)          # raw, untouched
    log["pages"] += 1
    log["items"] += len(page["items"])
    cursor = page.get("next_cursor")
    n += 1
    time.sleep(log["pause_seconds"])

with open(f"{RAW_DIR}/collection_log.json", "w", encoding="utf-8") as f:
    json.dump(log, f, indent=2)
print(log)
assert len(glob.glob(f"{RAW_DIR}/page_*.json")) == log["pages"], "Files saved do not match the pages collected"
""")

md("""
---
## Exercise 1: Collect, and save the raw data (required, about 30 min)

**Route A (your export).** Upload your export file to Colab (the folder icon on the left). Use the first cell below. It copies the file into `raw/` **untouched** (never open and re-save the original in Excel) and writes a log. Fill in the log by hand: what it is, where it came from, when you collected it, and how.

**Route B (the example).** Use the second cell below. It collects all 4 pages of the example.

If you do not have data yet, use Route B today and talk to the facilitators about getting some. Plan to have your own data before Week 6.

**Big files.** If your export is large (hundreds of MB), do not load it all at once. Read it in pieces and keep only the columns you need: `for chunk in pd.read_csv(path, chunksize=100_000): ...` (for JSON lines, `pd.read_json(path, lines=True, chunksize=100_000)`). Colab has limited memory and its files disappear when the session ends, so for a large file work on your own computer or keep it on Google Drive, and write in your log which file and which date. **Restricted data** (data from another researcher, a platform export with terms, or anything your ethics approval limits) goes only where those rules allow. If you are unsure, ask before uploading it anywhere.

**How you check it:** count the files in `raw/`, add up the items on each page, and compare with what your log says.
""")

code("""
ROUTE = "B"          # change to "A" if you are using your own export
""")

code("""
# ROUTE A ONLY: your export. Skip this cell on Route B.
EXPORT = "my_export.csv"      # the name of the file you uploaded (.csv or .json)
SOURCE = "Reddit"             # where it came from
QUERY = "my topic"            # what you searched for or how you chose the posts
HOW = "export from the platform's download tool"   # how you got it

import shutil
shutil.copy(EXPORT, f"{RAW_DIR}/{os.path.basename(EXPORT)}")      # an untouched copy
raw_df = pd.read_csv(EXPORT) if EXPORT.endswith(".csv") else pd.read_json(EXPORT)
RAW_ENTRIES = len(raw_df)
log = {"source": SOURCE, "query": QUERY, "tool": HOW, "collected_on": str(datetime.date.today()), "items": RAW_ENTRIES}
with open(f"{RAW_DIR}/collection_log.json", "w", encoding="utf-8") as f:
    json.dump(log, f, indent=2)
print(log)
print(raw_df.head(3))
""")

code("""
# ROUTE B ONLY: collect all 4 pages of the example. Skip this cell on Route A.
for f in glob.glob(f"{RAW_DIR}/page_*.json"):
    os.remove(f)

log = {"query": "AI", "tool": "sample_api (invented sample)", "collected_on": str(datetime.date.today()),
       "page_size": 25, "pause_seconds": 1, "pages": 0, "items": 0}
cursor, n = None, 0
while True:
    page = sample_api(cursor)
    with open(f"{RAW_DIR}/page_{n + 1:03d}.json", "w", encoding="utf-8") as f:
        json.dump(page, f, ensure_ascii=False, indent=2)
    log["pages"] += 1
    log["items"] += len(page["items"])
    cursor = page.get("next_cursor")
    n += 1
    if not cursor:
        break
    time.sleep(log["pause_seconds"])

with open(f"{RAW_DIR}/collection_log.json", "w", encoding="utf-8") as f:
    json.dump(log, f, indent=2)
print(log)
""")

code("""
# Check 1. Do the files, the items, and the log agree?
if ROUTE == "B":
    pages = [json.load(open(p, encoding="utf-8")) for p in sorted(glob.glob(f"{RAW_DIR}/page_*.json"))]
    RAW_ENTRIES = sum(len(p["items"]) for p in pages)
    print("files:", len(pages), end="  ")
print("entries in the files:", RAW_ENTRIES, "  log says:", log["items"])
assert RAW_ENTRIES == log["items"], "The log does not match what is saved. Which one is wrong?"
""")

md("""
> Log (Exercise 1): what did you collect, and what limits did you hit (items per page, requests per hour)? What did you do about them?
""")

md("""
---
## Exercise 2: Parse it, and compare the counts (required, about 30 min)

Turn your raw data into **one table with these columns** (the same for every platform, so later weeks work on anyone's data):

| Column | What it holds |
|---|---|
| `item_id` | The platform's ID for the post or comment (if your export has none, make one) |
| `parent_id` | The item it replies to; empty if top-level |
| `thread_id` | The post or video it sits under |
| `created_at` | When it was written |
| `author_id` | A pseudonymous ID (not the username) |
| `text` | The text |
| `like_count` | Likes or score |
| `platform`, `source`, `query`, `collected_on` | Where it came from, and when |

**How to prompt well.** Give the AI the context it cannot see, and **only invented or de-identified examples**:

> Here is the structure of one item in my data (a JSON item, or the column names of a CSV): *(paste the structure with invented values; remove any real names)*. Write a function `parse_page(page)` that returns a list of rows with these columns: *(paste the list)*. Then write code that reads all the files in `raw/` into one pandas DataFrame. Explain each line in one sentence.

**Route A:** read your export into a table, rename your columns to the names above, and fill any column you do not have with empty values (for example `df["parent_id"] = None`). Set `platform`, `source`, `query`, and `collected_on` yourself. Ask an AI to help, but give it only the **column names and invented example rows**, never real people's data.

**Route B:** the raw files are JSON pages. Write `parse_page(page)` and read all the files in `raw/`.

**Predict:** you saved some number of entries. How many rows will your table have? Will they be equal? Why might they differ?

> My prediction:
""")

code("""
# Task 2a: Route B: paste the AI's parse_page function here, then run it on one page and look at the result.
# Route A: look at raw_df.columns and decide which of your columns becomes which standard column.
""")
code("""
# Task 2b: build the full table df (Route B: from every file in raw/; Route A: from raw_df).
""")

code("""
# Check 2. Counts must be explained. Fill the numbers in the table below.
print("entries saved:", RAW_ENTRIES, "  rows in your table:", len(df))
assert all(c in df.columns for c in STANDARD), f"Missing columns: {[c for c in STANDARD if c not in df.columns]}"
print("Is item_id unique?", df["item_id"].is_unique)
print("Items with no text:", int(df["text"].isna().sum()), "  Items with no like count:", int(df["like_count"].isna().sum()))
""")

md("""
**Explain every difference** between the number of entries saved and the number of rows. For each, say why and what you decided.

| Count | Number | Why |
|---|---|---|
| Entries saved in `raw/` | | |
| Rows in my table | | |
| Difference | | |
| Items with no text | | What are they? Keep or drop? |

*Hint:* if your table has duplicate IDs, find out where they come from before you drop anything. On Route B, look at how the pages begin and end. On Route A, look for posts exported twice, or deleted posts with no text.

> Log (Exercise 2): which count did you not expect? What check did you use to find out why?
""")

md("""
---
## Exercise 3: Anonymize, and check that it worked (required, about 25 min)

Before you save or share a table, remove what identifies people. Today:

1. Replace each username with a **pseudonymous `author_id`** (for example `author_0001`). Keep the mapping out of any file you share.
2. Remove **@handles and links** from the text.
3. Make the timestamp **a date only** if you do not need the time of day.
4. Drop **display names, profile links, and anything else** your question does not need.

**Removing the username is not enough.** A distinctive post, an exact time, and a small place can still point to one person. Ask: what could someone find by searching this text?

**Predict:** after you remove handles and links, will any `@` or `http` be left in the text? Check, don't assume.

> My prediction:
""")

code("""
# Task 3a: replace usernames with author_id. 3b: remove @handles and links from text. 3c: keep only the date in created_at.
""")

code("""
# Check 3. Run after your changes. It stops with a message if something identifying remains.
bad_cols = [c for c in df.columns if re.search(r"handle|user|display|profile|url|name", c, re.I) and c not in ("author_id",)]
assert not bad_cols, f"These columns may identify people: {bad_cols}"
assert not df["text"].fillna("").str.contains(r"@\\w").any(), "There is still an @handle in the text"
assert not df["text"].fillna("").str.contains(r"https?://").any(), "There is still a link in the text"
assert df["created_at"].astype(str).str.fullmatch(r"\\d{4}-\\d{2}-\\d{2}").all(), "created_at should be a date like 2026-10-03"
assert df["author_id"].dropna().astype(str).str.startswith("author_").all(), "author_id should look like author_0001"
print("Passed. Remember: this table still contains people's words. Keep it private unless the terms and your ethics process say otherwise.")
""")

md("""
> Log (Exercise 3): what identifying information did you remove? What could still identify someone? Save the anonymized table with `df.to_csv("my_collection_anonymized.csv", index=False)`.
""")

md("""
---
## Exercise 4: Your data card (about 15 min)

Write one short card for your own project's data, even if you have only a small sample so far. Copy the template into a text cell and fill it in.

```
DATA CARD
Project:                      Date:

What it is (one row =):
Where it came from (platform, query, tool):
How the posts were chosen (all, random, ranked by the platform, keyword search):
When collected, and over what period:
How much (items, pages), and what was left out:
Which terms of use apply (and where I read them):
Which ethics process applies, and what I did about it:
What I removed to protect people:
What I saved, and where (raw, parsed, anonymized):
Who holds the raw files, and who may see them:
Known gaps and biases (who is missing? what did the query miss?):
What I would do differently next time:
```

Add the card to your project card.
""")

md("""
---
## Stretch (about 15 min)

- **Pagination with a pause:** read the Route B cell in Exercise 1. It loops until there is no `next_cursor`, waits between requests, and writes the log. Explain why each part is there.
- **A second dataset** (the example, or a second export). Does the standard table work for it? What changes?
- **Survive a limit:** if you collected from an API, what would your code do if the platform said "too many requests"? Write what you would do.
""")

md("""
---
## Log: what I learned today

- One check that caught a difference I did not expect:
- One thing I removed to protect people, and one thing that could still identify someone:
- One question I still have:

**Homework (45 min or less):** finish your data card and add it to your project card. If you do not have your own data yet, talk to the facilitators now and agree how you will get enough before Week 6.
""")

nb = nbf.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
nbf.write(nb, OUT)
print("wrote", os.path.normpath(OUT))
