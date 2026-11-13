# Week-by-week run sheets

One sheet per week. Use it with the [facilitator hub](README.md) (roles, rota, stuck protocol, hint ladder) and the slide script (presenter view, press **N**).

**Every week:** learning session (1 hour) and the practice page (20 minutes), then the coding session (2 hours, no lecture). Week 1 is two 2-hour sessions. Post a time check in the main chat at each boundary. Never reveal what a notebook will find: students find the bugs and the surprises.

**Private keys:** the hints for the bug hunts are in the private answer keys. They are not on this site. Ask Kokil for the link.

---

## Week 1: Define your problem, how code thinks (two sessions, about 2 hours each)

**Goal:** every student leaves with a finished project card, and has seen how code thinks (variables, lists, dictionaries, functions, loops, nested data).

**Before:** Lead runs the puzzle page and the notebook once. Check the saved searches zip works. The SerpAPI key is optional for students. Ask each student, before or at Session 1, whether they already have data for their project. Those without data talk offline with a data helper this week.

**Session 1 (learning, about 2 h)**

| Time | What | Notes |
|---|---|---|
| 0:00 | Welcome, "AI writes, you decide", the 8-week arc, the verification log | One live example of an AI answer that sounds right and is wrong |
| 0:20 | What is a researchable problem? | Case study, main question, sub-questions |
| 0:45 | Structures and the doable check | Structures are starting points, not a checklist |
| 1:05 | Breakout rooms: draft the project card | Use AI to sharpen it and log what was accepted and rejected |
| 1:40 | Sign-off and share-out | Check each card against the criteria on the schedule page. Two or three read theirs |
| 1:50 | What is an API? | Ten minutes, the restaurant analogy. Preview Session 2 |

**Session 2 (coding, about 2 h)**

| Time | What |
|---|---|
| 0:00 to 0:05 | Setup: open the puzzle page and the notebook; pair up; read the stuck protocol |
| 0:05 to 0:40 | Puzzle page, levels 1 to 16. Behind at 0:40? Do level 16 and skip the rest |
| 0:40 to 0:55 | Notebook Steps 2 and 3: helper cell, first search from the saved results, the raw response, the table |
| 0:55 to 1:15 | Step 3b (the Colab bridge): the project row, a path into the response, and a link written with an AI's help |
| 1:15 to 1:35 | Step 4: change one thing at a time and record what changed |
| 1:35 to 1:50 | Step 6: ask an AI to explain the helper code and test one claim |
| 1:50 to 2:00 | Fill in the verification log. Optional share-out |

**Watch for:** project cards that are too broad ("social media"); students who skip predicting; the block limit on puzzle levels 9 and 10; people who want a SerpAPI key (it is optional).

---

## Week 2: Clean it, chart it

**Goal:** students clean a table with AI help and check that each step did what they meant (row counts, by hand, a second method).

**Before:** do the practice page, the notebook, and the "silent changes" idea yourself. Have the Lululemon data and the Starbucks file ready for the demos.

**Learning session (1 h):** welcome and recap (0:00); what is a table (0:04); a good and a bad prompt, with the Lululemon data (0:09); verification, where a correct answer to the wrong question shows up (0:24); watching the row count change and reading an error (0:45); preview the practice page (0:54). The slides have 11 main slides; the appendix slides are not presented.

**Coding session (2 h)**

| Time | What |
|---|---|
| 0:00 to 0:10 | Warm-up: write the practice-page pipeline as real code on the small café table. The check cell says if it is clean |
| 0:10 to 0:15 | Load the Starbucks data and predict the shape |
| 0:15 to 0:40 | Ex 1: pair prompting (one prompts, one reviews; swap each task) |
| 0:40 to 1:00 | Ex 2: bug hunt in an "AI-written" analysis |
| 1:00 to 1:15 | Ex 3: read three errors, guess the cause, then fix |
| 1:15 to 1:30 | Ex 4 (stretch): a paper-ready chart, checked against the numbers |
| 1:30 to 1:50 | Ex 5 (stretch): own data; AI lists problems; students verify each by hand |
| 1:50 to 2:00 | Log; optional share-out |

**Watch for:** students who trust a chart because it looks right; the first bug takes the longest (do not rescue them too early); characters in other scripts in the CSV (Chinese, Thai) are normal.

---

## Week 3: Verify and analyze

**Goal:** students see that a statistic can be computed correctly and still be wrong for the question, using data where the true answer is known.

**Before:** run the notebook, including the GitHub step with a new account (it is the least tested part). Students need a GitHub account before the coding session.

**Learning session (1 h):** recap (0:00); what an estimate claims, with a simulated study and a prediction first (0:05); noise and sample size, rerun many times (0:20); a confounder (0:32); checking an AI's statistics against the known truth (0:42); preview (0:52).

**Coding session (2 h)**

| Time | What |
|---|---|
| 0:00 to 0:15 | Warm-up: simulate data with a true effect, fit a regression, check against the truth, repeat 100 times |
| 0:15 to 0:45 | Ex 1: descriptives and a regression on the experiment data; one sentence with the estimate and its uncertainty |
| 0:45 to 1:10 | Ex 2: bug hunt in AI-written statistics code |
| 1:10 to 1:35 | Ex 3: the survey data, naive versus adjusted; explain the difference in a paragraph |
| 1:35 to 1:55 | Ex 4: put the notebook and log on GitHub; check no key or personal data is in it |
| 1:55 to 2:00 | Log; optional share-out |

**Watch for:** "95% probable" readings of an interval; "proves" and "causes" from the wrong design; students who are anxious about statistics (the known truth makes it safer); GitHub sign-in problems.

---

## Week 4: Collect your own data

**Goal:** students keep the raw data untouched, write a log, parse to one standard table, explain every difference in counts, anonymize, and write a data card.

**Before:** do both routes (your own export and the saved example). **Route A** is an export the student already has (Twitter/X, Instagram, Facebook, Reddit, Bluesky). **Route B** is the invented saved example, for anyone without data. The data helpers should have noted in the access guide what works for each platform.

**Learning session (1 h):** the idea (0:00); what you may collect, and "public is not free to use" (0:05); anonymization (0:15); a raw response, shown from the saved example (0:21); save, log, count (0:29); limits and pacing (0:37); the data card (0:42); preview (0:46); questions (0:51).

**Coding session (2 h)**

| Time | What |
|---|---|
| 0:00 to 0:15 | Warm-up: the collection stub on the saved example (everyone) |
| 0:15 to 0:45 | Ex 1: put your export in the raw folder untouched and write the log (Route A), or collect the example (Route B) |
| 0:45 to 1:15 | Ex 2: parse to the standard table and compare counts: how many raw items, how many rows, and why? |
| 1:15 to 1:40 | Ex 3: anonymize and run the checks |
| 1:40 to 1:55 | Ex 4: write your data card |
| 1:55 to 2:00 | Log; optional share-out |

**Watch for:** students with no data (use Route B and agree a plan with a data helper); very large files (read in pieces, work on their own computer or on Drive); questions about terms and ethics (say it is a good question and send it to Kokil, who is the CACTUS ethics contact). The saved example has planted problems (repeats, deleted items): do not reveal them.

---

## Week 5: Analyze text

**Goal:** students split text into tokens (including Chinese), count and weigh words, run a dictionary sentiment score and check it by hand, and say what each step hides.

**Before:** in a fresh Colab runtime, run the install cell (`jieba` and `vaderSentiment`) and time it. Get the class data link from Kokil: the files are course use only and are not on this site. The notebook asks Colab users to upload the zip.

**Learning session (1 h):** the idea (0:00); what is a token (0:05); a live demo of one sentence under different tokenizers, including Chinese (0:11); counting and why raw counts mislead (0:17); distinctive terms (0:23); dictionary sentiment (0:30); where it fails (0:35); read before you name a cluster (0:42); preview (0:52).

**Coding session (2 h)**

| Time | What |
|---|---|
| 0:00 to 0:15 | Warm-up: tokenize five texts two ways; install and test the Chinese tokenizer |
| 0:15 to 0:45 | Ex 1: count and compare words per subreddit (raw, cleaned, distinctive); Chinese tokens per text by spaces versus jieba |
| 0:45 to 1:15 | Ex 2: dictionary sentiment on the Reddit posts; read ten posts by hand; then the Chinese news texts |
| 1:15 to 1:40 | Ex 3: bug hunt in an AI-written function that runs without errors |
| 1:40 to 1:55 | Ex 4 (stretch): cluster the posts, read examples, name or refuse to name |
| 1:55 to 2:00 | Log; optional share-out |

**Watch for:** install failures (the notebook names a fallback); some Reddit posts discuss personal and financial situations, so read them as data and with care; do not paste posts into an AI chat; do not say what the sentiment tool does to Chinese text.

---

## Week 6: AI as annotator

**Goal:** students compare an AI's labels with people's labels (accuracy, the always-no baseline, precision, recall, kappa), read the disagreements, and say what a result does and does not support.

**Before:** run the notebook, including Exercise 4 with an AI chat (time it). Get the class data link from Kokil (course use only). **The messages include abusive language**: say so at the start of the coding session and tell students they can step away or work on the other label. Prepare six invented messages for the live prompt demo. Do not use the class data in a chat tool.

**Learning session (1 h):** the idea (0:00); a codebook (0:05); from codebook to prompt, with a live demo on invented messages (0:11); the four counts and four measures (0:17); the accuracy trap (0:24); kappa (0:30); reading disagreements (0:36); reporting honestly (0:44); preview (0:52).

**Coding session (2 h)**

| Time | What |
|---|---|
| 0:00 to 0:10 | Warm-up: accuracy, the always-0 baseline, and kappa on 20 labels |
| 0:10 to 0:25 | Ex 1: build the evaluation table for 150 messages; compare how often people and the AI say yes |
| 0:25 to 0:50 | Ex 2: confusion matrix, accuracy and baseline, precision, recall, kappa for two labels |
| 0:50 to 1:10 | Ex 3: read the disagreements and sort them: labeler, codebook, or human label |
| 1:10 to 1:40 | Ex 4: write your own definition, label 20 messages with an AI, change it, then score it once on 20 fresh messages |
| 1:40 to 2:00 | Ex 5: bug hunt in an AI-written evaluation function |

**Watch for:** students pasting more than the 20 allowed messages into a chat tool; an AI that answers with extra text instead of yes or no (that is why the check cleans the answers); small samples (20 messages with one or two abusive ones gives unstable numbers); do not reveal how the AI did on the real messages.

---

## Week 7: Choose a track, and Week 8: Reproduce and present

To be added. Week 7 lets each student pick a track (networks, images and memes, a mock feed or experiment, and possibly models for nested data). Week 8 is "run it from scratch": rerun the whole pipeline, document it, and present results with limits.
