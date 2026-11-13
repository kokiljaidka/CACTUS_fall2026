# RA testing checklist: Weeks 1 to 8

Thank you for testing. Please try everything the way a student would, on a device and account like theirs, and write down anything that is confusing, broken, slow, or wrong. **You are testing the materials, not yourself.** If something confuses you, it will confuse students, so that is a finding.

Do not look at `instructor/` answer keys until you have finished a task. For the bug-hunt exercises, find the bugs yourself first.

## How to report

Open a GitHub issue (or add a row to the shared tracker Kokil gives you) with:

| Field | Example |
|---|---|
| Where | Week 1 notebook, Step 3b, Task 2 |
| What you did | Ran the cell after Step 3 |
| What you expected | A title printed |
| What happened | `NameError: name 'data' is not defined` (paste the full message) |
| Device and browser | Windows 11, Chrome 130 |
| Severity | **Blocker** (can't continue) / **Confusing** (a student would stall) / **Polish** (typo, wording) |

A screenshot helps for anything visual. **Never paste an API key into an issue.**

## Setup (everyone)

- [ ] Use a **Google account that has never used the course materials** (or a fresh browser profile), as students will.
- [ ] Have one AI chat assistant ready (ChatGPT, Claude, or Gemini).
- [ ] Pick a device: Windows laptop, Mac laptop, or phone/tablet. Each task below says which devices matter most. Please note which you used.
- [ ] Course site: https://kokiljaidka.github.io/CACTUS_fall2026/ (all course links should work from here)
- [ ] The eight practice pages and eight slide decks are published on the course site. If a link is missing, tell Kokil.

---

## A. Course website (1 hour, any device)

- [ ] Every link on **Home**, **Weeks 1 to 6**, **Project guide**, **Getting data access**, **Ethics checklist**, and **Data** works. Note any broken link or any link that goes to the wrong place.
- [ ] The "Open the notebook in Colab" buttons open the right notebook.
- [ ] The practice page buttons open the page in a new tab.
- [ ] The textbook links open the right chapter at https://cssbook.net, and the section numbers named in the reading list (for example "§3.1 to 3.3") actually exist in that chapter.
- [ ] Download links work (Starbucks CSV, toy café CSV, saved searches zip). Check the CSV opens and the zip unpacks.
- [ ] Read the Week 1 to 6 pages as a student. Is anything written for facilitators ("send with email", "before assigning", prep notes)? Report it.
- [ ] Search box: try three searches ("API", "prediction", "reading"). Do sensible results appear?
- [ ] Phone: does the site read well at phone width? Does any table run off the screen?
- [ ] Dark mode (if you use it): is text readable everywhere?

**Done when:** you have a list of every broken link and every line that sounds like it is for staff.

---

## B. Week 1 practice page: Cactus Code Garden (1.5 hours; use two devices, one a phone or tablet)

Work through **all 17 levels**.

- [ ] **Drag** every piece with a mouse (or finger). Does the piece follow your pointer? Does the drop zone highlight?
- [ ] **Tap** every piece instead of dragging. Does it get placed?
- [ ] Use only the **keyboard**: can you reach the pieces with Tab and place one with Enter? (Report what does not work. Do not spend more than 10 minutes on this.)
- [ ] **Remove** a placed piece in each style: tap it, drag it out, use the × button.
- [ ] For each level, write down how long it took and whether the instructions were clear. Flag any level where you were unsure what to do **before** you read the hint.
- [ ] Use the **Hint** button on at least five levels. Is the hint helpful without giving the answer away?
- [ ] Try to get a level **wrong** on purpose. Is the message helpful?
- [ ] Levels 1, 2, 9 and 10 (the cactus): tap a square to predict where the cactus stops. Does the marker appear? Does the page say whether your prediction matched?
- [ ] Levels 9 and 10 have a block limit. Does the limit message appear when you exceed it?
- [ ] **Level 16**: add a custom field, change an example value, remove a field. Does the Python code on the right update as you type? Does "Copy code" work?
- [ ] **Level 17 (Colab bridge)**: do the three tasks in the Week 1 notebook (see section C). Does the page's code match what the notebook expects?
- [ ] Refresh the page: does your progress remain? Does **Reset progress** clear it?
- [ ] Open the page on a phone in portrait: does anything overflow, overlap, or become impossible to reach?
- [ ] Try dark mode if you use it.

**Done when:** you completed all levels on a computer and at least ten on a phone or tablet, and listed every level that was confusing or broken.

---

## C. Week 1 notebook in Colab (1.5 hours; **two** RAs, one with a SerpAPI key, one without)

Use a fresh Colab notebook opened from the course site's button, not a copy someone has already run.

**RA without a key (this is the main case):**
- [ ] Open the notebook from the site. Read the intro: do you know what to do first?
- [ ] Step 1: skip the key. Can you still continue? Is the text clear that a key is optional?
- [ ] Upload `serp_cache.zip` (from the site) and unpack it with the provided cell.
- [ ] Run every cell from the top, one at a time, **predicting before you run**. Note any error.
- [ ] **Step 3b**, tasks 1 to 3: do them honestly. For task 3, use your AI assistant as written. Did the AI's line pass the check?
- [ ] **Step 4:** change the engine to `google` and back. Then try a search that is **not** saved. Is the error clear about why it failed and what to do?
- [ ] Step 5 and Step 7: run them. Is the saved CSV readable in Excel, including Chinese characters?
- [ ] Time each step and compare with the schedule in `schedule/week01.md`. Report any step that takes much longer than planned.

**RA with a key:**
- [ ] Set the key in **Colab Secrets** as described in Step 1. Does "Key found: True" appear?
- [ ] Run a **new** search in Step 4 (a query that is not saved). Does it work? Does it use one search credit?
- [ ] Confirm the key does **not** appear anywhere in the notebook output, the saved JSON files, or the downloaded CSV.

**Done when:** both RAs ran the notebook top to bottom, with times, and reported every error or unclear instruction.

---

## D. Week 2 practice page: Silent Changes (1 hour; at least one RA tests on a phone)

- [ ] **Level 1:** build the pipeline by dragging cards. Try these on purpose and note what the page says each time:
  - [ ] Only the good cards, in a sensible order
  - [ ] Add each "tempting" card (the ones that look helpful) one at a time
  - [ ] Run with an empty pipeline (should ask you to add a card)
  - [ ] Leave the prediction box empty (should ask for a prediction)
  - [ ] Put the same card in twice (should not duplicate)
- [ ] After a run, do the **row-count table** and the summary make sense? Could a student state in one sentence what each step did?
- [ ] **Levels 2 to 4:** find each bug **before** reading any hint. Time how long it takes. Write down how you found it.
- [ ] For each bug level, pick a wrong line and a wrong check on purpose. Are the messages fair and helpful?
- [ ] **Level 5 (Colab bridge):** copy the generated code and run it in the Week 2 notebook warm-up (see section E). Does it pass the check cell?
- [ ] Rebuild your pipeline with a **different** card order (when you can). Does the generated code reflect your order?
- [ ] Refresh, reset progress, phone portrait, dark mode: same as section B.

**Done when:** you have solved every level on a computer, tried at least the wrong choices on each bug level, and run the bridge code.

---

## E. Week 2 notebook in Colab (2 hours; two RAs)

- [ ] Open the notebook from the site. Upload `starbucks_sea_comments.csv` when asked. Does the upload step work smoothly?
- [ ] **Warm-up:** build the pipeline (paste it from the practice page, then also try an AI-written one). Run the check cell.
  - [ ] Does it pass with a correct pipeline?
  - [ ] Does it fail with an **incorrect** one, with a message that points you toward the problem?
- [ ] **Exercise 1:** do tasks 1a to 1d with a partner, one prompting and one reviewing. Use a real AI assistant. Does the prompt template in the notebook work for you? Note the first thing the AI got wrong.
- [ ] **Exercise 2:** find the three bugs **without help** and without opening `instructor/`. Record how long it takes, and which bug you found last.
- [ ] **Exercise 3:** read each error, say it in your own words, then fix it. Note any error message that did not match what the notebook says.
- [ ] Exercises 4 and 5: try each. Does the instruction to "verify every claim by hand" work with your AI's answers?
- [ ] Time every section and compare with `schedule/week02.md`.

**Done when:** you completed all required exercises, with times, and listed the bugs you found and any that you missed.

---

## F. Week 3: Planted-Effect Lab and notebook (3 hours; two RAs)

**Practice page** (`week03_planted_effect_lab.html`, 45 minutes; one RA on a phone):
- [ ] Do all levels: one study, 100 studies, the confounder story, judging claims, the Colab bridge. Does each level's message make sense when you get it wrong on purpose?
- [ ] Does the interval chart show minus signs on the tick labels?
- [ ] Run the bridge code in the Week 3 notebook warm-up (see the notebook list below). Does it pass the check?
- [ ] Refresh, reset progress, phone portrait, dark mode.

**Notebook** (`week03_verify_and_analyze.ipynb`, from the site button, 2 hours):
- [ ] Data loads from the web in Colab with no upload. If it fails, what does the error say?
- [ ] Warm-up: simulate, estimate, 100 repeats. Does the check pass with the correct code and fail with a wrong one?
- [ ] Exercise 2 (AI-written code with planted bugs): find each bug **before** opening `instructor/`. Record the time and the bug you found last.
- [ ] Exercise on the GitHub step: try it with a **new GitHub account**. Where did you stall?
- [ ] Time each section against `schedule/week03.md`.

**Done when:** every level and exercise is done, with times, and the GitHub step has been tried on a fresh account.

---

## G. Week 4: Before You Collect and the collection notebook (3 hours; two RAs)

**Practice page** (`week04_before_you_collect.html`, 30 minutes; one RA on a phone):
- [ ] Do all levels: keep, change or drop each field; the re-identification meter; plan around a limit; four "should you collect it?" scenarios; the Colab bridge.
- [ ] Do the limits on the planning level look clearly invented? Does the page say that its rules of thumb are not legal advice?
- [ ] Is any scenario answer one you would argue with? Write it down.
- [ ] Copy the bridge code into the Week 4 notebook. Does it run?
- [ ] Refresh, reset progress, phone portrait, dark mode.

**Notebook** (`week04_collect_your_own_data.ipynb`, 2 hours): test **both routes**. Route B is the saved example, which needs no key. For Route A, make a small fake export (a CSV with about a dozen invented rows and a repeated row), upload it, and follow the notebook as a student with an export would.
- [ ] Warm-up and Check 1: do they pass? Is the message clear if you forgot to save the raw files or the log?
- [ ] Exercise 2: do your counts show 100 entries saved, 97 rows after parsing? Can you explain the 3 missing rows without being told?
- [ ] Exercise 3 (anonymize): does Check 3 catch a leftover `@handle`, a link, or a profile column? Try each on purpose.
- [ ] Exercise 4: can you write the data card from the template?
- [ ] Route A: can you tell which cell to run and which to skip? Does the notebook explain how to rename your columns to the standard table? Do the counts and checks still make sense for an export?
- [ ] Do the Route A and Route B instructions each say what to do when you have no data yet?
- [ ] Time each section against `schedule/week04.md`.

**Ethics checklist** (site page): read it as a student. Is every question clear? Does anything read like a rule or legal advice rather than a question? Does it say who to ask?

**Done when:** every exercise is done on both routes, with times, and the 100 to 97 difference (Route B) has been explained in your own words.

---

## H. Week 5: What Counts as a Word? and the text notebook (3 hours; two RAs)

**Practice page** (`week05_what_counts_as_a_word.html`, 30 minutes; one RA on a phone):
- [ ] Level 1: try splitting on spaces for the Chinese texts, then fix it. Are the notes under each text fair and clear?
- [ ] Level 2: reach the goal. Did you notice that one setting deleted "AI" and another deleted "US"? Was the note under the table enough to find out why?
- [ ] Level 3: get as many right as you can. Is it clear why you cannot get all eight? Does the page say so honestly?
- [ ] Level 4: decide all three clusters. Is any answer one you would argue with? Write it down.
- [ ] Level 5: copy the code into the Week 5 notebook warm-up. Does it run?
- [ ] Refresh, reset progress, phone portrait, dark mode.

**Notebook** (`week05_analyze_text.ipynb`, 2 hours; you need the corpus zip from the class drive):
- [ ] The install cell works in a fresh Colab runtime. How long does it take? What happens if it fails?
- [ ] The upload step: is it clear how to upload `week05_corpus.zip` and what happens next?
- [ ] Warm-up and Check 0 pass with a correct `by_jieba`, and fail with the placeholder.
- [ ] Exercise 1: do the checks fail with a clear message if you leave the stopwords in, or give the same list for "distinctive" as for the counts?
- [ ] Exercise 2: read the ten posts. Was any post upsetting or identifying? **Do not paste any into an issue.** Tell Kokil privately.
- [ ] Exercise 3: find the three mistakes **without help** and without opening `instructor/`. Record how long it takes, and which you found last.
- [ ] Time each section against `schedule/week05.md`.
- [ ] Confirm no real Reddit or news text appears in the notebook file itself, the slides, or the practice page.

**Done when:** every exercise is done, with times, the install time is recorded, and you have listed the mistakes you found and any you missed.

---

## I. Week 6: Can You Trust the Labeler? and the AI-as-annotator notebook (3 hours; two RAs)

**Practice page** (`week06_trust_the_labeler.html`, 30 minutes; one RA on a phone):
- [ ] Level 1: try each labeler. Is each wrong pick explained clearly?
- [ ] Level 2: reach the goal. Do the sliders work with touch? Is it clear what sensitivity and specificity mean?
- [ ] Level 3: decide the six disagreements. Is any case one you would argue with? Write it down.
- [ ] Level 4: judge the six claims. Is any claim ambiguous?
- [ ] Level 5: copy the code into the Week 6 notebook warm-up. Does it run?
- [ ] Refresh, reset progress, phone portrait, dark mode.

**Notebook** (`week06_ai_as_annotator.ipynb`, 2 hours; you need the corpus zip from the class drive):
- [ ] The upload step: is it clear how to upload `week06_corpus.zip`?
- [ ] Warm-up and Check 0 pass with correct code and fail with the placeholders.
- [ ] Exercise 1: join on `row_id`. Does the check give a clear message if you join on `orig_message_id`?
- [ ] Exercise 2: do the checks accept correct numbers and reject wrong ones, with a clear message?
- [ ] Exercise 3: read the disagreements. **The messages include abusive language.** Is the content note enough? Tell Kokil privately about anything that looks identifying. Do not paste messages into an issue.
- [ ] Exercise 4 (use an AI chat): paste the 20 messages, write a definition, paste the answers into `my_llm`. Does Check 4 handle answers like "Yes", " no " and "YES"? What does the AI do that you did not expect (extra text, a different format)?
- [ ] Exercise 5: find the three mistakes **without help** and without opening `instructor/`. Record how long it takes, and which you found last.
- [ ] Time each section against `schedule/week06.md`.

**Done when:** every exercise is done, with times, and you have listed the mistakes you found and any you missed.

---

## J. Week 7: Plant It, Find It and the shared notebook (3 hours; two RAs)

**Practice page** (`week07_plant_it_find_it.html`, 30 minutes; one RA on a phone):
- [ ] Level 1: run 100 studies at the defaults, then plant 1.0 and find a setting that reaches 80 of 100. Do the sliders work with touch? Is it clear what "found" means?
- [ ] Level 2: decide the six variables. Is any answer one you would argue with? Write it down.
- [ ] Level 3: switch between raw counts and per 1,000 followers. Is the table clear?
- [ ] Level 4: decide the six cases. Is any ambiguous?
- [ ] Level 5: copy the code into a new cell in the Week 7 notebook. Does it run in Colab?
- [ ] Refresh, reset progress, phone portrait, dark mode.

**Notebook** (`week07_core_nested_data.ipynb`, 2 hours; the data load from the repository, so push `data/week07_*.csv` first):
- [ ] The data load in a fresh Colab runtime with no upload. What does the error say if they do not?
- [ ] Warm-up: do the naive and clustered counts look as predicted? Does the check pass?
- [ ] Exercise 1: does Check 1 give a clear message if you cluster by `comment_id`?
- [ ] Exercise 2: does Check 2 give a clear message if you leave out the offset or use `followers` instead of `log(followers)`?
- [ ] Exercise 3: find the three mistakes **without help** and without opening `instructor/`. Record how long it takes, and which you found last.
- [ ] Exercise 4: does the permutation take a reasonable time in Colab? Does shuffling comments instead of posts give a clearly narrower spread?
- [ ] Time each section against `schedule/week07.md`.

**Done when:** every exercise is done, with times, and you have listed the mistakes you found and any you missed.

---

## K. Week 8: Run It from Scratch and the rerun report (1 hour; one RA)

**Practice page** (`week08_run_it_from_scratch.html`, 30 minutes; one RA on a phone):
- [ ] Level 1: try Restart and run all in the starting order. Does the error name the right cell? Do the arrows work with touch? Reach the goal.
- [ ] Level 2: try each fix. Is each wrong pick explained fairly?
- [ ] Level 3: decide the six lines. Is any answer one you would argue with? Write it down.
- [ ] Level 4: sort the six lines and answer the leak question. Is any line ambiguous?
- [ ] Level 5: do the three tasks on a notebook of your own. Do the steps match what Colab's menu says?
- [ ] Refresh, reset progress, phone portrait, dark mode.

**Rerun report** (the site page `rerun-report.html`): fill it in for a notebook you did not write. Is every field clear? Does it say to use only shared or de-identified data?

**Done when:** every level is done and the rerun report has been filled in once.

---

## L. Slide decks (3 hours; Weeks 1 to 8)

- [ ] Weeks 3 to 6 have 11 main slides each. Weeks 3 to 6 notes include TIME / SAY / DO / WATCH FOR lines. Are they usable by someone who did not write the slides?
- [ ] Week 4 slide 4 needs one real raw API response from a facilitator. Is it clear what to prepare?
- [ ] Open each deck from its Week page on the site, both the web version and the PDF. Do both match? Do arrow keys, the Previous/Next buttons, and swiping on a phone all work? Does the PDF have one slide per page, with fonts intact?

- [ ] Present each deck aloud to a partner at normal speed. Time it. Does it fit the plan in the schedule (Week 1 session 1 is about 2 hours; the Week 2 learning session is 1 hour, with 11 slides presented and 3 appendix slides not presented)?
- [ ] Read the **speaker notes** for every slide. Are they complete, accurate, and not contradictory?
- [ ] Check every fact on the slides against the course site and schedule (times, chapter numbers, what to bring).
- [ ] Any text too small to read when screen-shared on Zoom? Any slide that is too crowded?
- [ ] Any typo or inconsistent term across slides?
- [ ] Dark/light projector test: view at the lowest brightness and note unreadable slides.

---

## M. Full dress rehearsal (2 sessions, as a group)

Run one RA as "Kokil" and the rest as students, on Zoom, with breakout rooms.

- [ ] **Week 1, Session 1 (about 2 hours):** follow the schedule. Test the project-card activity. Can students finish a card in 35 minutes? Do the sign-off criteria feel clear?
- [ ] **Week 1, Session 2 (about 2 hours):** puzzle page, then the notebook. Does the time allocation hold? Where do students stall?
- [ ] **Week 2 learning session (about 1 hour):** present the 11 main slides with the live demos. Does it fit in 60 minutes? Which slide runs long?
- [ ] **Week 2, learning session and coding session:** same approach.
- [ ] **Weeks 3 to 6:** the same, if there is time. Week 4 needs a facilitator's access for the live request.
- [ ] Note exactly which minutes ran over and what you would cut.
- [ ] Test the **stuck protocol**: can an RA in the main room see "Ask for help" and respond fast enough?

---

## N. Data checks (30 minutes, one RA)

- [ ] `starbucks_sea_comments.csv`: opens without error, Chinese, Thai and other scripts display correctly, and no usernames or links remain in any column.
- [ ] `lululemon_instagram.csv`, `week02_toy_cafe.csv`, and the Week 3 CSVs: same checks. Confirm the Week 4 sample JSON in `data/week04/sample/` has only invented names.
- [ ] Look through 30 random rows of the comment text for anything that looks like personal information (full names, phone numbers, addresses). **Do not paste any into an issue.** Tell Kokil privately.
- [ ] Confirm no file in the repository contains an API key (search for "api_key" and for long random strings).

---

## Summary table (fill in at the end)

| Area | Tester | Device | Time taken | Blockers | Confusing | Polish |
|---|---|---|---|---|---|---|
| A. Course website | | | | | | |
| B. Week 1 puzzle page | | | | | | |
| C. Week 1 notebook | | | | | | |
| D. Week 2 practice page | | | | | | |
| E. Week 2 notebook | | | | | | |
| F. Week 3 page and notebook | | | | | | |
| G. Week 4 page and notebook | | | | | | |
| H. Week 5 page and notebook | | | | | | |
| I. Week 6 page and notebook | | | | | | |
| J. Week 7 page and shared notebook | | | | | | |
| K. Week 8 page and rerun report | | | | | | |
| L. Slide decks | | | | | | |
| M. Rehearsal | | | | | | |
| N. Data | | | | | | |

**Suggested order:** A and N first (quick), then B and D in parallel, then C and E, then F to K, then L, then M.
