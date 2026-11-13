# Week 7: Applying statistics to social media data

**Theme:** Social media rows are not independent: replies sit inside threads, posts inside accounts, images inside templates, people inside groups. An analysis that ignores this looks more certain than it is. **Session 1** teaches the shared core for everyone, using data where the answer is planted. **Session 2** splits into three tracks (networks, images and memes, a mock feed or experiment), and each student applies the core to the kind of data in their project.
**Format:** Two sessions, like Week 1. **Session 1 (Tue Jan 12):** a 1-hour learning session, a 20-minute practice page, then a 2-hour coding session. **Session 2 (Thu Jan 14, to be confirmed):** a 2-hour coding session in breakout rooms by track, one facilitator per room. About 5 hours live.

<!-- facilitator:start -->
> **Status: plan for review. Nothing is built.** The Session 2 date is a placeholder. See the build plan and decisions at the end.
<!-- facilitator:end -->

## Objectives

By the end of the week, students can:
1. Explain what a known-answer test is, and plant an answer in simulated data.
2. Say why rows from the same post, account, template or group are not independent, and what that does to standard errors.
3. Fit a model with standard errors that account for the grouping, and compare it with the naive one.
4. Model counts with an exposure (comments per post, shares per follower) instead of raw counts.
5. Use a permutation or bootstrap check on a result that has no simple formula.
6. Run one track's method on planted data, check it against the known answer, and plan how to run it on their own data.

## Session 1: the shared core (everyone)

### Required reading

From *Computational Analysis of Communication* ([cssbook.net](https://cssbook.net)), the Python version. Required, not graded.

- **Before Session 1:** [Chapter 8](https://cssbook.net/content/chapter08.html), sections 8.1 and 8.2 (which you saw in Week 3) and section 8.5 (validation and best practices). Read them again with this question: what if my rows come in groups?

<!-- facilitator:start -->
Check before this goes live whether the book covers grouped (multilevel) models, and add a supplementary reading if it does not.
<!-- facilitator:end -->

### Learning session (about 1 h)

| Time | Activity |
|---|---|
| 0:00 | **Recap and the idea.** Week 3 planted an effect and found it. Week 6 measured an AI against people. Today: plant an answer for any method, and check before you trust. |
| 0:05 | **Known-answer tests.** Simulate, run, compare. What it proves and what it does not. |
| 0:15 | **Rows that come in groups.** Thirty comments under one viral post are not thirty independent opinions. Simulate it, and watch the naive standard errors shrink. |
| 0:30 | **The fixes.** Cluster-robust standard errors first (one option), then a mixed model as one line. Counts with an exposure. |
| 0:42 | **A check that always works.** Permutation: shuffle the labels, see what chance looks like. |
| 0:50 | **Preview the three tracks** (about 2 minutes each) and the coding session. |

<!-- facilitator:start -->
### Lecture plan (slides, about 11)

| # | Slide | Min | Notes |
|---|---|---|---|
| 1 | Title | 1 | The plan for the two sessions |
| 2 | Recap and the idea | 4 | Plant an answer, then check |
| 3 | What a known-answer test is | 5 | Simulate, run, compare |
| 4 | What it cannot tell you | 5 | Real data breaks the assumptions |
| 5 | Rows that come in groups | 8 | Predict first: how many "independent" comments are in 3,000? |
| 6 | Standard errors that notice groups | 7 | Cluster-robust; the mixed model as one line |
| 7 | Counts and exposure | 5 | Comments per post, not comments |
| 8 | Permutation: what chance looks like | 5 | Works when there is no formula |
| 9 | The three tracks | 6 | Networks, images, experiments: how the core shows up in each |
| 10 | Before the coding session | 4 | Practice page, reading, setup |
| 11 | Questions | 4 | |
<!-- facilitator:end -->

### Between sessions (about 20 min): practice page

One practice page for everyone: **Plant It, Find It.** Three levels, then a bridge.

- **Plant an answer.** Choose how strong a planted effect is and how many posts, and see whether a simple method finds it. Make it too weak or the sample too small and watch it fail.
- **When groups are ignored.** The same data analysed two ways, with and without accounting for posts. See how the uncertainty changes.
- **What breaks it.** Bots, duplicates, and repeated people. Choose which one breaks which method.
- **Colab task:** plant a known answer in a few lines of code.

### Coding session (about 2 h): everyone, one notebook

Notebook: the shared Week 7 notebook (nested comments in posts, all invented). Pairs in breakout rooms. All exercises are required.

| Time | Exercise |
|---|---|
| 0:00–0:15 | **Warm-up:** plant an effect in simulated data and recover it. Predict what the method should find. |
| 0:15–0:45 | **Ex 1:** about 3,000 comments in 80 posts. Fit the naive model and the cluster-robust model. How much do the standard errors change? |
| 0:45–1:10 | **Ex 2:** counts with an exposure. Model comments per post with and without the exposure. Which matches the planted answer? |
| 1:10–1:35 | **Ex 3:** bug hunt. AI-written code with planted mistakes. Find them using the known answer. |
| 1:35–1:50 | **Ex 4:** permutation check on a result of your own choosing from the data. |
| 1:50–2:00 | **Choose your track** (confirm in the chat), fill in the log. |

Hints for Exercise 3 come from facilitators only.

## Between sessions

- Read your track's chapter section (about 20 minutes).
- Bring a small sample of your own data if you have one (de-identified; see Week 4).

## Session 2: the tracks (2 h, breakout rooms)

Students choose by the end of Session 1. Pairs form within a track. One facilitator per room, and the same skeleton in each notebook, so a facilitator who knows one can help with another.

| Track | Good if your project is about | Method | Known answer planted in the data | Tools |
|---|---|---|---|---|
| **A. Networks** | Who talks to whom: replies, mentions, quotes | Build a graph from edges, find who is central and which groups form, check against shuffled networks | Two communities, a hub, and a few automated accounts | `networkx` |
| **B. Images and memes** | Repeated templates, reposts, visual spread | Fingerprint images (perceptual hash), group near-duplicates, count templates, treat images as nested within templates | Generated "meme" images from a handful of templates, with crops, captions and noise | `Pillow`, `imagehash` |
| **C. Mock feed or experiment** | A randomized comparison: a source cue, a chatbot condition, a manipulated feed | Compare conditions, check the manipulation, estimate effects and an interaction, with errors clustered by group | A planted effect and interaction, with a failed manipulation check in one subgroup | `statsmodels` |

All exercise data is **invented**, generated by a script, so it is public and has a known answer.

### Required reading (track)

- **Track A:** [Chapter 13](https://cssbook.net/content/chapter13.html), sections 13.1 and 13.2.
- **Track B:** [Chapter 14](https://cssbook.net/content/chapter14.html), sections 14.1 and 14.2.
- **Track C:** [Chapter 16](https://cssbook.net/content/chapter16.html), section 16.3.

| Time | Exercise |
|---|---|
| 0:00–0:10 | Recap of Session 1 and room assignments |
| 0:10–0:25 | **Warm-up:** plant a known answer for your track. Predict what the method should find. |
| 0:25–0:55 | **Ex 1:** run your track's method on the planted data. |
| 0:55–1:15 | **Ex 2:** check it against the known answer. Break the data on purpose (a smaller sample, a bot, a duplicate) and watch the result move. |
| 1:15–1:40 | **Ex 3:** bug hunt for your track, with planted mistakes. |
| 1:40–1:55 | **Ex 4:** your own data. List what you would check first, and run the first step on a sample. |
| 1:55–2:00 | Log; optional share-out |

## Homework (45 minutes or less)

- Run your track's method on your own data (or a sample), after one known-answer check.
- Write one paragraph: what the method assumes, and one way your data may break it (include whether your rows come in groups).
- Start thinking about Week 8: what you will present, and what must rerun from scratch.

## Hand-off to Week 8

Students leave with a method that passed a known-answer check, standard errors they can defend, and a plan for their own data. Week 8 is about rerunning the whole pipeline from scratch, documenting it, and presenting results with their limits.

<!-- facilitator:start -->
## Build plan (Week 7)

### Build order
1. **Shared core first:** data generator, notebook, practice page, slides, private key.
2. **Then the three track notebooks** (C first, since it extends Week 3; then A; then B, which has the install).

### Data generators (all invented, public, with a known answer)
| Part | Script | What it makes |
|---|---|---|
| Core | `scripts/make_week07_nested.py` | About 3,000 comments in 80 posts: a binary outcome with a post-level effect and a comment-level predictor, and a count outcome with an exposure. Known coefficients and known between-post variation |
| A | `scripts/make_week07_network.py` | An edge list of replies and mentions for about 300 accounts: two planted communities, one hub, a few bots. Known community labels |
| B | `scripts/make_week07_memes.py` | About 200 generated "meme" images from 6 templates, with crops, brightness changes and caption variants, plus 40 unrelated images. Known template ids |
| C | `scripts/make_week07_experiment.py` | A 2 by 2 online experiment (about 400 people, in groups) with a manipulation check, an outcome, a planted main effect and a planted interaction, and one subgroup where the manipulation failed |

### Notebooks
`notebooks/week07_core_nested_data.ipynb`, then `week07_track_a_networks.ipynb`, `..._b_images.ipynb`, `..._c_experiment.ipynb`. Checks use `assert` with helpful messages, tested with a correct solution as in Weeks 4 to 6. Bug hunts have three planted mistakes each (private key).

Candidate mistakes (to choose three per notebook):
- **Core:** ordinary standard errors on clustered data; a post-level predictor treated as comment-level; the exposure dropped from a counts model.
- **A:** treating a reply as undirected when direction matters; counting bots as people; reading degree as influence without looking at who the neighbours are.
- **B:** hashing images at different sizes without resizing first; a threshold that merges different templates; calling a repost a new template.
- **C:** reporting a main effect when the interaction flips it; skipping the manipulation check; dropping failed-manipulation participants after seeing the result.

### Practice page: Plant It, Find It (`practice/week07_plant_it_find_it.html`)
Three levels and a bridge, as above. All invented.

### Slides (11, `slides/src/week07/`)
As in the lecture plan, with notes in the same format. Invented examples only.

### Also to update when built
README row 7; the facilitator hub (rota table gets a Session 2 line; the "Where everything is" table); `week_by_week.md` (Week 7 run sheet with both sessions); `practice_pages_guide.md`; the RA checklist (a Week 7 section); `build_site.py` PAGES and `mkdocs.yml` nav.

### Suggested track matches (confirm with each person)
Networks: the addressee and mention networks in the Twitter data, a digital-activism project. Images and memes: the protest-meme study, an image and text dataset. Mock feed or experiment: a chatbot experiment, a source-cue survey experiment. Students whose rows are comments within posts (the Instagram comments study) use the shared core directly and can pick the track nearest their design.

## Decisions and open items (Week 7)

1. **Session 2 date.** Thursday Jan 14 is a placeholder. Confirm, and add it to the rota (a Lead and a room host per track).
2. **Rooms.** Three tracks, four facilitators: one hosts each room and the fourth is the Desk. Facilitator D (student-facilitator) joins a room as a participant if they prefer.
3. **Missed Session 1.** A student who misses it can use the shared notebook as a catch-up before Session 2.
4. **Statistics level.** Keep it to intuition: simulate first, no formulas on the slides. Cluster-robust errors first; the mixed model as one line.
5. **Reading.** Check the book's coverage of grouped data (see above).
6. **Image libraries.** `imagehash` is not preinstalled in Colab (a short `pip install`). Confirm the install time.
7. **Real data.** None in the exercises; all invented. Students bring their own for Exercise 4 of Session 2 and the homework.
<!-- facilitator:end -->
