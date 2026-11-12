"""Simulate the Week 3 datasets, with a known true effect.

Story (made up): a platform shows an "AI-generated" label on some posts. The
outcome is `sharing_intent`, how likely a person says they are to share a post, on
roughly a 0 to 10 scale. The TRUE effect of seeing the label is -0.6 points.

  data/week03_experiment.csv  randomized: who sees the label is decided by chance,
                              so a simple comparison recovers the true effect (up to noise)
  data/week03_survey.csv      observational: heavy AI users are more likely to see the
                              label AND share more, so the naive comparison is biased.
                              Adjusting for `prior_ai_use` recovers the true effect.

Seeds are fixed so the files can be rebuilt exactly. They were chosen so that the one
experiment lands noticeably off the truth, which makes the point that a single
estimate is not the truth. See instructor/week03_answer_key.md.

Run: python scripts/make_week03_data.py
"""
import os

import numpy as np
import pandas as pd

TRUE_EFFECT = -0.6
NOISE_SD = 2.0
EXPERIMENT_SEED = 45
SURVEY_SEED = 5
REGIONS = ["SG", "HK", "TW"]
REGION_P = [0.5, 0.3, 0.2]          # uneven group sizes on purpose
AGES = ["18-24", "25-34", "35+"]

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")


def _extras(seed, n):
    r = np.random.default_rng([seed, 1])  # separate stream so the outcome numbers do not change
    return r.choice(REGIONS, n, p=REGION_P), r.choice(AGES, n)


def experiment(seed=EXPERIMENT_SEED, n=300):
    r = np.random.default_rng(seed)
    prior = r.integers(1, 6, n)
    label = r.integers(0, 2, n)
    y = 5 + 0.5 * (prior - 3) + TRUE_EFFECT * label + r.normal(0, NOISE_SD, n)
    region, age = _extras(seed, n)
    return pd.DataFrame({
        "id": [f"e{i + 1:04d}" for i in range(n)],
        "group": np.where(label == 1, "label", "control"),
        "prior_ai_use": prior,
        "region": region,
        "age_group": age,
        "sharing_intent": y.round(2),
    })


def survey(seed=SURVEY_SEED, n=800):
    r = np.random.default_rng(seed)
    prior = r.integers(1, 6, n)
    p_seen = 1 / (1 + np.exp(-(-0.2 + 1.0 * (prior - 3))))
    seen = (r.random(n) < p_seen).astype(int)
    y = 5 + 0.9 * (prior - 3) + TRUE_EFFECT * seen + r.normal(0, NOISE_SD, n)
    region, age = _extras(seed, n)
    return pd.DataFrame({
        "id": [f"s{i + 1:04d}" for i in range(n)],
        "seen_label": seen,
        "prior_ai_use": prior,
        "region": region,
        "age_group": age,
        "sharing_intent": y.round(2),
    })


if __name__ == "__main__":
    e, s = experiment(), survey()
    e.to_csv(os.path.join(DATA, "week03_experiment.csv"), index=False)
    s.to_csv(os.path.join(DATA, "week03_survey.csv"), index=False)
    print("wrote data/week03_experiment.csv", e.shape, "and data/week03_survey.csv", s.shape)
