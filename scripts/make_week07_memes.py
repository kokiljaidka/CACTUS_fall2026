"""Simulate the Week 7 Track B dataset: generated "meme" images. All invented, drawn by this script.

Story (made up): 220 images posted in a discussion. Six "templates" (simple drawn layouts) are
reused with different captions, crops, brightness, sizes and compression. A couple of images are
reposted exactly by several accounts. Forty images are unrelated.

  data/week07_memes.zip          the images (jpg), in one folder
  data/week07_memes.csv          file, account (who posted it), what students see
  data/week07_memes_truth.csv    the planted truth: file, template (T1..T6 or none), kind

KNOWN ANSWERS (planted)
  - 6 templates, with 28 variants each (a different caption, a crop of up to 12%, brightness
    change, a different size, noise, JPEG quality): 168 images.
  - 12 exact reposts: two of the T1 images, each posted again 6 times by different accounts.
    They are byte-for-byte copies, so their fingerprints are identical.
  - 40 unrelated images (random shapes), template "none".

Run: python scripts/make_week07_memes.py
"""
import io
import os
import zipfile

import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

SEED = 23
SIZE = 400
CAPTIONS = ["WHEN THE AI WRITES IT", "NOBODY: ABSOLUTELY NOBODY", "ME CHECKING THE CODE", "TRUST BUT VERIFY",
            "IT RUNS SO IT MUST BE RIGHT", "THE LOG DOES NOT LIE", "ONE MORE ROW GONE", "PLANT THE ANSWER FIRST",
            "SURELY IT WORKED", "FOUND THE BUG", "THE CLUSTER STRIKES BACK", "COUNT THE RIGHT THING"]
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")


def _font(size):
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


def template(k):
    """Return a 400x400 RGB image for template k (1 to 6)."""
    im = Image.new("RGB", (SIZE, SIZE), "white")
    d = ImageDraw.Draw(im)
    s = SIZE
    if k == 1:      # vertical split with a big circle
        d.rectangle([0, 0, s // 2, s], fill=(30, 60, 140)); d.rectangle([s // 2, 0, s, s], fill=(230, 190, 50))
        d.ellipse([s * 0.25, s * 0.25, s * 0.75, s * 0.75], fill=(200, 40, 40))
    elif k == 2:    # three horizontal bands
        for i, c in enumerate([(20, 120, 80), (240, 240, 240), (150, 30, 90)]):
            d.rectangle([0, i * s // 3, s, (i + 1) * s // 3], fill=c)
        d.rectangle([s * 0.1, s * 0.4, s * 0.5, s * 0.6], fill=(20, 20, 20))
    elif k == 3:    # diagonal gradient with a triangle
        a = np.fromfunction(lambda y, x: (x + y) / (2 * s) * 255, (s, s))
        im = Image.fromarray(np.stack([a, 255 - a, 120 * np.ones_like(a)], axis=2).astype("uint8"))
        d = ImageDraw.Draw(im)
        d.polygon([(s * 0.5, s * 0.15), (s * 0.15, s * 0.8), (s * 0.85, s * 0.8)], fill=(250, 250, 250))
    elif k == 4:    # big checkerboard
        for i in range(4):
            for j in range(4):
                d.rectangle([i * s // 4, j * s // 4, (i + 1) * s // 4, (j + 1) * s // 4], fill=(20, 20, 20) if (i + j) % 2 == 0 else (235, 235, 235))
        d.ellipse([s * 0.4, s * 0.4, s * 0.6, s * 0.6], fill=(220, 60, 60))
    elif k == 5:    # concentric rectangles
        for i, c in enumerate([(250, 200, 40), (40, 40, 140), (230, 230, 230), (190, 40, 40), (20, 20, 20)]):
            m = int(i * s * 0.09)
            d.rectangle([m, m, s - m, s - m], fill=c)
    else:           # a big X on a dark background
        d.rectangle([0, 0, s, s], fill=(25, 25, 60))
        d.line([0, 0, s, s], fill=(240, 240, 80), width=60); d.line([0, s, s, 0], fill=(240, 120, 80), width=60)
    return im


def unrelated(r):
    im = Image.new("RGB", (SIZE, SIZE), tuple(int(x) for x in r.integers(30, 230, 3)))
    d = ImageDraw.Draw(im)
    for _ in range(int(r.integers(3, 7))):
        x0, y0 = r.integers(0, SIZE - 60, 2); w, h = r.integers(40, 200, 2)
        col = tuple(int(x) for x in r.integers(0, 255, 3))
        if r.random() < 0.5:
            d.rectangle([x0, y0, x0 + w, y0 + h], fill=col)
        else:
            d.ellipse([x0, y0, x0 + w, y0 + h], fill=col)
    return im


def add_caption(im, text, pos):
    d = ImageDraw.Draw(im)
    f = _font(int(im.width * 0.07))
    w = d.textlength(text, font=f)
    x = (im.width - w) / 2
    y = im.height * (0.03 if pos == "top" else 0.88)
    for dx in (-2, 0, 2):
        for dy in (-2, 0, 2):
            d.text((x + dx, y + dy), text, font=f, fill="black")
    d.text((x, y), text, font=f, fill="white")
    return im


def variant(base, r):
    im = base.copy()
    im = add_caption(im, CAPTIONS[int(r.integers(len(CAPTIONS)))], "top" if r.random() < 0.5 else "bottom")
    c = r.uniform(0, 0.12)                                  # crop up to 12% from each side
    w, h = im.size
    box = (int(w * r.uniform(0, c)), int(h * r.uniform(0, c)), int(w * (1 - r.uniform(0, c))), int(h * (1 - r.uniform(0, c))))
    im = im.crop(box)
    s = int(r.integers(300, 451))
    im = im.resize((s, int(s * r.uniform(0.9, 1.1))))
    im = ImageEnhance.Brightness(im).enhance(r.uniform(0.8, 1.2))
    a = np.asarray(im).astype(float) + r.normal(0, 6, (im.height, im.width, 3))
    return Image.fromarray(np.clip(a, 0, 255).astype("uint8"))


def jpeg_bytes(im, q):
    b = io.BytesIO()
    im.save(b, format="JPEG", quality=int(q))
    return b.getvalue()


def build(seed=SEED):
    r = np.random.default_rng(seed)
    files = []   # (bytes, template, kind)
    for k in range(1, 7):
        base = template(k)
        for _ in range(28):
            files.append((jpeg_bytes(variant(base, r), r.integers(45, 91)), f"T{k}", "variant"))
    t1 = [i for i, f in enumerate(files) if f[1] == "T1"]
    originals = [t1[3], t1[17]]
    for src in originals:
        for _ in range(6):
            files.append((files[src][0], "T1", "repost"))
    for _ in range(40):
        files.append((jpeg_bytes(unrelated(r), r.integers(45, 91)), "none", "unrelated"))
    order = r.permutation(len(files))
    names = [f"img_{i + 1:03d}.jpg" for i in range(len(files))]
    rows, truth, blobs = [], [], {}
    accounts = [f"acct_{i:03d}" for i in r.permutation(150) + 1]
    repost_accts = {originals[0]: accounts[:6], originals[1]: accounts[6:12]}
    rep_ix = {0: 0, 1: 0}
    for new_i, old_i in enumerate(order):
        b, tmpl, kind = files[old_i]
        name = names[new_i]
        blobs[name] = b
        acct = accounts[(new_i + 12) % len(accounts)]
        if kind == "repost":
            n_rep = old_i - 168
            grp = 0 if n_rep < 6 else 1
            acct = repost_accts[originals[grp]][n_rep % 6]
        rows.append((name, acct))
        truth.append((name, tmpl, kind))
    return blobs, pd.DataFrame(rows, columns=["file", "account"]), pd.DataFrame(truth, columns=["file", "template", "kind"])


if __name__ == "__main__":
    blobs, manifest, truth = build()
    with zipfile.ZipFile(os.path.join(DATA, "week07_memes.zip"), "w", zipfile.ZIP_DEFLATED) as z:
        for name, b in blobs.items():
            z.writestr("memes/" + name, b)
    manifest.sort_values("file").to_csv(os.path.join(DATA, "week07_memes.csv"), index=False)
    truth.sort_values("file").to_csv(os.path.join(DATA, "week07_memes_truth.csv"), index=False)
    print("wrote week07_memes.zip", len(blobs), "images,", round(os.path.getsize(os.path.join(DATA, "week07_memes.zip")) / 1e6, 2), "MB")
