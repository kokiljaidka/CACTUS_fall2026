# Week 8: Reproduce and present

**Theme:** A result you cannot rerun is a claim, not a finding. This week you rerun your whole pipeline from a clean start (and have someone else rerun it), document what you did, and present your project with its limits.
**Format:** Zoom, Tuesday, Jan 19. A short learning session (about 20 minutes), then a swap-and-rerun session in pairs (about 1 hour), then presentations (about 1.5 hours). About 3 hours live.

<!-- facilitator:start -->
> **Status: built.** The 20-minute slides and the practice page are built and tested; the rerun report template is on the site. There is no notebook or answer key this week. The plan: a short learning session, a swap-and-rerun hour, and about 9 presentations of 6 to 8 minutes each. See the materials and open items at the end.
<!-- facilitator:end -->

## Objectives

By the end of the week, students can:
1. Rerun a notebook from a fresh runtime, top to bottom, and fix what breaks.
2. Check that no key, password or private data is in a shared notebook or repository.
3. Document a project so that someone else can rerun it: a data card, a log, and a short README.
4. Say what a result does and does not support, with the sample, the checks and the limits.
5. Present a project in six to eight minutes, and answer questions about it.

## Required reading

From *Computational Analysis of Communication* ([cssbook.net](https://cssbook.net)), the Python version. Required, not graded.

- **Before the session:** [Chapter 15](https://cssbook.net/content/chapter15.html), section 15.3 (publishing your source), and [Chapter 16](https://cssbook.net/content/chapter16.html), section 16.3 (open, transparent, and ethical computational science).

## Before the session: get your project ready

1. Put your notebook, your data card, your verification log and a short README on GitHub (a repository you made in Week 3).
2. **Run it from a fresh runtime:** in Colab, **Runtime, then Restart session and run all**. Fix what breaks. Common causes: a variable defined in a cell you later deleted, cells run out of order, a file path that only works on your computer, a package that was never installed in the notebook.
3. **Check for secrets and private data:** no API key, password or raw private data in the notebook, the outputs, or the repository. Keys belong in Colab Secrets.
4. Write down, in the README, how to rerun: what to upload, in what order, and how long it takes.
5. Share the link in the chat **before your slot**.

## What happens on the day

| Time | What |
|---|---|
| 0:00 | **Learning session (about 20 minutes).** The reproducibility checklist, and how to say what you can claim and what you cannot |
| 0:20 | **Swap and rerun (about 1 hour, pairs).** A partner reruns your notebook from a fresh runtime while you rerun theirs, using the [rerun report](../project/rerun_report.md). Write down what broke and what they could not follow. Fix it |
| 1:20 | Break |
| 1:30 | **Presentations.** Six minutes each, plus two minutes of questions |
| about 3:00 | Close: what to take with you, and what comes next |

## The presentation (6 minutes)

Four parts, three or four slides, public or de-identified data only.

| Part | What to say |
|---|---|
| **1. Question** | Your case study and main question, in a sentence. What changed since Week 1 |
| **2. Data** | Where it came from, how many rows, what one row is, and what you left out (the data card in one slide) |
| **3. Method and check** | What you did, and the check that told you it worked (a known-answer test, a comparison with people, a manual check) |
| **4. Result and limits** | What you found, how sure you are, and what you would not claim. What would make it wrong |

**What we look for:** a clear question, data described honestly, at least one check you can show, claims that match the evidence, and a notebook someone else could rerun.

## After Week 8

Your repository is the record of what you did. Keep your verification log: it is the habit that carries over to any project.

<!-- facilitator:start -->
## Build plan (Week 8)

## Materials (Week 8)

| What | Where | Status |
|---|---|---|
| Lecture slides (8, about 20 minutes) | `slides/week08_reproduce_and_present.html` and `.pdf`; `..._presenter.html` (press N for the script) and `..._handout.pdf`. Source: `slides/src/week08/` | Built |
| Practice page: Run It from Scratch | `practice/week08_run_it_from_scratch.html` (source `practice/src/week08/`; all notebooks, paths and keys invented). Four levels and a bridge: put cells in order, the cell you deleted, paths that only work for you, keys and private data | Built and tested. Optional: students do it before the session |
| Rerun report template | `project/rerun_report.md` (on the site) | Built |
| Notebook / answer key | None this week | |

### Short learning session (about 20 minutes)
Eight slides with notes: why a result nobody can rerun is a claim; restart and run all; the checklist (runs, safe, documented); what you can claim; the six-minute talk; what happens next. Invented examples only.

### Swap and rerun
No new notebook. Pairs are made by the Lead the day before, so that nobody reruns a notebook on data they may not see: **the partner runs it on the shared or de-identified sample only**, never on private raw data. The [rerun report template](../project/rerun_report.md) (what I did, what broke, what I could not follow) is on the site.

### Presentations
About 9 presenters at 6 plus 2 minutes is about 72 minutes in one room. Order by volunteers. Facilitators fill in the feedback sheet (question, data, check, claims, rerun). Kokil leads.

## Run sheet

| Time | What | Who |
|---|---|---|
| Before | Make pairs; share the rerun-report template; collect repository links; make the order and the feedback sheet | Lead (Kokil) |
| 0:00 to 0:20 | Short learning session | Lead |
| 0:20 to 1:20 | Swap and rerun. Rooms visit pairs. Stuck pairs: check the runtime first, then the install cell, then paths | Everyone |
| 1:20 to 1:30 | Break | |
| 1:30 to 3:00 | Presentations. The Desk keeps time (a warning at 5 minutes, a stop at 6) | Desk |
| About 3:00 | Close | Lead |

**Watch for:** notebooks that only run because of leftover variables (a fresh runtime shows this); a key or private file in a repository (stop and fix it before the presentation); people with no data (present the plan and the checks you would run); long talks (hold the time).

## Open items (Week 8)

1. **Presenters.** About 8 to 9. If more, use two rooms.
2. **What participants get at the end** (a certificate, a letter, a recognition list): **[Kokil to confirm]**.
3. **Follow-up.** Whether there is a community channel or a showcase after the course: **[Kokil to confirm]**.
4. **Rerunning each other's notebooks** needs a repository link from everyone before the day. Collect them in the chat the day before.
<!-- facilitator:end -->
