"""Build notebooks/week03_verify_and_analyze.ipynb. Re-run after editing.

The data come from scripts/make_week03_data.py (simulated, with a known true effect).
"""
import os

import nbformat as nbf

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "notebooks", "week03_verify_and_analyze.ipynb")
cells = []


def md(t):
    cells.append(nbf.v4.new_markdown_cell(t.strip()))


def code(t):
    cells.append(nbf.v4.new_code_cell(t.strip()))


md("""
# Week 3: Verify and analyze

**CACTUS Fall 2026 · Coding session**

**The story (made up):** a platform shows an "AI-generated" label on some posts. The outcome is `sharing_intent`: how likely a person says they are to share a post, on roughly a 0 to 10 scale. In these simulated data the **true effect of seeing the label is -0.6 points**. Because we know the true answer, we can check whether code, including AI-written code, finds it.

**Goals today**
- run descriptive statistics and a simple regression, and say in a sentence what the numbers show
- test code against a known answer
- find mistakes in AI-written statistics code *without being told where they are*
- see why a confounder can make an estimate point the wrong way
- put your notebook on GitHub, with no key or private data in it

**Order**
1. The warm-up and Exercises 1 to 3 are required.
2. Exercise 4 (GitHub) and the stretch can be finished as homework.

**Rules**
- Predict before you run.
- Never accept AI code you have not read.
- Every cell you keep needs a note on how you checked it.
- Do not paste personal information or API keys into an AI chat.

**Run cells one at a time**, not "Run all". Some cells are wrong on purpose.
""")

md("""
## How this session runs

- There is **no lecture** in the coding session. You will be in a breakout room with a partner, and the facilitators visit the rooms.
- **Stuck?** Try these, in order, for no more than 5 minutes:
  1. Read the last line of any error message. What is it telling you?
  2. Re-read the instructions for the step. Did you skip a part?
  3. Ask your partner, then ask an AI assistant to explain the message (do not paste private data).
  4. Still stuck? Click **Ask for help** in Zoom or message the facilitators in the main chat. Say what you expected, what happened, and what you already tried.
- Use the AI freely for explanations and code. You are still responsible for checking what it says.
""")

code("""
import os

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

TRUE_EFFECT = -0.6   # the true effect of the label in these simulated data

BASE = "https://raw.githubusercontent.com/kokiljaidka/CACTUS_fall2026/main/data/"


def load(name):
    # use a local copy if you have one, otherwise read the file from the course repository
    return pd.read_csv(name) if os.path.exists(name) else pd.read_csv(BASE + name)


experiment = load("week03_experiment.csv")
survey = load("week03_survey.csv")
print("experiment:", experiment.shape, "  survey:", survey.shape)
""")

md("""
---
## Warm-up: simulate a study, then check your code against the truth (about 15 min)

Here you create the data yourself, so you know the true answer. **You can change the true effect and the sample size.**

**Predict:** with 50 people per group, will the estimate land close to the true effect? Will it be exactly the true effect? Write your guess.

> My prediction:
""")

code("""
rng = np.random.default_rng()   # a different result every time you run it


def simulate(n, true_effect, noise=2.0):
    # half the people are shown the label (treated = 1), half are not (treated = 0)
    treated = rng.integers(0, 2, n)
    y = 5 + true_effect * treated + rng.normal(0, noise, n)
    return pd.DataFrame({"treated": treated, "y": y})


def estimate(df):
    fit = smf.ols("y ~ treated", data=df).fit()
    lo, hi = fit.conf_int().loc["treated"]
    return fit.params["treated"], lo, hi


MY_TRUE_EFFECT = -0.6      # change me
MY_N = 100                 # change me

d = simulate(MY_N, MY_TRUE_EFFECT)
est, lo, hi = estimate(d)
print(f"true effect {MY_TRUE_EFFECT}   estimate {est:.2f}   interval {lo:.2f} to {hi:.2f}")
print("Does the interval contain the truth?", lo <= MY_TRUE_EFFECT <= hi)
""")

md("""
Run the cell above a few times. What changes each time? Now run the same study **100 times** and count how often the interval contains the truth.

**Predict:** out of 100 studies, about how many intervals will contain the true effect?

> My prediction:
""")

code("""
covered = 0
estimates = []
for _ in range(100):
    est, lo, hi = estimate(simulate(MY_N, MY_TRUE_EFFECT))
    estimates.append(est)
    covered += lo <= MY_TRUE_EFFECT <= hi

print("Intervals that contained the truth:", covered, "out of 100")
print("Estimates ranged from", round(min(estimates), 2), "to", round(max(estimates), 2))
assert 85 <= covered <= 100, "A 95% interval should contain the truth about 95 times in 100. Something is wrong."
""")

md("""
**Discuss with your partner:** why do the estimates vary when the truth is fixed? What happens to the range if you change `MY_N` to 20? To 1000?

> Log (warm-up): one thing you predicted, what happened, and the check you used.
""")

md("""
---
## Exercise 1: Descriptives and a regression (required, about 30 min)

Data: `experiment`, 300 people. `group` says who saw the label (`label`) and who did not (`control`), assigned by chance. `sharing_intent` is the outcome.

**Predict first:** will the label group's average sharing intent be higher or lower than the control group's? By about how much?

> My prediction:

**How to prompt well.** Give the AI the context it cannot see:

> I have a pandas DataFrame called `experiment` with columns: *(paste `list(experiment.columns)`)*. Here are the first 3 rows: *(paste `experiment.head(3)`)*. **Task:** ... Write the code, then explain each line in one sentence.

| Task | What to ask for | How to check it |
|---|---|---|
| **1a** | The mean, median, standard deviation and number of people in each group | Add up the counts: do they equal 300? Is the mean near the median? |
| **1b** | A regression of `sharing_intent` on `group`. Store the coefficient for the label group in `est` and its interval in `lo` and `hi` | The check cell below |
| **1c** | One sentence: "On average, people who saw the label ..., with an interval of ... to ..." | Does your sentence say more than the numbers do? |
""")

code("""
# Task 1a: paste the AI's code here, then run it.
""")
code("""
# Task 1b: paste the AI's code here. It must create est, lo and hi.
""")

code("""
# Check 1b. This compares your regression with a second method: the difference in group means.
by_hand = (experiment.loc[experiment.group == "label", "sharing_intent"].mean()
           - experiment.loc[experiment.group == "control", "sharing_intent"].mean())
assert abs(est - by_hand) < 0.001, f"Your estimate {est:.3f} is not the difference in group means {by_hand:.3f}"
print("Matches the difference in group means:", round(by_hand, 3))
print("Estimate:", round(est, 2), " interval:", round(lo, 2), "to", round(hi, 2))
print("Does your interval contain the true effect (-0.6)?", lo <= TRUE_EFFECT <= hi)
""")

md("""
**Think:** the estimate is not exactly -0.6. Is that a mistake in your code? What does the warm-up tell you?

> Task 1c, my sentence:
>
> Log (Exercise 1): what did the AI get wrong, or what check did you run? Did you reject any code, and why?
""")

md("""
---
## Exercise 2: Bug hunt (required, about 25 min)

Below is an analysis an AI assistant wrote for someone else. It runs without errors and prints a result. **It contains three mistakes that change the answer.** Find them without being told where they are.

**What to do**
1. Run the cell and read the result. Does anything look strange? You know the true effect.
2. Read each numbered step. What does each line do to the data or the number?
3. For each suspected bug, **prove it** with a check. Write down the check.
4. Fix the code and compare the corrected result with the original.

**Checks that work for statistics code**
- Compare with the **known answer**.
- Count the **rows before and after** each step.
- Run the method on **many simulated datasets** (as in the warm-up) and see whether it behaves as it claims.

**Hints.** If you are stuck for more than 5 minutes, ask a facilitator. The places to look are: the sign of the answer, how many rows are used, and what the interval claims to be.
""")

code("""
# ---- AI-written analysis. Do not edit this cell; copy it to a new one to fix. ----
d = experiment.copy()

# 1. Code the group as a number
d["treated"] = d["group"].map({"control": 1, "label": 0})

# 2. Remove outliers
d = d[d["sharing_intent"] > 2]
print("Rows used:", len(d))

# 3. Estimate the effect of the label
model = smf.ols("sharing_intent ~ treated", data=d).fit()
est2 = model.params["treated"]
se2 = model.bse["treated"]
print(f"Estimated effect of the label: {est2:.2f}")
print(f"Interval: {est2 - se2:.2f} to {est2 + se2:.2f}")
""")

md("""
**Write down each bug you find** (what was wrong, how you proved it, what changed after the fix):

| # | What was wrong | My check | Result after fix |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
""")

code("""
# Your fixed version here.
""")

md("""
> Log (Exercise 2): which bug was hardest to find? Which check would you use first next time?
""")

md("""
---
## Exercise 3: A confounder (required, about 25 min)

Data: `survey`, 800 people. This is **not** an experiment. People were not assigned to see the label: `seen_label` is 1 if they happened to see it. People who use AI more (`prior_ai_use`, from 1 to 5) are more likely to see the label **and** tend to share more.

**Predict:** if you compare people who saw the label with people who did not, will the difference be positive, negative, or near zero? The true effect of the label is -0.6.

> My prediction:

| Task | What to ask for | How to check it |
|---|---|---|
| **3a** | The **naive** estimate: sharing intent on `seen_label` only. Store the coefficient in `naive` | Compare with the true effect |
| **3b** | The **adjusted** estimate: add `prior_ai_use` to the model. Store the label coefficient in `adj` | Compare with the true effect |
| **3c** | A short paragraph: why do the two differ? Which would you trust, and why? | Read it aloud to your partner |
""")

code("""
# Task 3a:
""")
code("""
# Task 3b:
""")
code("""
# Check 3. Run after 3a and 3b.
print("naive:", round(naive, 2), "  adjusted:", round(adj, 2), "  true:", TRUE_EFFECT)
assert abs(adj - TRUE_EFFECT) < abs(naive - TRUE_EFFECT), "The adjusted estimate should be closer to the truth than the naive one."
""")

md("""
> Task 3c, my paragraph:
>
> Log (Exercise 3): what surprised you about the naive estimate?
""")

md("""
---
## Exercise 4: Put your work on GitHub (about 20 min; can be homework)

You need a free account at https://github.com. **Never put a key, a password, or private data in a repository.**

1. On github.com, click **New repository**. Name it `cactus-notebooks`. Choose **Private** if you prefer; you can change it later. Click **Create repository**.
2. In this notebook in Colab: **File, then Save a copy in GitHub**. The first time, Colab asks you to authorize GitHub. Choose your `cactus-notebooks` repository, keep the file name, write a short message such as "Week 3 notebook", and click **OK**.
3. Open the repository on github.com and check that your notebook is there.
4. Check what you have saved:
   - [ ] Does the notebook contain any API key, password, or private data? (Search the page for "key", "token", "secret".)
   - [ ] Are your answers and logs filled in?
   - [ ] Does it run top to bottom without an error?

If the menu looks different from this description, ask a facilitator. The menu names can change.

> My repository link:
""")

md("""
---
## Stretch: the same descriptives on real data (about 15 min)

Load the Starbucks comments from Week 2 and compute the average `tone_pos` for each country, **with the number of comments in each**. Then write what you would **not** claim from this table. Think about group sizes, how the comments were collected, and what `tone_pos` measures.

> What I would not claim:
""")

code("""
# Stretch: your code here.
""")

md("""
---
## Log: what I learned today

- One check that told me my code was right or wrong:
- One thing the AI got wrong, or one claim I would not accept:
- One question I still have:

**Homework (45 min or less):** finish Exercise 4 (GitHub) and anything you did not finish, and add to your project card: which statistics would answer each sub-question, and how you would test that code against a known answer. Also check your data access for Week 4.
""")

nb = nbf.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
nbf.write(nb, OUT)
print("wrote", os.path.normpath(OUT))
