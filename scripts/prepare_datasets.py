"""Turn the raw Excel export into student-safe CSVs.

Run with a Python that has pandas and openpyxl:
    python3 scripts/prepare_datasets.py

Reads  data/raw/lululemon_starbucks_2024.xlsx   (local only, not committed)
Writes data/starbucks_sea_comments.csv
       data/lululemon_instagram.csv

Privacy steps: usernames and account names become sequential IDs, and links
(post, channel, profile, photo) are dropped. Comment text is left as is, so it
can still contain @handles written by users. See data/README.md.
"""
import os

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
RAW = os.path.join(DATA, "raw", "lululemon_starbucks_2024.xlsx")


def sequential_ids(series, prefix):
    """Map each distinct value to prefix_0001, prefix_0002... in order of first appearance."""
    codes, _ = pd.factorize(series)
    return pd.Series([f"{prefix}_{c + 1:04d}" for c in codes], index=series.index)


sheets = pd.read_excel(RAW, sheet_name=None)

# Starbucks comments. The sheet "Copy of starbucks" is a near-duplicate and is not used.
s = sheets["starbucks"].copy()
s["voice_id"] = sequential_ids(s["Voice Name"], "voice")
s = s.drop(columns=["URL", "Channel URL", "Voice Name", "Voice URL"])
s.to_csv(os.path.join(DATA, "starbucks_sea_comments.csv"), index=False, encoding="utf-8-sig")
print("starbucks_sea_comments.csv", s.shape)

# Lululemon Instagram posts.
l = sheets["Lululemon"].copy()
l.insert(0, "account_id", sequential_ids(l["Account"], "account"))
l = l.drop(columns=["Account", "User Name", "URL", "Link", "Photo"])
l.to_csv(os.path.join(DATA, "lululemon_instagram.csv"), index=False, encoding="utf-8-sig")
print("lululemon_instagram.csv", l.shape)
