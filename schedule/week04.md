# Week 4: Collect your own data

**Theme:** Collecting data is a set of choices with consequences: what you may collect, what you save, what you protect. Students get their own access to a platform, then collect posts, save the raw response first, log what they did, and anonymize.
**Format:** Zoom. A 1-hour learning session (lecture with live demos), a 20-minute practice page, then a 2-hour coding session in breakout rooms with no lecture. About 3 hours live.

<!-- facilitator:start -->
> **Status: draft for review.** Not on the student site yet. The biggest risk is **platform access**, which students sort out themselves and which changes often. See the plan and decisions at the end of this file.
<!-- facilitator:end -->

## Objectives

By the end of the week, students can:
1. Get their own access to a platform, and store the key safely.
2. Collect posts through an API or an export, and save the raw response before changing anything.
3. Explain what a platform's terms, consent, and ethics approval allow for their data.
4. Anonymize a dataset (replace usernames, drop links) and check that it worked.
5. Plan collection around limits: a request quota, a page size, a pause between requests.
6. Record what was collected, when, how, and with which query, so someone else could repeat it.
7. Compare what was collected with what was saved and what was parsed, to catch silent loss.

## Get access before the session

**Start in Week 2 or 3, not Week 4.** Some platforms take days to approve. See [Getting data access](../project/getting_data_access.md) for the questions to answer and a shared table of what works.

- Week 2 homework: choose where your project's data will come from, and start applying.
- Week 3: an optional **access clinic** (30 minutes) for anyone stuck.
- Week 4: you should have a working key, or know exactly what you are waiting for. If you are still waiting, use the saved sample or an export (see Data).

## Data

| Session | Dataset | Why |
|---|---|---|
| Learning (walk-through) | One live request, using a facilitator's access | Everyone sees the same raw response |
| Practice page | None (field and scenario cards) | The ethics and planning decisions are the point |
| Coding (exercises) | **Route A (main):** your own collection from the platform you got access to. **Route B:** a small saved sample (about 100 items, no key needed) for anyone still waiting. **Route C:** an export you already have | No one is blocked, and most people collect their own |

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
| Notebook | `notebooks/week04_collect_your_own_data.ipynb` (built; run top to bottom with a correct solution on Route B; Route A cells are added by the platform owners) |
| Saved sample (Route B) | `data/week04/sample/` (built by `scripts/make_week04_sample.py`: invented, in the shape of a real API response, safe for the public repo. No real data and no key needed) |
| Ethics checklist | `project/ethics_checklist.md` (drafted as questions only; Kokil or an ethics-aware facilitator should review it and add the contact) |

## Prep

- **Assign each facilitator a platform to own** (for example YouTube, Bluesky, Reddit). Each owner gets access themselves, writes down exactly what worked, and fills in that row of the access table with the date. Do this before Week 2 ends.
- Run the access clinic in Week 3 with the platform owners.
- Make the small saved sample (about 100 items, a few pages) from one owner's access, for a topic about AI in Singapore, Hong Kong or Taiwan. Check the terms allow sharing a small sample with students.
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
| 0:25 | **What an API response looks like.** Live: one request with a facilitator's access, the raw JSON, a page of results, the limit on requests. |
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

Notebook: `notebooks/week04_collect_your_own_data.ipynb`. Students choose a route at the start; pairs may use different routes. Pair people on the same platform where possible. Exercises 1 to 4 are required.

| Time | Exercise |
|---|---|
| 0:00–0:15 | **Warm-up:** the collection stub from the practice page. Save raw, log the query and date, and count. |
| 0:15–0:45 | **Ex 1:** collect your own data (Route A), or work from the saved sample (Route B), or load your export (Route C). Save the raw data. |
| 0:45–1:15 | **Ex 2:** parse to a table and **compare counts**: how many raw items, how many rows, and why any difference? |
| 1:15–1:40 | **Ex 3:** anonymize. Replace usernames with IDs, drop links, and write a check that no username or link column remains. |
| 1:40–1:55 | **Ex 4:** write your **data card** for your own project: what, when, how, which terms and ethics apply. |
| 1:55–2:00 | Log; optional share-out. |

**Stretch:** a second query, a second platform, or a collection that survives hitting the request limit.

Post a time check in the main chat at each boundary. **Never paste an API key into an AI chat.**

## Homework (45 minutes or less)

- Finish your data card and add it to your project card.
- Add what you learned about access to the shared table in [Getting data access](../project/getting_data_access.md).
- If your collection is small or still pending, plan how you will get enough by Week 6 or 7.

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
- **Ex 1, collect (30 min):** a short cell per platform (written by each platform owner once access is verified), or load the saved sample (Route B), or load your export (Route C). Raw data is saved untouched.
- **Ex 2, parse (30 min):** parse the raw data into the standard table. **Check:** items collected = items saved = rows parsed, or explain each difference. `item_id` must be unique.
- **Ex 3, anonymize (25 min):** replace usernames with `author_id`, remove handles and links from `text`, coarsen timestamps if the time of day is not needed. **Check:** an `assert` that no username column, `@`, or `http` remains.
- **Ex 4, data card (15 min):** a short template: what, when, how, which terms, which ethics process, known gaps.
- **Stretch:** pagination with a pause, or a second query.

### Practice page: Before you collect (`practice/week04_before_you_collect.html`)
1. **Sort the fields.** Cards for the fields of a typical post export. For a stated research question, sort each into keep, anonymize, or drop. The feedback names the risk.
2. **Re-identification meter.** Switch fields on and off (exact time, a rare phrase, a small place) and watch a rough risk indicator change.
3. **Plan the pull.** A quota and page-size puzzle: collect N items with a daily request limit. Order the steps (save raw first, then parse, then anonymize) and choose a pause.
4. **Ask first.** Four short scenarios. For each, choose: fine to proceed, check first, or do not collect. The feedback says who to ask. It gives no legal advice.
5. **Colab bridge:** the collection stub, with an `assert` that counts match.

### Slides (11, in `slides/src/week04/`)
As in the lecture plan above. Notes include a live request with a facilitator's access, so the platform owner must prepare one working example.

### Ethics checklist (`project/ethics_checklist.md`)
One page the practice page points to: public or private, terms of use, ethics approval, personal and sensitive data, anonymization, storage, sharing, and who to ask. Written by Kokil or the ethics-aware facilitator, not by the AI.

### Timeline (assuming Week 4 is on 8 December)
| By | What |
|---|---|
| Nov 24 (Week 2) | Students told to start access (Week 2 homework). Platform owners start verifying their platform |
| Dec 1 (Week 3) | Optional access clinic. Platform rows of the access table verified. Small saved sample made |
| Dec 1 | Notebook, practice page, and slides ready, so the facilitators can rehearse |
| Dec 8 | Week 4 sessions |

## Decisions and open items (Week 4)

1. **Platform owners.** Who owns which platform, and by when must each have verified access and updated the table?
2. **Saved sample.** Decided: an invented sample (no real data), so no terms check is needed. A real one from a platform owner is optional.
3. **Ethics paragraph.** Who writes it, and what does your university require? Students need one clear paragraph, not a debate.
4. **Access clinic.** Is a Week 3 clinic worth the extra 30 minutes for facilitators? It is optional for students.
5. **Route C students.** Some will bring an export. Decide how facilitators help without seeing private data.
6. **Students who cannot get access.** Route B (the saved sample) is the safety net. Decide whether it is enough, or whether you want a second one.
<!-- facilitator:end -->
