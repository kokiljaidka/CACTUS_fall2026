# Week 5: Analyze text

**Theme:** Turning text into numbers loses things. Students learn to count, tokenize (including Chinese), run a dictionary-based sentiment score, and find patterns, first in a shared corpus and then in their own text, and to say what each step hides.
**Format:** Zoom. A 1-hour learning session (lecture with live demos), a 20-minute practice page, then a 2-hour coding session in breakout rooms with no lecture. About 3 hours live.

<!-- facilitator:start -->
> **Status: built, not yet on the site.** Slides, practice page and notebook are built and tested (the notebook was run end to end on the real corpus with a correct solution; the buggy Exercise 3 function is rejected by its check). The shared corpus is private (class drive). Students bring their own text from Week 4. See the decisions at the end.
<!-- facilitator:end -->

## Objectives

By the end of the week, students can:
1. Explain what a token is, and why whitespace tokenization fails for Chinese.
2. Count words and compare groups, and say why raw counts mislead (and what weighting does).
3. Run a dictionary-based sentiment score and check it against a few texts read by hand.
4. Find the distinctive terms or a cluster in a corpus, and read examples before naming it.
5. Report where each method fails, in a sentence.
6. Compare a method's output with what they read in the texts, as a verification step.

## Data

| Session | Dataset | Why |
|---|---|---|
| Learning (walk-through) | A few short texts in English and Chinese | Easy to follow token by token |
| Practice page | Precomputed tokenizations and scores in the page | Shows the effect of choices without running code |
| Coding (exercises) | **Guided exercises on a shared corpus:** 657 Reddit posts from r/jobs, r/personalfinance and r/mildlyinfuriating (English, with subreddit, month, score and comments), so facilitators can help everyone with the same data. **Chinese tokenization** on 202 Chinese news and web texts about AI from Hong Kong and Taiwan. **Then your own text** from Week 4, if you have it | Reddit gives long, informal, sarcastic text that shows where counting and dictionary sentiment fail. The news texts are mostly headlines, so they suit tokenization but not counting or sentiment. Your own data is what you will use for your project |

## Required reading

From *Computational Analysis of Communication* ([cssbook.net](https://cssbook.net)), the Python version. Required, not graded.

- **Before the learning session:** [Chapter 9](https://cssbook.net/content/chapter09.html), section 9.1 (text as a string of characters).
- **Before the coding session:** [Chapter 10](https://cssbook.net/content/chapter10.html), sections 10.1 and 10.4 (bag of words; which preprocessing to use), and [Chapter 11](https://cssbook.net/content/chapter11.html), section 11.3 (dictionary approaches).

<!-- facilitator:start -->
## Materials

| What | Where |
|---|---|
| Lecture slides (11 slides) | `slides/week05_analyze_text.html` and `.pdf` for students; `..._presenter.html` (press N for the script) and `..._handout.pdf` for the facilitator team. Source and notes: `slides/src/week05/` (built). The slides use invented text only |
| Practice page: What counts as a word? | `practice/week05_what_counts_as_a_word.html` (built; source in `practice/src/week05/`; tokenizations precomputed by `scripts/make_week05_practice_data.py`; all texts invented) |
| Notebook | `notebooks/week05_analyze_text.ipynb` (built by `scripts/build_week05_notebook.py`; installs jieba and vaderSentiment; asks Colab users to upload the corpus zip) |
| Answer key | `instructor/week05_answer_key.md` (private: the three planted mistakes, expected numbers, practice page answers) |
| Corpus | `data/private/week05_corpus.zip` (built by `scripts/prepare_week05_corpus.py`; **shared privately through the class drive, not in the public repository**) |

## Prep

- The corpus is built (`scripts/prepare_week05_corpus.py`). Put `data/private/week05_corpus.zip` on the class drive and give students the link. **Never put the files in the public repository.**
- In a fresh Colab runtime, run the install cell (`%pip install -q jieba vaderSentiment`) and time it. If it fails, the notebook tells students to use character pairs instead.
- Do the notebook yourself first. Note what breaks and how long installs take. Run the Exercise 3 mistakes without looking at the key, to see how long they take to find.
- Facilitators: read `facilitators/practice_pages_guide.md` and the private key for the planted bugs.
<!-- facilitator:end -->

---

## Learning session (about 1 h): lecture with live demos

| Time | Activity |
|---|---|
| 0:00 | **Recap and the idea.** Text is not numbers. Every step in turning it into numbers makes a choice. |
| 0:05 | **What is a token?** Live: the same sentence split four ways. Why Chinese needs a segmenter. |
| 0:17 | **Counting and weighting.** Raw counts are dominated by common words. What stopwords and weighting do. A quick look at "distinctive" terms by place. |
| 0:30 | **Dictionary sentiment.** How it works, and a gallery of texts where it fails: negation, sarcasm, a name that is also a word. |
| 0:42 | **Read before you name.** Cluster or topic outputs need reading examples, not just labels. |
| 0:52 | **Preview:** the practice page, the reading, and the coding session. |

<!-- facilitator:start -->
### Lecture plan (slides)

| # | Slide | Min | Notes |
|---|---|---|---|
| 1 | Title | 1 | The plan for the week |
| 2 | Recap and the idea | 4 | Every step is a choice |
| 3 | What is a token? | 6 | Words, characters, subwords |
| 4 | Demo: one sentence, different tokenizers | 6 | English, Chinese, and mixed; jieba is not perfect |
| 5 | Counting, and why raw counts mislead | 6 | Common words; stopwords; "US" becomes "us" |
| 6 | Distinctive terms | 7 | Weighting; compare groups (invented numbers) |
| 7 | Dictionary sentiment | 5 | A toy dictionary; negation |
| 8 | Where it fails | 7 | Gallery. Do **not** say that Chinese scores zero: students find it in Exercise 2d |
| 9 | Read before you name | 10 | Coherent, too mixed, boilerplate: the main point |
| 10 | Before the coding session | 4 | Practice page, reading, the data rules |
| 11 | Questions | 4 | |
<!-- facilitator:end -->

---

## Between sessions (about 20 min): practice page

Students open **What counts as a word?** after the learning session and before the coding session.

- **Pick a tokenizer:** five invented texts (English, Chinese, mixed); choose a tokenizer and see the tokens and the count change.
- **Same headlines, different counts:** switch lowercasing, stopwords, and a short-word filter on and off. One setting deletes "AI", and one deletes the country "US".
- **Fix the dictionary:** a toy sentiment dictionary on eight texts. Some can be fixed, and three cannot.
- **Read before you name:** three clusters; decide to name it, call it too mixed, or say it is boilerplate.
- **Colab task:** tokenize five texts two ways and print the counts.

---

## Coding session (about 2 h): breakout rooms, no lecture

Notebook: `notebooks/week05_analyze_text.ipynb`. Pairs in breakout rooms. Exercises 1 to 3 are required.

| Time | Exercise |
|---|---|
| 0:00–0:15 | **Warm-up:** tokenize five texts two ways. Install and test the Chinese tokenizer. |
| 0:15–0:45 | **Ex 1:** count and compare. Top words per subreddit, raw, cleaned, and distinctive. Then Chinese tokens per text, by spaces versus jieba. What changes, and what do you not trust? |
| 0:45–1:15 | **Ex 2:** VADER sentiment on the Reddit posts. Read ten texts by hand and compare with the score. Then run VADER on the Chinese news texts. Where does it fail? |
| 1:15–1:40 | **Ex 3:** bug hunt. An AI-written function that runs without errors and has three planted mistakes. Find them. |
| 1:40–1:55 | **Ex 4 (stretch):** cluster the Reddit posts, read examples from each cluster, and name it (or say it is too mixed). |
| 1:55–2:00 | Log; optional share-out. |

Post a time check in the main chat at each boundary. Hints for Exercise 3 come from facilitators only.

## Homework (45 minutes or less)

- Run one method from today on your own project's text, or on a sample of it.
- Add to your project card: one thing this method would hide in your data.

## Hand-off to Week 6

Students leave with counts, a sentiment score, and a list of where the methods fail. Week 6 asks an AI to label texts instead, and measures how well it agrees with humans.

<!-- facilitator:start -->
## Decisions and open items (Week 5)

**Decided**
1. **Shared corpus:** the Reddit sample (657 posts from three less-personal subreddits) for counting, sentiment and clustering, plus the Chinese news texts from the Week 1 searches for tokenization. Students then apply the methods to their own Week 4 text.
2. **Reddit data rights:** Kokil confirmed the HAPS Reddit data may be shared with students. The posts are public, but some discuss personal and financial situations. The files are scrubbed (links, handles and phone-like numbers replaced; post URLs removed; dates reduced to year-month), kept **out of the public repository**, and shared with the class only, with a handling note.
3. **Week 6 human labels:** use Kokil's published CLAPTON data, which has human labels (constructiveness, justification, empathy and respect, uncivil abuse) and ready-made LLM outputs on Twitter and Reddit messages. Student-labeled samples of their own text are an extra.

**Still to do**
4. **Share the files.** Upload `week05_corpus.zip` to the class drive and put the link in the Week 5 materials (not on the public site).
5. **Chinese tokenizer.** Chosen: jieba (`%pip install -q jieba`). Still to do: time the install in a fresh Colab runtime.
6. **English sentiment tool.** Chosen: VADER (`vaderSentiment`), an English dictionary made for social media. The notebook has students run it on the Chinese texts to see that it does not cover them.
7. **Students without their own text yet.** They can stay on the shared corpora. Decide whether that is acceptable.
8. **Bugs for Exercise 3.** Chosen (in `instructor/week05_answer_key.md`): whitespace tokenizing Chinese; averaging English-dictionary sentiment over Chinese texts; scoring only the post titles. A fourth candidate (`>= 0` for positive) was dropped because it changed only one number.
9. **Redistribution of the news snippets.** The news texts are search-result titles and snippets from the Week 1 searches. Check that sharing them with the class (privately) is acceptable.
10. **Add Week 5 to the site** (`build_site.py` and `mkdocs.yml`) when you want it released. Not done yet.
<!-- facilitator:end -->
