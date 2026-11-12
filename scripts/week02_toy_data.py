"""Toy table for the Week 2 practice page and the Week 2 notebook warm-up.

An invented cafe ("Brew Lane"), 30 rows with planted problems:
  - 3 exact duplicate rows (c03, c08, c14 appear twice)
  - 2 rows with no comment text (c26, c27)
  - 2 dates in another format (13/10/2024 style) (c10, c19)
  - tone_pos stored as text, with 'unknown', '-' and one empty cell (c04, c11, c18, c23)
A clean pipeline (drop duplicates, drop rows with no comment, parse dates, convert
tone_pos to numbers) leaves 25 rows.

Run this file to write data/week02_toy_cafe.csv. build_practice.py and
build_week02_notebook.py import it, so the page, the notebook and the CSV agree.
"""
import csv
import io
import os

COLUMNS = ["id", "date", "comment", "country", "tone_pos"]

ROWS = [
    ("c01", "2024-10-05", "Love the new oat latte", "SG", "6.2"),
    ("c02", "2024-10-05", "Queue was too long today", "SG", "0.0"),
    ("c03", "2024-10-06", "Best iced coffee near the MRT", "SG", "8.3"),
    ("c04", "2024-10-06", "Prices went up again", "SG", "unknown"),
    ("c05", "2024-10-07", "Friendly staff at Orchard", "SG", "5.0"),
    ("c06", "2024-10-07", "Wifi keeps dropping", "SG", "0.0"),
    ("c07", "2024-10-07", "ร้านนี้กาแฟอร่อยมาก", "TH", "7.1"),
    ("c08", "2024-10-08", "Seasonal menu is great", "TH", "5.6"),
    ("c03", "2024-10-06", "Best iced coffee near the MRT", "SG", "8.3"),
    ("c09", "2024-10-08", "Too sweet for me", "TH", "0.0"),
    ("c10", "13/10/2024", "Cup design is so cute", "TH", "9.1"),
    ("c11", "2024-10-09", "Loyalty app is confusing", "TH", "-"),
    ("c12", "2024-10-09", "Cold brew sold out again", "TH", "0.0"),
    ("c13", "2024-10-09", "Nice quiet place to work", "TH", "6.4"),
    ("c14", "2024-10-10", "Staff remembered my order", "HK", "8.0"),
    ("c15", "2024-10-10", "好耐冇嚟，味道依然好", "HK", "5.5"),
    ("c08", "2024-10-08", "Seasonal menu is great", "TH", "5.6"),
    ("c16", "2024-10-10", "Pastries were stale", "HK", "0.0"),
    ("c17", "2024-10-11", "Great value lunch set", "HK", "7.7"),
    ("c18", "2024-10-11", "Seats are always taken", "HK", "unknown"),
    ("c19", "12/10/2024", "Pumpkin latte is back!", "SG", "7.9"),
    ("c20", "2024-10-12", "Mobile order took 20 minutes", "SG", "0.0"),
    ("c21", "2024-10-12", "Barista art was lovely", "TH", "8.8"),
    ("c22", "2024-10-12", "Not enough plug sockets", "TH", "0.0"),
    ("c23", "2024-10-13", "Free refill promo is good", "SG", ""),
    ("c24", "2024-10-13", "Cozy corner seats", "HK", "6.0"),
    ("c25", "2024-10-13", "Rainy day, warm mocha", "TH", "7.0"),
    ("c26", "2024-10-14", "", "SG", "0.0"),
    ("c27", "2024-10-14", "", "TH", "4.5"),
    ("c14", "2024-10-10", "Staff remembered my order", "HK", "8.0"),
]
assert len(ROWS) == 30


def as_records():
    return [dict(zip(COLUMNS, r)) for r in ROWS]


def to_csv_text():
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(COLUMNS)
    w.writerows(ROWS)
    return buf.getvalue()


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "week02_toy_cafe.csv")
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(to_csv_text())
    print("wrote", os.path.normpath(out))
