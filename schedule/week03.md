# Week 3: Verify and analyze

**Theme:** AI as pair programmer for statistics. Week 2 checked cleaning code. This week checks *statistics* code, where wrong code still produces a plausible number. Students test AI-written code against an answer they know.
**Format:** Zoom. A 1-hour learning session (lecture with live demos), a 20-minute practice page, then a 2-hour coding session in breakout rooms with no lecture. About 3 hours live.

<!-- facilitator:start -->
> **Status: draft for review.** Not on the student site until the data, notebook and practice page exist. Decisions needed are at the end of this file.
<!-- facilitator:end -->

## Objectives

By the end of the week, students can:
1. Run descriptive statistics (mean, median, spread, group comparison) in code and say what each number does and does not show.
2. Fit a simple regression and read the coefficient and its uncertainty in plain words.
3. Check AI-written statistics code against a **known answer** (simulated data with a planted effect).
4. Explain why a small sample gives a noisy estimate, and why an ignored confounder gives a biased one.
5. Spot common AI mistakes in statistics code: the wrong test for the data, a group stored as a number, rows silently dropped, over-claiming from a result.
6. Put a notebook and their verification log on GitHub, without any key in it.

## Data

| Session | Dataset | Why |
|---|---|---|
| Learning (walk-through) | Simulated in the notebook, live | The true effect is chosen by the presenter, so everyone can see whether the estimate recovers it |
| Practice page | Simulated in the browser | Sliders for effect size, noise and sample size |
| Coding (exercises) | `data/week03_experiment.csv` and `data/week03_survey.csv` (simulated; the true effects are stated in the notebook) | An experiment (randomized) and a survey (observational, with a confounder) about a made-up "AI label" on shared posts |

Both files are made by `scripts/make_week03_data.py` with a fixed seed, so the numbers can be rebuilt.

## Required reading

From *Computational Analysis of Communication* ([cssbook.net](https://cssbook.net)), the Python version. Required, not graded.

- **Before the learning session:** [Chapter 7](https://cssbook.net/content/chapter07.html), section 7.1 (simple exploratory data analysis).
- **Before the coding session:** [Chapter 8](https://cssbook.net/content/chapter08.html), sections 8.1 to 8.2 (statistical modeling and prediction; concepts and principles), and [Chapter 4](https://cssbook.net/content/chapter04.html), section 4.3 (GitHub and notebooks).

## Before the session

- Create a GitHub account (free) at https://github.com. Do this before the coding session so it is not done in the session.

<!-- facilitator:start -->
## Materials

| What | Where |
|---|---|
| Lecture slides (about 11 slides) | `slides/week03_*.html`, `.pdf`, presenter view and handout (to build) |
| Practice page: Planted-effect lab | `practice/week03_planted_effect_lab.html` (to build; spec in `practice/page_specs.md`) |
| Notebook | `notebooks/week03_verify_and_analyze.ipynb` (to build) |
| Data | `data/week03_experiment.csv`, `data/week03_survey.csv`, from `scripts/make_week03_data.py` (to build) |

## Prep

- Do the notebook yourself before the session, including the GitHub step, with a brand-new GitHub account.
- Check what Colab's **File, then Save a copy in GitHub** does with a new account, and what permissions it asks for. Write the exact click path for students.
- Facilitators: read `facilitators/practice_pages_guide.md` and the private answer key for the planted bugs.
- Decide which statistics package the notebook uses (`statsmodels` is installed in Colab by default).
<!-- facilitator:end -->

---

## Learning session (about 1 h): lecture with live demos

| Time | Activity |
|---|---|
| 0:00 | **Recap and the idea.** Week 2 checked cleaning. Week 3 checks statistics. A number can be computed correctly and still be wrong for the question. |
| 0:05 | **What an estimate claims.** Simulate a study live with a known effect. Show the group means and a regression coefficient next to the truth. Ask the room to predict first. |
| 0:20 | **Noise and sample size.** Rerun with a small sample, many times. Show how much estimates move. A confidence interval is a statement about this variation, not a probability the effect is real. |
| 0:32 | **A confounder.** Show a survey where the naive estimate is far from the truth, and the adjusted one is close. Say why randomization avoids this. |
| 0:42 | **Check the AI's statistics.** Ask an AI to analyze the data. Compare its answer with the known truth, and read what it says it proves. |
| 0:52 | **Preview:** the practice page, the reading, the GitHub account, and the coding session. |

<!-- facilitator:start -->
### Lecture plan (slides)

| # | Slide | Min | Notes |
|---|---|---|---|
| 1 | Title | 1 | The plan for the week |
| 2 | Recap and the idea | 4 | Cleaning versus statistics |
| 3 | What an estimate claims | 5 | Mean difference and regression coefficient, in words |
| 4 | Demo: one simulated study | 8 | Known effect. Predict, run, compare |
| 5 | Noise and sample size | 6 | Run 20 studies, then 100; show the spread |
| 6 | What an interval says (and does not) | 6 | No "95% probable"; no p-value thresholds as decisions |
| 7 | A confounder | 8 | Survey, naive versus adjusted, and why experiments differ |
| 8 | Demo: check an AI's answer | 8 | Compare with the known effect |
| 9 | Over-claiming | 4 | "Proves", "causes", from the wrong design |
| 10 | Before the coding session | 4 | Practice page, reading, GitHub |
| 11 | Preview of GitHub | 3 | Why a notebook lives in a repo |
<!-- facilitator:end -->

---

## Between sessions (about 20 min): practice page

Students open **Planted-effect lab** after the learning session and before the coding session. They set a true effect, a noise level and a sample size, see the estimate beside the truth, run 100 studies, switch a confounder on and off, and judge three "AI answers". It ends with a Colab task: simulate with their own true effect, fit a regression, and repeat 100 times.

---

## Coding session (about 2 h): breakout rooms, no lecture

Notebook: `notebooks/week03_verify_and_analyze.ipynb`. Pairs in breakout rooms. Exercises 1 to 3 are required; 4 is stretch (and may be homework).

| Time | Exercise |
|---|---|
| 0:00–0:15 | **Warm-up:** simulate data with a true effect you choose, fit a regression, check the estimate against the truth, then repeat it 100 times. |
| 0:15–0:45 | **Ex 1:** descriptives and a regression on the experiment data. Does your estimate recover the true effect? Report the estimate and its uncertainty in a sentence. |
| 0:45–1:10 | **Ex 2:** bug hunt. AI-written statistics code with planted mistakes. Find them using the known answer. |
| 1:10–1:35 | **Ex 3:** the survey data. Compare the naive and adjusted estimates. Explain the difference in one paragraph. |
| 1:35–1:55 | **Ex 4:** put your notebook and log on GitHub. Check that no key or personal data is in it. |
| 1:55–2:00 | Log; optional share-out. |

**Stretch:** apply the same descriptives to `tone_pos` by country in the Starbucks data and write what you would *not* claim.

Post a time check in the main chat at each boundary. Hints for Exercise 2 come from facilitators only, using the ladder in the answer key.

## Homework (45 minutes or less)

- Finish Exercise 4 (GitHub) and Ex 3 if not done.
- Add to your project card: which statistics would answer each sub-question, and how you would test that code against a known answer.

## Hand-off to Week 4

Students leave with a notebook on GitHub, a verification log, and a sense of which statistics fit their project. Week 4 moves from analyzing data you are given to collecting your own.

<!-- facilitator:start -->
## Decisions and open items (Week 3)

1. **GitHub route.** Confirm that Colab's "Save a copy in GitHub" works smoothly for new accounts. If not, fall back to uploading the notebook through the GitHub website.
2. **Simulation story.** Draft: a made-up "AI label" on shared posts; outcome is sharing intent; a survey where heavy AI users are more likely to see the label. Change if you prefer another story.
3. **Statistics level.** One or two predictors, linear regression. No logistic regression this week unless you want it.
4. **Bugs for Exercise 2.** Candidates: a group coded 0 and 1 treated as a continuous number; a one-tailed test chosen to get a result; rows silently dropped before fitting; reporting "significant" for a tiny effect; claiming causation from the survey. Choose three and keep them in the private key.
<!-- facilitator:end -->
