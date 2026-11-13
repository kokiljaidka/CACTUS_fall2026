"""Build notebooks/week05_analyze_text.ipynb. Re-run after editing.

Data: the two private CSV files in week05_corpus.zip (see scripts/prepare_week05_corpus.py). They are shared with the class
through the class drive and are NOT in the public repository. The notebook asks Colab users to upload the zip.
"""
import os

import nbformat as nbf

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "notebooks", "week05_analyze_text.ipynb")
cells = []


def md(t):
    cells.append(nbf.v4.new_markdown_cell(t.strip()))


def code(t):
    cells.append(nbf.v4.new_code_cell(t.strip()))


md("""
# Week 5: Analyze text

**CACTUS Fall 2026 · Coding session**

Turning text into numbers loses things. Today you split text into tokens, count words, score sentiment with a dictionary, and find a pattern. At each step you ask: **what did this step hide?**

**Goals today**
- tokenize English and Chinese, and see why one method does not fit both
- count words and compare groups, raw and weighted
- run a dictionary sentiment score and **check it against texts you read by hand**
- find mistakes in AI-written text-analysis code
- say, in a sentence, where each method fails

**Data (private to this class)**
- **Reddit sample:** 657 public posts from r/jobs, r/personalfinance and r/mildlyinfuriating (English). Some posts discuss personal and financial situations.
- **News texts:** 307 news and web results about AI from Singapore (English), Hong Kong and Taiwan (Traditional Chinese). Mostly headlines.
- Your own text from Week 4 is for the homework.

**Rules**
- Predict before you run. Never accept AI code you have not read.
- **The data is for this course only.** Do not post it, upload it to a public place, or share it outside the class.
- **Do not paste posts from the data into an AI chat.** Describe the problem, or use invented examples.
- Do not try to identify anyone. If a post identifies someone, tell a facilitator and do not copy it.
- Keys and passwords never go in a cell.

**Run cells one at a time**, not "Run all". Some cells are for you to fill in.
""")

md("""
## How this session runs

- There is **no lecture** in the coding session. You will be in a breakout room with a partner, and the facilitators visit the rooms.
- **Stuck?** Try these, in order, for no more than 5 minutes:
  1. Read the last line of any error message. What is it telling you?
  2. Re-read the instructions for the step. Did you skip a part?
  3. Ask your partner, then ask an AI assistant to explain the message (never paste data from the corpora).
  4. Still stuck? Click **Ask for help** in Zoom or message the facilitators in the main chat. Say what you expected, what happened, and what you already tried.
""")

md("""
## Setup (about 5 min)

Two small libraries are not in Colab by default: **jieba** (splits Chinese into words) and **vaderSentiment** (an English sentiment dictionary made for social media). The install takes under a minute.

If the install fails, tell a facilitator. You can still do the exercises: for Chinese, use pairs of neighbouring characters instead of jieba, and say so in your log.
""")

code("""
%pip install -q jieba vaderSentiment
""")

code("""
import math
import os
import re
import zipfile
from collections import Counter

import numpy as np
import pandas as pd
import jieba
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

FILES = ["week05_reddit_sample.csv", "week05_news_corpus.csv"]
if not all(os.path.exists(f) for f in FILES):
    try:
        from google.colab import files
        print("Upload week05_corpus.zip (the link is on the class drive).")
        for name in files.upload():
            if name.endswith(".zip"):
                zipfile.ZipFile(name).extractall(".")
    except ImportError:
        raise SystemExit("Put " + " and ".join(FILES) + " in the same folder as this notebook.")

reddit = pd.read_csv("week05_reddit_sample.csv")
news = pd.read_csv("week05_news_corpus.csv")
print(len(reddit), "Reddit posts;", len(news), "news texts")
print(news.groupby(["place", "language"]).size())
""")

md("""
---
## Warm-up: tokenize five texts two ways (about 15 min)

These are the same five texts as the practice page. The practice page gave you a short script. Paste it below (or use this one), run it, and then add **jieba**.

**Predict:** how many tokens will splitting on spaces give for the two Chinese texts? And for the regex?

> My prediction:
""")

code("""
texts = [
    "AI isn't replacing teachers, it's changing homework.",
    "New York-based startup launches #AI tutor for $5/month",
    "新加坡推出人工智能學習計劃",
    "香港大學生如何使用生成式人工智慧",
    "Singapore 學生 use ChatGPT 寫功課",
]


def by_spaces(t):
    return t.split()


def by_words(t):
    return re.findall(r"\\w+", t.lower())


def by_jieba(t):
    # Task: return the words jieba finds, without blanks.
    pass


for t in texts:
    print(len(by_spaces(t)), len(by_words(t)), t)
""")

code("""
# Check 0. Do the numbers match what you saw on the practice page?
assert len(by_spaces(texts[2])) == 1, "Splitting a Chinese sentence on spaces should give one token. Did you change by_spaces?"
j = by_jieba(texts[2])
assert j and len(j) >= 3, "by_jieba should return a list of several words for the Chinese sentence. Did you fill it in?"
print("jieba:", j)
print("spaces:", by_spaces(texts[2]))
""")

md("""
> Log (warm-up): what surprised you? Which text got the most sensible tokens from which method? (There is no perfect one.)
""")

md("""
---
## Exercise 1: Count and compare (required, about 30 min)

**Question:** what do people write about in each subreddit, and how much do we trust the word counts?

Build the **Reddit text** first: the title and the post text together.

**1a.** Tokenize every post (lowercase words only), and count the 15 most common words in each subreddit.
**1b.** Do it again after removing **stopwords** (little words like *the*, *and*). Use `ENGLISH_STOP_WORDS` from scikit-learn.
**1c.** Raw counts mostly show what is common everywhere. Find the **distinctive** words for each subreddit: words used much more there than in the other two. One simple way: for each word, compare its share of the words in this subreddit with its share in the others (a log ratio), and keep words used at least 15 times.

**How to prompt well.** Give the AI the context it cannot see, and **never paste posts**:

> I have a pandas DataFrame `reddit` with columns `subreddit` and `body` (text). Write code to (1) lowercase and tokenize `body` with a regular expression, (2) count the 15 most common words per subreddit, (3) do it again without scikit-learn's English stopwords, (4) find words that are distinctive for each subreddit using a smoothed log ratio of relative frequencies, ignoring words used fewer than 15 times. Explain each step in one sentence.

**Predict:** what will the top 5 words per subreddit be before you remove stopwords? What will change after?

> My prediction:
""")

code("""
# Task 1a. Build reddit["body"] and the raw top words per subreddit.
# Store results as dicts: top_raw[subreddit] = [(word, count), ...] (15 pairs).
""")

code("""
# Task 1b. The same, without stopwords. top_clean[subreddit] = [(word, count), ...]
""")

code("""
# Task 1c. Distinctive words. distinct[subreddit] = [word, word, ...] (best first, at least 15 words)
""")

code("""
# Check 1.
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
for s in sorted(reddit["subreddit"].unique()):
    assert s in top_raw and s in top_clean and s in distinct, f"Missing results for {s}"
    clean_words = [w for w, _ in top_clean[s]]
    assert len(clean_words) >= 10, f"{s}: top_clean should have 15 words"
    assert not (set(clean_words) & ENGLISH_STOP_WORDS), f"{s}: stopwords are still in top_clean: {sorted(set(clean_words) & ENGLISH_STOP_WORDS)}"
    overlap = len(set(clean_words[:15]) & set(distinct[s][:15]))
    assert overlap <= 10, f"{s}: your distinctive words are almost the same as the plain counts. What should weighting change?"
    print(s, "->", ", ".join(distinct[s][:8]))
""")

md("""
**What changed, and what do you not trust?** Fill in.

| Question | Your answer |
|---|---|
| The top 5 raw words in one subreddit were... | |
| After removing stopwords they were... | |
| The distinctive words are different because... | |
| One word that stopword removal or lowercasing may have deleted that you wanted | |
| One thing you do not trust in these lists | |

**1d. Chinese.** The news texts in Hong Kong and Taiwan are Chinese. Compute the **average number of tokens per text** for Hong Kong when you (i) split on spaces and (ii) use jieba. Store them as `hk_spaces` and `hk_jieba`.
""")

code("""
# Task 1d.
""")

code("""
# Check 1d.
assert hk_spaces < 3, "Splitting Chinese on spaces should give very few tokens per text."
assert hk_jieba > 5, "jieba should find several words per headline. Did you apply it to the Hong Kong texts?"
print(f"Hong Kong: {hk_spaces:.1f} tokens per text by spaces, {hk_jieba:.1f} with jieba")
""")

md("""
> Log (Exercise 1): which choice (lowercasing, stopwords, tokenizer) changed your results the most? What would you do differently on your own text?
""")

md("""
---
## Exercise 2: Dictionary sentiment, and checking it by hand (required, about 30 min)

VADER is a dictionary: it gives each word a score, adds them up, and adjusts for a few rules (not, very, capital letters, !). It returns a **compound** score from -1 (very negative) to +1 (very positive). Use ±0.05 as the cut-offs for negative and positive.

**2a.** Compute the compound score for every Reddit post (the `body` text), as a new column `compound`.
**2b.** Compare the **mean score** by subreddit. Does the order match what you expected?
**2c.** **Read ten posts by hand**, label each positive, negative, or neutral yourself, then compare with VADER.
**2d.** Run VADER on the **Chinese** news texts. What do you get? What should you report?

**Predict:** which subreddit will be most positive, and which most negative? Will VADER agree with you on most posts?

> My prediction:
""")

code("""
# Task 2a. analyzer = SentimentIntensityAnalyzer(); then add reddit["compound"].
""")

code("""
# Task 2b. Mean compound by subreddit.
""")

code("""
# Task 2c. Here are ten posts. Read each one and fill my_labels with "pos", "neg" or "neu" in the same order.
sample = reddit.sample(10, random_state=5).reset_index(drop=True)
for i, row in sample.iterrows():
    print(i, f"[{row['subreddit']}]", row["body"][:350].replace("\\n", " "))
    print()
my_labels = []   # ten labels, e.g. ["neg", "neu", ...]
""")

code("""
# Check 2.
assert "compound" in reddit.columns, "Add a compound column to reddit (Task 2a)."
assert len(my_labels) == 10 and set(my_labels) <= {"pos", "neg", "neu"}, "my_labels should hold 10 labels, each pos, neg or neu."
to_label = lambda c: "pos" if c > 0.05 else "neg" if c < -0.05 else "neu"
vader_labels = [to_label(c) for c in sample["compound"]]
agree = sum(a == b for a, b in zip(my_labels, vader_labels))
print(f"You and VADER agree on {agree} of 10.")
for i, (a, b) in enumerate(zip(my_labels, vader_labels)):
    if a != b:
        print(f"  text {i}: you said {a}, VADER said {b} (compound {sample['compound'][i]:.2f})")
""")

md("""
**Where does VADER fail?** Pick two texts where you and VADER disagree and say why (negation? sarcasm? a word used differently here? a long post with mixed feelings?).

> Log (2c):
""")

code("""
# Task 2d. Run VADER on the Chinese news texts (language == "zh-Hant") and look at the scores.
# Store the share of Chinese texts that score exactly 0 as share_zero_zh.
""")

code("""
# Check 2d.
assert share_zero_zh > 0.9, "Check that you scored the Chinese texts (language == 'zh-Hant') and measured the share that equal exactly 0."
print(f"{share_zero_zh:.0%} of the Chinese texts score exactly 0.")
""")

md("""
> Log (Exercise 2): why do the Chinese texts score 0? What would you report to a reader? What does a sentiment score **hide** in the Reddit posts?
""")

md("""
---
## Exercise 3: Bug hunt (required, about 25 min)

An AI assistant wrote this function. It **runs without errors** and prints a tidy summary. **It contains three mistakes.** Find them by checking the output against what you know from Exercises 1 and 2. Do not ask the facilitators for the answer first: they give hints only.

**Predict:** before you run it, which numbers do you expect to be wrong, and why?

> My prediction:
""")

code("""
def analyze(news, reddit):
    \"\"\"Written by an AI assistant. How long are the headlines, how positive is each place, which subreddit is most positive?\"\"\"
    an = SentimentIntensityAnalyzer()
    out = {}

    # 1. How long are the headlines, in words, in each place?
    news = news.copy()
    news["n_tokens"] = news["text"].apply(lambda t: len(t.split()))
    out["mean_tokens"] = news.groupby("place")["n_tokens"].mean().round(1).to_dict()

    # 2. How positive is each place's coverage?
    news["sentiment"] = news["text"].apply(lambda t: an.polarity_scores(t)["compound"])
    out["mean_sentiment"] = news.groupby("place")["sentiment"].mean().round(2).to_dict()

    # 3. Which subreddit has the largest share of positive posts?
    reddit = reddit.copy()
    reddit["compound"] = reddit["title"].fillna("").apply(lambda t: an.polarity_scores(t)["compound"])
    out["share_positive"] = (reddit["compound"] > 0.05).groupby(reddit["subreddit"]).mean().round(2).to_dict()
    return out


result = analyze(news, reddit)
print("The AI's summary:")
print("- Headline length (words):", result["mean_tokens"])
print("- Average sentiment by place:", result["mean_sentiment"])
print("- Share of positive posts:", result["share_positive"])
""")

md("""
**Find the three mistakes.** For each, write: where it is, what it does wrong, and what number or claim it makes wrong.

| # | Where | What is wrong | The claim it distorts |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

Then copy the function into the next cell, rename it `analyze_fixed`, and fix it.
""")

code("""
# Write analyze_fixed here.
""")

code("""
# Check 3.
res = analyze_fixed(news, reddit)
assert res["mean_tokens"]["Hong Kong"] > 3 and res["mean_tokens"]["Taiwan"] > 3, "Headline length in Hong Kong and Taiwan is still too small. Look at how the words are counted."
assert all(math.isnan(res["mean_sentiment"][p]) for p in ("Hong Kong", "Taiwan")), "Sentiment for Chinese texts should not be reported as a number. What is the English dictionary measuring there?"
an = SentimentIntensityAnalyzer()
body = reddit["title"].fillna("") + ". " + reddit["text"].fillna("")
expected = (body.apply(lambda t: an.polarity_scores(t)["compound"]) > 0.05).groupby(reddit["subreddit"]).mean().round(2).to_dict()
assert res["share_positive"] == expected, f"Share of positive posts is not right yet. Expected {expected}. Which text is being scored?"
print("All three fixed.")
""")

md("""
> Log (Exercise 3): which mistake was hardest to see? Why did the code run without any error?
""")

md("""
---
## Exercise 4 (stretch): find a cluster and name it (about 15 min)

Group the Reddit posts by their words, then **read examples before you name a group**.

1. Turn each post into a TF-IDF vector (words weighted by how distinctive they are). Use `TfidfVectorizer(stop_words="english", min_df=5)`.
2. Cluster with `KMeans(n_clusters=5, random_state=0, n_init=10)`.
3. For each cluster, print the **top 8 words** and **three example posts** (first 200 characters).
4. Name each cluster **after reading the examples**, or write "too mixed to name" or "not content".

> Log (Exercise 4): which cluster could you name, and which could you not? What did the top words alone not tell you?
""")

code("""
# Task 4.
""")

md("""
---
## Stretch 2: tag the script (about 10 min)

Real social media text mixes scripts and languages. Before you count or score anything, **tag each text by script**: how many of its letters are Latin (A to Z), Chinese (CJK), or another script?

A simple way: look at each character's Unicode code point. Latin letters are below U+024F, and Chinese characters are in U+4E00 to U+9FFF. (Devanagari, used for Hindi, is U+0900 to U+097F: change the range for the script in your own data.)

Tag the news texts as `latin`, `cjk`, `mixed`, or `none` (only emoji, numbers, or punctuation), and count how many of each. Then ask: what would you do with the `mixed` and `none` texts?
""")

code("""
# Stretch 2.
""")

md("""
---
## Log: what I learned today

- One choice that changed my results, and what it hid:
- One place a method failed, in one sentence:
- One thing I would check before trusting a sentiment score on my own data:

**Homework (45 minutes or less):** run one method from today on your own project's text (or a sample of it). Before you count, **tag the script or language, and flag exact duplicates and likely automated posts** (many posts that repeat the same text) instead of counting them as many voices. Add to your project card: **one thing this method would hide in your data.** If you do not have your own text yet, use the news texts and say so.
""")

nb = nbf.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
nbf.write(nb, OUT)
print("wrote", os.path.normpath(OUT))
