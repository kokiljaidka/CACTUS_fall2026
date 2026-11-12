"""Build notebooks/week01_first_api_calls.ipynb.

The helper code in the notebook is copied from cactus_serp.py so the two
never drift apart. Re-run this script after editing either file.
"""
import os
import re

import nbformat as nbf

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "notebooks", "week01_first_api_calls.ipynb")

# ---- helper code: copy of cactus_serp.py without the docstring and key lines ----
src = open(os.path.join(HERE, "cactus_serp.py"), encoding="utf-8").read()
src = re.sub(r'^""".*?"""\n', "", src, flags=re.S)
src = re.sub(r"# --- key \(set per environment\) ---.*?# --- end key ---\n", "", src, flags=re.S)
HELPERS = "# Do not edit this cell. In Step 6 you will ask an AI to explain it.\n" + src.strip() + "\n"

cells = []


def md(text):
    cells.append(nbf.v4.new_markdown_cell(text.strip()))


def code(text):
    cells.append(nbf.v4.new_code_cell(text.strip()))


md("""
# Week 1: Your first API calls

**CACTUS Fall 2026 · Coding session**

An **API** lets your code ask a service a question and get structured data back. Today you will ask Google (through SerpAPI) what it shows people in Singapore, Hong Kong, and Taiwan when they search for AI.

**By the end of this session you can:**
- run a notebook cell by cell
- turn what you practiced in the puzzle page (dictionaries, paths into a response) into real code
- call an API and change the query, country, and language
- turn the raw response into a table
- ask an AI assistant to explain code, and predict output before you run it
- keep your API key secret

**Today there is no debugging.** The code is a working template. You change a few values and read what happens. If a cell fails, ask a facilitator for help (see below) and keep going. Debugging starts in Week 2.

**Rule for every step:** write your prediction *before* you run the cell. The gap between what you expected and what happened is where you learn.
""")

md("""
## How this session runs

- There is **no lecture** in the coding session. You will be in a breakout room with a partner, and the facilitators visit the rooms.
- **Start with the puzzle page**, Cactus Code Garden (about 30 minutes; your facilitator will post the link). Come back here for Step 3b when you reach the last level.
- **Stuck?** Try these, in order, for no more than 5 minutes:
  1. Read the last line of any error message. What is it telling you?
  2. Re-read the instructions for the step. Did you skip a part?
  3. Ask your partner, then ask an AI assistant to explain the message (never paste your API key).
  4. Still stuck? Click **Ask for help** in Zoom or message the facilitators in the main chat. Say what you expected, what happened, and what you already tried.
- Use the AI freely for explanations. You are still responsible for checking what it says.
""")

md("""
## Step 1: Set up your API key

Your key is like a password. Do not paste it into a chat with an AI, a shared notebook, or GitHub.

1. Sign up for a free account at https://serpapi.com and copy your API key from the dashboard.
2. In Colab, click the **key icon** in the left sidebar (Secrets).
3. Click **Add new secret**. Name: `SERPAPI_KEY`. Value: your key.
4. Switch on **Notebook access** for this notebook.

Ideally you did this before the session. If not, it takes about 10 minutes now.

No key, or ran out of searches? A facilitator will give you `serp_cache.zip`. Upload it in the Colab file panel (folder icon on the left, then the upload icon), then run the second cell below. You can then do everything except brand-new searches.
""")

code("""
import os

try:
    from google.colab import userdata
    API_KEY = userdata.get("SERPAPI_KEY")
except Exception:
    API_KEY = os.environ.get("SERPAPI_KEY")

print("Key found:", bool(API_KEY))
""")

md("""
**Key found: False?** Check that the secret is named exactly `SERPAPI_KEY` (capital letters, no spaces), that **Notebook access** is switched on, and run the cell again. If it still says False, use the saved results below.
""")

code("""
# Only needed if a facilitator gave you serp_cache.zip
import zipfile
if os.path.exists("serp_cache.zip"):
    zipfile.ZipFile("serp_cache.zip").extractall(".")
    print("Saved results unpacked:", len(os.listdir("serp_cache")), "files")
else:
    print("No serp_cache.zip found. That is fine if your key works.")
""")

md("""
## Step 2: What is an API?

Think of ordering at a restaurant. You do not walk into the kitchen. You send an order in a fixed format (dish, size, table number), and the kitchen sends back the dish.

An API works the same way:
- **Your order** is the *parameters*: what to search for (`q`), which country (`gl`), which language (`hl`).
- **The kitchen** is SerpAPI, which asks Google for you.
- **The dish** is the *response*, usually JSON: nested labeled data.

**Predict before you continue:** if you search the same words in Singapore and in Taiwan, would the results be the same? Why or why not? Write your guess here:

> My prediction:
""")

code(HELPERS)

md("""
## Step 3: Your first search

**Predict:** how many results will come back? What will the first one be about?

> My prediction:
""")

code("""
data = search(q="artificial intelligence", gl="sg", hl="en", engine="google")

# The raw response is a dictionary. These are its top-level labels:
print(list(data.keys()))
""")

md("""
The response has many parts. Which label do you think holds the actual search results? Check by running the next cell. It turns the results into a table.
""")

code("""
table = results_table(data, engine="google", place="Singapore")
print(len(table), "results")
table[["position", "title", "source"]]
""")

md("""
**Compare:** how close was your prediction? Pick one row and open its link to confirm the table matches the real page.
""")

md("""
## Step 3b: Your puzzle skills in real code (about 20 min)

You practiced these ideas in the Cactus Code Garden. Now do three short tasks. Each ends with a check (`assert`) that stops with a message if something is wrong. **A cell that prints nothing after the print lines means the check passed.**

**Task 1: your project row.** Replace the example with the row you built in level 16 of the puzzle page (use its Copy button), then run it.
""")

code("""
# Task 1: replace this example with your own row from the puzzle page
row = {
    "text": "Love the new cups",
    "country": "Vietnam",
    "likes": 12,
}
print(list(row.keys()))
print(row[list(row.keys())[0]])
assert len(row) >= 3, "Add at least three fields"
""")

md("""
**Task 2: read the response.** `data` is the Singapore search from Step 3. **Predict** what the next cell prints, then run it. The path is the kind you built in world 6 of the puzzle page.
""")

code("""
first_title = data["organic_results"][0]["title"]
print(first_title)
assert first_title == table.loc[0, "title"], "Not the same as the table: check your path"
""")

md("""
**Task 3: ask an AI, then check it.** First write down your own path to the **link of the second result**. Then paste this prompt into your AI assistant:

> I have a Python dictionary called `data` from a SerpAPI Google search. Write one line of Python that gets the link of the second organic result. Explain each `[ ]` in plain English.

Paste the AI's line in place of `None`, run it, and compare with your own guess.

> My own path (before asking the AI):
""")

code("""
second_link = None   # paste the AI's line here, e.g. second_link = data[...]...
print(second_link)
assert second_link == table.loc[1, "link"], "Not the same as the table: check the path"
""")

md("""
**Log it** in the verification log (row 3b): your prediction, what the AI wrote, and the check you ran.
""")

md("""
## Step 4: Your turn. Change one thing at a time

The cell below is the one you are meant to edit. Change **one** value, run it, and note what changed.

| Parameter | What it controls | Examples |
|---|---|---|
| `q` | What to search for | `"ChatGPT"`, `"AI jobs"`, `"人工智能"` |
| `gl` | Country the search comes from | `"sg"`, `"hk"`, `"tw"`, `"cn"`, `"my"` |
| `hl` | Language of the results | `"en"`, `"zh-TW"`, `"zh-CN"` |
| `engine` | Which Google product | `"google"` (web), `"google_news"` (news) |

Each new search uses one API credit. Repeating a search you already ran is free, because it is saved.

**No key? You can only run the searches that were saved.** These are the saved ones:

| Place | `q` | `gl` | `hl` | `engine` |
|---|---|---|---|---|
| Singapore | `"artificial intelligence"` | `"sg"` | `"en"` | `"google"` or `"google_news"` |
| Hong Kong | `"人工智能"` | `"hk"` | `"zh-TW"` | `"google"` or `"google_news"` |
| Taiwan | `"人工智慧"` | `"tw"` | `"zh-TW"` | `"google"` or `"google_news"` |

The one-value change that works for everyone is `engine`: switch between `"google"` and `"google_news"` for the same place. With a key you can change any value, and the other tables above explain what each one does.
""")

code("""
# YOUR TURN: change one value at a time, then run.
MY_SEARCH = dict(
    q="artificial intelligence",
    gl="sg",
    hl="en",
    engine="google_news",
)

my_data = search(**MY_SEARCH)
my_table = results_table(my_data, engine=MY_SEARCH["engine"], place=MY_SEARCH["gl"])
print(len(my_table), "results")
my_table[["position", "title", "source"]].head(10)
""")

md("""
**Write down:** what did you change, what did you expect, and what happened?

> Changed: &nbsp;&nbsp; Expected: &nbsp;&nbsp; Happened:
""")

md("""
## Step 5: Compare three places (homework if you run short on time)

Now run the same topic across Singapore, Hong Kong, and Taiwan, using each place's own language and wording. Note that "artificial intelligence" is written differently: 人工智能 in Hong Kong and mainland China, 人工智慧 in Taiwan.

**Predict:** which sources (news sites, companies, Wikipedia) will show up in all three places? Which will be unique?

> My prediction:
""")

code("""
PLACES = [
    # (place, country gl, language hl, search text)
    ("Singapore", "sg", "en", "artificial intelligence"),
    ("Hong Kong", "hk", "zh-TW", "人工智能"),
    ("Taiwan", "tw", "zh-TW", "人工智慧"),
]
ENGINES = ["google", "google_news"]

import pandas as pd

tables = []
for place, gl, hl, q in PLACES:
    for engine in ENGINES:
        raw = search(q=q, gl=gl, hl=hl, engine=engine)
        tables.append(results_table(raw, engine=engine, place=place))

all_results = pd.concat(tables, ignore_index=True)
print(len(all_results), "results in total")
all_results.groupby(["place", "engine"]).size()
""")

code("""
# The three most common sources in each place and engine
top_sources = (
    all_results.groupby(["place", "engine"])["source"]
    .value_counts()
    .groupby(level=[0, 1])
    .head(3)
)
top_sources
""")

md("""
**Discuss with your partner:**
1. How close was your prediction?
2. Which sources appear in more than one place?
3. What does the different wording (人工智能 vs 人工智慧) suggest about how each place talks about AI?
4. Search results depend on the day, your location, and Google's choices. What would you need to record so someone else could repeat this search?
""")

md("""
## Step 6: Ask an AI to explain the code

You have run code you did not write. Now use an AI assistant to understand it. **Do not paste your API key.**

1. Copy the `search` function from the helper cell above.
2. Paste it into your AI assistant with this prompt:

> I am a beginner and I don't know Python. Explain this function line by line in plain English. Then tell me three things that could go wrong when I run it.

3. Read the answer, then test one claim it made. For example: it says results are saved to a folder. Open the Colab file panel and check that the folder `serp_cache` exists and has files in it.

**Log it:** what did the AI say, what did you check, and was it right?

> AI claim: &nbsp;&nbsp; My check: &nbsp;&nbsp; Result:
""")

md("""
## Step 7: Save your results (homework, after Step 5)

This file is your starting data for Week 2, where you will clean and chart it.
""")

code("""
# utf-8-sig keeps Chinese characters readable when you open the file in Excel
all_results.to_csv("week01_results.csv", index=False, encoding="utf-8-sig")
print("Saved", len(all_results), "rows to week01_results.csv")

try:
    from google.colab import files
    files.download("week01_results.csv")
except Exception:
    print("Not in Colab, so the file stayed in this folder.")
""")

md("""
## Verification log (Week 1)

Fill in at the end of the session.

| Step | What I predicted | What happened | One thing I checked |
|---|---|---|---|
| 3 | | | |
| 3b | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |

## Stretch (optional)

- Search for a topic from **your own research** in two places.
- Try `engine="google_news"` with a term from your field and compare the sources.
- Ask the AI: "What other questions could I answer by comparing search results across countries?"
""")

nb = nbf.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
nbf.write(nb, OUT)
print("wrote", os.path.normpath(OUT))
