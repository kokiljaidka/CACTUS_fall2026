"""Simulate the Week 7 Track A dataset: a reply and mention network. All invented.

Story (made up): 300 accounts in a discussion of a (made-up) topic over 30 days.

  data/week07_edges.csv     one row per reply or mention: source, target, type, day
  data/week07_accounts.csv  the planted truth: account, kind (person or bot), community (1, 2, or none for bots), is_hub

KNOWN ANSWERS (planted)
  - 294 people in two communities of 147. People reply to people in their own community
    much more often than to the other community.
  - One hub account (in community 1) is replied to by 90 different accounts, 60 from its own
    community and 30 from the other.
  - 6 bots each mention about 110 different accounts, from both communities. They have very high
    out-degree (high total degree) but are not people, and they blur the communities.
  - One "chatty pair" (two people in community 2) reply to each other 120 times each. They have
    many rows in the edge list but few different people.

Account ids are shuffled so an id does not give away its community.
Seeds are fixed. See instructor/week07_answer_key.md.

Run: python scripts/make_week07_network.py
"""
import os

import numpy as np
import pandas as pd

SEED = 17
N_PER = 147
N_BOTS = 6
P_IN = 0.05
P_OUT = 0.012
HUB_IN, HUB_OUT = 60, 30
BOT_TARGETS = 110
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")


def build(seed=SEED):
    r = np.random.default_rng(seed)
    n = 2 * N_PER + N_BOTS
    ids = [f"u{i:03d}" for i in r.permutation(n) + 1]
    comm = np.array([1] * N_PER + [2] * N_PER + [0] * N_BOTS)   # 0 = bot
    ppl = np.arange(2 * N_PER)
    rows = []
    for a in ppl:
        for b in ppl:
            if a == b:
                continue
            p = P_IN if comm[a] == comm[b] else P_OUT
            if r.random() < p:
                rows.append((a, b, "mention" if r.random() < 0.2 else "reply"))
    hub = 0
    chatty = (N_PER + 1, N_PER + 2)
    have = {(a, b) for a, b, _ in rows}
    sources_in = r.choice([i for i in range(1, N_PER)], HUB_IN, replace=False)
    sources_out = r.choice(np.arange(N_PER, 2 * N_PER), HUB_OUT, replace=False)
    for s in list(sources_in) + list(sources_out):
        if (s, hub) not in have:
            rows.append((s, hub, "reply"))
            have.add((s, hub))
    for s in range(1, 8):                     # the hub replies back to a few
        rows.append((hub, s, "reply"))
    for _ in range(120):
        rows.append((chatty[0], chatty[1], "reply"))
        rows.append((chatty[1], chatty[0], "reply"))
    for k in range(N_BOTS):
        bot = 2 * N_PER + k
        for t in r.choice(ppl, BOT_TARGETS, replace=False):
            rows.append((bot, t, "mention"))
    e = pd.DataFrame(rows, columns=["s", "t", "type"])
    e["source"] = [ids[i] for i in e.s]
    e["target"] = [ids[i] for i in e.t]
    e["day"] = r.integers(1, 31, len(e))
    e = e[["source", "target", "type", "day"]].sample(frac=1, random_state=seed).reset_index(drop=True)
    acc = pd.DataFrame({
        "account": ids,
        "kind": np.where(comm == 0, "bot", "person"),
        "community": np.where(comm == 0, "", comm.astype(str)),
        "is_hub": [int(i == hub) for i in range(n)],
    }).sort_values("account").reset_index(drop=True)
    return e, acc, ids[hub], [ids[chatty[0]], ids[chatty[1]]]


if __name__ == "__main__":
    e, acc, hub, chatty = build()
    e.to_csv(os.path.join(DATA, "week07_edges.csv"), index=False)
    acc.to_csv(os.path.join(DATA, "week07_accounts.csv"), index=False)
    print("wrote week07_edges.csv", e.shape, "and week07_accounts.csv", acc.shape, "hub", hub, "chatty", chatty)
