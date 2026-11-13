"""Build notebooks/week07_core_nested_data.ipynb (Week 7, Session 1: the shared core).

Data from scripts/make_week07_nested.py (invented, with planted answers).
Re-run after editing.
"""
import os

import nbformat as nbf

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "notebooks", "week07_core_nested_data.ipynb")
cells = []


def md(t):
    cells.append(nbf.v4.new_markdown_cell(t.strip()))


def code(t):
    cells.append(nbf.v4.new_code_cell(t.strip()))


md("""
# Week 7, Session 1: Applying statistics to social media data

**CACTUS Fall 2026 · Coding session (everyone)**

**The story (made up):** some posts carry an "AI-generated" label. We look at the comments under 80 posts. The outcome is `warmth`: how warm a comment is, on roughly a 0 to 10 scale. In these invented data **the true effect of the label on a comment's warmth is -0.5 points**, and **a long comment is 0.4 points warmer**. We also know how many comments each post received, and how many followers its author has. Because we planted the answers, we can check whether our methods find them.

**The big idea:** comments under the same post are not 3,000 independent opinions. They share a post. Ignoring that makes results look far more certain than they are.

**Goals today**
- plant an answer in simulated data, and check a method against it
- see what happens to standard errors when rows come in groups, and fix it
- model counts with an exposure (comments per follower, not comments)
- find mistakes in AI-written code using the known answer
- check a result with a permutation test, which works when there is no formula

**Order**
1. The warm-up and Exercises 1 to 3 are required. Exercise 4 if you have time.
2. At the end, choose your track for Session 2.

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
import statsmodels.api as sm
import statsmodels.formula.api as smf

TRUE_LABEL = -0.5        # true effect of the post label on warmth (planted)
TRUE_RATE_RATIO = 0.8    # true effect of the label on comments per follower (planted)

BASE = "https://raw.githubusercontent.com/kokiljaidka/CACTUS_fall2026/main/data/"


def load(name):
    # use a local copy if you have one, otherwise read the file from the course repository
    return pd.read_csv(name) if os.path.exists(name) else pd.read_csv(BASE + name)


comments = load("week07_comments.csv")   # a sample of comments, with the post each is under
posts = load("week07_posts.csv")         # one row per post
print("comments:", comments.shape, "  posts:", posts.shape)
""")

md("""
---
## Warm-up: plant an answer, then see what ignoring posts does (about 15 min)

Here you build the data, so you know the answer. Each simulated post has a **post effect**: some posts just attract warmer comments, whatever the label. You can change how many posts, how many comments per post, and how big the post effect is.

We run the same study 200 times and compare two ways to build a 95% interval:
- **naive:** treat every comment as independent
- **clustered:** allow for comments sharing a post (cluster-robust standard errors)

**Predict:** out of 200 studies, about how many naive intervals will contain the true effect? And the clustered ones?

> My prediction:
""")

code("""
rng = np.random.default_rng()   # a different result every time you run it


def simulate(n_posts, per_post, effect, post_sd):
    # half the posts carry the label (a post-level variable); every comment gets its post's effect
    labeled = np.repeat(rng.permutation([0, 1] * (n_posts // 2)), per_post)
    post_id = np.repeat(np.arange(n_posts), per_post)
    post_effect = np.repeat(rng.normal(0, post_sd, n_posts), per_post)
    y = 5 + effect * labeled + post_effect + rng.normal(0, 2.0, n_posts * per_post)
    return pd.DataFrame({"post_id": post_id, "labeled": labeled, "y": y})


def intervals(d):
    naive = smf.ols("y ~ labeled", d).fit()
    clustered = smf.ols("y ~ labeled", d).fit(cov_type="cluster", cov_kwds={"groups": d["post_id"]})
    return naive.conf_int().loc["labeled"].values, clustered.conf_int().loc["labeled"].values


MY_POSTS = 40        # change me (an even number)
MY_PER_POST = 20     # change me
MY_POST_SD = 1.5     # change me: 0 means posts do not differ at all

hit_naive = hit_clustered = 0
for _ in range(200):
    n_lo_hi, c_lo_hi = intervals(simulate(MY_POSTS, MY_PER_POST, TRUE_LABEL, MY_POST_SD))
    hit_naive += n_lo_hi[0] <= TRUE_LABEL <= n_lo_hi[1]
    hit_clustered += c_lo_hi[0] <= TRUE_LABEL <= c_lo_hi[1]

print(f"Naive intervals that contained the truth:     {hit_naive} out of 200")
print(f"Clustered intervals that contained the truth: {hit_clustered} out of 200")
assert hit_clustered >= 160, "A 95% interval should contain the truth about 190 times in 200. Check the clustering."
""")

md("""
**Discuss with your partner:** a "95%" interval should contain the truth about 190 times in 200. Which method keeps that promise? Now set `MY_POST_SD = 0` (posts do not differ) and run again. What happens to the naive intervals, and why?

> Log (warm-up): one thing you predicted, what happened, and the check you used.
""")

md("""
---
## Exercise 1: Naive versus clustered, on the data (required, about 30 min)

Data: `comments`, a sample of about 3,000 comments under 80 posts. Columns: `post_id`, `labeled` (1 if **the post** carries the label, so every comment under a post has the same value), `long_comment` (1 if **the comment** is long, which varies within a post), and `warmth`.

**Predict first:** if you ignore the posts, will the label's interval be wider or narrower than if you cluster by post? By about how much? Will the same be true for `long_comment`?

> My prediction:

**How to prompt well.** Give the AI the context it cannot see:

> I have a pandas DataFrame called `comments` with columns: *(paste `list(comments.columns)`)*. Each comment is under one post (`post_id`), and `labeled` is a property of the post. **Task:** ... Use statsmodels. Write the code, then explain each line in one sentence.

| Task | What to ask for | How to check it |
|---|---|---|
| **1a** | How many comments, how many posts, comments per post (min, median, max), and mean warmth for labeled and unlabeled posts | Do the comments add up? |
| **1b** | The **naive** regression `warmth ~ labeled + long_comment`. Store the label's coefficient, standard error and interval in `est_naive`, `se_naive`, `lo_naive`, `hi_naive`, and the long-comment standard error in `se_long_naive` | The check cell |
| **1c** | The **same regression with standard errors clustered by `post_id`**. Store `est_cl`, `se_cl`, `lo_cl`, `hi_cl`, and `se_long_cl` | The check cell |
| **1d** | Two numbers: how many times bigger is the clustered standard error than the naive one, for the label, and for the long-comment variable. One sentence on why they differ | Say it to your partner |
| **1e** (one line) | The mixed model `smf.mixedlm("warmth ~ labeled + long_comment", comments, groups=comments["post_id"]).fit()`. Compare its label coefficient and standard error with 1c | Are they close? |
""")

code("""
# Task 1a: paste the AI's code here, then run it.
""")
code("""
# Task 1b: the naive regression. It must create est_naive, se_naive, lo_naive, hi_naive, se_long_naive.
""")
code("""
# Task 1c: the same regression, clustered by post. It must create est_cl, se_cl, lo_cl, hi_cl, se_long_cl.
""")

code("""
# Check 1. Run after 1b and 1c. It compares your numbers with a second method.
# Second method: average the warmth of each post, and compare the 40 labeled posts with the 40 others.
by_post = comments.groupby("post_id").agg(warmth=("warmth", "mean"), labeled=("labeled", "first"))
second = smf.ols("warmth ~ labeled", by_post).fit()

assert abs(est_naive - est_cl) < 1e-6, "Clustering should not change the estimate, only its standard error."
assert se_cl > se_naive, "The clustered standard error should be bigger. Did you cluster by post_id?"
assert 0.75 < se_cl / second.bse["labeled"] < 1.25, (
    f"Your clustered standard error ({se_cl:.2f}) should be close to the post-level one ({second.bse['labeled']:.2f}). "
    "Are you clustering by post_id, not by comment_id or something else?")
print(f"label: estimate {est_cl:.2f}, naive SE {se_naive:.2f}, clustered SE {se_cl:.2f}   (ratio {se_cl / se_naive:.1f})")
print(f"long comment: naive SE {se_long_naive:.2f}, clustered SE {se_long_cl:.2f}   (ratio {se_long_cl / se_long_naive:.1f})")
print(f"True label effect {TRUE_LABEL}. Naive interval {lo_naive:.2f} to {hi_naive:.2f}; clustered interval {lo_cl:.2f} to {hi_cl:.2f}")
print("Does the naive interval contain the truth?   ", lo_naive <= TRUE_LABEL <= hi_naive)
print("Does the clustered interval contain the truth?", lo_cl <= TRUE_LABEL <= hi_cl)
""")

md("""
**Think:** which variable's standard error changed a lot, the post-level one (`labeled`) or the comment-level one (`long_comment`)? Why? What would a reader conclude from the naive interval alone?

> Task 1d, my sentence:
>
> Log (Exercise 1): what did the AI get wrong, or what check did you run? Did you reject any code, and why?
""")

md("""
---
## Exercise 2: Counts and exposure (required, about 25 min)

Data: `posts`, one row per post. `comments_total` is **all** the comments the post received (the comments file only has a sample). `followers` is the size of the author's audience: the **exposure**. A post with more followers gets more comments, whatever the label.

In these data the platform labeled posts from **bigger accounts**. The true effect of the label is that a labeled post gets **0.8 times** the comments **per follower**.

**Predict:** if you compare the raw number of comments, will labeled posts have more or fewer? What do you expect once you account for followers?

> My prediction:

| Task | What to ask for | How to check it |
|---|---|---|
| **2a** | Mean `comments_total` and mean `followers` for labeled and unlabeled posts | Compare the two columns |
| **2b** | A **Poisson regression** of `comments_total` on `labeled`, with `log(followers)` as the **offset**, and robust standard errors (`cov_type="HC0"`). Store the rate ratio `rr = exp(coefficient)` and its interval `rr_lo`, `rr_hi` | The check cell |
| **2c** | The same model **without** the offset. Store `rr_no_offset`. Compare | Which one matches the truth? |
| **2d** | One sentence: "Labeled posts got ... times the comments per follower, with an interval of ...". Why can the raw counts say the opposite? | Say it to your partner |

An **offset** tells the model "this count is proportional to this exposure", so it models comments *per follower*. A **rate ratio** of 0.8 means 20% fewer.
""")

code("""
# Task 2a:
""")
code("""
# Task 2b: Poisson with an offset. It must create rr, rr_lo, rr_hi.
""")
code("""
# Task 2c: the same without the offset. It must create rr_no_offset.
""")

code("""
# Check 2. A second method: the total comments per follower in each group, by hand.
g = posts.groupby("labeled")[["comments_total", "followers"]].sum()
rate = g["comments_total"] / g["followers"]
by_hand = rate[1] / rate[0]

assert abs(rr - by_hand) < 1e-6, f"With one yes/no variable and an offset, the rate ratio is the ratio of the two rates: {by_hand:.3f}. You got {rr:.3f}. Is the offset log(followers)?"
assert rr_lo < rr < rr_hi, "The interval should contain the estimate."
print(f"raw mean comments:  unlabeled {posts.loc[posts.labeled == 0, 'comments_total'].mean():.1f}, labeled {posts.loc[posts.labeled == 1, 'comments_total'].mean():.1f}")
print(f"rate ratio with offset: {rr:.2f}  (interval {rr_lo:.2f} to {rr_hi:.2f})   without the offset: {rr_no_offset:.2f}   true: {TRUE_RATE_RATIO}")
print("Does the interval contain the true rate ratio?", rr_lo <= TRUE_RATE_RATIO <= rr_hi)
""")

md("""
> Task 2d, my sentence:
>
> Log (Exercise 2): how did the no-offset result mislead? In your own work, what is the "followers" (the exposure)?
""")

md("""
---
## Exercise 3: Bug hunt (required, about 25 min)

Below is an analysis an AI assistant wrote for someone else. It runs without errors and prints a result. **It contains three mistakes that change the answer.** Find them without being told where they are.

**What to do**
1. Run the cell and read the result. You know the true answers: a label effect of -0.5 and a rate ratio of 0.8.
2. Read each numbered step. What does each line do?
3. For each suspected bug, **prove it** with a check. Write down the check.
4. Fix the code. The fixed numbers go in `se_fixed` and `rr_fixed`.

**Checks that work here**
- Compare with the **known answer**.
- Compare with a **second method** (as in Checks 1 and 2).
- Count **how many groups** the code thinks it has.

**Hints.** If you are stuck for more than 5 minutes, ask a facilitator.
""")

code("""
# ---- AI-written analysis. Do not edit this cell; copy it to a new one to fix. ----
# 1. The effect of the label on warmth, "accounting for posts"
m1 = smf.ols("warmth ~ labeled + long_comment", data=comments).fit(
    cov_type="cluster", cov_kwds={"groups": comments["comment_id"]})
print(f"Effect of the label on warmth: {m1.params['labeled']:.2f} (SE {m1.bse['labeled']:.2f})")
print(f"95% interval: {m1.conf_int().loc['labeled', 0]:.2f} to {m1.conf_int().loc['labeled', 1]:.2f}")

# 2. Comments per post, as a Poisson model
m2 = smf.glm("comments_total ~ labeled", data=posts, family=sm.families.Poisson()).fit(cov_type="HC0")
rr_ai = m2.params["labeled"]

# 3. Report it
print(f"Labeled posts get {rr_ai:.2f} times as many comments")
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
# Your fixed version here. It must create se_fixed (the SE of the label on warmth) and rr_fixed (the rate ratio).
""")

code("""
# Check 3.
assert 0.25 < se_fixed < 0.5, f"The standard error of the label should be about 0.37 once comments are grouped by post. You have {se_fixed:.2f}."
assert 0.65 < rr_fixed < 0.95, f"The rate ratio should be a little below 1 once followers are accounted for. You have {rr_fixed:.2f}."
print("Both numbers are now close to what the planted answers allow.")
""")

md("""
> Log (Exercise 3): which bug was hardest to find? Which check would you use first next time?
""")

md("""
---
## Exercise 4: A check that always works: permutation (about 15 min; start it, finish as homework if needed)

Some results have no neat formula for their standard error (a network statistic, a count of templates). A **permutation test** works anyway: shuffle the labels so any pattern is due to chance, compute your statistic many times, and see where the real one falls.

**Predict:** if you shuffle the label **across the 3,000 comments**, versus **across the 80 posts**, which gives a wider spread of "chance" results? Which one matches what the clustered standard error told you?

> My prediction:

| Task | What to ask for | How to check it |
|---|---|---|
| **4a** | The observed difference in mean warmth between comments under labeled and unlabeled posts. Store it in `obs` | Compare with your regression |
| **4b** | Shuffle the label **across posts** (the 80 post labels), 1,000 times. Each time recompute the difference in mean warmth. Store the 1,000 differences in `perm_posts` | The check cell |
| **4c** | The same, but shuffling the label **across comments**. Store `perm_comments` | Compare the two spreads |
| **4d** | The share of `perm_posts` at least as extreme as `obs` (two-sided). Store it in `p_perm`. Compare with the naive and clustered intervals | Do they agree? |
""")

code("""
# Task 4a, 4b, 4c, 4d. Hint for the shuffle across posts: shuffle a 80-long list of labels, then map each comment to its post's new label.
""")

code("""
# Check 4.
assert len(perm_posts) == 1000 and len(perm_comments) == 1000, "Run 1,000 shuffles of each kind."
sd_posts, sd_comments = np.std(perm_posts), np.std(perm_comments)
print(f"observed difference {obs:.2f}")
print(f"spread of chance results: shuffling posts {sd_posts:.2f}, shuffling comments {sd_comments:.2f}")
print(f"permutation p-value (across posts): {p_perm:.3f}")
assert sd_posts > 2 * sd_comments, "Shuffling posts should give a much wider spread than shuffling comments. Did you shuffle the 80 post labels, then map them to comments?"
""")

md("""
> Log (Exercise 4): what did the permutation test say about the label's effect? Does it match the clustered interval?
""")

md("""
---
## Choose your track for Session 2

Pick the track nearest your project. Tell the facilitators in the chat.

| Track | Good if your project is about | You will |
|---|---|---|
| **A. Networks** | Who talks to whom: replies, mentions, quotes | Build a graph, find who is central and which groups form, and check it against shuffled networks |
| **B. Images and memes** | Repeated templates, reposts, visual spread | Fingerprint images, group near-duplicates, and count templates |
| **C. Mock feed or experiment** | A randomized comparison: a source cue, a chatbot condition, a manipulated feed | Compare conditions, check the manipulation, and estimate an interaction |

> My track:

**Before Session 2:** read your track's chapter section (about 20 minutes), and bring a small de-identified sample of your own data if you have one.

---
## Log: what I learned today

- One check that told me my code was right or wrong:
- One thing the AI got wrong, or one claim I would not accept:
- One question I still have:

**Homework (45 minutes or less):** finish Exercise 4 and anything you did not finish. In one paragraph: in your own project, which rows come in groups (comments in posts, posts by one account, people in one group)? What would ignoring the grouping do to your results?
""")

nb = nbf.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
nbf.write(nb, OUT)
print("wrote", os.path.normpath(OUT))
