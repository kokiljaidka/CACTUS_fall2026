# Week 1: Define your problem, and how code thinks

**Theme:** AI as explainer. Students leave with a finished project card and a first feel for how code works. No debugging this week.
**Format:** Zoom. The learning session is a lecture and guided activity; the coding session is breakout rooms with no lecture.

## Objectives

By the end of the week, students can:
1. State a case study, one main research question, and two or three sub-questions, and say what one row of their data is.
2. Explain, in plain words, variables, lists, dictionaries, functions with parameters, and loops.
3. Read a nested response (a dictionary of lists of dictionaries) and write the path to one value.
4. Run a Colab notebook cell by cell, predict the output first, and compare.
5. Call SerpAPI (or use saved results) and change the query, country, and language.
6. Ask an AI assistant to explain code, and test one of its claims.
7. Keep an API key secret (Colab Secrets, never in a chat, notebook, or repo).

<!-- facilitator:start -->
## Materials

| What | Where |
|---|---|
| Project guide and card | [project/designing_your_project.md](../project/designing_your_project.md) |
| Puzzle page: Cactus Code Garden (16 puzzles, then a Colab task) | `practice/week01_cactus_code_garden.html` (published as a private Artifact; share the link from its Share menu). Source in `practice/src/week01/` |
| Notebook | `notebooks/week01_first_api_calls.ipynb` |
| Saved searches (no key needed) | `data/week01/serp_cache.zip` (made by `scripts/cache_week1.py`) |
<!-- facilitator:end -->

## Reading (optional, no credit)

From *Computational Analysis of Communication* (van Atteveldt, Trilling & Arcila, open access):
- **Before Session 1:** Chapter 1, Introduction (skim).
- **Before Session 2:** Chapter 3, Programming concepts for data analysis. It covers the ideas the puzzle page practices. Skim; you do not need to memorize syntax.
- **Later, if curious:** Chapter 4, How to write code.

<!-- facilitator:start -->
Chapter picks are based on the book's table of contents. Skim the sections before assigning, since the book predates AI coding assistants and assumes you type the code yourself.
<!-- facilitator:end -->

## Before the first session

- Create a Google account (for Colab) and have a chat AI assistant ready.
- **Optional:** create a free SerpAPI account and add the key to Colab Secrets as `SERPAPI_KEY`. Everyone can finish Week 1 with the saved searches, so this is not required.
- Bring a topic you care about. A rough idea is enough.

<!-- facilitator:start -->
## Prep (Kokil and facilitators)

- Run `python3 scripts/cache_week1.py` with a key (6 API calls) and give students `data/week01/serp_cache.zip`. Everyone uses it for Step 3 and Step 3b.
- Run the notebook top to bottom in Colab once. The helper code was tested only against mocked responses, so confirm the real results parse (the cache script warns if a search returns nothing).
- Do the puzzle page once, including the Colab task, so you know where students will pause. Levels 6, 11 and 12 to 14 are the ones most students find tricky.
- Decide the fallback data for students with no dataset: `data/starbucks_sea_comments.csv` or `data/lululemon_instagram.csv`.
- Facilitators: read `instructor/facilitator_guide.md` (Week 1 section).
<!-- facilitator:end -->

---

## Session 1 (about 2 h): Learning session. Define your problem

Kokil leads. Facilitators watch the chat and, in the pair activity, visit rooms.

| Time | Activity |
|---|---|
| 0:00 | **Welcome, and "AI writes, you decide."** The 8-week arc, how sessions run, the verification log. One live example of an AI answer that sounds right and is wrong. |
| 0:20 | **What is a researchable problem?** Case study, main question, sub-questions, with two worked examples. |
| 0:45 | **Structures and the doable check.** Pick a structure for your question; then check data, what one row is, what you would measure, and which week teaches the tool. |
| 1:05 | **Hands-on in pairs (breakout rooms).** Draft the project card. Use AI to sharpen it and log what you accepted and rejected. |
| 1:40 | **Sign-off and share-out.** Facilitators check each card against the criteria below. Two or three volunteers read theirs. |
| 1:50 | **What is an API?** Ten minutes: the restaurant analogy (order, kitchen, dish). Preview Session 2. |

<!-- facilitator:start -->
### Lecture plan (slides)

| # | Slide | Notes |
|---|---|---|
| 1 | Title, welcome | Who is here, what the series is, no credit, weekly work builds up |
| 2 | The 8-week arc | One line per week from the README table; Week 1 is today |
| 3 | AI writes, you decide | The four ways AI code goes wrong (silent data loss, invented names, does something else, confident wrong explanations). Show one live example. Then the cycle: describe, read, test, record |
| 4 | How a week works | Learning session, puzzle or coding session, notebook, verification log |
| 5 | What is a case study? | "Social media" is too broad; "How Singapore, Hong Kong and Taiwan users talk about AI chatbots on Reddit" is a case study |
| 6 | One main question, two or three sub-questions | The mental-health example from the guide |
| 7 | Structures | The six templates (predictors, mechanism, comparative, debate, multi-level, problem-cause-intervention). Say they are starting points, not a checklist |
| 8 | A CACTUS example | The Starbucks comparative question; each sub-question maps to something taught in the series |
| 9 | The doable check | Data, size, measure, method, ethics, scope. Too big versus better |
| 10 | Use AI to sharpen, not decide | The prompt from the guide. Log accepted and rejected suggestions |
| 11 | Your task now | The card template; what "finalized" means; time (35 min) |
| 12 | What is an API? | Restaurant analogy; parameters, response, JSON. One slide, no code |
| 13 | Next session | Puzzle page, then the notebook. Optional: SerpAPI key. Bring your card |
<!-- facilitator:end -->

### Sign-off criteria ("finalized")

A card is finished when it has:
- a case study (topic, place, period),
- one main question and two or three sub-questions,
- what one row of the data is, and a data source (the fallback corpus counts),
- one thing to measure for each sub-question.

The question may still change. The point is that every student has something specific to build on.

---

## Session 2 (about 2 h): Coding session. How code thinks

Breakout rooms, pairs (or 3s), no lecture. Facilitators visit rooms; the main room stays open for key and account problems.

| Time | Activity |
|---|---|
| 0:00–0:05 | Setup: open the puzzle page and the notebook; pair up; read the stuck protocol. |
| 0:05–0:40 | **Puzzle page, levels 1 to 16.** Predict first, then run. Behind schedule at 0:40? Do level 16 and skip the rest. |
| 0:40–0:55 | **Notebook Steps 2 and 3:** helper cell, the first search from the saved results, the raw response, the table. |
| 0:55–1:15 | **Step 3b (the Colab bridge):** your project row, the first result's title as a path into the response, and the second result's link written with an AI's help. |
| 1:15–1:35 | **Step 4:** change one thing at a time and record what changed. |
| 1:35–1:50 | **Step 6:** ask an AI to explain the helper code and test one claim. |
| 1:50–2:00 | Fill in the verification log. Optional share-out. |

Post a time check in the main chat at each boundary. Step 1 (the key) is optional today; Step 5 (compare three places) and Step 7 (save results) are homework.

### Stuck protocol (printed in the notebook)

Five minutes max: read the last line of the error, re-read the step, ask the partner, ask an AI. Then click **Ask for help** in Zoom or message the facilitators.

---

## Homework (45 minutes or less)

- Finish the project card if sign-off is pending.
- Notebook Step 5: compare Singapore, Hong Kong and Taiwan, then Step 7 to save `week01_results.csv`.
- Run one search on a topic from your own research in two places and add the results to your CSV.

## Hand-off to Week 2

Students leave with a finished project card, a first search saved to CSV, and a verification log. Week 2 builds on the same habits (prompt with context, check output) using a different dataset.
