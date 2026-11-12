# Worked example: measuring gendered incivility in comments

A participant-sized version of a real study (the twoc project: gendered incivility in Instagram comments on a film-commentary account). You can follow it end to end as your own project, or borrow the parts that fit. It is built to match the weeks of CACTUS, so each week has one thing to show by the end.

**This page contains no real comments and no data from the original study.** You collect your own data in Week 4 from a public source, and you invent or paraphrase any example you show.

<!-- facilitator:start -->
> **Status: draft for review.** Not linked from the student site (`scripts/build_site.py` publishes only the files it lists, so this one stays unpublished until you add it). The original study's data are not in this repository: the repository is public, the source platform's terms on storing and sharing are not yet confirmed, and the comments, though pseudonymized, are other people's words. If a shared practice sample is wanted for Week 5 or 6, build a small invented one, as `data/week02_toy_cafe.csv` does.
<!-- facilitator:end -->

## The project card, filled in

```
Case study:     Comments under public videos or posts from creators who talk about
                gender and film, TV or games, over one month.
Main question:  What predicts whether a comment is uncivil in a gendered way?
Sub-question 1: How common is gendered incivility, and how does it differ between
                top-level comments and replies?
Sub-question 2: Does a comment's position (a reply to an uncivil comment, or a
                reply to someone who disagrees with it) predict incivility?
Sub-question 3: Do uncivil comments get more likes, or fewer?
Structure:      Predictors, then consequences (see Designing your project)
Data:           One row = one comment. Needs the text, the time, the like count,
                the parent comment if it is a reply, and the post it sits under.
```

## Objectives by week

By the end of each week you can show the item in bold. Every notebook cell the AI writes needs a note on how you checked it.

| Week | Objective | You show | How you check it |
|---|---|---|---|
| 1 | State the question and what one row is | **The project card above, in your own words** | A classmate can say what you will count |
| 2 | Load and clean a table of comments; chart basic counts | **A cleaned table and a chart of comments per post and per day** | Row counts before and after each cleaning step; no step drops rows silently |
| 3 | Estimate a simple model in code | **A regression of likes on one predictor, plus the same code run on a table where you know the answer** | The planted effect is recovered |
| 4 | Collect public comments, save the raw response, anonymize | **A raw file, a collection log, and an anonymized table** | Number collected equals number saved equals number parsed; no usernames or links left |
| 5 | Turn text into numbers and say what is lost | **Word counts and a dictionary sentiment score, compared with 30 comments you read** | Where does sentiment disagree with your reading? Write three examples |
| 6 | Write a codebook and have an LLM apply it; compare with humans | **A one-page codebook and agreement (accuracy and kappa) between the LLM and your own labels on 60 comments** | Where the LLM fails, and for which kind of comment |
| 7 | Pick one track | **Replies as a network** (who replies to whom), or a small mock feed | Edge counts match the reply counts in the table |
| 8 | Rerun everything from scratch and present | **A rerunnable notebook and a 5-minute talk with limitations** | A classmate reruns it and gets your numbers |

## A small codebook to start from

Keep it to three questions. Code each comment together with the post it sits under and, for a reply, the comment it replies to. Never code a comment on its own.

| Variable | Values | Rule |
|---|---|---|
| `incivility` | 0 / 1 | Aimed at a specific person: an insult, mockery, or a threat. A civil disagreement is 0 |
| `gendered` | 0 / 1 (only if `incivility` = 1) | The insult itself invokes gender or sexuality |
| `stance` | `echo` / `rebut` / `neither` | Toward the post if top-level; toward the parent if a reply |

Three invented examples (not from any real account):

| Comment | `incivility` | `gendered` | Why |
|---|---|---|---|
| "I disagree, the film was well paced." | 0 | | Disagreement without attack |
| "Typical critic, never watched a film in her life." | 1 | 0 | Insult, but not about gender |
| "Of course a woman would say that." | 1 | 1 | The insult invokes gender |

Hard cases to discuss in pairs before you code: sarcasm; a joke that contains a threat; a comment that stereotypes a group without attacking a person (is that incivility?); an emoji-only comment.

## What to keep in mind

- **Do not infer who people are.** Do not guess a commenter's gender, religion, caste or nationality from a name or picture. Code what the comment says, not who wrote it.
- **Aggregate, do not expose.** Report counts and rates. Quote only comments you have paraphrased so they cannot be searched.
- **Say what the sample is.** If you took the top comments on a handful of posts, say so; it is not "all comments on the topic."
- **Likes are a snapshot** taken when you collected them, and older comments have had longer to collect them. Put comment age in your model or say why you did not.
- **A classifier is not a coder.** Report where the LLM disagrees with you, split by kind of comment. A single accuracy number hides the failures.

## Stretch goals

- Do your codes and the LLM's codes disagree more on replies than on top-level comments?
- Does the result change if you drop emoji-only comments? Report both.
- Compare your small result with what a general toxicity score says on the same comments. Where do they differ, and why?
