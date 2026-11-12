"""Build notebooks/week02_clean_and_chart.ipynb. Re-run after editing."""
import os

import nbformat as nbf

HERE = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.insert(0, HERE)
import week02_toy_data  # noqa: E402
OUT = os.path.join(HERE, "..", "notebooks", "week02_clean_and_chart.ipynb")
cells = []


def md(t):
    cells.append(nbf.v4.new_markdown_cell(t.strip()))


def code(t):
    cells.append(nbf.v4.new_code_cell(t.strip()))


md("""
# Week 2: Clean it, chart it, and check what the AI wrote

**CACTUS Fall 2026 · Coding session**

**Data:** about 4,000 public comments mentioning Starbucks, collected 5–14 October 2024 from Thailand, Vietnam, Malaysia, the Philippines, Singapore, Indonesia, and Hong Kong. The comments are in many languages.

**Goals today**
- load, clean, and chart a table with an AI assistant's help
- find mistakes in AI-written code *without being told where they are*
- read an error message and explain it before fixing it
- check your own data for problems

**Order**
0. The warm-up (10 minutes) comes first. Do it after the puzzle page.
1. Exercises 1–3 are required. Task 1d is optional if time is short.
2. Exercises 4–5 are stretch. Do them if you finish early; Exercise 5 can be homework.

**Rules**
- Predict before you run.
- Never accept AI code you have not read.
- Every cell you keep needs a note on how you checked it.
- Do not paste personal information or API keys into an AI chat.

**Run cells one at a time**, not "Run all". Some cells are broken on purpose.
""")

md("""
## How this session runs

- There is **no lecture** in the coding session. You will be in a breakout room with a partner, and the facilitators visit the rooms.
- **Stuck?** Try these, in order, for no more than 5 minutes:
  1. Read the last line of any error message. What is it telling you?
  2. Re-read the instructions for the step. Did you skip a part?
  3. Ask your partner, then ask an AI assistant to explain the message (do not paste private data).
  4. Still stuck? Click **Ask for help** in Zoom or message the facilitators in the main chat. Say what you expected, what happened, and what you already tried.
- Use the AI freely for explanations and code. You are still responsible for checking what it says.
""")

code("""
import os
import pandas as pd

DATA_FILE = "starbucks_sea_comments.csv"
if not os.path.exists(DATA_FILE):
    try:
        from google.colab import files
        print("Choose starbucks_sea_comments.csv from your computer")
        files.upload()
    except ImportError:
        raise SystemExit("Put starbucks_sea_comments.csv in this folder first.")

raw = pd.read_csv(DATA_FILE)
print(raw.shape)
""")

md("""
**Predict:** how many rows and columns did you expect? Look at the numbers above. Then run the next cell and note one thing in the data that surprises you.

> Surprise:
""")

code("""
raw.head()
""")

code("""
raw.info()
""")

md("""
---
## Warm-up: the pipeline from the puzzle page (about 10 min)

On the Silent Changes puzzle page you built a cleaning pipeline and watched the row count change. Now write it as real code on the same small table. You can write it yourself, paste the code the page generated, or ask your AI assistant. Whichever you choose, **read every line before you run it**.

The table is 30 invented café comments with planted problems. The cell below loads it.
""")

code("""
import io

TOY_CSV = """ + '"""' + week02_toy_data.to_csv_text() + '"""' + """
toy = pd.read_csv(io.StringIO(TOY_CSV))
print(toy.shape)
toy.head(8)
""")

md("""
**Predict:** how many rows will be left after you remove duplicates and rows with no comment text? Write your guess, then build the pipeline in the next cell.

> My prediction:
""")

code("""
# Paste your pipeline here. Start from a fresh copy of the table, and print len(df) after each step.
df = toy.copy()
counts = {"start": len(df)}

""")

code("""
# Check. A cell that prints only the last line means every check passed.
assert not df.duplicated().any(), "Duplicate rows are still there"
assert df["comment"].notna().all(), "Rows with no comment text are still there"
assert str(df["date"].dtype).startswith("datetime"), "date is still text"
assert pd.api.types.is_float_dtype(df["tone_pos"]), "tone_pos is still text"
assert len(df) == 25, f"Expected 25 rows but found {len(df)}. Which step removed rows it should not have, or missed some?"
print("Clean:", len(df), "rows")
""")

md("""
> **Log (warm-up):** which check caught a mistake, or confirmed your code was right? Did the AI's code match what you built on the page?
""")

md("""
---
## Exercise 1: Pair prompting (required, about 25 min)

Work in pairs. **One person prompts, the other reviews and decides whether to accept the code.** Swap roles after each task.

**How to prompt well.** Give the AI the context it cannot see:

> I have a pandas DataFrame called `raw` loaded from a CSV with columns: *(paste the output of `list(raw.columns)`)*. Here are the first 3 rows: *(paste `raw.head(3)`)*. **Task:** ... Write the code, then explain each line in one sentence.

**Reviewer's job:** read every line. Ask "what does this do to my data?" Reject code you cannot explain.

| Task | What to ask for | How to check it |
|---|---|---|
| **1a** | Rename columns to lowercase with underscores (`Post Date` → `post_date`) | Print `list(df.columns)` and compare with the original |
| **1b** | Turn the post date into a real date column | Check the earliest and latest date and the number of rows before and after |
| **1c** | Remove duplicate rows | Pick one `Post ID` that appears twice. Count its rows before and after |
| **1d** | Count comments per country, and per day | Add up the counts. Do they equal the number of rows you have? |

Paste the AI's code below, run it, and run your check.
""")

code("""
# Task 1a: paste the AI's code here, then run it.
""")
code("""
# Check 1a:
""")
code("""
# Task 1b:
""")
code("""
# Check 1b:
""")
code("""
# Task 1c:
""")
code("""
# Check 1c:
""")
code("""
# Task 1d:
""")
code("""
# Check 1d:
""")

md("""
> **Log (Exercise 1):** What did the AI get wrong, or what check did you run? Did you reject any code, and why?
""")

md("""
---
## Exercise 2: Bug hunt (required, about 20 min)

Below is an analysis an AI assistant wrote for someone else. It runs without errors and produces a chart and a table. **It contains three mistakes that change the answer.** Find them without being told where they are.

**What to do**
1. Run the cell and look at the output. Does anything look strange?
2. Read each numbered step. What does each line do to the data?
3. For each suspected bug, **prove it** with a check (row counts, a hand count of a few rows, comparing with a different method). Write down the check.
4. Fix the code and compare the corrected result with the original.

**Hints.** If you are stuck for more than 5 minutes, ask a facilitator for a hint. The places to look are: how many rows each step keeps, what the dates look like on the chart, and what each number is the average *of*.
""")

code("""
# ---- AI-written analysis. Do not edit this cell; copy it to a new one to fix. ----
data = pd.read_csv(DATA_FILE)

# 1. Remove duplicate comments
clean = data.drop_duplicates(subset="Content").copy()
print("Removed", len(data) - len(clean), "duplicate comments")

# 2. Comments per month
clean["date"] = pd.to_datetime(clean["Post Date"], format="%Y-%d-%m %H:%M:%S", errors="coerce")
clean = clean.dropna(subset=["date"])
monthly = clean.groupby(clean["date"].dt.to_period("M")).size()
monthly.plot(kind="bar", title="Starbucks comments per month, 2024")

# 3. How positive are the comments in each country?
positive = clean[clean["tone_pos"] > 0]
by_country = positive.groupby("Channel Country")["tone_pos"].mean().round(1)
print("Average positivity (%) by country:")
print(by_country)
""")

md("""
**Write down each bug you find** (what was wrong, how you proved it, what changed after the fix):

| # | What was wrong | My check | Result after fix |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
""")

code("""
# Your fixed version here.
""")

md("""
---
## Exercise 3: Read the error (required, about 15 min)

Each cell below fails. For each one, **before** you ask an AI:
1. Read the last line of the message. What kind of error is it?
2. Say in your own words what Python is complaining about.
3. Guess the fix.

Then paste the full message to an AI assistant, compare its explanation with your guess, apply the fix, and explain in one sentence *why it works*.

Run these cells one at a time. They are supposed to fail.
""")

code("""
# 3a
raw["Channel country"].value_counts()
""")
code("""
# 3b
fresh = pd.read_csv(DATA_FILE)
fresh["Post Date"].dt.day.value_counts()
""")
code("""
# 3c
fresh.groupby("Channel Country")["Channel Language"].mean()
""")

md("""
| Cell | My guess | What the AI said | The fix and why it works |
|---|---|---|---|
| 3a | | | |
| 3b | | | |
| 3c | | | |
""")

md("""
---
## Exercise 4: A chart you could put in a paper (stretch, about 15 min)

Ask an AI for a chart of the **average share of positive words (`tone_pos`) by country**, using your cleaned data from Exercise 1. Then ask it to make the chart ready for a paper: axis labels with units, readable fonts, a title that states what is shown.

**Check before you trust it**
- Does the number of bars equal the number of countries (7)?
- Print `df.groupby("channel_country")["tone_pos"].mean()`. Do the bar heights match?
- Is the average over *all* comments, or a subset?
- Some countries have very few comments (Hong Kong has 13). What does that mean for how much weight a bar deserves?
""")

code("""
# Chart code here.
""")

md("""
---
## Exercise 5: Your own data (stretch, about 20 min; can be homework)

Load your own dataset into a new DataFrame. Then ask an AI:

> Here is the output of `df.info()` and `df.head()` for my dataset *(paste it. Do not paste private data)*. List the data quality problems you can see: missing values, wrong types, duplicates, odd values. For each one, say how I could confirm it in code.

**Verify every claim by hand.** The AI may report problems that are not there, or miss ones that are.

| Claimed problem | Check I ran | Real or not? |
|---|---|---|
| | | |
""")

code("""
# Load your own data here.
""")

md("""
---
## Log: what I learned today

- One thing the AI got wrong, or a check that caught a problem:
- One prompt that worked well, and why:
- One question I still have:

**Homework (45 min or less):** finish Exercise 5 on your own data, and add to your project card: what could go wrong in my data, and how would I check?
""")

nb = nbf.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
nbf.write(nb, OUT)
print("wrote", os.path.normpath(OUT))
