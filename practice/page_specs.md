# Practice pages: specs

One short interactive page per week. Each page is a warm-up before the coding session, not a replacement for the notebook. This file is the plan; nothing here is built except Week 1.

Status: **Weeks 1 and 2 built** (Cactus Code Garden, Silent Changes). Weeks 3 to 8 are drafts for review.

Build with `python3 scripts/build_practice.py`. Each page is made from `practice/shared/` (theme and drag engine) plus `practice/src/weekNN/` (head, body, page code), and written to `practice/`.

## What a practice page is for

Each page has two parts, and neither replaces the notebook:

1. **Brush-up (10 to 15 min, no typing).** Drag, sort, and check puzzles that fix the week's lecture concepts. This runs in the browser.
2. **Colab bridge (15 to 20 min, real code).** The page ends with a short coding task for the student's own Colab notebook. They (or their AI assistant) write the code, read it, run it, and verify it against a check built into the task, then log how they checked.

Pages cannot run real Python: a browser page can't load Python tooling under its sandbox, and a hand-written imitation would drift from real Python. So coding always happens in Colab. The page's job is to make the concept clear enough that the Colab task is quick.

**Bridge rules**
- Three to eight lines of code at most. Small, concrete, runnable.
- Uses the week's real data or a tiny CSV supplied for that purpose.
- Ends with a **self-check** (an `assert` or a printed number to compare with the page) so the student knows whether it worked without a facilitator.
- Students may use AI to write it; the log records one check they ran.
- Where the page produces something (a dictionary, a pipeline order, a codebook), the page offers a **Copy** button so the student pastes it into Colab and builds on it.

| Week | Colab bridge (student writes or prompts, then verifies) | Self-check |
|---|---|---|
| 1 | Paste the project row from level 16 into a cell, print one field, then pull the first result's title out of a saved search response with `data[...][...][...]` | `assert` the title is a string; compare with the path built in the page |
| 2 | Write the pandas steps in the order chosen on the page and print `len(df)` after each | Row counts match the waterfall |
| 3 | Simulate data with a chosen true effect, fit a regression, then repeat 100 times in a loop | The estimate's interval covers the truth in about 95 of 100 runs |
| 4 | Write a collection stub: save the raw response first, drop the fields chosen on the page, write a one-line log of query and date | `assert` no username or link column remains |
| 5 | Tokenize five texts two ways and print the counts | Counts differ in the way the page predicted, including for Chinese |
| 6 | Compute accuracy, Cohen's kappa, and a confusion table from two label lists | Numbers match the page's example |
| 7 | **Network:** compute degree for a small edge list and remove the most connected node. **Feed:** sort posts by a chosen ranking rule | Top node or top post matches the page |
| 8 | Restart and run all on your own notebook, and fix the first failure | The notebook runs top to bottom with no errors |

## Principles (apply to every page)

1. **Predict, then run.** Wherever a result appears, ask for a guess first and compare afterwards. This is the series-wide habit.
2. **Check, don't trust.** Every page contains at least one result that looks right but is wrong. The student must find out why with a check they could run in the notebook (row counts, hand count, second method, known answer).
3. **Same objects as the notebook.** Use the same column names, function names, and datasets (or a clearly marked toy version) so the page transfers.
4. **No spoilers.** Pages use different cases from the notebook exercises. Answer keys stay in `instructor/` (gitignored) and are never embedded in a page's source in readable form that students are told to avoid reading. Assume a curious student will view source.
5. **No keys, no personal data.** Pages run entirely in the browser. No API calls, no key fields, no student data collected. Text comes from the already-anonymized shared CSVs.
6. **Phone and keyboard friendly.** Tap as an alternative to drag; a keyboard path for every action; works at phone width and in light and dark themes.
7. **Short.** About 15 minutes for the brush-up, plus the Colab bridge. Done = the student can say what a result does and does not show, and has run the bridge code.
8. **Progress stays local.** Per-browser only (localStorage). Facilitators can't see completion; the weekly verification log remains the record.

## Shared build approach

- Single self-contained HTML file per page, built from small parts: a shared drag-and-drop engine, a shared theme, and page-specific content.
- Keep the shared parts in `practice/shared/` and have a build script (like `scripts/build_week0N_notebook.py`) inline them, so every published page is self-contained.
- Page source lives in `practice/weekNN_name.html`. Week 1's source is not in the repo yet and should be added.
- Reusable from Week 1: drag engine, slot puzzles, path builder, theme tokens, feedback and hint pattern, level map.
- Each page ends with a link or note pointing to that week's notebook exercise.

## Effort scale

| Size | Meaning |
|---|---|
| S | Recombines existing parts; mostly content writing |
| M | One new interactive mechanic, or a small calculation |
| L | Several new mechanics, or real computation and charts |

---

## Week 1: First API calls and how code thinks (built)

**Goal:** variables, lists and dictionaries, functions and parameters, loops, reading nested JSON, and writing one project row as a dictionary.
**Page:** Cactus Code Garden, 16 levels in 7 worlds.
**Open items:** add its source to the repo; link it from `schedule/week01.md`; decide whether level 16's output should go into the project card template.

---

## Week 2: Clean it, chart it, check what the AI wrote

**Learning goals**
- Describe what each cleaning step does to the row count and to the answer.
- Recognize that code can run without errors and still be wrong.
- Prove a suspected bug with a check.

**Notebook link:** Exercise 2 (bug hunt) and Exercise 1 (cleaning).

**Spoiler rule:** the page must use bug types **different** from the notebook's Exercise 2 (the list of those bugs is in `instructor/`, not here), so it doesn't give away the live exercise.

**Page: "Silent changes"** (two parts)

*Part A: Build the pipeline.*
- A toy table of about 30 rows of invented café comments (columns like `Content`, `Date`, `Country`, `tone_pos`) with planted problems: exact duplicates, blank text, dates stored as text, a number stored as text.
- Step cards to drag into order: drop duplicates, drop blanks, parse dates, convert types, filter. Each card has a short code line.
- A live **row-count waterfall** shows how many rows each step keeps and what the final average becomes.
- Task: reach a clean table of the right size and say which step removed what. Wrong orders or wrong keys produce a visibly different count.

*Part B: Find the bug.*
- Show 12 lines of "AI-written" code and its output. The student clicks the line they suspect, then picks the check that would prove it from a short menu (row count before and after, hand count of 3 rows, compare with a second method).
- Reveal runs the check on the toy data and shows what changes.
- Bug types to use (none from the notebook): average of group averages when groups differ in size, an inner join that silently drops unmatched rows, a case-sensitive match that misses "starbucks", `head()` treated as the whole data, the wrong column (original text where translated text was needed).
- Three bug rounds, each with its own toy output.

**Success feedback:** after each round, say which check exposes the bug and what number changes.
**Reuses:** drag engine, feedback pattern. **New:** row-count waterfall, clickable code lines.
**Risks:** keep the toy table small enough to hand-count. Avoid making it look like the Starbucks file.
**Effort:** M.
**Needs:** toy table and bug scripts (small content job). Answer key goes in `instructor/`.

---

## Week 3: Verify and analyze

**Learning goals**
- Know that an estimate varies from sample to sample, and what a confidence interval says.
- See that a "significant" result can be tiny, and that a non-significant one can be real but under-powered.
- See how an ignored confounder biases an estimate.
- Compare any AI-written statistics against a known answer.

**Notebook link:** the simulated dataset (not built yet; design below) and the "test AI code against known truth" exercise.

**Page: "Planted-effect lab"**

*Part A: One study.*
- The page simulates a dataset in the browser: an outcome, a treatment, and optionally a confounder. Sliders: true effect, noise, sample size.
- It computes the group means and a regression estimate with a 95% confidence interval and shows them beside the **true** effect.
- Prediction first: "With n = 20, will the estimate land near the truth?"

*Part B: Run it again.*
- A button runs 100 studies and draws their intervals in one chart. The student sees how many cover the truth and how widely estimates scatter at small n.
- A prompt asks them to find the smallest n at which they would trust one study.

*Part C: The confounder.*
- Toggle a confounder that affects both treatment and outcome. Show the estimate with and without adjusting for it, against the truth.

*Part D: Check the AI.*
- Three "AI answers" (an estimate and a sentence of interpretation). The student decides, using the known truth, which are plausible, and picks the sentence that over-claims ("proves", "caused" without design).

**Reuses:** feedback pattern, theme. **New:** simulation, simple regression and interval, a small SVG chart of 100 intervals.
**Risks:** keep statistics honest. Use the t distribution or say clearly that the interval is approximate. Don't teach p-value thresholds as a decision rule.
**Effort:** L (the largest page).
**Needs:** agree the dataset story with the notebook so the numbers and names match.

---

## Week 4: Collect your own data

**Learning goals**
- Save raw data before changing it.
- Describe what a platform's terms and consent allow.
- Anonymize, and recognize when anonymization is not enough.
- Plan collection around quotas and pagination.

**Notebook link:** the collection exercise and the ethics checklist.

**Page: "Before you collect"** (three small tasks)

1. **Sort the fields.** Cards for the fields in a typical post export (post text, username, profile link, timestamp, location tag, number of likes, language). The student drags each into keep, anonymize, or drop, for a stated research question. Feedback names the risk for each.
2. **Re-identification meter.** Combine fields (rare phrase, exact time, small place) and watch a rough risk indicator rise, to show that removing the username alone isn't enough.
3. **Plan the pull.** A quota-and-pagination scenario: collect N posts with a request limit and a page size. The student orders the steps (save the raw response first, then clean, then log the query and date) and picks a pause time that avoids rate limits.

**Reuses:** drag engine and ordering puzzle. **New:** sorting cards, a simple risk indicator.
**Risks:** don't give legal advice. State that rules differ by platform and by ethics approval, and point to the course's checklist.
**Effort:** S.
**Needs:** a short ethics checklist in the repo for the page to point to.

---

## Week 5: Analyze text

**Learning goals**
- Explain how tokenizing choices change counts, including for Chinese.
- See what a sentiment lexicon gets wrong.
- Read a cluster or topic result critically.

**Notebook link:** counting, tokenizing, sentiment, topics on the shared AI-in-SG/HK/TW corpus (not built yet).

**Page: "What counts as a word?"**

- **Tokenizer picker.** About 8 short example texts (English, Chinese, mixed). The student chooses a tokenizer (whitespace, characters, word segmentation, subwords) and sees the token list and the count. Chinese examples show why whitespace gives one giant token.
- **Lexicon sentiment.** Drag words in and out of a small positive/negative lexicon and watch scores on a gallery of tricky texts (negation, sarcasm, a brand name that is also a sentiment word). The student marks which scores they'd trust.
- **Stretch: read a cluster.** A precomputed 2D scatter of comments; click a point to read it and name a cluster, then see whether the labels hold up across clusters.

**Data note:** all tokenizations and the 2D layout are **precomputed** by a script and embedded. Don't attempt Chinese segmentation or embeddings in the browser.
**Reuses:** feedback pattern. **New:** precomputed tokenization display, lexicon editor, optional scatter.
**Risks:** depends on the corpus, which isn't built yet. Use texts from the existing Starbucks CSV until then.
**Effort:** M to L. Treat the scatter as optional.

---

## Week 6: AI as annotator

**Learning goals**
- Write label definitions that cover edge cases.
- Compare model labels with human labels using accuracy, agreement, and a confusion matrix.
- Report where the model fails.

**Notebook link:** the codebook and LLM-labeling exercise.

**Page: "Codebook and agreement lab"**

1. **Label 20 texts yourself** using a short codebook (3 to 4 labels, with one deliberately ambiguous label).
2. **See the model's labels.** These come from a **precomputed** LLM run on the same 20 items, so no API is called. The page shows agreement as it is computed: accuracy, Cohen's kappa, and a confusion matrix, with an explanation of why accuracy alone can mislead when one label is common.
3. **Where it fails.** The student sorts the disagreements into causes (unclear definition, sarcasm, language issue, truly ambiguous, human slip).
4. **Revise the codebook.** Choose among edge-case rules to add. A second precomputed run shows how agreement changes with the revised codebook.

**Reuses:** feedback pattern, drag engine for sorting. **New:** confusion matrix and kappa calculation (small).
**Risks:** the quality of the page depends on running a real LLM labeling pass once and keeping its actual errors. Don't invent errors. Record the model and date used.
**Effort:** M.
**Needs:** 20 texts with trusted human labels (from the hand-coded subset), two LLM runs.

---

## Week 7: Choose a track

Only build the tracks students actually pick (use the planning survey).

**Track A: Networks, "Who connects whom?"**
- A small graph (about 20 nodes) from a mock reply network. Drag nodes; the page shows degree and a simple centrality measure.
- Remove a node and watch the network split. The student predicts which node matters most before checking.
- Teaches: centrality depends on what an edge means.

**Track B: Mock feed, "Rank the feed"**
- Ten posts. Toggle ranking signals (newest, most liked, similar to what you liked) and see the order change and which author groups gain or lose visibility.
- Teaches: design choices shape exposure; connect to the mock-experiment setup.

**Track C: Images and memes**
- Defer. It needs images, and rights and privacy are harder to handle. Consider a coding exercise with placeholder images instead.

**Reuses:** drag engine. **New:** a small graph layout and centrality, ranking logic.
**Effort:** M per track.
**Risk:** do not build all tracks speculatively.

---

## Week 8: Reproduce and present

**Learning goals**
- Rerun a whole pipeline from scratch and find what breaks.
- State what a result does and doesn't show.

**Notebook link:** the final reproduction and presentation steps.

**Page: "Run it from scratch"**
- A simulated notebook of about 8 cells. The student presses "Restart and run all" and sees the failure: a variable defined in a cell that was later deleted, a cell run out of order, a hard-coded local path, and a key pasted into a cell.
- The student fixes each (reorder, define, use a relative path, move the key to Secrets) and re-runs until it is clean.
- **Claims check:** four sample result statements. The student sorts each into supported, partly supported, or not supported by the shown numbers, and writes the limitation sentence they would add.
- A reproducibility checklist the student can copy into their final write-up.

**Reuses:** ordering and fix puzzles. **New:** a notebook-like cell runner with hidden state.
**Effort:** S to M.

---

## Suggested order and sizes

| Order | Week | Size | Why now |
|---|---|---|---|
| 1 | 2 | M | Next to run; teaches the check habit |
| 2 | 6 | M | Highest value for an AI-annotation course |
| 3 | 3 | L | Largest; needs the simulated data story settled |
| 4 | 4 | S | Quick win |
| 5 | 8 | S to M | Needed by the end |
| 6 | 5 | M to L | Wait for the corpus |
| 7 | 7 | M each | After the survey shows track choices |

## Open questions

1. Should pages be linked from the weekly schedule file, the notebook, or both?
2. Do you want the page source in this repo (recommended) or only published?
3. For Weeks 2, 3 and 6: should the page's toy data be generated by a script in `scripts/` so the numbers can be rebuilt?
4. Should level 16 of Week 1 (the project row) feed into the project card template?
