# Week 2: Clean it, chart it, check what the AI wrote

**Theme:** AI as pair programmer. Students read, test, and distrust AI code.
**Format:** Zoom. Learning session is a supervised walk-through; coding session is breakout rooms with no lecture.

## Objectives

By the end of the week, students can:
1. Load and clean a table (column names, dates, duplicates) and explain each step.
2. Prompt with context: column names, sample rows, desired output.
3. Run at least three kinds of checks: row counts before and after, a hand count of a few rows, and comparing a result with a second method.
4. Find mistakes in AI-written code without being told where they are.
5. Read an error message, explain it in their own words, then fix it.

## Data

| Session | Dataset | Why |
|---|---|---|
| Learning (walk-through) | `data/lululemon_instagram.csv` | Real engagement data with a natural trap: 91% of posts have 0 views |
| Coding (exercises) | `data/starbucks_sea_comments.csv` | Multilingual comments from 7 SE/East Asian places. Has duplicates, missing text, text stored as dates, uneven group sizes |

See [data/README.md](../data/README.md). Students use a different dataset in the exercises than in the walk-through so they can't pattern-match.

## Prep

- Share `data/starbucks_sea_comments.csv` with students (a shared Drive link, so they can upload it to Colab in seconds).
- Kokil runs the walk-through once, including the Lululemon check.
- Facilitators: read `instructor/facilitator_guide.md` (Week 2 section) and `instructor/week02_answer_key.md`. Both are local only.
- Facilitators should do Exercise 2 themselves beforehand, without the key.

## Learning session (about 2 h): supervised walk-through

Kokil leads; facilitators watch the chat and help anyone who falls behind.

| Time | Activity |
|---|---|
| 0:00 | **Concept: what is a table?** Rows, columns, types, missing values, and why messy data is normal. No syntax yet. |
| 0:20 | **Walk-through: good vs bad prompt** (Lululemon). Ask for "the average views per post" first with no context, then again after pasting column names and a sample. Read the code line by line. |
| 1:00 | **Walk-through: verification.** Run the AI's average views (2,506). Then check: how many posts have 0 views? Show that the code is correct but the question was wrong. Show `len()` before and after, `.head()`, and a hand count. |
| 1:30 | **Walk-through: reading an error.** Trigger a real error, read the last line aloud, paste to the AI, and explain why the fix works. |
| 1:50 | **Preview the exercises** and the stuck protocol. |

## Coding session (about 2 h): breakout rooms, no lecture

Notebook: `notebooks/week02_clean_and_chart.ipynb`. Pairs in breakout rooms; mix experienced and new students where possible (the survey's experience items help). Facilitators visit rooms. Exercises 1 to 3 are required; 4 and 5 are stretch.

| Time | Exercise |
|---|---|
| 0:00–0:10 | Load data and predict the shape. Note one surprise. |
| 0:10–0:40 | **Ex 1:** pair prompting (rename, parse dates, deduplicate, count). One prompts, one reviews; swap each task. |
| 0:40–1:00 | **Ex 2:** bug hunt. Three planted bugs in an "AI-written" analysis. |
| 1:00–1:15 | **Ex 3:** read three errors, guess the cause, then fix with AI help. |
| 1:15–1:30 | **Ex 4 (stretch):** a paper-ready chart, checked against the numbers. |
| 1:30–1:50 | **Ex 5 (stretch):** own data. AI lists problems; students verify each by hand. |
| 1:50–2:00 | Log; optional share-out in the main room. |

Post a time check in the main chat at each boundary. Hints for Exercise 2 come from facilitators only, using the ladder in the answer key.

## Homework (45 minutes or less)

- Finish Exercise 5 on your own data.
- Add to your project card: what could go wrong in my data, and how would I check?

## Hand-off to Week 3

Students leave with a cleaned dataset and a verification log. Week 3 moves from checking cleaning code to checking *statistics* code.
