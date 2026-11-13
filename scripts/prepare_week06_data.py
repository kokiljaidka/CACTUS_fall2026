"""Prepare the Week 6 data from the CLAPTON validation file (human-labeled Twitter and Reddit messages).

Usage:
    python scripts/prepare_week06_data.py --val "<path to CLAPTON-main/delib_data/val.csv>"

Writes (gitignored, shared with the class through the class drive, see data/private/README_week06_data.txt):
    data/private/week06_clapton_val.csv        649 messages: row_id, source, orig_message_id, message, six human labels
    data/private/week06_eval_sample.csv        the 150-message sample (row_id, message only: NO human labels), for labeling by an LLM
    data/private/week06_corpus.zip             val + LLM labels (if data/private/week06_llm_labels.csv exists) + handling notes

The sample is fixed (random_state=6) so everyone evaluates the same 150 messages.
Clean-up done here: URLs are replaced with "URL"; leftover encoding junk (<U+FFFD>) is removed; the original message ids are kept (they are NOT unique: four ids repeat,
which is a real-data trap the notebook uses).
"""
import argparse
import os
import re
import zipfile

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "data", "private")
RENAME = {"Constructiveness": "constructive", "Justification": "justification", "Relevance": "relevance",
          "Reciprocity": "reciprocity", "Empathy_Respect": "empathy_respect", "Uncivil_abuse": "uncivil_abuse",
          "dataset": "source", "message_id": "orig_message_id"}
KEEP = ["row_id", "source", "orig_message_id", "message", "constructive", "justification", "relevance", "reciprocity",
        "empathy_respect", "uncivil_abuse"]

NOTES = """CACTUS Week 6 shared data: handling notes (for students and facilitators)

week06_clapton_val.csv   649 Twitter, Reddit and debate-forum messages with human labels, from the validation split of the CLAPTON
  dataset (Kokil Jaidka and collaborators). Labels (1 = yes, 0 = no): constructive, justification, relevance, reciprocity,
  empathy_respect, uncivil_abuse. @USER marks removed user names; links were replaced with URL.
  orig_message_id is NOT unique (some ids repeat). row_id (0 to 648) is the row's position and is unique.
week06_llm_labels.csv    LLM labels for 150 of the messages (row_id, llm_uncivil, llm_justification), made with the prompt in the notebook.

Content note: this data contains political arguments, insults, and abusive language. Read it as data. Step away if it bothers you.

Rules for using these files
- Use them for this course. Do not post them in a public place or share them outside the class unless a facilitator tells you it is allowed.
- Do not try to identify any person.
- Human labels are not ground truth. They are one group's judgments, and the notebook asks you to look for disagreement.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--val", required=True)
    a = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    v = pd.read_csv(a.val).rename(columns=RENAME)
    v["row_id"] = range(len(v))
    v["message"] = (v["message"].astype(str)
                    .str.replace(r"https?://\S+", "URL", regex=True)
                    .str.replace(r"<U\+[0-9A-Fa-f]{4,8}>|<f0>", "", regex=True)   # leftover encoding junk from the original export
                    .str.replace("&amp;", "&", regex=False)
                    .str.replace(r"\s+", " ", regex=True).str.strip())
    v = v[KEEP]
    v.to_csv(os.path.join(OUT, "week06_clapton_val.csv"), index=False, encoding="utf-8")
    sample = v.sample(150, random_state=6).sort_values("row_id")[["row_id", "message"]]
    sample.to_csv(os.path.join(OUT, "week06_eval_sample.csv"), index=False, encoding="utf-8")
    with open(os.path.join(OUT, "README_week06_data.txt"), "w", encoding="utf-8") as f:
        f.write(NOTES)
    llm = os.path.join(OUT, "week06_llm_labels.csv")
    with zipfile.ZipFile(os.path.join(OUT, "week06_corpus.zip"), "w", zipfile.ZIP_DEFLATED) as z:
        z.write(os.path.join(OUT, "week06_clapton_val.csv"), "week06_clapton_val.csv")
        z.write(os.path.join(OUT, "README_week06_data.txt"), "README_week06_data.txt")
        if os.path.exists(llm):
            z.write(llm, "week06_llm_labels.csv")
    print(f"wrote {len(v)} messages, sample of {len(sample)}; LLM labels included: {os.path.exists(llm)}")


if __name__ == "__main__":
    main()
