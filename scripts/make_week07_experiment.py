"""Simulate the Week 7 Track C dataset: a mock-feed experiment. All invented.

Story (made up): people in 12 sessions each saw one mock social media post. The post
came from either a news outlet or an anonymous account (`source`), and carried an
"AI-generated" label or not (`label`). Both were assigned by chance to each person.
The outcome is `credibility`: how credible they rated the post, 1 to 7. After the post,
people were asked whether they noticed an AI label (`noticed_label`, the
manipulation check).

  data/week07_experiment.csv
      pid, session, device (desktop or mobile), source, label, noticed_label,
      credibility, age_group

KNOWN ANSWERS (planted)
  - Anonymous accounts are rated lower by 0.8 points overall.
  - A label lowers credibility only for people who NOTICED it, and the effect depends
    on the source: -0.2 for the news outlet, -1.0 for the anonymous account. So there
    is a real interaction (the label matters most for anonymous accounts).
  - The manipulation FAILED on mobile: on desktop 90% of people in the label arm
    noticed it, on mobile only 35%. (A few people in the control arm say they noticed
    one, about 5%.)
  - Noticing is not random: people who are more skeptical (a trait that is not in the
    data) both notice more and rate lower. So dropping people who failed the manipulation
    check, after seeing the result, makes the label look stronger than it is.
  - Sessions differ a little (a session-level bump, sd 0.4).

Run: python scripts/make_week07_experiment.py
"""
import os

import numpy as np
import pandas as pd

SEED = 2
N_SESSIONS = 12
PER_SESSION = 50
EFFECT_OUTLET = -0.2
EFFECT_ANON = -1.0
ANON_MAIN = -0.8
NOTICE_DESKTOP = 0.9
NOTICE_MOBILE = 0.35
NOTICE_CONTROL = 0.05
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")


def _logit(p):
    return np.log(p / (1 - p))


def _expit(x):
    return 1 / (1 + np.exp(-x))


def build(seed=SEED):
    r = np.random.default_rng(seed)
    n = N_SESSIONS * PER_SESSION
    session_ix = np.repeat(np.arange(N_SESSIONS), PER_SESSION)
    bump = r.normal(0, 0.4, N_SESSIONS)[session_ix]
    device = np.where(r.random(n) < 0.4, "mobile", "desktop")
    anon = r.integers(0, 2, n)
    label = r.integers(0, 2, n)
    z = r.normal(0, 1, n)                              # skepticism (not in the data)
    base = np.where(device == "mobile", NOTICE_MOBILE, NOTICE_DESKTOP)
    p_notice = np.where(label == 1, _expit(_logit(base) + 1.5 * z), NOTICE_CONTROL)
    noticed = (r.random(n) < p_notice).astype(int)
    effect = np.where(anon == 1, EFFECT_ANON, EFFECT_OUTLET)
    y = 4.6 + bump + ANON_MAIN * anon - 1.0 * z + (label * noticed) * effect + r.normal(0, 1.0, n)
    y = np.clip(y, 1, 7).round(1)
    age = r.choice(["18-24", "25-34", "35+"], n, p=[0.5, 0.35, 0.15])
    return pd.DataFrame({
        "pid": [f"u{i + 1:04d}" for i in range(n)],
        "session": [f"S{s + 1:02d}" for s in session_ix],
        "device": device,
        "source": np.where(anon == 1, "anonymous", "outlet"),
        "label": np.where(label == 1, "ai_label", "none"),
        "noticed_label": noticed,
        "credibility": y,
        "age_group": age,
    })


if __name__ == "__main__":
    d = build()
    d.to_csv(os.path.join(DATA, "week07_experiment.csv"), index=False)
    print("wrote data/week07_experiment.csv", d.shape)
