"""Build notebooks/week07_track_c_experiment.ipynb (Week 7, Session 2, Track C: mock feed or experiment).

Data from scripts/make_week07_experiment.py (invented, with planted answers). Re-run after editing.
"""
import os

import nbformat as nbf

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "notebooks", "week07_track_c_experiment.ipynb")
cells = []


def md(t):
    cells.append(nbf.v4.new_markdown_cell(t.strip()))


def code(t):
    cells.append(nbf.v4.new_code_cell(t.strip()))


md("""
# Week 7, Session 2, Track C: a mock feed or experiment

**CACTUS Fall 2026 · Coding session (Track C)**

**The story (made up):** 600 people in 12 sessions each saw one mock social media post. It came from a **news outlet** or an **anonymous account** (`source`), and it carried an **"AI-generated" label** or not (`label`). Both were assigned by chance to each person. The outcome is `credibility`: how credible they rated the post, 1 to 7. Afterwards they were asked whether they noticed an AI label (`noticed_label`): the **manipulation check**.

**What we planted (the known answer):** the label lowers credibility **only for people who noticed it**, by **0.2 points for the news outlet** and **1.0 point for the anonymous account**. Anonymous accounts are also rated about 0.8 lower on their own. Because we know this, we can check what each analysis finds.

**Goals today**
- check whether the manipulation worked, before looking at the outcome
- estimate a label effect for each source, and an interaction, and check them against the known answer
- see what happens when you drop people who failed the manipulation check
- find mistakes in AI-written code using the known answer
- plan the same checks for your own data

**Order**
1. The warm-up and Exercises 1 to 3 are required. Exercise 4 (your own data) can be finished as homework.

**Rules**
- Predict before you run.
- Never accept AI code you have not read.
- Every cell you keep needs a note on how you checked it.
- Do not paste personal information or API keys into an AI chat.

**Run cells one at a time**, not "Run all". Some cells are wrong on purpose.
""")

md("""
## How this session runs

- There is **no lecture**. You are in a breakout room with a partner, and a facilitator visits.
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

TRUE_OUTLET = -0.2   # the label's effect for people who noticed it, news outlet (planted)
TRUE_ANON = -1.0     # the same for the anonymous account (planted)

BASE = "https://raw.githubusercontent.com/kokiljaidka/CACTUS_fall2026/main/data/"


def load(name):
    # use a local copy if you have one, otherwise read the file from the course repository
    return pd.read_csv(name) if os.path.exists(name) else pd.read_csv(BASE + name)


experiment = load("week07_experiment.csv")
print(experiment.shape)
experiment.head()
""")

md("""
---
## Warm-up: plant an interaction and see how often you find it (about 15 min)

Here you build the data yourself. You plant an effect of a label that differs between a news outlet and an anonymous account (an **interaction**), then run the study 200 times and count how often the interaction is found (its 95% interval excludes zero).

**Predict:** with 100 people, will the interaction be found in most of 200 studies, about half, or rarely? What about with 400 people?

> My prediction:
""")

code("""
rng = np.random.default_rng()   # a different result every time you run it


def simulate(n, outlet_effect, anon_effect, noise=1.3):
    anon = rng.integers(0, 2, n)
    label = rng.integers(0, 2, n)
    y = 4.6 - 0.8 * anon + label * np.where(anon == 1, anon_effect, outlet_effect) + rng.normal(0, noise, n)
    return pd.DataFrame({"anon": anon, "label": label, "y": y})


def interaction_interval(d):
    fit = smf.ols("y ~ label * anon", d).fit()
    lo, hi = fit.conf_int().loc["label:anon"]
    return fit.params["label:anon"], lo, hi


TRUE_INTERACTION = TRUE_ANON - TRUE_OUTLET   # -0.8
MY_N = 100                                   # change me

found = covered = 0
for _ in range(200):
    est, lo, hi = interaction_interval(simulate(MY_N, TRUE_OUTLET, TRUE_ANON))
    found += (lo > 0) or (hi < 0)
    covered += lo <= TRUE_INTERACTION <= hi
print(f"With {MY_N} people: interaction found in {found} of 200 studies; interval contained the truth in {covered} of 200")
assert covered >= 170, "A 95% interval should contain the truth about 190 times in 200. Something is wrong."
""")

md("""
**Discuss with your partner:** change `MY_N` to 400 and to 1000. How many people do you need to find an interaction of this size reliably? Why is it harder to find an interaction than a main effect?

> Log (warm-up): one thing you predicted, what happened, and the check you used.
""")

md("""
---
## Exercise 1: Check the manipulation, then estimate (required, about 30 min)

Data: `experiment`, 600 people. Columns: `session`, `device`, `source`, `label`, `noticed_label` (1 if they said they noticed an AI label), `credibility`, `age_group`.

**Predict first:** in the group that saw the label, what share will say they noticed it? In the group that did not, what share? Will it be the same on desktop and on mobile?

> My prediction:

**How to prompt well.** Give the AI the context it cannot see:

> I have a pandas DataFrame called `experiment` with columns: *(paste `list(experiment.columns)`)*. It is a 2 by 2 experiment: `source` (outlet or anonymous) by `label` (none or ai_label), randomly assigned to each person, with outcome `credibility`. **Task:** ... Use statsmodels. Write the code, then explain each line in one sentence.

| Task | What to ask for | How to check it |
|---|---|---|
| **1a** | The manipulation check: the share who noticed a label, by `label`, and within the label group by `device` | Read the table. Did the manipulation work, everywhere? |
| **1b** | From group means: the label effect for each source (`eff_outlet`, `eff_anon`: the mean credibility with the label minus without) and the interaction (`interaction = eff_anon - eff_outlet`) | The check cell |
| **1c** | A regression `credibility ~ label * source` with robust standard errors (`.fit(cov_type="HC3")`). Make `none` and `outlet` the reference levels. Store the interaction coefficient and interval in `inter_est`, `inter_lo`, `inter_hi` | The check cell |
| **1d** | Two sentences: the label effect for each source, with an interval, and what you would not claim | Say it to your partner |
""")

code("""
# Task 1a: the manipulation check.
""")
code("""
# Task 1b: simple effects from group means. It must create eff_outlet, eff_anon and interaction.
""")
code("""
# Task 1c: the regression. It must create inter_est, inter_lo, inter_hi.
""")

code("""
# Check 1. A second method: with a full interaction model, the interaction equals the difference of the two simple effects.
assert abs(interaction - (eff_anon - eff_outlet)) < 1e-9, "interaction should be eff_anon - eff_outlet."
assert abs(inter_est - interaction) < 1e-6, f"The regression interaction ({inter_est:.3f}) should match the one from group means ({interaction:.3f}). Did you set the reference levels to 'none' and 'outlet'?"
assert inter_lo < inter_est < inter_hi, "The interval should contain the estimate."
print(f"label effect, outlet: {eff_outlet:.2f}   anonymous: {eff_anon:.2f}   interaction: {interaction:.2f}")
print(f"interaction interval: {inter_lo:.2f} to {inter_hi:.2f}")
""")

md("""
**Think:** the planted effects are -0.2 (outlet) and -1.0 (anonymous), but only for people who noticed the label. Are your estimates exactly those? Why not? What do the estimates describe: people who noticed the label, or everyone who was randomized?

> Task 1d, my sentences:
>
> Log (Exercise 1): what did the AI get wrong, or what check did you run? Did you reject any code, and why?
""")

md("""
---
## Exercise 2: Check against the known answer, and break it (required, about 20 min)

The planted effect applies to people who **noticed** the label. Exercise 1a should have shown that the manipulation did not work equally everywhere. Now see what that does.

**Predict:** for the anonymous source, will the label effect be bigger on desktop or on mobile? How big will it be on desktop compared with the planted -1.0?

> My prediction:

| Task | What to ask for | How to check it |
|---|---|---|
| **2a** | The label effect for the **anonymous** source, separately for desktop and mobile (mean credibility with the label minus without). Store them in `anon_desktop` and `anon_mobile` | The check cell |
| **2b** | The "tempting" analysis: **drop people in the label group who did not notice the label**, keep everyone in the control group, and compute the label effect for the anonymous source. Store it in `pp_anon` | Compare with `eff_anon`, `anon_desktop`, and the planted -1.0 |
| **2c** | Break it on purpose: take a random 100 people (`experiment.sample(100, random_state=1)`) and repeat Exercise 1b and 1c. Is the interaction still found? | Does the interval still exclude zero? |
| **2d** | Two sentences: which of `eff_anon`, `anon_desktop`, and `pp_anon` is closest to the planted -1.0? Which would you report, and what would you say about the others? | Say it to your partner |
""")

code("""
# Task 2a:
""")
code("""
# Task 2b:
""")
code("""
# Task 2c:
""")

code("""
# Check 2. A second method for 2a.
g = experiment[experiment.source == "anonymous"].groupby(["device", "label"]).credibility.mean()
by_hand_desktop = g["desktop", "ai_label"] - g["desktop", "none"]
by_hand_mobile = g["mobile", "ai_label"] - g["mobile", "none"]
assert abs(anon_desktop - by_hand_desktop) < 1e-9 and abs(anon_mobile - by_hand_mobile) < 1e-9, "Check the filters: anonymous source only, label minus none, desktop and mobile separately."
assert abs(anon_mobile) < abs(anon_desktop), "The label effect should be weaker on mobile, where fewer people noticed it. Did you subtract the right way round?"
print(f"anonymous source: everyone {eff_anon:.2f}, desktop {anon_desktop:.2f}, mobile {anon_mobile:.2f}, drop-non-noticers {pp_anon:.2f}   planted (noticers) {TRUE_ANON}")
""")

md("""
> Task 2d, my sentences:
>
> Log (Exercise 2): why is dropping people who failed the manipulation check, after seeing the result, risky? (Hint: who notices a label? Is it a random subset?)
""")

md("""
---
## Exercise 3: Bug hunt (required, about 25 min)

Below is an analysis an AI assistant wrote for someone else. It runs without errors and prints a result. **It contains three mistakes that change the answer.** Find them without being told where they are.

**What to do**
1. Run the cell and read the result. You know what was planted.
2. Read each numbered step. What does each line do to the data or the number?
3. For each suspected bug, **prove it** with a check. Write down the check.
4. Fix the code. Put the corrected label effects in `fixed_outlet` and `fixed_anon`: the effect of the label for each source, using **all randomized people**.

**Checks that work here**
- Compare with the **known answer** (and with your own group means from Exercise 1).
- Count the **rows before and after** each step, and look at which rows were removed.
- Check the **sign** of the result against the group means.

**Hints.** If you are stuck for more than 5 minutes, ask a facilitator.
""")

code("""
# ---- AI-written analysis. Do not edit this cell; copy it to a new one to fix. ----
d = experiment.copy()

# 1. Code the label as a number
d["label_on"] = (d["label"] == "none").astype(int)

# 2. Keep the participants for whom the manipulation worked
d = d[(d["label"] == "none") | (d["noticed_label"] == 1)]
print("Rows used:", len(d))

# 3. Estimate the effect of the label
model = smf.ols("credibility ~ label_on + C(source)", data=d).fit()
print(f"Effect of the AI label on credibility: {model.params['label_on']:.2f}")
print("The label works the same way whatever the source.")
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
# Your fixed version here. It must create fixed_outlet and fixed_anon.
""")

code("""
# Check 3.
assert fixed_anon < 0, f"The label should lower credibility for the anonymous account. You have {fixed_anon:.2f}. Check the sign (which level is 1?)."
assert -1.05 < fixed_anon < -0.45, f"For the anonymous source, using everyone randomized, the label effect should be moderately negative. You have {fixed_anon:.2f}."
assert fixed_anon < fixed_outlet - 0.3, "The effect should differ between sources. Did you allow the label's effect to depend on the source (an interaction)?"
print(f"Corrected: outlet {fixed_outlet:.2f}, anonymous {fixed_anon:.2f}. Matches your group means from Exercise 1:", abs(fixed_anon - eff_anon) < 1e-6)
""")

md("""
> Log (Exercise 3): which bug was hardest to find? Which check would you use first next time?
""")

md("""
---
## Exercise 4: Your own data (about 15 min; can be homework)

Think of the comparison in your project: two or more conditions, versions of a post, a group that saw something and a group that did not. If you have no experiment, think of the comparison you would most like to make.

**Write down before you run anything:**

| Question | My answer |
|---|---|
| What are the conditions, and how were people assigned (by chance, or by themselves)? | |
| What is the manipulation check, and could it fail for some group? | |
| What is the outcome, and how is it measured? | |
| Do people come in groups (sessions, classes, accounts)? If the treatment was assigned within groups, or to whole groups, what changes? | |
| Is there an interaction you expect? What would it look like? | |
| How many people do you have per cell, and is that enough (see the warm-up)? | |
| What would you check first? | |

**Then, if you have a sample of your own data** (de-identified, small), load it and count the people in each condition. If you have none, use `experiment` and count people by `source`, `label` and `device`.
""")

code("""
# Exercise 4: your own data, or experiment. Count people per condition.
""")

md("""
---
## Log: what I learned today

- One check that told me my code was right or wrong:
- One thing the AI got wrong, or one claim I would not accept:
- One question I still have:

**Homework (45 minutes or less):** finish Exercise 4. Run the manipulation check and one group comparison on your own data (or a sample), after one known-answer check. In one paragraph: what does your method assume, and one way your data may break it (include whether people come in groups).
""")

nb = nbf.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
nbf.write(nb, OUT)
print("wrote", os.path.normpath(OUT))
