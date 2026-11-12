# CACTUS Fall 2026

**CACTUS: Computational Analysis for Communication on Text, User-generated content, and Social networks**
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
- **SerpAPI:** a free account. Optional in week 1 (saved searches work for everyone), used for new searches from week 2.
- **GitHub account:** set up in week 3.

**API keys are secrets.** Store them in Colab Secrets. Never paste a key into an AI chat, a notebook you share, or a GitHub repository.

## Schedule

Topics may shift slightly after the planning survey.

| Week | Focus | You will be able to… | Data |
|---|---|---|---|
| 1 | **Define your problem, and how code thinks** | Write a project card: case study, main question, sub-questions. Explain variables, lists, dictionaries, functions, and loops. Run a notebook, read a search response, and ask an AI to explain code. | Google search, news, and trends results for AI topics across Singapore, Hong Kong, and Taiwan (saved searches) |
| 2 | **Clean it, chart it** | Load and clean a table, chart it, and catch silent errors with checks. Read an error message and make a first attempt at a fix. | Starbucks comments from seven Southeast and East Asian places (Oct 2024) |
| 3 | **Verify and analyze** | Run descriptive stats and a simple regression in code. Test AI-written stats code against a known answer. Use basic GitHub. | Simulated experiment or survey data with known effects |
| 4 | **Collect your own data** | Collect posts through an API or export and save raw data. Explain platform terms, consent, and anonymization. | Reddit, YouTube comments, or Bluesky |
| 5 | **Analyze text** | Count, tokenize (including Chinese), run sentiment, and find topics or clusters. Interpret results critically. | Shared corpus on AI in Singapore, Hong Kong, and Taiwan |
| 6 | **AI as annotator** | Write a codebook, have an LLM label texts, and compare to human labels (accuracy, agreement). Report where it fails. | Shared corpus subset with hand-coded labels |
| 7 | **Choose a track** | Networks, images and memes, or a mock feed or experiment. | Track-specific data, or your own |
| 8 | **Reproduce and present** | Rerun your whole pipeline from scratch, document it, and present results with limitations. | Your own data |

## Week 1 in brief

Week 1 has no debugging. **Session 1** (learning) is about your project: you leave with a finished project card. **Session 2** (coding) starts with a drag-and-drop puzzle page that teaches how code thinks (variables, lists, dictionaries, functions, loops, reading a nested response). Then you do the same ideas in real code in Colab: write your project row as a dictionary, read a SerpAPI response, and ask an AI to explain code. Debugging starts in Week 2.

## Practice pages

Each week has a short interactive page that recaps the basics, followed by a small coding task in Colab with a built-in check. The pages run in the browser, need no installation, and send nothing anywhere. Source is in `practice/`; the plan for all weeks is in [practice/page_specs.md](practice/page_specs.md). Built so far: Week 1 (Cactus Code Garden) and Week 2 (Silent Changes).

## Required reading

The course text is *Computational Analysis of Communication* by van Atteveldt, Trilling & Arcila (2022). It is free and open access at [cssbook.net](https://cssbook.net). Each week has required sections, listed below and on the week's page. Reading is required but not graded. Plan to read before the session it is listed under.

The book shows code in Python and R. **Follow the Python.** You will not type this code from memory: an AI assistant writes it with you, and the book is where you learn what the code means so you can check it. The book predates AI coding assistants.

| Week | Required sections |
|---|---|
| 1 | [Ch 1](https://cssbook.net/content/chapter01.html) §1.1; [Ch 3](https://cssbook.net/content/chapter03.html) §3.1 to 3.3 (objects and data types, loops and conditions, functions) |
| 2 | [Ch 5](https://cssbook.net/content/chapter05.html) §5.1 to 5.2 (data frames; reading and saving); [Ch 6](https://cssbook.net/content/chapter06.html) §6.1 to 6.4 (filtering, calculating, grouping, merging); [Ch 4](https://cssbook.net/content/chapter04.html) §4.2 (understanding errors and getting help) |
| 3 | [Ch 7](https://cssbook.net/content/chapter07.html) §7.1 (exploratory analysis); [Ch 8](https://cssbook.net/content/chapter08.html) §8.1 to 8.2 (statistical modeling, concepts and principles); [Ch 4](https://cssbook.net/content/chapter04.html) §4.3 (GitHub and notebooks) |
| 4 | [Ch 12](https://cssbook.net/content/chapter12.html) §12.1 (web APIs) and §12.4 (ethical, legal, and practical considerations); [Ch 5](https://cssbook.net/content/chapter05.html) §5.3 (data from online sources) |
| 5 | [Ch 9](https://cssbook.net/content/chapter09.html) §9.1 (text as a string of characters); [Ch 10](https://cssbook.net/content/chapter10.html) §10.1 and §10.4 (bag of words; which preprocessing to use); [Ch 11](https://cssbook.net/content/chapter11.html) §11.3 (dictionary approaches) |
| 6 | [Ch 11](https://cssbook.net/content/chapter11.html) §11.1 and §11.4 (choosing a method; supervised classification); [Ch 8](https://cssbook.net/content/chapter08.html) §8.5 (validation and best practices) |
| 7 | Your track: networks, [Ch 13](https://cssbook.net/content/chapter13.html) §13.1 to 13.2; images, [Ch 14](https://cssbook.net/content/chapter14.html) §14.1 to 14.2; mock feed or experiment, [Ch 8](https://cssbook.net/content/chapter08.html) §8.1 and [Ch 16](https://cssbook.net/content/chapter16.html) §16.3 |
| 8 | [Ch 15](https://cssbook.net/content/chapter15.html) §15.3 (publishing your source); [Ch 16](https://cssbook.net/content/chapter16.html) §16.3 (open, transparent, and ethical computational science) |

Other sections of these chapters are good for going further. Weeks 3 to 8 may shift slightly after the planning survey, and the list will be updated.

## What we expect

- Attend both sessions each week and bring a laptop.
- Bring a rough topic. In Week 1 you turn it into a project card with [Designing your project](project/designing_your_project.md): a main question, sub-questions, and a plan for the data.
- Do the required reading for the week.
- Complete the short weekly notebook and keep your verification log.
- In week 8, present a working pipeline on your own data.

This workshop is not for credit. There are no grades, but the weekly work (and the required reading) builds on itself, so keeping up matters.

<!-- facilitator:start -->
## Repository layout

```
README.md            this file
schedule/            weekly plans (learning session and coding session)
project/             guide and template for designing your project
practice/            interactive practice pages (source in src/, shared parts in shared/)
slides/             lecture slides: web pages, PDFs, presenter views with notes (built by build_slides.py)
facilitators/       guide for the team running the sessions
mkdocs.yml, .github/   the student site: build_site.py makes docs/, mkdocs builds site/, an Action publishes it
notebooks/           Colab-ready notebooks for each week
data/                shared datasets (see data/README.md)
scripts/             helpers that build the notebooks and datasets
CACTUS_fall_2026_clean.qsf   planning survey (Qualtrics export)
```
<!-- facilitator:end -->

## Credits

CACTUS began as a 2021 NUS tutorial series forked from COMM313 (Spring 2018, Annenberg School for Communication, University of Pennsylvania) by Dr. Matt O'Donnell. This 2026 series is a new design built around AI-assisted coding. Optional reading is from *Computational Analysis of Communication* by Wouter van Atteveldt, Damian Trilling and Carlos Arcila Calderón (Wiley-Blackwell, 2022; open access).
