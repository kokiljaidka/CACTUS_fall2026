# Week 1: First API calls

**Theme:** AI as explainer. Students run a working template, no debugging.
**Format:** Zoom. Learning session is a supervised walk-through; coding session is breakout rooms with no lecture.

## Objectives

By the end of the week, students can:
1. Run a Colab notebook cell by cell and predict output before running.
2. Call SerpAPI and change the query (`q`), country (`gl`), and language (`hl`).
3. Turn a raw JSON response into a table.
4. Ask an AI assistant to explain code, and test one of its claims.
5. Keep an API key secret (Colab Secrets, never in a chat, notebook, or repo).

## Before the first session (send with the schedule email)

Students should do these **before** the learning session, so the coding session isn't spent on sign-ups:
- Create a Google account (for Colab) and a free SerpAPI account.
- Copy the SerpAPI key and add it to Colab Secrets as `SERPAPI_KEY` (the walk-through shows how, but doing it early helps).
- Have a chat AI assistant account ready.

## Prep (Kokil and facilitators)

- Run `python3 scripts/cache_week1.py` with a key (6 API calls). Give students `data/week01/serp_cache.zip` if they have no key or run out of searches.
- Run the notebook top to bottom in Colab once. The code was only tested against mocked responses, so confirm the real results parse. The cache script warns if a search returns no results.
- Check the free-tier quota. Re-running a search they have already run costs nothing, because results are saved.
- Facilitators: read `instructor/facilitator_guide.md` (Week 1 section).

## Learning session (about 2 h): supervised walk-through

Kokil leads; facilitators watch the chat and help students who fall behind. Students may follow along in Colab.

| Time | Activity |
|---|---|
| 0:00 | **What is an API?** The restaurant analogy: order (parameters), kitchen (service), dish (JSON response). |
| 0:20 | **Walk through one search.** Make a search, show the raw JSON, find where the results are, turn them into a table. Say your predictions out loud. Use a topic that isn't in the notebook (food or sport). |
| 1:00 | **Keys and quotas.** What a key is, what it costs, where it goes (Colab Secrets). What to do if one leaks (regenerate it in the SerpAPI dashboard). |
| 1:20 | **AI as explainer.** Paste the `search` function into an assistant. Read the answer together and test one claim in front of the class. |
| 1:50 | **Preview the coding session** and the stuck protocol (below). |

## Coding session (about 2 h): breakout rooms, no lecture

Notebook: `notebooks/week01_first_api_calls.ipynb`. Pairs (or 3s) in breakout rooms. Facilitators visit rooms. The main room stays open for key and account problems.

| Time | Exercise |
|---|---|
| 0:00–0:20 | **Step 1:** key into Colab Secrets (most students will have done this already). Anyone without a key unpacks `serp_cache.zip`. |
| 0:20–0:40 | **Step 3:** first search and table. Compare prediction with result. |
| 0:40–1:05 | **Step 4:** change one parameter at a time and record what changed. |
| 1:05–1:30 | **Step 5:** compare Singapore, Hong Kong, and Taiwan. Discuss the wording difference (人工智能 vs 人工智慧). |
| 1:30–1:50 | **Step 6:** ask the AI to explain the helper code and test one claim. |
| 1:50–2:00 | **Step 7:** save `week01_results.csv` and fill in the verification log. |

Post a time check in the main chat at each boundary.

## Stuck protocol (printed in the notebook)

Five minutes max: read the last line of the error, re-read the step, ask the partner, ask an AI. Then click **Ask for help** in Zoom or message the facilitators.

## Homework (45 minutes or less)

- Run one search on a topic from your own research in two places and add the results to your CSV.
- Add one line to your project card: what question could comparing search results across places help answer?

## Hand-off to Week 2

Students bring `week01_results.csv`. Week 2 builds on the same skills (prompting with context, checking output) using a different dataset.
