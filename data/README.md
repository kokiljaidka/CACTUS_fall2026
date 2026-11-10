# Data

Shared datasets for CACTUS Fall 2026. Raw exports stay in `data/raw/` (local only, not committed).

| File | Used in | Rows | What it is |
|---|---|---|---|
| `starbucks_sea_comments.csv` | Week 2 exercises | 4,174 | Public comments mentioning Starbucks, 5–14 Oct 2024, from TH, VN, MY, PH, SG, ID, HK. Many languages. Column `Translated` is machine translation |
| `lululemon_instagram.csv` | Week 2 demo | 11,019 | Instagram posts mentioning Lululemon, Nov 2022 to Apr 2023. Accounts appear mostly North American |
| `week01/serp_cache/` and `serp_cache.zip` | Week 1 | 6 files | Saved SerpAPI responses for students without a key (create with `scripts/cache_week1.py`) |

## Columns worth knowing

**starbucks_sea_comments.csv:** `Post ID`, `Post Date`, `Content` (original text), `Translated`, `Channel Name`, `Channel Country`, `Channel Language`, `Channel Site Type`, `voice_id` (pseudonymous author), `tone_pos` and `tone_neg` (percent of words in the comment that are positive or negative), and topic columns (`food`, `money`, `health`, and so on), each a percent of words.

**lululemon_instagram.csv:** `account_id` (pseudonymous), `Post Created`, `Type` (Photo, Album, Video), `Followers at Posting`, `Likes`, `Comments`, `Views`, `Description`, and similar word-percent columns.

## Known quirks (useful for teaching, don't "fix" in the file)

- Starbucks: 85 exact duplicate rows, 17 comments with missing text, some comments are only numbers, dates are stored as text in the CSV.
- Lululemon: `Views` is 0 for every photo (it is not recorded), and the filename on the original export said 2024 but the posts are from Nov 2022 to Apr 2023.
- The original spreadsheet had a second sheet, "Copy of starbucks", that is not identical to the first. It was not used.

## Privacy

The raw export contained usernames, profile links, and post links. In the processed CSVs:
- usernames and account names are replaced by sequential IDs (`voice_0001`, `account_0001`)
- post, channel, profile, and photo links are removed

Comment text and post descriptions are unchanged, so they can still contain `@handles` that users wrote themselves. Before sharing outside the workshop, check the terms of the source platform and your ethics approval. Students should not try to identify individuals.

Rebuild the processed files with `python3 scripts/prepare_datasets.py` (needs pandas and openpyxl).
