# CACTUS Fall 2026

**CACTUS: Computational Analysis for Communication on Text, User-generated content, and Social networks**
An 8-week hands-on Python series for graduate students working on AI, culture, social media, and related topics.

National University of Singapore · Organizer: Dr. Kokil Jaidka (jaidka@nus.edu.sg)
Starts Tuesday, Nov 17, 2026

## What this is

A workshop where you learn to use AI to write code for your own research, and to check that the code does what you meant. **No prior coding experience is needed.** You bring a rough topic and, ideally, some data. Over 8 weeks it becomes working code on your own project, and you present it in Week 8.

**Who it is for:** graduate students in communication and related fields, working on AI, culture, social media, or similar topics. It is not for credit and there are no grades, but each week builds on the last, so keeping up matters.

**What you leave with**
- A project card: a case study, a main question, and sub-questions you can actually answer.
- Your own dataset, collected, logged, anonymized, and described in a data card.
- A notebook that cleans, analyzes, and charts your data, with a record of how you checked each AI-written step.
- A habit: predict, read, test, record.

## How each week runs

All sessions run on Zoom, and you follow along on your own laptop. Facilitators are there to help anyone who gets stuck.

| Part | Time | What happens |
|---|---|---|
| **Reading** | About 1 hour, before the session | Required sections from the course book (listed in the table below). Not graded |
| **Learning session** | About 1 hour (2 hours in Week 1) | A lecture with live demos on the week's ideas |
| **Practice page** | About 20 minutes | A short interactive page in your browser. It recaps the ideas and ends with a small coding task |
| **Coding session** | About 2 hours | No lecture. You join a breakout room and work through the exercises in a Colab notebook, in pairs early on and on your own data later |
| **Homework** | 45 minutes or less | A small step on your own project |

So plan for about 3 hours live each week, plus the reading and the homework. Week 1 has two 2-hour sessions, and Week 7 has two sessions (a shared one and a track one).

## Before Week 1: three things

1. **A Google account**, for Colab. Nothing to install.
2. **A chat AI assistant** (ChatGPT, Claude, Gemini, or Colab's built-in help). Use whichever you have.
3. **A rough topic**, and a thought about where your data will come from. In Week 1 you turn the topic into a project card with [Designing your project](project/designing_your_project.md). **If you do not have data yet, talk to the facilitators in Week 1.** You should have your data (or a plan agreed with us) by Week 3.

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
- **SerpAPI:** a free account. Optional in Week 1 (saved searches work for everyone), used for new searches from Week 2.
- **GitHub account:** set up in Week 3.

**API keys are secrets.** Store them in Colab Secrets. Never paste a key into an AI chat, a notebook you share, or a GitHub repository.

## Schedule: what to read and have ready, week by week

Everything you need for a week is in its row: the date, what you will do, the required reading, and what to have ready. Click the week's name for the full plan. Topics may shift slightly after the planning survey.

The course text is *Computational Analysis of Communication* by van Atteveldt, Trilling & Arcila (2022), free and open access at [cssbook.net](https://cssbook.net). The book shows code in Python and R: **follow the Python.** You will not type this code from memory (an AI assistant writes it with you). The book is where you learn what the code means, so you can check it. Reading is required but not graded.

| Week | Date | You will be able to… | Read first (required) | Have ready | Data |
|---|---|---|---|---|---|
| [1: Define your problem, and how code thinks](schedule/week01.md) | Tue Nov 17 (two sessions) | Write a project card: case study, main question, sub-questions. Explain variables, lists, dictionaries, functions, and loops. Run a notebook, read a search response, and ask an AI to explain code | [Ch 1](https://cssbook.net/content/chapter01.html) §1.1; [Ch 3](https://cssbook.net/content/chapter03.html) §3.1 to 3.3 (objects and data types, loops and conditions, functions) | A Google account, a chat AI, a rough topic. Tell us whether you already have data for your project. SerpAPI is optional | Google search, news, and trends results for AI topics across Singapore, Hong Kong, and Taiwan (saved searches) |
| [2: Clean it, chart it](schedule/week02.md) | Tue Nov 24 | Load and clean a table, chart it, and catch silent errors with checks. Read an error message and make a first attempt at a fix | [Ch 5](https://cssbook.net/content/chapter05.html) §5.1 to 5.2 (data frames; reading and saving), then [Ch 6](https://cssbook.net/content/chapter06.html) §6.1 to 6.4 (filtering, calculating, grouping, merging) and [Ch 4](https://cssbook.net/content/chapter04.html) §4.2 (understanding errors and getting help) | Your project card from Week 1. A plan for your data (talk to us if you have none) | Starbucks comments from seven Southeast and East Asian places (Oct 2024) |
| [3: Verify and analyze](schedule/week03.md) | Tue Dec 1 | Run descriptive stats and a simple regression in code. Test AI-written stats code against a known answer. Use basic GitHub | [Ch 7](https://cssbook.net/content/chapter07.html) §7.1 (exploratory analysis), then [Ch 8](https://cssbook.net/content/chapter08.html) §8.1 to 8.2 (statistical modeling, concepts and principles) and [Ch 4](https://cssbook.net/content/chapter04.html) §4.3 (GitHub and notebooks) | **A free GitHub account, made before the coding session.** Your data, or a plan agreed with the facilitators | Simulated experiment or survey data with known effects |
| [4: Collect your own data](schedule/week04.md) | Tue Dec 8 | Start from your own export, save raw data untouched, and log it. Explain platform terms, consent, and anonymization | [Ch 12](https://cssbook.net/content/chapter12.html) §12.4 (ethical, legal, and practical considerations), then Ch 12 §12.1 (web APIs) and [Ch 5](https://cssbook.net/content/chapter05.html) §5.3 (data from online sources) | **Your own export** (Twitter/X, Instagram, Facebook, Reddit, or Bluesky), or use the saved example. Read the [Ethics checklist](project/ethics_checklist.md) | Your own export, or a saved example |
| [5: Analyze text](schedule/week05.md) | Tue Dec 15 | Count, tokenize (including Chinese), run sentiment, and find topics or clusters. Interpret results critically | [Ch 9](https://cssbook.net/content/chapter09.html) §9.1 (text as a string of characters), then [Ch 10](https://cssbook.net/content/chapter10.html) §10.1 and §10.4 (bag of words; which preprocessing to use) and [Ch 11](https://cssbook.net/content/chapter11.html) §11.3 (dictionary approaches) | **Download the class corpus (a zip) from the class drive**; your facilitators share the link. It is for this course only | Shared corpus of Reddit posts and news texts (class drive) |
| [Midpoint show-and-tell](schedule/midpoint.md) | Tue Dec 22 | Present your project so far: the question, the data, one result and the check that told you it was right. No new content | Nothing new. Optional, to start Week 6 early: Ch 11 §11.1 and §11.4, Ch 8 §8.5 | **3 or 4 slides, 5 minutes**: your project card, your data and data card, one result with its check, and one thing your log caught. Public or de-identified data only | Your own data |
| | *Dec 29: break* | | | | |
| [6: AI as annotator](schedule/week06.md) | Tue Jan 5 | Write a codebook, have an LLM label texts, and compare to human labels (accuracy, agreement). Report where it fails | [Ch 11](https://cssbook.net/content/chapter11.html) §11.1 and §11.4 (choosing a method; supervised classification), then [Ch 8](https://cssbook.net/content/chapter08.html) §8.5 (validation and best practices) | **Download the class messages zip from the class drive.** A chat AI. The messages include abusive language, and you may step away at any time | Shared set of messages with human labels (class drive) |
| [7: Applying statistics to social media data](schedule/week07.md) | Tue Jan 12, and a second session on Thu Jan 14 (to be confirmed) | Session 1, everyone: plant an answer, handle rows that come in groups, and check results by permutation. Session 2, your track: networks, images and memes, or a mock feed or experiment | Before Session 1: [Ch 8](https://cssbook.net/content/chapter08.html) §8.1, 8.2 and 8.5. Between sessions, your track: networks, [Ch 13](https://cssbook.net/content/chapter13.html) §13.1 to 13.2; images, [Ch 14](https://cssbook.net/content/chapter14.html) §14.1 to 14.2; mock feed or experiment, [Ch 16](https://cssbook.net/content/chapter16.html) §16.3 | A small de-identified sample of your own data, for Session 2. Decide your track at the end of Session 1 | Simulated data with known answers, then your own |
| [8: Reproduce and present](schedule/week08.md) | Tue Jan 19 (presentations). The exercise is done before, by Jan 18 | Rerun your whole pipeline from scratch and have a partner rerun it (before Jan 19). Optionally present your project with its limits (Jan 19: five places, first come first served) | [Ch 15](https://cssbook.net/content/chapter15.html) §15.3 (publishing your source), then [Ch 16](https://cssbook.net/content/chapter16.html) §16.3 (open, transparent, and ethical computational science) | **Before Jan 19:** a GitHub repository with a notebook that runs from a fresh runtime, your data card, your verification log and a short README; your partner's rerun report. **Jan 19, if you sign up to present:** a 6-minute talk (3 or 4 slides). No keys or private data in the repository | Your own data |

Other sections of these chapters are good for going further.

## Week 1 in brief

Week 1 has no debugging. **Session 1** (learning) is about your project: you leave with a finished project card. **Session 2** (coding) starts with a drag-and-drop puzzle page that teaches how code thinks (variables, lists, dictionaries, functions, loops, reading a nested response). Then you do the same ideas in real code in Colab: write your project row as a dictionary, read a SerpAPI response, and ask an AI to explain code. Debugging starts in Week 2.

## Practice pages

Each week has a short interactive page that recaps the basics, followed by a small coding task in Colab with a built-in check. The pages run in the browser, need no installation, and send nothing anywhere. Source is in `practice/`; the plan for all weeks is in [practice/page_specs.md](practice/page_specs.md). Built so far: Weeks 1 to 6.

## What we expect

- Attend every session and bring a laptop.
- Bring a rough topic. In Week 1 you turn it into a project card with [Designing your project](project/designing_your_project.md): a main question, sub-questions, and a plan for the data.
- Do the required reading in the table above.
- Complete the weekly notebook and keep your verification log.
- On Dec 22, show where your project stands (5 minutes). In Week 8, rerun your project with a partner. Presenting on Jan 19 is optional: five places, first come first served.

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
