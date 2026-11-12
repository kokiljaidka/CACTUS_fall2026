# Week 5: Analyze text

**Theme:** Turning text into numbers loses things. Students learn to count, tokenize (including Chinese), run a dictionary-based sentiment score, and find patterns in a shared corpus, and to say what each step hides.
**Format:** Zoom. A 1-hour learning session (lecture with live demos), a 20-minute practice page, then a 2-hour coding session in breakout rooms with no lecture. About 3 hours live.

<!-- facilitator:start -->
> **Status: draft for review.** Not on the student site yet. This week depends on a **shared corpus** that does not exist as its own file yet. See the decisions at the end.
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
| Coding (exercises) | **Shared corpus:** news results about AI from Singapore, Hong Kong and Taiwan (from the Week 1 saved searches, about 300 short texts in English and Chinese). Stretch: the Starbucks comments | Already collected, on topic, in two scripts |

## Required reading

From *Computational Analysis of Communication* ([cssbook.net](https://cssbook.net)), the Python version. Required, not graded.

- **Before the learning session:** [Chapter 9](https://cssbook.net/content/chapter09.html), section 9.1 (text as a string of characters).
- **Before the coding session:** [Chapter 10](https://cssbook.net/content/chapter10.html), sections 10.1 and 10.4 (bag of words; which preprocessing to use), and [Chapter 11](https://cssbook.net/content/chapter11.html), section 11.3 (dictionary approaches).

<!-- facilitator:start -->
## Materials

| What | Where |
|---|---|
| Lecture slides (about 11 slides) | `slides/week05_*` (to build) |
| Practice page: What counts as a word? | `practice/week05_what_counts_as_a_word.html` (to build; tokenizations precomputed by a script) |
| Notebook | `notebooks/week05_analyze_text.ipynb` (to build) |
| Corpus | `data/week05_corpus.csv` (to build from the Week 1 saved searches) |

## Prep

- Build the corpus from `data/week01/serp_cache/` (news titles and snippets, with place, language, and source). Check how many rows have usable text, and which language each is in.
- Check that a Chinese tokenizer installs in Colab quickly (`jieba` is not preinstalled). Write the install cell and time it.
- Decide the sentiment tool for English, and be honest that no single dictionary covers both languages. Part of the week is noticing that.
- Do the notebook yourself first. Note what breaks and how long installs take.
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
| 4 | Demo: one sentence, four tokenizers | 6 | Include one Chinese sentence |
| 5 | Counting, and why raw counts mislead | 5 | Common words; stopwords |
| 6 | Distinctive terms | 5 | Weighting; compare places |
| 7 | Dictionary sentiment | 5 | What it measures |
| 8 | Where it fails | 6 | A small gallery |
| 9 | Read before you name | 6 | Examples inside a cluster |
| 10 | Before the coding session | 4 | Practice page, reading |
| 11 | Questions | 3 | |
<!-- facilitator:end -->

---

## Between sessions (about 20 min): practice page

Students open **What counts as a word?** after the learning session and before the coding session.

- **Tokenizer picker:** about eight short texts in English and Chinese; choose a tokenizer and see the tokens and the count change.
- **Lexicon sentiment:** drag words in and out of a small dictionary and watch the scores on tricky texts.
- **Colab task:** tokenize five texts two ways and print the counts.

---

## Coding session (about 2 h): breakout rooms, no lecture

Notebook: `notebooks/week05_analyze_text.ipynb`. Pairs in breakout rooms. Exercises 1 to 3 are required.

| Time | Exercise |
|---|---|
| 0:00–0:15 | **Warm-up:** tokenize five texts two ways. Install and test the Chinese tokenizer. |
| 0:15–0:45 | **Ex 1:** count and compare. Top words per place, raw versus weighted. What changes, and what do you not trust? |
| 0:45–1:15 | **Ex 2:** dictionary sentiment on a sample. Read ten texts by hand and compare with the score. Where does it fail? |
| 1:15–1:40 | **Ex 3:** bug hunt. AI-written text-analysis code with planted mistakes. Find them. |
| 1:40–1:55 | **Ex 4 (stretch):** find a cluster or topic, read its examples, and name it. |
| 1:55–2:00 | Log; optional share-out. |

Post a time check in the main chat at each boundary. Hints for Exercise 3 come from facilitators only.

## Homework (45 minutes or less)

- Run one method from today on your own project's text, or on a sample of it.
- Add to your project card: one thing this method would hide in your data.

## Hand-off to Week 6

Students leave with counts, a sentiment score, and a list of where the methods fail. Week 6 asks an AI to label texts instead, and measures how well it agrees with humans.

<!-- facilitator:start -->
## Decisions and open items (Week 5)

1. **The shared corpus.** Draft: the Week 1 news results about AI from Singapore, Hong Kong and Taiwan. Pros: already collected, on topic, two scripts. Cons: short texts (titles and snippets), about 300 rows, and the texts come from search results. Alternative: use the Starbucks comments, which are plentiful and multilingual but not about AI. Which do you prefer?
2. **Redistribution.** The saved search results include publisher snippets. Check SerpAPI's terms and the publishers' terms before keeping them in a public repository.
3. **Chinese tokenizer.** Confirm the choice and the install time in Colab.
4. **English sentiment tool.** Choose one dictionary-based tool. Say plainly that none covers Chinese well; students should notice and report it.
5. **Week 6 dependency.** Week 6 needs human labels on a subset of this corpus (about 100 texts). Start labeling soon. The RAs could do it as a first community task, with a short codebook.
6. **Bugs for Exercise 3.** Candidates: whitespace tokenizing Chinese; removing a stopword list that deletes "AI"; counting without lowercasing; averaging sentiment across languages; scoring translated text and calling it the original. Choose three and keep them in the private key.
<!-- facilitator:end -->
