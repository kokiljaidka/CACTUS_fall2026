# Week-by-week run sheets

One sheet per week. Use it with the [facilitator hub](README.md) (roles, stuck protocol, hint ladder) and the slide script (presenter view, press **N**).

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

## Dec 22: Midpoint show-and-tell (Kokil leads)

**Goal:** everyone shows where their project stands, so problems (no data, a question that is too broad) show up before January.

**Before:** send the order two days ahead; make a shared feedback sheet (three lines each: question, data, check); remind everyone about the data rules (public or de-identified, no names or raw posts on screen). The Desk keeps time.

**Session (about 2 h)**

| Time | What |
|---|---|
| 0:00 | Welcome, format, order |
| 0:10 | Presentations: 5 minutes each plus 3 for questions (one from a peer, one from a facilitator) |
| About 1:30 | What we heard: three to five common themes |
| About 1:45 | Look ahead to Weeks 6 to 8 |

**Watch for:** anyone with no data (agree a plan with a data helper, so there is data before Week 6); long talks (a warning at 4 minutes, a stop at 5); results shown without a check (ask "what check would you add?"). Send each person their feedback within two days.

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

## Week 7: Applying statistics to social media data (two sessions)

**Goal:** Session 1 (everyone): students plant an answer, see why ignoring groups makes results look too certain, fix it with clustered standard errors, model counts with an exposure, and check a result by permutation. Session 2 (tracks): each student applies the core to networks, images and memes, or a mock feed or experiment.

**Before (Session 1):** run the practice page, the shared notebook, and its bug hunt (do not open the key first). The data are invented and public, so no class drive. Push the data files so Colab can load them.

**Learning session (1 h):** the idea (0:00); known-answer tests (0:05); what they cannot tell you (0:10); rows that come in groups, with a prediction first (0:15); standard errors that notice groups (0:23); counts and exposure (0:30); permutation (0:35); the three tracks (0:40); preview (0:46); questions (0:50).

**Coding session (2 h, everyone)**

| Time | What |
|---|---|
| 0:00 to 0:15 | Warm-up: plant an effect and run 200 studies, naive versus clustered |
| 0:15 to 0:45 | Ex 1: naive versus clustered on 3,000 comments in 80 posts; the post-level and comment-level variables |
| 0:45 to 1:10 | Ex 2: counts with an exposure (comments per follower) |
| 1:10 to 1:35 | Ex 3: bug hunt in AI-written code |
| 1:35 to 1:50 | Ex 4: permutation, shuffling posts versus shuffling comments |
| 1:50 to 2:00 | Choose a track; log |

**Watch for:** students shuffling comments instead of posts in Ex 4 (that is the lesson; do not rescue them early); anyone who thinks clustering changes the estimate (it changes the standard error); people unsure which track (ask what their data look like: edges, images, or conditions).

**Session 2 (tracks, 2 h, Thu Jan 14, tentative)**

**Before:** each facilitator does their room's notebook, **including the bug hunt**, before the session. Push the data files so Colab loads them. Collect track choices at the end of Session 1 and match rooms to facilitators. The Desk keeps the main room.

| Time | What |
|---|---|
| 0:00 to 0:10 | Main room: a two-minute recap of Session 1 (plant, compare, check). Send people to their track rooms. Anyone who has not chosen goes to the Desk |
| 0:10 to 0:25 | Warm-up: plant a known answer for the track and predict |
| 0:25 to 0:55 | Ex 1: run the method on the planted data |
| 0:55 to 1:15 | Ex 2: check against the planted answer, then break it on purpose |
| 1:15 to 1:40 | Ex 3: bug hunt (three planted mistakes) |
| 1:40 to 1:55 | Ex 4: own data (write down what to check first; run a first step on a small sample) |
| 1:55 to 2:00 | Log; optional share-out |

**By room** (the keys are private; ask Kokil)

| Room | What the exercises find | Where students stall | What to ask |
|---|---|---|---|
| **A. Networks** | Who gets the most replies, who sends the most, the communities (a small one is the bots), and whether the structure beats shuffled networks | They count rows instead of different accounts; they call a bot "influential"; they are surprised by three communities | "What is this number a count of? Who is in the small community?" |
| **B. Images and memes** | Fingerprints, groups at a threshold, a collapse at a loose threshold, posts versus different images versus different accounts | A loose threshold gives one giant group and they think everything is the same meme; they count reposts as new memes | "Which pair joined two different templates? How do the chains form?" |
| **C. Mock feed or experiment** | The manipulation check by device, the label effect for each source, the interaction, and what dropping non-noticers does | They read the `label` coefficient as the overall effect; they call mobile "a weaker label" when the label was not delivered; they run the interaction on a tiny sample | "Who saw the label? Who did you drop, and why?" |

**Watch for:** Ex 2 in Room A is the longest (20 shuffled networks): if time runs out, say to skip the shuffle and return to it as homework; students who finish early can try the stretch or help a neighbour; anyone alone in a track joins the nearest room; do not rescue the bug hunt early; images are invented, but remind everyone that real images of people need ethics approval before they are collected or shared.

**Not built:** AI image annotation for Room B (waiting on Niranjan's DeepInfra code). If it is added, facilitators run it ahead and share the labels; no student gets a key.

---

## Week 8: Reproduce and present

**Goal:** everyone reruns a notebook from a clean start (their own and a partner's), documents the project, and presents it in six minutes with its limits.

**Before:** make pairs the day before; share the rerun-report template; collect repository links in the chat; make the order and the feedback sheet. Partners rerun on the shared or de-identified sample only, never on private raw data. The slides and practice page are not built yet.

**Session (about 3 h)**

| Time | What |
|---|---|
| 0:00 to 0:20 | Short learning session: the reproducibility checklist, and what a result supports |
| 0:20 to 1:20 | Swap and rerun in pairs: restart and run all, write down what broke and what could not be followed, fix it |
| 1:20 to 1:30 | Break |
| 1:30 to 3:00 | Presentations: 6 minutes each plus 2 for questions (about 9 people). The Desk keeps time |
| About 3:00 | Close |

**Watch for:** notebooks that only run because of leftover variables; a key or private file in a repository (stop and fix it before the presentation); people with no data (present the plan and the checks); long talks.
