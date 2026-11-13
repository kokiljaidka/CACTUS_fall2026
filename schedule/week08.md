# Week 8: Reproduce and present

**Theme:** A result you cannot rerun is a claim, not a finding. **Before presentation day** you rerun your whole pipeline from a clean start, have a partner rerun it, and fix what breaks. **On presentation day** (Tue Jan 19) there are only presentations. **Presenting is optional: there are five places, first come first served.** Everyone is welcome to come and listen.
**Format:** a reproducibility exercise in pairs before Jan 19 (about 2 hours of your own time, spread over the days before), then Zoom on Tuesday, Jan 19 for the presentations (about 1 hour).

<!-- facilitator:start -->
> **Status: built.** The slides and the practice page are built and tested; the rerun report template is on the site. There is no notebook or answer key this week. **Decided:** the reproducibility exercise is done before presentation day, with the partner feedback shared at least; on Jan 19 there are only presentations (opt-in, first come first served, at most 5; 6 minutes plus 2 for questions each). The exercise dates below are a proposal: confirm them.
<!-- facilitator:end -->

## Objectives

By the end of the week, students can:
1. Rerun a notebook from a fresh runtime, top to bottom, and fix what breaks.
2. Check that no key, password or private data is in a shared notebook or repository.
3. Document a project so that someone else can rerun it: a data card, a log, and a short README.
4. Say what a result does and does not support, with the sample, the checks and the limits.
5. If you choose to present: present a project in six minutes, and answer questions about it.

## Required reading

From *Computational Analysis of Communication* ([cssbook.net](https://cssbook.net)), the Python version. Required, not graded.

- **Before the exercise:** [Chapter 15](https://cssbook.net/content/chapter15.html), section 15.3 (publishing your source), and [Chapter 16](https://cssbook.net/content/chapter16.html), section 16.3 (open, transparent, and ethical computational science).

## Before presentation day: the reproducibility exercise

Do this in pairs, before Jan 19. The slides (about 20 minutes) and the practice page (about 20 minutes, optional) are in "Your links".

| When (proposed) | What |
|---|---|
| By Thu Jan 14 | Put your notebook, data card, verification log and a short README in your GitHub repository, and **run it from a fresh runtime yourself** first: in Colab, **Runtime, then Restart session and run all**. Fix what breaks. Common causes: a variable defined in a cell you later deleted, cells run out of order, a file path that only works on your computer, a package that was never installed in the notebook |
| By Fri Jan 15 | Check for secrets and private data: no API key, password or raw private data in the notebook, its outputs, or the repository (keys belong in Colab Secrets). Share the repository link in the chat. You are given a partner |
| By Sun Jan 17 | **Rerun your partner's notebook** from a fresh runtime, with only the notebook and the README, on the **shared or de-identified sample only**. Fill in the [rerun report](../project/rerun_report.md) and send it to the owner |
| By Mon Jan 18 | Read the report you received. Fix what broke, and reply: what you changed and what you left |

**What is shared at least:** your repository link, and the rerun report each way.

## Presentation day (Tue Jan 19)

**Presenting is optional.** There are **five places, first come first served**. To take one, add your name to the sign-up sheet your facilitators share (**[sign-up link and opening date to be added]**). Once five are taken, the sheet closes. Everyone else is welcome to attend and ask questions. The reproducibility exercise is for everyone, whether or not you present.

| Time | What |
|---|---|
| 0:00 | Welcome, the order, the rules (5 minutes) |
| 0:05 | Presentations: six minutes each, plus two minutes of questions (up to five) |
| About 0:50 | Close: what to take with you, and what comes next |

### The presentation (6 minutes, if you present)

Four parts, three or four slides, public or de-identified data only.

| Part | What to say |
|---|---|
| **1. Question** | Your case study and main question, in a sentence. What changed since Week 1 |
| **2. Data** | Where it came from, how many rows, what one row is, and what you left out (the data card in one slide) |
| **3. Method and check** | What you did, and the check that told you it worked (a known-answer test, a comparison with people, a manual check). Say what the rerun found |
| **4. Result and limits** | What you found, how sure you are, and what you would not claim. What would make it wrong |

**What we look for:** a clear question, data described honestly, at least one check you can show, claims that match the evidence, and a notebook someone else could rerun.

## After Week 8

Your repository is the record of what you did. Keep your verification log: it is the habit that carries over to any project.

<!-- facilitator:start -->
## Materials (Week 8)

| What | Where | Status |
|---|---|---|
| Slides (8, about 20 minutes) | `slides/week08_reproduce_and_present.html` and `.pdf`; `..._presenter.html` (press N for the script) and `..._handout.pdf`. Source: `slides/src/week08/`. Present them at the end of Week 7 Session 2 (Jan 14), or share them for self-study | Built |
| Practice page: Run It from Scratch | `practice/week08_run_it_from_scratch.html` (source `practice/src/week08/`; all notebooks, paths and keys invented). Four levels and a bridge | Built and tested. Optional |
| Rerun report template | `project/rerun_report.md` (on the site) | Built |
| Notebook / answer key | None this week | |

## Run sheet

**Before (Jan 12 to Jan 18)**
- Jan 12 or 14: announce the exercise and dates; show the slides (about 20 minutes) at the end of Week 7 Session 2, or send them.
- By Jan 15: collect the repository links in the chat and make the pairs (nobody reruns a notebook on data they may not see). Pairs are announced the same day.
- Open the sign-up sheet with five slots (first come first served; proposal: opens when the exercise is announced, closes when pairs are made on Jan 15). Anyone who takes a place gives their repository link by Jan 15.
- Jan 15 to 18: the Desk checks the chat for stuck pairs. A pair that cannot rerun a notebook after the owner's fix should say so, and the Lead looks.
- By Jan 18: collect the rerun reports (everyone shares at least the report they received, or says why not). Make the order of presentations (by sign-up time) and the feedback sheet.

**Presentation day (Kokil leads)**

| Time | What | Who |
|---|---|---|
| 0:00 to 0:05 | Welcome, the order, the rules (public or de-identified data only) | Lead |
| 0:05 to 0:50 | Presentations: 6 minutes each plus 2 for questions (up to 5 people). The Desk keeps time (a warning at 5 minutes, a stop at 6) | Desk |
| About 0:50 | Close | Lead |

**Watch for:** a key or private file in a repository (stop and fix it before the presentation); people with no data (present the plan and the checks); long talks; pairs that did not exchange reports (ask what happened, and do not shame).

## Open items (Week 8)

1. **Dates for the exercise** (above) are a proposal. Confirm them.
2. **Presenters.** Decided: opt-in, first come first served, at most 5. Open items: where the sign-up sheet lives and when it opens; whether to keep a waiting list; whether people who presented on Dec 22 can also take a place.
3. **What participants get at the end** (a certificate, a letter, a recognition list): **[Kokil to confirm]**.
4. **Follow-up.** Whether there is a community channel or a showcase after the course: **[Kokil to confirm]**.
<!-- facilitator:end -->
