# Week 4: Collect your own data

**Theme:** Collecting data is a set of choices with consequences: what you may collect, what you save, what you protect. Students bring data they already have (an export from Twitter/X, Instagram, Facebook, Reddit, or Bluesky), or use a saved example. They save the raw data first, log what they did, parse it into one standard table, and anonymize.
**Format:** Zoom. A 1-hour learning session (lecture with live demos), a 20-minute practice page, then a 2-hour coding session in breakout rooms with no lecture. About 3 hours live.

<!-- facilitator:start -->
> **Status: built and on the site.** The biggest risk is **students arriving with no data**. Decided: two routes only. **Route A** is an export they already have; **Route B** is the invented saved example. Facilitators can help with Twitter/X, Instagram, Facebook, Reddit, and Bluesky data. Students without data should talk to the facilitators offline in Week 1 and have data before Week 3. See the plan and decisions at the end of this file.
<!-- facilitator:end -->

## Objectives

By the end of the week, students can:
1. Bring their own data (an export), or work from a saved example, and know where it came from.
2. Save the raw data untouched before changing anything, and keep a log.
3. Explain what a platform's terms, consent, and ethics approval allow for their data.
4. Anonymize a dataset (replace usernames, drop links) and check that it worked.
5. Explain how collection through an API is paced: a request quota, a page size, a pause between requests.
6. Record what was collected, when, how, and with which query, so someone else could repeat it.
7. Compare what was collected with what was saved and what was parsed, to catch silent loss.

## Get your data before the session

**If you do not have data yet, talk to the facilitators offline in Week 1.** Do not wait until Week 4. You should have your data by Week 3. The facilitators can help with Twitter/X, Instagram, Facebook, Reddit, and Bluesky data. See [Getting data access](../project/getting_data_access.md) for how to get data and a shared table of what works, and the [Ethics checklist](../project/ethics_checklist.md) for the questions to answer before you collect.

- Week 1: if you do not have data for your project yet, tell the facilitators. Talk to them offline.
- Week 3: you should have your data (or a firm plan agreed with a facilitator).
- Week 4: bring your export. If you still have no data, use the saved example (see Data) and keep working with the facilitators so you have data before Week 6.

## Data

| Session | Dataset | Why |
|---|---|---|
| Learning (walk-through) | The saved example, shown as a raw response (optionally one live request from a facilitator) | Everyone sees the same raw response |
| Practice page | None (field and scenario cards) | The ethics and planning decisions are the point |
| Coding (exercises) | **Route A (main):** an export you already have, from Twitter/X, Instagram, Facebook, Reddit, Bluesky, or another source. **Route B:** the saved example (about 100 items, no key needed) for anyone who does not have data yet | No one is blocked, and most people work on their own data |

## Required reading

From *Computational Analysis of Communication* ([cssbook.net](https://cssbook.net)), the Python version. Required, not graded.

- **Before the learning session:** [Chapter 12](https://cssbook.net/content/chapter12.html), section 12.4 (ethical, legal, and practical considerations).
- **Before the coding session:** Chapter 12, section 12.1 (web APIs), and [Chapter 5](https://cssbook.net/content/chapter05.html), section 5.3 (data from online sources).

<!-- facilitator:start -->
## Materials

| What | Where |
|---|---|
| Lecture slides (11 slides) | `slides/week04_collect_your_own_data.html` and `.pdf` for students; `..._presenter.html` (press N for the script) and `..._handout.pdf` for the facilitator team. Source and notes: `slides/src/week04/` (built) |
| Access guide | `project/getting_data_access.md` (drafted; the platform table must be verified) |
| Practice page: Before you collect | `practice/week04_before_you_collect.html` (built; source in `practice/src/week04/`) |
| Notebook | `notebooks/week04_collect_your_own_data.ipynb` (built; run top to bottom with a correct solution on both routes: Route B 100 entries to 97 rows, Route A a small fake export) |
| Saved example (Route B) | `data/week04/sample/` (built by `scripts/make_week04_sample.py`: invented, in the shape of a real API response, safe for the public repo. No real data and no key needed) |
| Ethics checklist | `project/ethics_checklist.md` (questions only; Kokil is the named contact) |

## Prep

- **In Week 1, ask every student whether they already have data** for their project, and talk to those who do not, offline. Facilitators can help with Twitter/X, Instagram, Facebook, Reddit, and Bluesky data. Agree who helps whom.
- Each facilitator writes in the access table what they know about the platform they help with: how a student gets an export, and what to check. Do this before Week 3.
- Run the optional access clinic in Week 3 for anyone still without data.
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
| 0:25 | **What a raw response looks like.** The saved example (or one live request, if a facilitator wants): the raw JSON, a page of results, the limit on requests. |
| 0:38 | **Collect safely.** Save raw first. Log the query and date. Pause between requests. Count what you got. |
| 0:50 | **Preview:** the practice page, the reading, and the two routes for the coding session. |

<!-- facilitator:start -->
### Lecture plan (slides)

| # | Slide | Min | Notes |
|---|---|---|---|
| 1 | Title | 1 | The plan for the week |
| 2 | From given data to collected data | 4 | Every choice has a consequence |
| 3 | What you may collect | 5 | Terms, consent, ethics approval; ask when unclear |
| 4 | Public is not the same as free to use | 5 | Examples; no legal advice |
| 5 | Anonymization | 6 | Replace names, drop links; why that is not enough |
| 6 | Demo: a raw response | 8 | The saved example is enough; JSON, one page, the request limit |
| 7 | Demo: save, log, count | 8 | Raw first; query and date; raw versus parsed counts |
| 8 | Pagination and rate limits | 5 | A quota is a plan, not a surprise |
| 9 | The data card | 4 | What, when, how, ethics |
| 10 | Before the coding session | 4 | Practice page, reading, two routes |
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

Notebook: `notebooks/week04_collect_your_own_data.ipynb`. Students choose a route at the start; pairs may use different routes. Pair people on the same platform where possible, and put students without data next to someone with an export. Exercises 1 to 4 are required.

| Time | Exercise |
|---|---|
| 0:00–0:15 | **Warm-up:** the collection stub from the practice page. Save raw, log the query and date, and count. |
| 0:15–0:45 | **Ex 1:** put your export in `raw/` untouched and write the log (Route A), or collect the saved example (Route B). |
| 0:45–1:15 | **Ex 2:** parse to a table and **compare counts**: how many raw items, how many rows, and why any difference? |
| 1:15–1:40 | **Ex 3:** anonymize. Replace usernames with IDs, drop links, and write a check that no username or link column remains. |
| 1:40–1:55 | **Ex 4:** write your **data card** for your own project: what, when, how, which terms and ethics apply. |
| 1:55–2:00 | Log; optional share-out. |

**Stretch:** read the paging loop and explain each line, or run the standard table on a second dataset.

Post a time check in the main chat at each boundary. **Never paste an API key into an AI chat.**

## Homework (45 minutes or less)

- Finish your data card and add it to your project card.
- If you do not have your own data yet, talk to the facilitators now and agree how you will get enough before Week 6.
- Add what you learned about getting data to the shared table in [Getting data access](../project/getting_data_access.md).

## Hand-off to Week 5

Students leave with raw data saved, a parsed table, an anonymized version, and a data card. Week 5 turns the text in a corpus into numbers, using the students' own text where they have it.

<!-- facilitator:start -->
## Build plan (Week 4)

### One standard table, for every platform
Every route ends in the same tidy table, so Weeks 5 to 7 work on anyone's data. The worked example (`project/example_track_gendered_incivility.md`) needs exactly these columns.

| Column | What it holds | Used in |
|---|---|---|
| `item_id` | The platform's ID for the post or comment | Counting, deduplication (Week 2 habits) |
| `parent_id` | The item it replies to; empty for a top-level post | Reply structure, networks (Week 7) |
| `thread_id` | The post or video the item sits under | Coding comments in context (Week 6) |
| `created_at` | Date (and time, if you keep it; see anonymization) | Time charts |
| `author_id` | A pseudonymous ID, never the username | Counting authors, networks |
| `text` | The text, with handles and links removed | Weeks 5 and 6 |
| `like_count` | Likes or score | Simple models (Week 3 methods) |
| `platform`, `source`, `query`, `collected_on` | Where it came from, and when | The data card, reproducibility (Week 8) |

### Notebook outline (`notebooks/week04_collect_your_own_data.ipynb`)
- **Warm-up (15 min):** the collection stub: save raw first, write a log (query, date, tool, limits), count.
- **Ex 1, raw data (30 min):** Route A: copy the export into `raw/` untouched and write the log. Route B: collect the 4 pages of the example. Raw data is saved untouched.
- **Ex 2, parse (30 min):** parse the raw data into the standard table. **Check:** items collected = items saved = rows parsed, or explain each difference. `item_id` must be unique.
- **Ex 3, anonymize (25 min):** replace usernames with `author_id`, remove handles and links from `text`, coarsen timestamps if the time of day is not needed. **Check:** an `assert` that no username column, `@`, or `http` remains.
- **Ex 4, data card (15 min):** a short template: what, when, how, how the posts were chosen, which terms, which ethics process, who holds the raw files, known gaps.
- **Stretch:** explain the paging loop, or a second dataset.

### Practice page: Before you collect (`practice/week04_before_you_collect.html`)
1. **Sort the fields.** Cards for the fields of a typical post export. For a stated research question, sort each into keep, anonymize, or drop. The feedback names the risk.
2. **Re-identification meter.** Switch fields on and off (exact time, a rare phrase, a small place) and watch a rough risk indicator change.
3. **Plan the pull.** A quota and page-size puzzle: collect N items with a daily request limit. Order the steps (save raw first, then parse, then anonymize) and choose a pause.
4. **Ask first.** Four short scenarios. For each, choose: fine to proceed, check first, or do not collect. The feedback says who to ask. It gives no legal advice.
5. **Colab bridge:** the collection stub, with an `assert` that counts match.

### Slides (11, in `slides/src/week04/`)
As in the lecture plan above. The raw-response demo can use the saved example. A live request is optional, and if a facilitator does one, they hide the key and any real people's names.

### Ethics checklist (`project/ethics_checklist.md`)
One page the practice page points to: public or private, terms of use, ethics approval, personal and sensitive data, anonymization, storage, sharing, and who to ask. Written by Kokil or the ethics-aware facilitator, not by the AI.

### Timeline (assuming Week 4 is on 8 December)
| By | What |
|---|---|
| Nov 17 (Week 1) | Students without data talk to the facilitators offline. Facilitators note who needs help with which platform |
| Nov 24 (Week 2) | Students get or request their data (Week 2 homework) |
| Dec 1 (Week 3) | Students have their data. Optional access clinic. Platform rows of the access table written |
| Dec 1 | Notebook, practice page, and slides ready, so the facilitators can rehearse |
| Dec 8 | Week 4 sessions |

## Decisions and open items (Week 4)

1. **Facilitator platforms.** Decided: facilitators help with Twitter/X, Instagram, Facebook, Reddit, and Bluesky data. Who helps with which, and by when must each have noted what students should do?
2. **Saved example.** Decided: an invented sample (no real data), so no terms check is needed.
3. **Ethics paragraph.** Who writes it, and what does your university require? Students need one clear paragraph, not a debate.
4. **Access clinic.** Is a Week 3 clinic worth the extra 30 minutes for facilitators? It is optional for students.
5. **Facilitators and private data.** Students will bring real exports. Decide how facilitators help without seeing private data (for example by looking only at column names).
6. **Students with no data.** Route B is the safety net for the day. Decide the cut-off, and who works with each student so they have data before Week 6.
<!-- facilitator:end -->
