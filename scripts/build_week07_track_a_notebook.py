"""Build notebooks/week07_track_a_networks.ipynb (Week 7, Session 2, Track A: networks).

Data from scripts/make_week07_network.py (invented, with planted answers). Re-run after editing.
"""
import os

import nbformat as nbf

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "notebooks", "week07_track_a_networks.ipynb")
cells = []


def md(t):
    cells.append(nbf.v4.new_markdown_cell(t.strip()))


def code(t):
    cells.append(nbf.v4.new_code_cell(t.strip()))


md("""
# Week 7, Session 2, Track A: networks

**CACTUS Fall 2026 · Coding session (Track A)**

**The story (made up):** 300 accounts in a discussion over 30 days. Each row of the edge list is one **reply** or **mention** from a `source` account to a `target` account. We planted: **two communities of people** who mostly talk within their own community, **one hub** that many different accounts reply to, and **a few automated accounts (bots)**. We also planted a pair of people who reply to each other again and again. Because we know this, we can check what the usual network methods find.

**Goals today**
- build a network from an edge list, and say what a node and an edge are
- measure who gets the most replies, and who sends the most
- find communities, and check them against the planted ones
- check whether the structure is more than chance, with shuffled networks
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

import networkx as nx
import numpy as np
import pandas as pd
from sklearn.metrics import adjusted_rand_score

BASE = "https://raw.githubusercontent.com/kokiljaidka/CACTUS_fall2026/main/data/"


def load(name):
    # use a local copy if you have one, otherwise read the file from the course repository
    return pd.read_csv(name) if os.path.exists(name) else pd.read_csv(BASE + name)


edges = load("week07_edges.csv")        # who replied to or mentioned whom
print(edges.shape)
edges.head()
""")

md("""
---
## Warm-up: plant two communities and see whether the method finds them (about 15 min)

Here you build a small network yourself, so you know the communities. Accounts in the same community link with probability `p_in`, accounts in different communities with probability `p_out`. Then a community-finding method (greedy modularity) tries to recover them. We score it with the **adjusted Rand index** (ARI): 1 means the same grouping, 0 means no better than chance.

**Predict:** with 40 accounts per community, `p_in = 0.3` and `p_out = 0.05`, will the method recover the communities? What if `p_out` is 0.15?

> My prediction:
""")

code("""
def simulate(n_each, p_in, p_out, seed=None):
    G = nx.stochastic_block_model([n_each, n_each], [[p_in, p_out], [p_out, p_in]], seed=seed)
    truth = [0] * n_each + [1] * n_each
    return G, truth


def recovered(G, truth):
    comms = nx.community.greedy_modularity_communities(G)
    label = {n: i for i, c in enumerate(comms) for n in c}
    return adjusted_rand_score(truth, [label[n] for n in range(len(truth))])


MY_P_IN = 0.3         # change me
MY_P_OUT = 0.05       # change me

scores = []
for seed in range(50):
    G, truth = simulate(40, MY_P_IN, MY_P_OUT, seed)
    scores.append(recovered(G, truth))
scores = np.array(scores)
print(f"Average ARI over 50 networks: {scores.mean():.2f}.   Networks with ARI of at least 0.8: {(scores >= 0.8).sum()} of 50")
if MY_P_OUT <= MY_P_IN / 4:
    assert scores.mean() > 0.6, "With few links between communities the method should usually find them. Check the code."
""")

md("""
**Discuss with your partner:** raise `MY_P_OUT` towards `MY_P_IN`. What happens to the score, and why? What does that say about a real network where communities overlap a lot?

> Log (warm-up): one thing you predicted, what happened, and the check you used.
""")

md("""
---
## Exercise 1: Build the network and measure it (required, about 30 min)

Data: `edges`, 3,647 rows. Columns: `source`, `target`, `type` (reply or mention), `day`.

**Predict first:** how many different accounts are in the data? Will the number of rows equal the number of edges in the network? Which accounts will have the most **different** accounts replying to or mentioning them? Which will send the most?

> My prediction:

**How to prompt well.** Give the AI the context it cannot see:

> I have a pandas DataFrame called `edges` with columns: *(paste `list(edges.columns)`)*. Each row is a reply or mention from `source` to `target`. **Task:** ... Use networkx. Write the code, then explain each line in one sentence.

| Task | What to ask for | How to check it |
|---|---|---|
| **1a** | How many rows, how many different sources and targets, how many different accounts overall, and rows per `type` | Do the numbers add up? |
| **1b** | A **directed** graph `G` from the edge list (`source` to `target`) | The check cell |
| **1c** | For every account, the number of **different** accounts that replied to or mentioned it (`in_deg`) and the number it replied to or mentioned (`out_deg`), as pandas Series. Store the account with the highest `in_deg` in `top_in`, and the six accounts with the highest `out_deg` in `top_out` (a list) | The check cell |
| **1d** | An undirected copy `U = G.to_undirected()`, and communities with `comms = nx.community.greedy_modularity_communities(U)`. Print how many communities and how big | Do the sizes add up to the number of accounts? |
""")

code("""
# Task 1a:
""")
code("""
# Task 1b: the directed graph G.
""")
code("""
# Task 1c: in_deg, out_deg, top_in and top_out.
""")
code("""
# Task 1d: U and comms.
""")

code("""
# Check 1.
pairs = edges[["source", "target"]].drop_duplicates().shape[0]
assert G.is_directed(), "G should be a directed graph (nx.DiGraph)."
assert G.number_of_nodes() == len(set(edges["source"]) | set(edges["target"])), "G should have one node per account."
assert G.number_of_edges() == pairs, f"G should have one edge per different pair ({pairs}); repeated rows between the same two accounts count once. You have {G.number_of_edges()}."
assert in_deg.loc[top_in] == in_deg.max() and len(top_out) == 6, "top_in is the account with the highest in_deg; top_out has six accounts."
assert sum(len(c) for c in comms) == G.number_of_nodes(), "Every account should be in exactly one community."
print(f"{G.number_of_nodes()} accounts, {G.number_of_edges()} edges from {len(edges)} rows")
print(f"top in: {top_in} ({in_deg.max()} different accounts)")
print(f"top out: {top_out} ({out_deg.loc[top_out].min()} to {out_deg.loc[top_out].max()} different accounts)")
print("community sizes:", sorted((len(c) for c in comms), reverse=True))
""")

md("""
**Think:** why do 3,647 rows give fewer edges? What would you lose if you counted rows instead of different accounts?

> Log (Exercise 1): what did the AI get wrong, or what check did you run? Did you reject any code, and why?
""")

md("""
---
## Exercise 2: Check against the known answer, and shuffle the network (required, about 25 min)

Now compare with what we planted. `accounts` lists every account's **true** kind (person or bot) and community. In a real project you would not have this file. Here it is the known answer.

**Predict:** will the six highest-sending accounts be people or bots? Will the account with the most repliers be a person? How many communities did the method find, compared with the two we planted?

> My prediction:
""")

code("""
accounts = load("week07_accounts.csv").set_index("account")


def ari_people(comms):
    # how well do these communities match the planted ones, for people only (bots have no community)?
    label = {n: i for i, c in enumerate(comms) for n in c}
    people = [n for n in label if accounts.loc[n, "kind"] == "person"]
    return adjusted_rand_score([accounts.loc[n, "community"] for n in people], [label[n] for n in people])
""")

md("""
| Task | What to ask for | How to check it |
|---|---|---|
| **2a** | What kind (person or bot) are the accounts in `top_out`? How many are bots? Store the number in `n_bots_in_top_out`. What kind is `top_in`? | The check cell |
| **2b** | Score your `comms` with `ari_people(comms)` and store it in `ari_with_bots`. Which community is small, and who is in it? Then drop the six `top_out` accounts from `U`, find communities again (`comms_clean`), and store the score in `ari_clean`. Which score is better? | The check cell |
| **2c** | Is the community structure more than chance? Ask an AI for a **degree-preserving shuffle** check (`nx.double_edge_swap`): shuffle the cleaned network 20 times, find communities in each, and compare modularity. Store the real modularity in `obs_mod` and the 20 shuffled ones in `shuffled_mods` | The check cell |
| **2d** | Two sentences: what do the communities show, and what would you not claim? | Say it to your partner |

Tip for 2c: the shuffled networks keep every account's number of connections but randomize who is linked to whom. `nx.community.modularity(H, communities)` measures how community-like a split is.
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
assert accounts.loc[top_out, "kind"].eq("bot").sum() == n_bots_in_top_out, "Count the bots among the top_out accounts."
assert 0 <= ari_with_bots <= 1 and 0 <= ari_clean <= 1, "ARI should be between 0 and 1."
assert len(shuffled_mods) == 20, "Run 20 shuffles."
assert obs_mod > max(shuffled_mods), "The real network should have more community structure than shuffled ones. Did you compute modularity on the cleaned network, with its own communities?"
print(f"bots among the six top senders: {n_bots_in_top_out}; kind of top_in: {accounts.loc[top_in, 'kind']}, is_hub: {accounts.loc[top_in, 'is_hub']}")
print(f"match with planted communities: with bots {ari_with_bots:.2f}, bots removed {ari_clean:.2f}")
print(f"modularity: real {obs_mod:.2f}, shuffled {np.mean(shuffled_mods):.2f} on average (highest {max(shuffled_mods):.2f})")
""")

md("""
> Task 2d, my sentences:
>
> Log (Exercise 2): in your own work, how would you find the bots? What would you check before calling an account a bot?
""")

md("""
---
## Exercise 3: Bug hunt (required, about 25 min)

Below is an analysis an AI assistant wrote for someone else. It runs without errors and prints two results. **It contains three mistakes that change the answer.** Find them without being told where they are.

**What to do**
1. Run the cell and read the results. You know what was planted.
2. Read each numbered step. What does each line do?
3. For each suspected bug, **prove it** with a check. Write down the check.
4. Fix the code. Put the account that **the most different accounts replied to** in `top_replied`, and the agreement between the found and planted communities (for people) in `comm_agreement`.

**Checks that work here**
- Compare with the **known answer** and with your own results from Exercises 1 and 2.
- Look at **which account** is returned, and what kind it is.
- Ask what each number is a **count of**: rows, edges, or different accounts?

**Hints.** If you are stuck for more than 5 minutes, ask a facilitator.
""")

code("""
# ---- AI-written analysis. Do not edit this cell; copy it to a new one to fix. ----
# 1. Who gets the most replies?
replies = edges[edges["type"] == "reply"]
received = replies.groupby("source").size()
most_replied = received.idxmax()
print("Most replied-to account:", most_replied, "with", received.max(), "replies")

# 2. Do the communities match the planted ones?
U2 = nx.from_pandas_edgelist(edges, "source", "target")
comms2 = nx.community.greedy_modularity_communities(U2)
comms2 = sorted(comms2, key=len)          # smallest community first
label2 = {n: i for i, c in enumerate(comms2) for n in c}
people = [n for n in label2 if accounts.loc[n, "kind"] == "person"]
true_comm = [int(accounts.loc[n, "community"]) - 1 for n in people]
pred_comm = [label2[n] for n in people]
accuracy = np.mean(np.array(true_comm) == np.array(pred_comm))
print(f"Share of people in the right community: {accuracy:.2f}")
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
# Your fixed version here. It must create top_replied and comm_agreement.
""")

code("""
# Check 3.
assert accounts.loc[top_replied, "kind"] == "person", f"{top_replied} is not a person. Who replies, and who is replied to?"
assert accounts.loc[top_replied, "is_hub"] == 1, f"{top_replied} is a person, but it is not the account the most different accounts replied to. Count different accounts, not rows, and check the direction."
assert comm_agreement >= 0.75, f"The found communities should match the planted ones well for people. You have {comm_agreement:.2f}. Community numbers are arbitrary: how do you compare two groupings?"
print("Both numbers now match what was planted.")
""")

md("""
> Log (Exercise 3): which bug was hardest to find? Which check would you use first next time?
""")

md("""
---
## Exercise 4: Your own data (about 15 min; can be homework)

Think of the network in your project: replies, mentions, retweets, shared hashtags, follows. If you have no network yet, think of the one you would most like to study.

**Write down before you run anything:**

| Question | My answer |
|---|---|
| What is a node (an account, a hashtag, a page)? What is an edge (a reply, a mention, a retweet)? | |
| Is the edge directed, and does direction matter for your question? | |
| Can the same pair appear many times? Do you count rows, or different accounts? | |
| Could some accounts be automated, or one organization with many accounts? | |
| How did the data get collected? Does your search query decide which edges you see? | |
| What would you check first, and what would you shuffle to test chance? | |

**Then, if you have a small sample of your own edge list** (de-identified), load it and build a graph, and say how many nodes and edges it has. If you have none, use `edges` and build a graph from only the `mention` rows.
""")

code("""
# Exercise 4: your own edge list, or the mention rows of edges. Build a graph and count nodes and edges.
""")

md("""
---
## Log: what I learned today

- One check that told me my code was right or wrong:
- One thing the AI got wrong, or one claim I would not accept:
- One question I still have:

**Homework (45 minutes or less):** finish Exercise 4. Build a graph from your own data (or a sample), count different accounts rather than rows, and run one known-answer check. In one paragraph: what does your method assume, and one way your data may break it (include bots, repeats and how the data were collected).
""")

nb = nbf.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
nbf.write(nb, OUT)
print("wrote", os.path.normpath(OUT))
