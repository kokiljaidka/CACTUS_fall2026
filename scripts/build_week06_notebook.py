"""Build notebooks/week06_ai_as_annotator.ipynb. Re-run after editing.

Data: week06_corpus.zip (private; shared through the class drive): week06_clapton_val.csv (649 messages with human labels, from the
CLAPTON validation split) and week06_llm_labels.csv (LLM labels for a fixed sample of 150). See scripts/prepare_week06_data.py.
"""
import os

import nbformat as nbf

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "notebooks", "week06_ai_as_annotator.ipynb")
cells = []


def md(t):
    cells.append(nbf.v4.new_markdown_cell(t.strip()))


def code(t):
    cells.append(nbf.v4.new_code_cell(t.strip()))


PROMPT = """You are labeling social media messages for a research project. For each numbered message, answer two yes/no questions.
1. abusive: Does the message insult, name-call, mock, or attack a person or group? Strong disagreement with, or harsh criticism of, an idea or a policy is not abuse.
2. justification: Does the message give a reason, evidence, an example, or an explanation for its claim or request?
Reply with one line per message in the form: number, abusive (yes or no), justification (yes or no). Do not explain."""

md("""
# Week 6: AI as annotator

**CACTUS Fall 2026 · Coding session**

You can ask an AI to label thousands of texts in minutes. Whether you can **trust** those labels is a measurement question. Today you compare an AI's labels with people's labels, with numbers and with your own eyes.

**Goals today**
- compute accuracy, precision, recall and Cohen's kappa, and say what each one hides
- compare with the "always no" baseline, because accuracy alone can mislead
- read the disagreements and sort them: the labeler, the codebook, or the human label
- run your own labeling with an AI, change the definition, and measure again
- find three mistakes in AI-written evaluation code

**Data (private to this class)**
- **649 Twitter, Reddit and forum messages** with human labels, from the validation split of the CLAPTON dataset (Jaidka and collaborators). `@USER` replaces user names and links are replaced with `URL`.
- **LLM labels** for a fixed sample of **150** of those messages, for two labels: *abusive* and *justification* (the prompt is shown below).

**Content note:** the messages are political arguments, insults, and abusive language. Read them as data. Step away if it bothers you.

**Rules**
- Predict before you run. Never accept AI code you have not read.
- **Human labels are not ground truth.** They are one group's judgments. You will see where they disagree with the AI, and sometimes the AI is not the one that is wrong.
- The data is for this course. Do not post it in a public place, and do not try to identify anyone.
- **For Exercise 4 only:** you may paste up to 20 messages from this dataset into your AI assistant. Names are already removed. Do not paste anything else from the data.
- Keys and passwords never go in a cell.

**Run cells one at a time**, not "Run all". Some cells are for you to fill in.
""")

md("""
## How this session runs

- There is **no lecture** in the coding session. You will be in a breakout room with a partner, and the facilitators visit the rooms.
- **Stuck?** Try these, in order, for no more than 5 minutes:
  1. Read the last line of any error message. What is it telling you?
  2. Re-read the instructions for the step. Did you skip a part?
  3. Ask your partner, then ask an AI assistant to explain the message (never paste data other than in Exercise 4).
  4. Still stuck? Click **Ask for help** in Zoom or message the facilitators in the main chat. Say what you expected, what happened, and what you already tried.
""")

code("""
import os
import zipfile

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, cohen_kappa_score, confusion_matrix, precision_recall_fscore_support

FILES = ["week06_clapton_val.csv", "week06_llm_labels.csv"]
if not all(os.path.exists(f) for f in FILES):
    try:
        from google.colab import files
        print("Upload week06_corpus.zip (the link is on the class drive).")
        for name in files.upload():
            if name.endswith(".zip"):
                zipfile.ZipFile(name).extractall(".")
    except ImportError:
        raise SystemExit("Put " + " and ".join(FILES) + " in the same folder as this notebook.")

val = pd.read_csv("week06_clapton_val.csv")
llm = pd.read_csv("week06_llm_labels.csv")
print(len(val), "messages with human labels;", len(llm), "with LLM labels")
print(val["source"].value_counts().to_dict())
""")

md("""
---
## Warm-up: the measures on 20 labels (about 10 min)

These are the same 20 labels as on the practice page. **Predict:** will the accuracy be above or below the "always 0" baseline? Then compute: accuracy, the baseline, kappa, and the confusion matrix.

> My prediction:
""")

code("""
human = [0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0]
llm20 = [0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0]

# Task: fill in acc, baseline, kappa (and print the confusion matrix).
acc = None
baseline = None
kappa = None
""")

code("""
# Check 0.
assert acc is not None and baseline is not None and kappa is not None, "Fill in acc, baseline and kappa."
assert abs(acc - accuracy_score(human, llm20)) < 1e-9, "acc is not the share of labels that agree."
assert abs(baseline - (1 - sum(human) / len(human))) < 1e-9, "The baseline is the accuracy of always predicting 0."
assert abs(kappa - cohen_kappa_score(human, llm20)) < 1e-9, "kappa should be Cohen's kappa."
print(f"accuracy {acc:.2f}, always-0 baseline {baseline:.2f}, kappa {kappa:.2f}")
""")

md("""
> Log (warm-up): which is bigger, accuracy or the baseline? What does that tell you about this labeler?
""")

md("""
---
## The prompt that produced the LLM labels

Someone has to write the definitions. These are the ones the AI was given for the 150 messages (labels made by Claude, an AI assistant, in November 2026, one pass, without seeing the human labels):

```
""" + PROMPT + """
```

The AI did **not** see the CLAPTON codebook, so its idea of "abusive" is its own reading of this sentence. Keep that in mind in Exercise 3.
""")

md("""
---
## Exercise 1: Build the evaluation table (required, about 15 min)

Join the human labels and the LLM labels for the 150 messages. **Join on `row_id`** (the position of the message in the file), which is unique.

Then add two 0/1 columns, `llm_uncivil_bin` and `llm_just_bin` (1 for "yes"), and compare **how often each side says yes**: the human prevalence of `uncivil_abuse` and `justification` versus the LLM's.

**Predict:** will the LLM say "abusive" more often or less often than the people did? And for justification?

> My prediction:
""")

code("""
# Task 1: build eval_df (150 rows) with the human labels and the two LLM columns, as 0/1 columns.
""")

code("""
# Check 1.
assert len(eval_df) == 150, f"Expected 150 rows, got {len(eval_df)}. How are you joining?"
assert eval_df["row_id"].is_unique, "row_id should be unique after the join."
for c in ["uncivil_abuse", "justification", "llm_uncivil_bin", "llm_just_bin"]:
    assert c in eval_df.columns and set(eval_df[c].unique()) <= {0, 1}, f"{c} should be a 0/1 column."
print("human abusive:", round(eval_df["uncivil_abuse"].mean(), 3), " LLM abusive:", round(eval_df["llm_uncivil_bin"].mean(), 3))
print("human justification:", round(eval_df["justification"].mean(), 3), " LLM justification:", round(eval_df["llm_just_bin"].mean(), 3))
""")

md("""
> Log (Exercise 1): which side says "abusive" more often? Why might that be?
""")

md("""
---
## Exercise 2: Measure the agreement (required, about 25 min)

For **each** of the two labels, compute: the confusion matrix, accuracy, the **always-no baseline**, precision and recall for the "yes" class, and Cohen's kappa. Store them in a dict:

```
scores = {"uncivil":      {"accuracy": ..., "baseline": ..., "precision": ..., "recall": ..., "kappa": ...},
          "justification": {...}}
```

**How to prompt well.** Never paste the data. Describe it:

> I have a pandas DataFrame `eval_df` with 0/1 columns `uncivil_abuse` (people) and `llm_uncivil_bin` (an AI). Write code that prints the confusion matrix, accuracy, the accuracy of always predicting 0, precision and recall for the 1 class, and Cohen's kappa, using scikit-learn. Explain each line in one sentence.

**Predict:** for the abusive label, will the accuracy be above or below the always-no baseline?

> My prediction:
""")

code("""
# Task 2: compute scores for both labels.
scores = {}
""")

code("""
# Check 2.
pairs = {"uncivil": ("uncivil_abuse", "llm_uncivil_bin"), "justification": ("justification", "llm_just_bin")}
for name, (h_col, l_col) in pairs.items():
    y, p = eval_df[h_col], eval_df[l_col]
    prec, rec, _, _ = precision_recall_fscore_support(y, p, average="binary", zero_division=0)
    exp = {"accuracy": accuracy_score(y, p), "baseline": max(y.mean(), 1 - y.mean()), "precision": prec, "recall": rec, "kappa": cohen_kappa_score(y, p)}
    assert name in scores, f"scores is missing '{name}'."
    for k, v in exp.items():
        assert abs(scores[name][k] - v) < 0.005, f"{name} {k}: expected about {v:.3f}, you have {scores[name][k]:.3f}."
    s = scores[name]
    print(f"{name}: accuracy {s['accuracy']:.2f} (baseline {s['baseline']:.2f}), precision {s['precision']:.2f}, recall {s['recall']:.2f}, kappa {s['kappa']:.2f}")
""")

md("""
**Say it in one sentence per label.** A good sentence names the numbers, the baseline, and the sample size, and claims no more than they show.

| Label | Your sentence |
|---|---|
| Abusive | |
| Justification | |

> Log (Exercise 2): which number surprised you? Which one would you put first in a report, and why?
""")

md("""
---
## Exercise 3: Read the disagreements (required, about 20 min)

Numbers say how often they disagree. Reading says **why**. For the abusive label, look at messages where the AI said "yes" and people said "no", and the reverse.

For each message in the sample below, decide on one reason:
- `"labeler"`: the AI got it wrong, given a fair reading of the definition
- `"codebook"`: the definition does not settle it (it could go either way)
- `"human"`: the human label looks questionable

There is no key to check against. Be ready to defend your choices to your partner.
""")

code("""
# Show up to 6 messages where the AI said abusive and people said not abusive, and every case of the reverse.
fp = eval_df[(eval_df["llm_uncivil_bin"] == 1) & (eval_df["uncivil_abuse"] == 0)].head(6)
fn = eval_df[(eval_df["llm_uncivil_bin"] == 0) & (eval_df["uncivil_abuse"] == 1)]
cases = pd.concat([fp, fn])
for _, r in cases.iterrows():
    kind = "AI yes, people no" if r["llm_uncivil_bin"] == 1 else "AI no, people yes"
    print(r["row_id"], f"[{kind}]", r["message"][:240].replace("\\n", " "))
    print()
reasons = {}   # row_id -> "labeler", "codebook" or "human"
""")

code("""
# Check 3.
assert len(reasons) >= 8, "Sort at least 8 of the disagreements."
assert set(reasons.values()) <= {"labeler", "codebook", "human"}, 'Each reason must be "labeler", "codebook" or "human".'
assert set(reasons) <= set(cases["row_id"]), "Use the row_id numbers printed above."
print(pd.Series(reasons).value_counts().to_dict())
""")

md("""
> Log (Exercise 3): which reason was most common? If most were "codebook", what would you change: the prompt, the codebook, or the human labels?
""")

md("""
---
## Exercise 4: Run your own labeling (required, about 30 min)

Now you write the definition. Work from 20 messages.

1. Run the cell below. It prints 20 numbered messages (everyone gets a different set, from your number).
2. Write your **own definition** of "abusive" in the prompt template (a sentence, plus one example of what is and is not abusive).
3. Paste the prompt and the 20 messages into your AI assistant. Ask for **one line per message: number, yes or no**.
4. Paste the AI's answers into `my_llm` (as a list of 20 strings), and run the check.
5. Make the definition **stricter or looser**, run it again, and compare. Did kappa with the human labels go up?

If you do not have AI access, work with a partner who does, or use the saved LLM labels and say so in your log.

**Optional:** label the same 20 messages **yourself and with your partner, independently**, before you look at the human labels, and compute kappa between the two of you. That number is a ceiling: an AI should not be expected to agree with people much more than people agree with each other.

**Prompt template**
```
You are labeling social media messages for a research project. For each numbered message, answer yes or no:
Is the message abusive? DEFINITION: <your definition here>.
Reply with one line per message: the number, then yes or no. Do not explain.

<paste the 20 messages>
```
""")

code("""
MY_NUMBER = 1   # use a different number from your partner
mine = eval_df.sample(20, random_state=MY_NUMBER).reset_index(drop=True)
for i, r in mine.iterrows():
    print(i + 1, "|", r["message"][:220].replace("\\n", " "))
""")

code("""
# Paste the AI's answers here, in message order, e.g. ["no", "yes", ...]. First attempt:
my_llm = []
""")

code("""
# Check 4. Cleans the labels the way an AI's answers usually need (spaces, capital letters).
clean = [str(x).strip().lower() for x in my_llm]
assert len(clean) == 20, f"my_llm should have 20 answers, not {len(clean)}."
assert set(clean) <= {"yes", "no"}, f"Answers should be yes or no. Found: {sorted(set(clean) - {'yes', 'no'})}"
mine_bin = [1 if x == "yes" else 0 for x in clean]
y = mine["uncivil_abuse"]
print("your labeler vs people:  agree", sum(a == b for a, b in zip(mine_bin, y)), "of 20, kappa", round(cohen_kappa_score(y, mine_bin), 2))
print("saved LLM vs people:     agree", sum(a == b for a, b in zip(mine["llm_uncivil_bin"], y)), "of 20, kappa", round(cohen_kappa_score(y, mine["llm_uncivil_bin"]), 2))
print("your labeler vs saved LLM: agree", sum(a == b for a, b in zip(mine_bin, mine["llm_uncivil_bin"])), "of 20")
""")

md("""
**4b. Score it once on fresh messages.** You changed the definition after seeing how it did on these 20, so the kappa you got is **optimistic**: you tuned on the same messages you tested on. Take your **final** definition and run it **once** on 20 messages you have not used. That number is your honest estimate.
""")

code("""
# Task 4b: 20 fresh messages. Run your FINAL definition on them once, and paste the answers below.
fresh = eval_df[~eval_df["row_id"].isin(mine["row_id"])].sample(20, random_state=MY_NUMBER + 100).reset_index(drop=True)
for i, r in fresh.iterrows():
    print(i + 1, "|", r["message"][:220].replace("\\n", " "))
my_llm_fresh = []
""")

code("""
# Check 4b.
clean2 = [str(x).strip().lower() for x in my_llm_fresh]
assert len(clean2) == 20 and set(clean2) <= {"yes", "no"}, "my_llm_fresh should have 20 answers, each yes or no."
fresh_bin = [1 if x == "yes" else 0 for x in clean2]
print("on fresh messages:  agree", sum(a == b for a, b in zip(fresh_bin, fresh["uncivil_abuse"])), "of 20, kappa", round(cohen_kappa_score(fresh["uncivil_abuse"], fresh_bin), 2))
print("Compare with the kappa you got while tuning. Which one would you report?")
""")

md("""
> Log (Exercise 4): what did you change in the definition, and what happened to the agreement? With only 20 messages, how sure are you? (Look at how many "abusive" messages are in your 20.)
""")

md("""
---
## Exercise 5: Bug hunt (required, about 25 min)

An AI assistant wrote this evaluation function. It **runs without errors** and prints a confident summary. **It contains three mistakes.** Find them. Facilitators give hints only.

**Predict:** before you run it, what numbers would make you suspicious?

> My prediction:
""")

code("""
def evaluate(val, llm):
    \"\"\"Written by an AI assistant. Compares the LLM's labels with the human labels.\"\"\"
    df = val.merge(llm, on="row_id")
    df = df.head(50)                                          # keep it fast
    out = {"n": len(df)}
    pairs = {"uncivil": ("uncivil_abuse", "llm_uncivil"), "justification": ("empathy_respect", "llm_justification")}
    for name, (human_col, llm_col) in pairs.items():
        y_true = df[human_col]
        y_pred = (df[llm_col] == "Yes").astype(int)
        out[name] = {"accuracy": round(accuracy_score(y_true, y_pred), 2),
                     "kappa": round(cohen_kappa_score(y_true, y_pred), 2),
                     "predicted_yes": int(y_pred.sum())}
    return out


result = evaluate(val, llm)
print("The AI's summary:")
print(f"- On {result['n']} messages, the LLM is {result['uncivil']['accuracy']:.0%} accurate at spotting abuse.")
print(f"- Justification: accuracy {result['justification']['accuracy']:.0%}, kappa {result['justification']['kappa']}.")
print(result)
""")

md("""
**Find the three mistakes.** For each, write where it is, what it does wrong, and which number or claim it distorts.

| # | Where | What is wrong | The claim it distorts |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

Then copy the function into the next cell, rename it `evaluate_fixed`, and fix it.
""")

code("""
# Write evaluate_fixed here.
""")

code("""
# Check 5.
res = evaluate_fixed(val, llm)
assert res["n"] == 150, f"The evaluation should use all 150 messages, not {res['n']}."
assert res["uncivil"]["predicted_yes"] > 0 and res["justification"]["predicted_yes"] > 0, "The LLM says yes to some messages. Check how its answers are read."
e = eval_df
exp_u = round(cohen_kappa_score(e["uncivil_abuse"], e["llm_uncivil_bin"]), 2)
exp_j = round(cohen_kappa_score(e["justification"], e["llm_just_bin"]), 2)
assert res["uncivil"]["kappa"] == exp_u, f"Abusive kappa should be {exp_u}, you have {res['uncivil']['kappa']}."
assert res["justification"]["kappa"] == exp_j, f"Justification kappa should be {exp_j}, you have {res['justification']['kappa']}. Is it compared with the right human column?"
print("All three fixed.")
""")

md("""
> Log (Exercise 5): which mistake was hardest to see? Why did the code run without an error?
""")

md("""
---
## Stretch (about 15 min)

- **By source.** Compute kappa for each source (`twitter`, `reddit`, `trivium`). How many messages are in each? What can you say, and what can you not?
- **How sure are you?** Resample the 150 messages with replacement 1,000 times, compute kappa each time, and report the 2.5th and 97.5th percentiles.
- **A third label.** Pick another human label (for example `empathy_respect`), write a definition, label 20 messages, and measure.
""")

code("""
# Stretch.
""")

md("""
---
## Log: what I learned today

- One number that looked good and was not, and what showed it:
- One disagreement that was not the AI's fault:
- One thing I would record every time I label with an AI (model, prompt, date, ...):

**Homework (45 minutes or less):** for your own project, write a short **codebook** for one label (a definition and two examples of yes and two of no). **Write down the agreement you would accept before you look at the result** (for example, kappa of at least 0.6, and close to how much two people agree). Hand-label 30 texts, ask an AI to label the same 30, and report accuracy, the baseline, and kappa. Tune on some texts and score a separate set once. Save the prompt, the model name, and the date. **Before you send any texts to an AI service, de-identify them first (names, handles, links) and check that your data terms and ethics approval allow it.** If you do not have your own text yet, use the Week 5 corpora and say so.
""")

nb = nbf.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
nbf.write(nb, OUT)
print("wrote", os.path.normpath(OUT))
