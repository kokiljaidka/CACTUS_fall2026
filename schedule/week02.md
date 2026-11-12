# Week 2: Clean it, chart it, check what the AI wrote

**Theme:** AI as pair programmer. Students read, test, and distrust AI code.
**Format:** Zoom. Learning session is a lecture with live demos; coding session is breakout rooms with no lecture. Between them, students do a 20-minute practice page.

## Objectives

By the end of the week, students can:
1. Load and clean a table (column names, dates, duplicates) and explain each step.
2. Say what each cleaning step does to the row count, and why each removed row was removed.
3. Prompt with context: column names, sample rows, desired output.
4. Run at least three kinds of checks: row counts before and after, a hand count of a few rows, and comparing a result with a second method.
5. Find mistakes in AI-written code without being told where they are.
6. Read an error message, explain it in their own words, then fix it.

## Data

| Session | Dataset | Why |
|---|---|---|
| Learning (walk-through) | `data/lululemon_instagram.csv` | Real engagement data with a natural trap: 91% of posts have 0 views |
| Practice page and notebook warm-up | `data/week02_toy_cafe.csv` (30 invented rows; also embedded in the notebook) | Small enough to count by hand. Planted: 3 duplicates, 2 rows with no text, 2 dates in another format, scores stored as text |
| Coding (exercises) | `data/starbucks_sea_comments.csv` | Multilingual comments from 7 SE/East Asian places. Has duplicates, missing text, text stored as dates, uneven group sizes |

<!-- facilitator:start -->
See [data/README.md](../data/README.md). Students use a different dataset in each part so they can't pattern-match. The toy table is rebuilt by `python3 scripts/week02_toy_data.py`.
<!-- facilitator:end -->

<!-- facilitator:start -->
## Materials

| What | Where |
|---|---|
| Practice page: Silent Changes | `practice/week02_silent_changes.html` (private Artifact; share its link). Source in `practice/src/week02/` |
| Lecture slides (13 slides) | `slides/week02_clean_it_chart_it.html` and `.pdf` (source in `slides/src/week02/`, with speaker notes) |
| Notebook | `notebooks/week02_clean_and_chart.ipynb` |
| Rebuild commands | `python3 scripts/build_practice.py` and `python3 scripts/build_week02_notebook.py` |
<!-- facilitator:end -->

## Required reading

From *Computational Analysis of Communication* ([cssbook.net](https://cssbook.net)), the Python version. Required, not graded.

- **Before the learning session:** [Chapter 5, From file to data frame and back](https://cssbook.net/content/chapter05.html), sections 5.1 to 5.2.
- **Before the coding session:** [Chapter 6, Data wrangling](https://cssbook.net/content/chapter06.html), sections 6.1 to 6.4 (filtering, calculating, grouping, merging), and [Chapter 4, How to write code](https://cssbook.net/content/chapter04.html), section 4.2 (understanding errors and getting help).

<!-- facilitator:start -->
Section titles were checked against the chapter pages on cssbook.net (Nov 2026), but the chapter contents have not been reviewed for this course. Skim them before the week. The book predates AI coding assistants and assumes you type the code yourself.
<!-- facilitator:end -->

<!-- facilitator:start -->
## Prep

- Share `data/starbucks_sea_comments.csv` with students (a shared Drive link, so they can upload it to Colab in seconds).
- Share the Silent Changes link after the learning session.
- Kokil runs the walk-through once, including the Lululemon check.
- Do the practice page and the notebook warm-up yourself. Try a trap card (drop rows with missing tone) to see what students see.
- Facilitators: read `instructor/facilitator_guide.md` (Week 2 section), `instructor/week02_answer_key.md`, and `instructor/week02_practice_key.md`. All are local only.
- Facilitators should do Exercise 2 themselves beforehand, without the key.
<!-- facilitator:end -->

---

## Learning session (about 2 h): lecture with live demos

Kokil leads; facilitators watch the chat and help anyone who falls behind.

| Time | Activity |
|---|---|
| 0:00 | **Concept: what is a table?** Rows, columns, types, missing values, and why messy data is normal. No syntax yet. |
| 0:20 | **Walk-through: good vs bad prompt** (Lululemon). Ask for "the average views per post" first with no context, then again after pasting column names and a sample. Read the code line by line. |
| 1:00 | **Walk-through: verification.** Run the AI's average views (2,506). Then check: how many posts have 0 views? Show that the code is correct but the question was wrong. Show `len()` before and after, `.head()`, and a hand count. |
| 1:30 | **Walk-through: reading an error.** Trigger a real error, read the last line aloud, paste to the AI, and explain why the fix works. |
| 1:50 | **Preview:** the Silent Changes page (do it before the coding session), the stuck protocol, and the exercises. |

<!-- facilitator:start -->
### Lecture plan (slides)

| # | Slide | Notes |
|---|---|---|
| 1 | Recap of Week 1 | The project card, dictionaries and lists, the key habit: predict before you run |
| 2 | What is a table? | Rows are things, columns are facts about them. One row of your project is what you wrote on your card |
| 3 | Types | Number, text, date, true/false. A number stored as text looks the same and behaves differently |
| 4 | Missing and messy | Empty cells, "N/A", duplicates. Messy is normal, not a failure |
| 5 | Demo: the prompt with no context | Lululemon: "average views per post". Show what the AI guesses |
| 6 | Demo: the prompt with context | Paste column names and sample rows. Read each line of the answer |
| 7 | Demo: a right answer to the wrong question | 2,506 average, but 91% of posts have 0 views. Code correct, question wrong |
| 8 | Three checks | Row count before and after; hand count of a few rows; compare with a second method |
| 9 | Demo: `len()` and `.head()` | Show how a step changes the row count |
| 10 | Reading an error | Last line first. Say it in your own words, then fix |
| 11 | Silent changes | The idea behind the practice page: steps that remove or change rows without an error |
| 12 | Next steps | The practice page (20 min), then the coding session. Stuck protocol |
<!-- facilitator:end -->

---

## Between sessions (about 20 min): practice page

Students open **Silent Changes** after the learning session and before the coding session.

- **Level 1:** build a cleaning pipeline from cards and watch the row-count waterfall. Some cards quietly damage the data.
- **Levels 2 to 4:** click the buggy line in AI-written code that runs without any error, then pick the check that proves it.
- **Level 5:** the Colab bridge, which hands them the code for their pipeline.

This page uses bug types **different** from the live Exercise 2, so it does not give that exercise away.

---

## Coding session (about 2 h): breakout rooms, no lecture

Notebook: `notebooks/week02_clean_and_chart.ipynb`. Pairs in breakout rooms; mix experienced and new students where possible (the survey's experience items help). Facilitators visit rooms. Exercises 1 to 3 are required; 4 and 5 are stretch.

| Time | Exercise |
|---|---|
| 0:00–0:10 | **Warm-up:** write the pipeline from the practice page as real code on the small café table. The notebook's check cell tells you if it is clean. |
| 0:10–0:15 | Load the Starbucks data and predict the shape. Note one surprise. |
| 0:15–0:40 | **Ex 1:** pair prompting (rename, parse dates, deduplicate, count). One prompts, one reviews; swap each task. Task 1d is optional if time is short. |
| 0:40–1:00 | **Ex 2:** bug hunt. Three planted bugs in an "AI-written" analysis. |
| 1:00–1:15 | **Ex 3:** read three errors, guess the cause, then fix with AI help. |
| 1:15–1:30 | **Ex 4 (stretch):** a paper-ready chart, checked against the numbers. |
| 1:30–1:50 | **Ex 5 (stretch):** own data. AI lists problems; students verify each by hand. |
| 1:50–2:00 | Log; optional share-out in the main room. |

Post a time check in the main chat at each boundary. Hints for Exercise 2 come from facilitators only, using the ladder in the answer key.

## Homework (45 minutes or less)

- Finish Exercise 5 on your own data.
- Add to your project card (`project/designing_your_project.md`): what could go wrong in my data, and how would I check?

## Hand-off to Week 3

Students leave with a cleaned dataset and a verification log. Week 3 moves from checking cleaning code to checking *statistics* code.
