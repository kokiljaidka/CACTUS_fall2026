# CACTUS Fall 2026

**Coding with AI for Communication and Culture Research**
An 8-week hands-on Python series for graduate students working on AI, culture, social media, and related topics.

National University of Singapore · Organizer: Dr. Kokil Jaidka (jaidka@nus.edu.sg)
Starts Tuesday, Nov 17, 2026

## What this is

A workshop where you learn to use AI to write code for your own research, and to check that the code does what you meant. No prior coding experience is needed. All sessions run on Zoom. Each week has two parts:

- **Learning session (about 2 hours):** a supervised walk-through of the week's concepts and worked examples. You can follow along on your laptop, and facilitators help anyone who gets stuck.
- **Coding session (about 2 hours):** no lecture. You join a breakout room and work through the exercises, in pairs early on and on your own data later. Facilitators visit the rooms to troubleshoot.

You bring a dataset (or a plan to get one) and a rough research question. Over 8 weeks it becomes working code.

## Approach

**AI writes, you decide.** You will use AI assistants every week. The skill you are building is not typing code from memory. It is:

1. describing a task precisely,
2. reading what the AI wrote,
3. testing it on a small sample, and
4. recording how you checked.

Every notebook cell the AI wrote needs a note on how you verified it. You will keep a short **prompt-and-verification log** throughout the series.

**Common ways AI code goes wrong** (we practice catching these):
- code that runs but silently drops or changes data
- invented column names, functions, or packages
- code that does something different from what you asked
- confident explanations that are wrong

## Tools

- **Google Colab:** nothing to install. You need a Google account.
- **A chat AI assistant** (ChatGPT, Claude, Gemini, or Colab's built-in help). Use whichever you have.
- **SerpAPI:** a free account, used from week 1.
- **GitHub account:** set up in week 3.

**API keys are secrets.** Store them in Colab Secrets. Never paste a key into an AI chat, a notebook you share, or a GitHub repository.

## Schedule

Topics may shift slightly after the planning survey.

| Week | Focus | You will be able to… | Data |
|---|---|---|---|
| 1 | **First API calls** | Run a notebook, call SerpAPI, and change the query, country, and language. Explain each line with an AI assistant. Store a key safely. | Google search, news, and trends results for AI topics across Singapore, Hong Kong, and Taiwan |
| 2 | **Clean it, chart it** | Load and clean a table, chart it, and catch silent errors with checks. Read an error message and make a first attempt at a fix. | Starbucks comments from seven Southeast and East Asian places (Oct 2024) |
| 3 | **Verify and analyze** | Run descriptive stats and a simple regression in code. Test AI-written stats code against a known answer. Use basic GitHub. | Simulated experiment or survey data with known effects |
| 4 | **Collect your own data** | Collect posts through an API or export and save raw data. Explain platform terms, consent, and anonymization. | Reddit, YouTube comments, or Bluesky |
| 5 | **Analyze text** | Count, tokenize (including Chinese), run sentiment, and find topics or clusters. Interpret results critically. | Shared corpus on AI in Singapore, Hong Kong, and Taiwan |
| 6 | **AI as annotator** | Write a codebook, have an LLM label texts, and compare to human labels (accuracy, agreement). Report where it fails. | Shared corpus subset with hand-coded labels |
| 7 | **Choose a track** | Networks, images and memes, or a mock feed or experiment. | Track-specific data, or your own |
| 8 | **Reproduce and present** | Rerun your whole pipeline from scratch, document it, and present results with limitations. | Your own data |

## Week 1 in brief

Week 1's coding session has **no debugging**. You run a working template, change the search query, country (`gl`), and language (`hl`), and compare what Google returns in different places. You ask an AI assistant to explain each part of the code and predict what the output will look like before you run it. Debugging starts in week 2.

## What we expect

- Attend both sessions each week and bring a laptop.
- Bring a dataset or a plan for one, plus a rough research question.
- Complete the short weekly notebook and keep your verification log.
- In week 8, present a working pipeline on your own data.

This workshop is not for credit. There are no grades, but the weekly work builds on itself, so keeping up matters.

## Repository layout

```
README.md            this file
schedule/            weekly plans (learning session and coding session)
notebooks/           Colab-ready notebooks for each week
data/                shared datasets (see data/README.md)
scripts/             helpers that build the notebooks and datasets
CACTUS_fall_2026_clean.qsf   planning survey (Qualtrics export)
```

## Credits

CACTUS began as a 2021 NUS tutorial series forked from COMM313 (Spring 2018, Annenberg School for Communication, University of Pennsylvania) by Dr. Matt O'Donnell. This 2026 series is a new design built around AI-assisted coding.
