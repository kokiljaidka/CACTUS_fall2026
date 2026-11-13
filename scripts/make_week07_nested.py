"""Simulate the Week 7 shared-core datasets: comments nested inside posts.

Story (made up): some posts carry an "AI-generated" label. We look at the comments
under 80 posts. All names, numbers and posts are invented.

  data/week07_comments.csv   a sample of comments (about 3,000) from the 80 posts
      post_id        which post the comment is under
      labeled        1 if the POST carries the label (a post-level variable)
      long_comment   1 if the comment is long (a comment-level variable)
      warmth         how warm the comment is, roughly 0 to 10
  data/week07_posts.csv      one row per post
      post_id, labeled, followers (the post author's audience), comments_total
      (all comments the post received; `comments_total` is the count outcome and
      `followers` is the exposure)

KNOWN ANSWERS (planted)
  warmth:  true effect of the post label = -0.5 points; of a long comment = +0.4.
           Posts differ a lot from each other (post-level sd 1.5, comment-level sd 2.0),
           so comments under one post are alike.
  counts:  comments_total ~ followers x rate. The true rate under a label is 0.8 times
           the rate without one (a 20% drop per follower). But labeled posts come from
           bigger accounts (about 2.5 times the followers), so raw counts are HIGHER
           under a label while the rate is LOWER.

Seeds are fixed so the files can be rebuilt exactly and chosen so that the one dataset
shows the lessons (see instructor/week07_answer_key.md).

Run: python scripts/make_week07_nested.py
"""
import os

import numpy as np
import pandas as pd

TRUE_LABEL = -0.5
TRUE_LONG = 0.4
POST_SD = 1.5
COMMENT_SD = 2.0
RATE_RATIO = 0.8
BASE_RATE = 0.004          # comments per follower for an unlabeled post
N_POSTS = 80
SEED = 7

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")


def simulate_posts(seed=SEED, n_posts=N_POSTS):
    r = np.random.default_rng(seed)
    labeled = np.zeros(n_posts, int)
    labeled[r.choice(n_posts, n_posts // 2, replace=False)] = 1
    followers = np.where(labeled == 1,
                         np.exp(r.normal(np.log(5000), 0.7, n_posts)),
                         np.exp(r.normal(np.log(2000), 0.7, n_posts))).round().astype(int)
    followers = np.maximum(followers, 200)
    mean = followers * BASE_RATE * np.where(labeled == 1, RATE_RATIO, 1.0)
    shape = 8.0   # some extra post-to-post variation (overdispersion)
    lam = r.gamma(shape, mean / shape)
    comments_total = r.poisson(lam)
    posts = pd.DataFrame({
        "post_id": [f"p{i + 1:03d}" for i in range(n_posts)],
        "labeled": labeled,
        "followers": followers,
        "comments_total": comments_total,
    })
    return posts, r


def simulate_comments(posts, r):
    rows = []
    post_effect = r.normal(0, POST_SD, len(posts))
    sizes = r.integers(25, 51, len(posts))
    for i, p in posts.iterrows():
        m = sizes[i]
        long_c = r.integers(0, 2, m)
        y = 5 + TRUE_LABEL * p.labeled + post_effect[i] + TRUE_LONG * long_c + r.normal(0, COMMENT_SD, m)
        for k in range(m):
            rows.append((p.post_id, int(p.labeled), int(long_c[k]), round(float(y[k]), 2)))
    c = pd.DataFrame(rows, columns=["post_id", "labeled", "long_comment", "warmth"])
    c.insert(0, "comment_id", [f"c{i + 1:05d}" for i in range(len(c))])
    return c


def build(seed=SEED):
    posts, r = simulate_posts(seed)
    comments = simulate_comments(posts, r)
    return posts, comments


if __name__ == "__main__":
    posts, comments = build()
    posts.to_csv(os.path.join(DATA, "week07_posts.csv"), index=False)
    comments.to_csv(os.path.join(DATA, "week07_comments.csv"), index=False)
    print("wrote week07_posts.csv", posts.shape, "and week07_comments.csv", comments.shape)
