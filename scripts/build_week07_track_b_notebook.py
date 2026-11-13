"""Build notebooks/week07_track_b_images.ipynb (Week 7, Session 2, Track B: images and memes).

Data from scripts/make_week07_memes.py (invented images drawn by the script). Re-run after editing.
The fingerprint (a difference hash) is written with Pillow and numpy, so nothing extra needs installing.
"""
import os

import nbformat as nbf

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "notebooks", "week07_track_b_images.ipynb")
cells = []


def md(t):
    cells.append(nbf.v4.new_markdown_cell(t.strip()))


def code(t):
    cells.append(nbf.v4.new_code_cell(t.strip()))


md("""
# Week 7, Session 2, Track B: images and memes

**CACTUS Fall 2026 · Coding session (Track B)**

**The story (made up):** 220 images posted in a discussion. Six "meme templates" (simple drawn layouts) are reused with different captions, crops, brightness, sizes and compression. Some images are **reposted exactly** by several accounts. Some images are unrelated. We planted all of this, so we know how many templates there are and which image belongs to which. The images were drawn by a script: there are no real people or posts here.

**The method:** a **perceptual hash** is a short fingerprint of what an image *looks like*. Two copies of the same template, even cropped or recolored a little, get fingerprints that are close; different templates get fingerprints that are far apart. We group images whose fingerprints are close.

**Goals today**
- plant near-copies of an image and see how far their fingerprints drift
- fingerprint every image and group near-duplicates
- check the groups against the planted templates, and see what a bad threshold does
- separate "how many posts", "how many different images" and "how many accounts"
- find mistakes in AI-written code using the known answer
- plan the same checks for your own images

**Order**
1. The warm-up and Exercises 1 to 3 are required. Exercise 4 (your own data) can be finished as homework.

**Rules**
- Predict before you run.
- Never accept AI code you have not read.
- Every cell you keep needs a note on how you checked it.
- Do not paste personal information or API keys into an AI chat. Real images of real people raise extra privacy questions: ask before you collect or share them.

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
import urllib.request
import zipfile

import networkx as nx
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageEnhance
from sklearn.metrics import adjusted_rand_score

BASE = "https://raw.githubusercontent.com/kokiljaidka/CACTUS_fall2026/main/data/"


def load(name):
    # use a local copy if you have one, otherwise read the file from the course repository
    return pd.read_csv(name) if os.path.exists(name) else pd.read_csv(BASE + name)


def dhash(img, n=8):
    # a difference hash: shrink to 9x8 grey pixels, then record whether each pixel is brighter than its left neighbour.
    # The result is 64 yes/no values (a fingerprint of what the image looks like, not of its exact pixels).
    g = img.convert("L").resize((n + 1, n), Image.LANCZOS)
    a = np.asarray(g, dtype=float)
    return (a[:, 1:] > a[:, :-1]).flatten()


def distance(h1, h2):
    # the number of positions where two fingerprints differ (0 to 64)
    return int((h1 != h2).sum())
""")

md("""
---
## Warm-up: plant near-copies and see how far their fingerprints drift (about 15 min)

Here you draw two simple "templates" yourself, make 50 slightly changed copies of the first (cropped, resized, a different brightness), and measure how far each copy's fingerprint is from the original and from the *other* template.

**Predict:** will the copies of template 1 be closer to template 1 than to template 2? By how many bits (out of 64)? What if you crop more?

> My prediction:
""")

code("""
rng = np.random.default_rng()   # a different result every time you run it


def base(k):
    im = Image.new("RGB", (400, 400), "white")
    d = ImageDraw.Draw(im)
    if k == 1:
        d.rectangle([0, 0, 200, 400], fill=(30, 60, 140)); d.rectangle([200, 0, 400, 400], fill=(230, 190, 50)); d.ellipse([100, 100, 300, 300], fill=(200, 40, 40))
    else:
        for i, c in enumerate([(20, 120, 80), (240, 240, 240), (150, 30, 90)]):
            d.rectangle([0, i * 133, 400, (i + 1) * 133], fill=c)
        d.rectangle([40, 160, 200, 240], fill=(20, 20, 20))
    return im


def perturb(im, max_crop):
    w, h = im.size
    box = (int(w * rng.uniform(0, max_crop)), int(h * rng.uniform(0, max_crop)), int(w * (1 - rng.uniform(0, max_crop))), int(h * (1 - rng.uniform(0, max_crop))))
    im = im.crop(box).resize((int(rng.integers(300, 451)), int(rng.integers(300, 451))))
    return ImageEnhance.Brightness(im).enhance(rng.uniform(0.8, 1.2))


MY_MAX_CROP = 0.10   # change me: the most that can be cropped from each side (0.10 is 10%)

h1, h2 = dhash(base(1)), dhash(base(2))
d_same = [distance(dhash(perturb(base(1), MY_MAX_CROP)), h1) for _ in range(50)]
d_other = [distance(dhash(perturb(base(1), MY_MAX_CROP)), h2) for _ in range(50)]
print(f"copy to its own original: average {np.mean(d_same):.1f} bits, furthest {max(d_same)}")
print(f"copy to the other template: average {np.mean(d_other):.1f} bits, closest {min(d_other)}")
assert np.mean(d_same) < np.mean(d_other), "Copies of a template should be closer to it than to a different template. Check the code."
""")

md("""
**Discuss with your partner:** set `MY_MAX_CROP = 0.3`, then `0.5`. What happens to the distances, and when does a copy become closer to the wrong template? What does that say about where to put a threshold?

> Log (warm-up): one thing you predicted, what happened, and the check you used.
""")

code("""
# Get the images (a zip of 220 jpg files, about 3 MB) and the lists that go with them.
if not os.path.exists("memes"):
    if not os.path.exists("week07_memes.zip"):
        urllib.request.urlretrieve(BASE + "week07_memes.zip", "week07_memes.zip")
    zipfile.ZipFile("week07_memes.zip").extractall(".")

manifest = load("week07_memes.csv")          # file, account
files = sorted(manifest["file"])
print(len(files), "images;", manifest["account"].nunique(), "different accounts")
manifest.head()
""")

md("""
---
## Exercise 1: Fingerprint and group (required, about 30 min)

**Predict first:** will every image be the same size? How many of the 220 images do you think are exact repeats of another image? How many groups of near-duplicates do you expect?

> My prediction:

**How to prompt well.** Give the AI the context it cannot see:

> I have a folder `memes/` of jpg files, and a list `files` of their names. I have a function `dhash(img)` that returns a 64-value True/False array. **Task:** ... Use numpy and networkx. Write the code, then explain each line in one sentence.

| Task | What to ask for | How to check it |
|---|---|---|
| **1a** | Open a few images. Print the smallest and largest width and height. How many different accounts posted, and what is the most images any one account posted? | Are the images all the same size? |
| **1b** | The fingerprint of every image: a dictionary `hashes` from file name to `dhash(Image.open("memes/" + file))` | The check cell |
| **1c** | A distance matrix `D` (220 by 220) of the number of differing bits between every pair of fingerprints | The check cell |
| **1d** | Groups: connect two images if their distance is at most `THRESHOLD = 10`, and take the connected components (networkx `connected_components`). Store a list of lists of file names in `groups` | The check cell |
""")

code("""
# Task 1a: sizes and accounts.
""")
code("""
# Task 1b: the dictionary hashes.
""")
code("""
# Task 1c: the distance matrix D (rows and columns in the order of `files`).
""")
code("""
# Task 1d: THRESHOLD = 10, then groups.
""")

code("""
# Check 1.
assert len(hashes) == len(files) and all(len(v) == 64 for v in hashes.values()), "One 64-value fingerprint per image."
assert D.shape == (len(files), len(files)) and (np.diag(D) == 0).all() and (D == D.T).all(), "D should be square, symmetric, with zeros on the diagonal."
assert sorted(f for g in groups for f in g) == files, "Every image should be in exactly one group."
sizes = sorted((len(g) for g in groups), reverse=True)
print(f"{(np.triu(D == 0, 1)).sum()} pairs of images have identical fingerprints (distance 0)")
print(f"{len(groups)} groups. Largest sizes: {sizes[:8]}. Groups of one image: {sum(s == 1 for s in sizes)}")
""")

md("""
**Think:** why are there more groups than templates? What are the groups of one image? What would you lose if you looked only at exact duplicates (distance 0)?

> Log (Exercise 1): what did the AI get wrong, or what check did you run? Did you reject any code, and why?
""")

md("""
---
## Exercise 2: Check against the known answer, and break it (required, about 25 min)

`truth` lists each image's true template (T1 to T6, or `none` for the unrelated ones). In a real project you would not have this. Here it is the known answer.

**Predict:** at a threshold of 10, will the groups match the templates? What will happen at 20? At 30?

> My prediction:
""")

code("""
truth = load("week07_memes_truth.csv").set_index("file")


def ari_groups(groups):
    # how well do these groups match the planted templates? 1 is a perfect match, 0 is no better than chance.
    # Unrelated images (template "none") each count as their own group.
    pred = {f: i for i, g in enumerate(groups) for f in g}
    true_label = [t if t != "none" else "none_" + f for f, t in zip(files, truth.loc[files, "template"])]
    return adjusted_rand_score(true_label, [pred[f] for f in files])
""")

md("""
| Task | What to ask for | How to check it |
|---|---|---|
| **2a** | Score your `groups` with `ari_groups(groups)`. Store it in `ari_10`. How many groups hold at least 3 images? | The check cell |
| **2b** | Repeat 1d and 2a for thresholds 4, 8, 12, 16, 20, 25. Store the scores in a dictionary `ari_by_threshold` (threshold to score). Where does it work, and where does it fall apart? | The check cell |
| **2c** | Look at your **largest** group. How many images are in it (`top_group_posts`), how many of those are **different** images, i.e. different fingerprints (`top_group_images`), and how many **different accounts** posted them (`top_group_accounts`; use `manifest`)? | The check cell |
| **2d** | Two sentences: how popular is the biggest template, counted three ways, and which number would you report? | Say it to your partner |
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
# Check 2.
assert 0.9 < ari_10 <= 1, f"At a threshold of 10 the groups should match the templates closely. You have {ari_10:.2f}. Is THRESHOLD 10 and D built from the right pairs?"
assert ari_by_threshold[12] > 0.9 and ari_by_threshold[25] < 0.1, "A moderate threshold should work, and a very loose one should merge everything. Check your loop."
assert top_group_images <= top_group_posts and top_group_accounts <= top_group_posts, "Different images and accounts cannot outnumber posts."
print("threshold -> ARI:", {k: round(v, 2) for k, v in sorted(ari_by_threshold.items())})
print(f"largest group: {top_group_posts} posts, {top_group_images} different images, {top_group_accounts} different accounts")
""")

md("""
> Task 2d, my sentences:
>
> Log (Exercise 2): why does one loose threshold ruin the groups? (Hint: think about chains: A is close to B, B to C, C to D.)
""")

md("""
---
## Exercise 3: Bug hunt (required, about 25 min)

Below is an analysis an AI assistant wrote for someone else. It runs without errors and prints a result. **It contains three mistakes that change the answer.** Find them without being told where they are.

**What to do**
1. Run the cell and read the result. You know there are six templates.
2. Read each numbered step. What does each line do?
3. For each suspected bug, **prove it** with a check. Write down the check.
4. Fix the code. Put the number of templates in `n_templates`, and the agreement with the planted templates (`ari_groups`) in `ari_fixed`.

**Checks that work here**
- Compare with the **known answer** (six templates) and with your own groups from Exercises 1 and 2.
- Look at what a **fingerprint** is made of, for two images you know are copies.
- Ask what each number is a **count of**.

**Hints.** If you are stuck for more than 5 minutes, ask a facilitator.
""")

code("""
# ---- AI-written analysis. Do not edit this cell; copy it to a new one to fix. ----
# 1. Fingerprint each image
def fingerprint(path):
    img = Image.open(path).convert("L")
    px = np.asarray(img, dtype=float)[:8, :9]        # a 9x8 patch
    return (px[:, 1:] > px[:, :-1]).flatten()

fp = {f: fingerprint("memes/" + f) for f in files}

# 2. Group images whose fingerprints are close
M = np.array([fp[f] for f in files])
D2 = (M[:, None, :] != M[None, :, :]).sum(axis=2)
G2 = nx.Graph()
G2.add_nodes_from(files)
for i in range(len(files)):
    for j in range(i + 1, len(files)):
        if D2[i, j] <= 28:
            G2.add_edge(files[i], files[j])
groups2 = [list(c) for c in nx.connected_components(G2)]

# 3. Count the templates
print("Templates found:", len(groups2))
print("Agreement with the planted templates:", round(ari_groups(groups2), 2))
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
# Your fixed version here. It must create n_templates and ari_fixed.
""")

code("""
# Check 3.
assert n_templates == 6, f"There are six templates. You report {n_templates}. What counts as a template: any group, or a group of several images?"
assert ari_fixed > 0.9, f"The fixed groups should match the planted templates (agreement above 0.9). You have {ari_fixed:.2f}."
print("Both numbers now match what was planted.")
""")

md("""
> Log (Exercise 3): which bug was hardest to find? Which check would you use first next time?
""")

md("""
---
## Exercise 4: Your own data (about 15 min; can be homework)

Think of the images in your project: memes, screenshots, photos, posters. If you have none, think of the images you would most like to study.

**Write down before you run anything:**

| Question | My answer |
|---|---|
| Are the images real people, or could they identify someone? What do your ethics rules say about collecting and sharing them? | |
| What counts as the "same" image: an exact repost, a crop, a new caption, a re-photograph? | |
| Which changes should the fingerprint ignore, and which should it notice? | |
| Where would you put a threshold, and how would you check it (by looking at examples)? | |
| Could one account or a bot be posting the same image many times? | |
| What would you check first? | |

**Then, if you have a small sample of your own images** (a handful, and only ones you may use), fingerprint them with `dhash` and look at the distances between a few pairs. If you have none, look at the five closest pairs of images in `D` that are in *different* planted templates, and open them.

**Stretch.** Describing images with an AI model (for example, naming what a meme is about) is a separate step with its own checks, like Week 6. If your facilitators have shared pre-run labels, compare them with the groups. Do not put API keys in a shared notebook, and do not send images of people to a service without checking the terms and your ethics approval.
""")

code("""
# Exercise 4: your own images, or the closest pairs across different templates in D.
""")

md("""
---
## Log: what I learned today

- One check that told me my code was right or wrong:
- One thing the AI got wrong, or one claim I would not accept:
- One question I still have:

**Homework (45 minutes or less):** finish Exercise 4. Fingerprint a sample of your own images (if you may use them), pick a threshold by looking at examples, and run one known-answer check. In one paragraph: what does your method assume, and one way your images may break it (include repeats, crops and what counts as the same).
""")

nb = nbf.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
nbf.write(nb, OUT)
print("wrote", os.path.normpath(OUT))
