# Data

Shared datasets for CACTUS Fall 2026. Raw exports stay in `data/raw/` (local only, not committed).

| File | Used in | Rows | What it is |
|---|---|---|---|
| `starbucks_sea_comments.csv` | Week 2 exercises | 4,174 | Public comments mentioning Starbucks, 5–14 Oct 2024, from TH, VN, MY, PH, SG, ID, HK. Many languages. Column `Translated` is machine translation |
| `lululemon_instagram.csv` | Week 2 demo | 11,019 | Instagram posts mentioning Lululemon, Nov 2022 to Apr 2023. Accounts appear mostly North American |
| `week02_toy_cafe.csv` | Week 2 practice page and notebook warm-up | 30 | Invented café comments (Brew Lane) with planted problems: 3 duplicates, 2 rows with no text, 2 dates in another format, scores stored as text. Clean result: 25 rows. Rebuild with `python3 scripts/week02_toy_data.py` |
| `week03_experiment.csv` | Week 3 exercises | 300 | Simulated randomized experiment: a made-up "AI label" on shared posts and a `sharing_intent` score. The true effect is -0.6 and is stated in the notebook. Rebuild with `python3 scripts/make_week03_data.py` |
| `week03_survey.csv` | Week 3 exercises | 800 | Simulated observational survey with a confounder (`prior_ai_use`), same true effect. The naive comparison is biased |
| `week01/serp_cache/` and `serp_cache.zip` | Week 1 | 6 files | Saved SerpAPI responses for students without a key (create with `scripts/cache_week1.py`) |

## Columns worth knowing

**starbucks_sea_comments.csv:** `Post ID`, `Post Date`, `Content` (original text), `Translated`, `Channel Name`, `Channel Country`, `Channel Language`, `Channel Site Type`, `voice_id` (pseudonymous author), `tone_pos` and `tone_neg` (percent of words in the comment that are positive or negative), and topic columns (`food`, `money`, `health`, and so on), each a percent of words.

**lululemon_instagram.csv:** `account_id` (pseudonymous), `Post Created`, `Type` (Photo, Album, Video), `Followers at Posting`, `Likes`, `Comments`, `Views`, `Description`, and similar word-percent columns.

## Shared privately (not in this repository)

The Week 5 text corpora are shared with the class through a private drive. They contain posts written by real people, so they are not published here. See the Week 5 page when it is released.

## Known quirks

These datasets are real and messy on purpose, and the problems are not listed here: finding them is part of the exercises. Teaching staff have notes in the private instructor folder.

## Privacy

The raw export contained usernames, profile links, and post links. In the processed CSVs:
- usernames and account names are replaced by sequential IDs (`voice_0001`, `account_0001`)
- post, channel, profile, and photo links are removed

Comment text and post descriptions are unchanged, so they can still contain `@handles` that users wrote themselves. Before sharing outside the workshop, check the terms of the source platform and your ethics approval. Students should not try to identify individuals.

Rebuild the processed files with `python3 scripts/prepare_datasets.py` (needs pandas and openpyxl).
