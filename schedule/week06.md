# Week 6: AI as annotator

**Theme:** An AI can label thousands of texts in minutes. Whether you can trust the labels is a measurement question. Students write a definition, have an AI label messages, compare with people's labels (accuracy, precision, recall, kappa), read the disagreements, and say what the result does and does not show.
**Format:** Zoom. A 1-hour learning session (lecture with live demos), a 20-minute practice page, then a 2-hour coding session in breakout rooms with no lecture. About 3 hours live.

<!-- facilitator:start -->
> **Status: built, not yet on the site.** Slides, practice page and notebook are built and tested (the notebook was run end to end with correct solutions; the buggy Exercise 5 function is rejected by its check). The data is private (class drive). **Read the "Decisions and open items" at the end before the session: the human "abusive" label needs your review.**
<!-- facilitator:end -->

## Objectives

By the end of the week, students can:
1. Write a short codebook (a definition, examples, and a rule for hard cases) and turn it into a prompt.
2. Have an AI label texts in a fixed format, and record the model, the prompt, and the date.
3. Compute and read a confusion matrix, accuracy, precision, recall, and Cohen's kappa.
4. Explain why accuracy can mislead when a label is rare, and compare with the "always no" baseline.
5. Read disagreements and sort them: the labeler is wrong, the codebook does not say, or the human label is questionable.
6. Say, in a sentence, what a result supports, with the sample size and what was not tested.

## Data

| Session | Dataset | Why |
|---|---|---|
| Learning (walk-through) | Invented messages and invented numbers | Nothing real is shown on slides |
| Practice page | Invented messages and tables in the page | Shows the measures and the reasons for disagreement without running code |
| Coding (exercises) | **649 Twitter, Reddit and forum messages with human labels** (the validation split of the CLAPTON dataset), and **LLM labels for a fixed sample of 150** of them, for two labels: *abusive* and *justification* (class drive, course use only; contains abusive language) | A real dataset with human labels, so students can measure an AI against people. **Then your own text**, for the homework |

## Required reading

From *Computational Analysis of Communication* ([cssbook.net](https://cssbook.net)), the Python version. Required, not graded.

- **Before the learning session:** [Chapter 11](https://cssbook.net/content/chapter11.html), section 11.1 (choosing a method) and section 11.4 (supervised classification).
- **Before the coding session:** [Chapter 8](https://cssbook.net/content/chapter08.html), section 8.5 (validation and best practices).

<!-- facilitator:start -->
## Materials

| What | Where |
|---|---|
| Lecture slides (11 slides) | `slides/week06_ai_as_annotator.html` and `.pdf` for students; `..._presenter.html` (press N for the script) and `..._handout.pdf` for the facilitator team. Source and notes: `slides/src/week06/` (built). Invented examples only |
| Practice page: Can You Trust the Labeler? | `practice/week06_trust_the_labeler.html` (built; source in `practice/src/week06/`; all messages and numbers invented) |
| Notebook | `notebooks/week06_ai_as_annotator.ipynb` (built by `scripts/build_week06_notebook.py`; asks Colab users to upload the corpus zip) |
| Data | `data/private/week06_corpus.zip` (built by `scripts/prepare_week06_data.py`; **shared through the class drive, not in the public repository**) |
| Answer key | `instructor/week06_answer_key.md` (private: the three planted mistakes, the expected numbers, how the LLM labels were made) |

## Prep

- Put `data/private/week06_corpus.zip` on the class drive and give students the link. **Do not publish it** until you have decided to (see the open items).
- **Review the human labels** (see the open items below): the "abusive" label disagrees with an ordinary reading in several places.
- Prepare six invented messages for the live prompt demo in slide 4. Do not use the class data in a chat tool.
- Do the notebook yourself first. Time Exercise 4 (the students' own labeling). Run Exercise 5 without looking at the key.
- Facilitators: read `facilitators/practice_pages_guide.md` and the private key.
<!-- facilitator:end -->

---

## Learning session (about 1 h): lecture with live demos

| Time | Activity |
|---|---|
| 0:00 | **Recap and the idea.** Fast labels, unknown quality. Treat the AI as a measuring instrument. |
| 0:05 | **Codebooks and prompts.** A definition, examples, and edge cases. From codebook to prompt, with a live demo on invented messages. |
| 0:17 | **Measuring agreement.** The four counts, accuracy, precision and recall, the accuracy trap, and kappa. |
| 0:36 | **Read the disagreements.** Three reasons: the labeler, the codebook, the human label. |
| 0:44 | **Report it honestly.** What to record and what to claim. |
| 0:52 | **Preview:** the practice page, the reading, and the coding session. |

<!-- facilitator:start -->
### Lecture plan (slides)

| # | Slide | Min | Notes |
|---|---|---|---|
| 1 | Title | 1 | The plan for the week |
| 2 | Fast labels, unknown quality | 4 | Promise, risk, and the rule |
| 3 | Start with a codebook | 6 | Ask the room for a one-sentence definition of "abusive" and compare |
| 4 | Demo: from codebook to prompt | 6 | Six **invented** messages in an AI chat; compare with hand labels |
| 5 | Four counts, four measures | 7 | Confusion matrix; accuracy, recall, precision |
| 6 | The accuracy trap | 6 | Always saying no scores 94% |
| 7 | What kappa asks | 6 | Agreement beyond chance; no magic threshold |
| 8 | Three reasons they disagree | 8 | Do **not** say what happens with the real messages |
| 9 | Report it honestly | 8 | The setup, the numbers, the limits; privacy |
| 10 | Before the coding session | 4 | Practice page, reading, the data rules |
| 11 | Questions | 4 | |
<!-- facilitator:end -->

---

## Between sessions (about 20 min): practice page

Students open **Can You Trust the Labeler?** after the learning session and before the coding session.

- **Which labeler would you use?** Three labelers on 100 invented messages. Accuracy ties two of them, but one finds nothing.
- **High accuracy, no agreement.** Sliders for how rare abuse is and how good the labeler is. Make a labeler with 90% accuracy and a kappa near zero.
- **Why do they disagree?** Six invented disagreements. Sort each: the labeler, the codebook, or the human label.
- **What does the result support?** Judge six claims against a table.
- **Colab task:** compute the measures on 20 labels.

---

## Coding session (about 2 h): breakout rooms, no lecture

Notebook: `notebooks/week06_ai_as_annotator.ipynb`. Pairs in breakout rooms. Exercises 1 to 5 are required.

| Time | Exercise |
|---|---|
| 0:00–0:10 | **Warm-up:** accuracy, the always-0 baseline, and kappa on 20 labels. |
| 0:10–0:25 | **Ex 1:** build the evaluation table for 150 messages. Compare how often people and the AI say yes. |
| 0:25–0:50 | **Ex 2:** measure agreement for two labels: confusion matrix, accuracy and baseline, precision, recall, kappa. Say it in one sentence. |
| 0:50–1:10 | **Ex 3:** read the disagreements for the abusive label and sort them by reason. |
| 1:10–1:40 | **Ex 4:** write your own definition, have an AI label 20 messages, and compare. Change the definition, measure again, then score it once on 20 fresh messages. |
| 1:40–2:00 | **Ex 5:** bug hunt. An AI-written evaluation function that runs without errors and has three mistakes. |

**Stretch:** kappa by source; a bootstrap range for kappa; a third label.

Post a time check in the main chat at each boundary. Hints for Exercise 5 come from facilitators only. In Exercise 4 students may paste up to 20 messages from the dataset into an AI chat (names are already removed), and nothing else from the data.

## Homework (45 minutes or less)

- For your own project, write a short codebook for one label (a definition and two examples of yes and two of no). Write down the agreement you would accept before you look at the result.
- Hand-label 30 texts, ask an AI to label the same 30, and report accuracy, the baseline, and kappa. Tune on some texts and score a separate set once. Save the prompt, the model name, and the date.
- Before you send any texts to an AI service, de-identify them first (names, handles, links) and check that your data terms and ethics approval allow it.
- If you do not have your own text yet, use the Week 5 corpora and say so.

## Hand-off to Week 7

Students leave with a way to check any AI labeling against people, and a habit of recording the model, the prompt and the date. Week 7 lets them choose a track (networks, images and memes, or a mock feed or experiment) and apply a method to their own data or a track dataset.

<!-- facilitator:start -->
## Decisions and open items (Week 6)

**Decided**
1. **Data:** the validation split of the CLAPTON dataset (Kokil's published data): 649 human-labeled messages. The repository has human labels but **no LLM labels**, so we made them (below).
2. **LLM labels:** 150 messages (fixed sample, random seed 6) labeled for *abusive* and *justification* by Claude, an AI assistant, in November 2026, in one pass, **without seeing the human labels**, using the prompt printed in the notebook. The definitions in that prompt were written for this course. They are **not** the CLAPTON codebook.
3. **Exercise 5 mistakes:** `"Yes"` versus `"yes"` (every answer read as no), the wrong human column for justification, and evaluating only the first 50 rows. Details in the private key.

**Needs your review before the session**
4. **The human "abusive" label.** In this file only 6.7% of messages are labeled abusive (42 of 649), and the labels often disagree with an ordinary reading: plain insults are labeled 0 and some mild messages are labeled 1 (specific rows are listed in the private key). I checked that the columns are not shifted by a row (agreement is highest at offset 0). Please check what the `Uncivil_abuse` column means in the CLAPTON codebook (for example, abuse aimed at another participant) and whether the validation file's label is the one you want. If it is a different definition, I will put the CLAPTON wording into the prompt and regenerate the LLM labels. As it stands, the notebook treats the disagreement as the lesson (codebook versus labeler versus human label), and does not claim the human labels are wrong.
5. **Can the data go in the public repository?** It is kept private (class drive) like Week 5. The messages are tweets and Reddit posts. If you confirm that publishing the validation split is allowed, I can move it to `data/week06/` so Colab loads it without an upload. Please also give me the citation to print on the data page.
6. **Content warning.** The messages include abusive language. The notebook has a content note. Decide whether to add an opt-out (for example, students may work on the justification label only).
7. **Pasting data into an AI chat.** The notebook lets students paste up to 20 messages in Exercise 4, because the dataset is already de-identified and published. Confirm you are comfortable with that.
8. **A repeated-id trap.** `orig_message_id` repeats for four messages in the file, so a join on it duplicates rows. The notebook uses `row_id` instead. The Exercise 5 mistakes do not use this, but it is a good thing to mention.
<!-- facilitator:end -->
