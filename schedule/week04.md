# Week 4: Collect your own data

**Theme:** Collecting data is a set of choices with consequences: what you may collect, what you save, what you protect. Students leave knowing how to collect posts, save the raw response first, log what they did, and anonymize.
**Format:** Zoom. A 1-hour learning session (lecture with live demos), a 20-minute practice page, then a 2-hour coding session in breakout rooms with no lecture. About 3 hours live.

<!-- facilitator:start -->
> **Status: draft for review.** Not on the student site yet. The biggest risk this week is **platform access**, which changes often. See the decisions at the end of this file.
<!-- facilitator:end -->

## Objectives

By the end of the week, students can:
1. Collect posts through an API or an export, and save the raw response before changing anything.
2. Explain what a platform's terms, consent, and ethics approval allow for their data.
3. Anonymize a dataset (replace usernames, drop links) and check that it worked.
4. Plan collection around limits: a request quota, a page size, a pause between requests.
5. Record what was collected, when, how, and with which query, so someone else could repeat it.
6. Compare what was collected with what was saved and what was parsed, to catch silent loss.

## Data

| Session | Dataset | Why |
|---|---|---|
| Learning (walk-through) | Saved responses from one platform, shown live | Everyone sees the same raw response without needing a key |
| Practice page | None (field and scenario cards) | The ethics and planning decisions are the point |
| Coding (exercises) | **Route A:** live collection from a platform the student has access to. **Route B:** saved raw responses in `data/week04/` (no key needed). **Route C:** an export the student already has | No student is blocked by access |

The saved responses (Route B) are made by `scripts/cache_week4.py` with a key, in the same way as Week 1.

## Required reading

From *Computational Analysis of Communication* ([cssbook.net](https://cssbook.net)), the Python version. Required, not graded.

- **Before the learning session:** [Chapter 12](https://cssbook.net/content/chapter12.html), section 12.4 (ethical, legal, and practical considerations).
- **Before the coding session:** Chapter 12, section 12.1 (web APIs), and [Chapter 5](https://cssbook.net/content/chapter05.html), section 5.3 (data from online sources).

<!-- facilitator:start -->
## Materials

| What | Where |
|---|---|
| Lecture slides (about 11 slides) | `slides/week04_*` (to build) |
| Practice page: Before you collect | `practice/week04_before_you_collect.html` (to build; spec in `practice/page_specs.md`) |
| Notebook | `notebooks/week04_collect_your_own_data.ipynb` (to build) |
| Saved responses | `data/week04/` from `scripts/cache_week4.py` (to build) |
| Ethics checklist | `project/ethics_checklist.md` (to write; the practice page points to it) |

## Prep

- **Verify platform access at least a week ahead.** For each platform (Bluesky, YouTube comments, Reddit, or others students want): what an account needs, whether an API key or approval is required, rate limits, and whether the terms allow research use. These change often, so do not rely on memory or on this file.
- Make the saved responses (Route B) with your own key, for one platform and a topic about AI in Singapore, Hong Kong or Taiwan.
- Do each route yourself before the session, including saving and anonymizing.
- Check what your university's ethics process requires for collecting public social media data, and write one honest paragraph for students. Do not give legal advice.
- Facilitators: read `facilitators/practice_pages_guide.md`.
<!-- facilitator:end -->

---

## Learning session (about 1 h): lecture with live demos

| Time | Activity |
|---|---|
| 0:00 | **Recap and the idea.** So far you analyzed data you were given. Now you decide what data exists. |
| 0:05 | **What counts as permitted.** Platform terms, public versus private, consent, ethics approval. Where the rules are unclear, ask. |
| 0:15 | **Anonymization.** What removing a username does and does not protect. A combination of details can still identify someone. |
| 0:25 | **What an API response looks like.** Live: one saved response, the raw JSON, a page of results, the limit on requests. |
| 0:38 | **Collect safely.** Save raw first. Log the query and date. Pause between requests. Count what you got. |
| 0:50 | **Preview:** the practice page, the reading, and the three routes for the coding session. |

<!-- facilitator:start -->
### Lecture plan (slides)

| # | Slide | Min | Notes |
|---|---|---|---|
| 1 | Title | 1 | The plan for the week |
| 2 | From given data to collected data | 4 | Every choice has a consequence |
| 3 | What you may collect | 5 | Terms, consent, ethics approval; ask when unclear |
| 4 | Public is not the same as free to use | 5 | Examples; no legal advice |
| 5 | Anonymization | 6 | Replace names, drop links; why that is not enough |
| 6 | Demo: a raw response | 8 | JSON, one page, the request limit |
| 7 | Demo: save, log, count | 8 | Raw first; query and date; raw versus parsed counts |
| 8 | Pagination and rate limits | 5 | A quota is a plan, not a surprise |
| 9 | The data card | 4 | What, when, how, ethics |
| 10 | Before the coding session | 4 | Practice page, reading, three routes |
| 11 | Questions | 5 | Leave room for ethics questions |
<!-- facilitator:end -->

---

## Between sessions (about 20 min): practice page

Students open **Before you collect** after the learning session and before the coding session.

- **Sort the fields:** for a stated research question, decide whether each field of a typical post export is kept, anonymized, or dropped.
- **Re-identification meter:** combine fields and watch a rough risk indicator rise.
- **Plan the pull:** a quota and pagination scenario; order the steps; choose a pause.
- **Colab task:** write a collection stub that saves raw first, drops the chosen fields, and logs the query and date.

---

## Coding session (about 2 h): breakout rooms, no lecture

Notebook: `notebooks/week04_collect_your_own_data.ipynb`. Students choose a route at the start; pairs may use different routes. Exercises 1 to 4 are required.

| Time | Exercise |
|---|---|
| 0:00–0:15 | **Warm-up:** the collection stub from the practice page. Save raw, log the query and date, and count. |
| 0:15–0:45 | **Ex 1:** collect (Route A), or work from the saved responses (Route B), or load your export (Route C). Save the raw data. |
| 0:45–1:15 | **Ex 2:** parse to a table and **compare counts**: how many raw items, how many rows, and why any difference? |
| 1:15–1:40 | **Ex 3:** anonymize. Replace usernames with IDs, drop links, and write a check that no username or link column remains. |
| 1:40–1:55 | **Ex 4:** write your **data card** for your own project: what, when, how, which terms and ethics apply. |
| 1:55–2:00 | Log; optional share-out. |

**Stretch:** a second query, a second platform, or a collection that survives hitting the request limit.

Post a time check in the main chat at each boundary. **Never paste an API key into an AI chat.**

## Homework (45 minutes or less)

- Finish your data card and add it to your project card.
- If you have not collected data for your own project, plan how and when you will. Week 5 uses a shared corpus, but you need your own data by Week 6 or 7.

## Hand-off to Week 5

Students leave with raw data saved, a parsed table, an anonymized version, and a data card. Week 5 turns the text in a corpus into numbers.

<!-- facilitator:start -->
## Decisions and open items (Week 4)

1. **Which platforms to support.** Suggestion: one platform with the lowest barrier (such as Bluesky, if its public access still works without approval), one with a familiar key flow (such as YouTube comments), and saved responses for everyone. Confirm all three at least a week ahead.
2. **Reddit.** Its access terms have been restrictive in recent years. Verify the current position before promising it.
3. **Ethics paragraph.** Who writes it, and what does your university require? Students need one clear paragraph, not a debate.
4. **Saved responses.** Who runs `scripts/cache_week4.py`, with which key, and for what query? Check the terms for redistributing saved responses before putting them in a public repository.
5. **Route C students.** Some will bring an export. Decide how facilitators help without seeing private data.
<!-- facilitator:end -->
