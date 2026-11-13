# Facilitator hub

Everything the team needs to run CACTUS Fall 2026, in one place. If you are new to this, read this page first, then [the week-by-week run sheets](week_by_week.md).

**You do not need to be the expert.** The course teaches people to check AI-written code, so "I am not sure, let us test it" is exactly on message. There is a script for every session, and there are four of you.

## What is on this page, and where the rest is

| Need | Where |
|---|---|
| How we run it as a team (this page) | Below |
| What to do in each week, minute by minute | [Week-by-week run sheets](week_by_week.md) |
| What each practice page teaches, where students stall, what to ask | [Practice page guide](practice_pages_guide.md) |
| How to make this a community, and what to say when you do not know | [Running CACTUS together](running_this_together.md) |
| Testing everything before students see it | [Testing checklist](../testing/ra_checklist.md) |
| Slides with a script beside each one | Presenter links in the table at the bottom (press **N** for the notes) |
| Answer keys for the bug hunts | Private. Ask Kokil for the link. They are never posted here |

## The team

Four facilitators (called **A, B, C and D** on this page; the names are in the team's private rota). Facilitator D is also a participant (a student-facilitator): D learns alongside the group, and helps the people near them.

Every session has these roles:

| Role | What you do | Who |
|---|---|---|
| **Lead** | Runs the learning session (1 hour) from the slides and script. In the coding session, opens, posts the time checks, and closes. Does the main prep for the week. | One person per week |
| **Desk** | Stays in the main Zoom room during the coding session. Watches the chat and "Ask for help", fixes Colab and install problems, sends people to the right room, keeps the timing. | One person per week |
| **Rooms** | Visit the breakout rooms. Ask a guiding question before you give an answer. Use the hint ladder below. | Everyone else |
| **Data helper** (Weeks 1 to 4) | Helps anyone without data to get an export (Twitter/X, Instagram, Facebook, Reddit, Bluesky). Notes what worked in the access guide. | Whoever knows that platform |

There is no lecture in the coding session, so the Lead is a Rooms person too.

## Round-robin: who does what each week

Each person leads twice. The Lead rotates, the Desk rotates, and everyone else visits rooms. This is a suggestion: swap it if someone knows a week's content better, or if someone cannot make a date.

| Week | Date (Tue) | Topic | Lead | Desk | Rooms |
|---|---|---|---|---|---|
| 1 | Nov 17 | Define your problem; how code thinks | A | B | C (D helps their pair) |
| 2 | Nov 24 | Clean it, chart it | B | C | A |
| 3 | Dec 1 | Verify and analyze | C | A | B |
| 4 | Dec 8 | Collect your own data | A | B | C |
| 5 | Dec 15 | Analyze text | D (C backs up) | A | B, C |
| 6 | Dec 22 | AI as annotator | C | B | A |
| 7 | Dec 29 | Choose a track | B | A | C |
| 8 | Jan 5 | Reproduce and present | D (A backs up) | C | A, B |

Weeks 6 and 7 fall in the year-end break: confirm the dates with the group.

**Rules of the rota**

- **A person who leads for the first time has a backup** (shown in brackets) who has done the notebook and will take over the slide if needed.
- **Facilitator D does not hold the Desk.** In coding sessions D works through the exercises with a partner and helps the people next to them, and leads only the learning session in Weeks 5 and 8.
- **Swap freely**, but tell the team chat at least two days ahead.
- Roughly: a Lead puts in about 3 hours of prep and 3 hours in session; the Desk and Rooms about 1 hour of prep and 3 hours in session. Week 1 is about 4 hours in session.

## A week at a glance

| When | What | Who |
|---|---|---|
| 2 to 3 days before | Lead reads the schedule page and the slide notes, runs the practice page and the notebook once, and notes anything that stumbles. Posts "ready" in the team chat. | Lead |
| The day before | **30-minute huddle.** The Lead walks through the slides in two minutes each. Everyone else asks what they would ask a student. Agree the Desk and who visits which rooms. | All |
| The day | Learning session (1 hour), then the participants do the practice page (20 minutes), then the coding session (2 hours). | All |
| Within a day after | **15-minute debrief** and three lines in the team chat: what worked, what stalled, what to fix. Anything confusing becomes a GitHub issue. The Desk updates the access table if anyone learned something. | All |

## Running the learning session (1 hour)

1. Open the **presenter view** of the slides and press **N** to show the notes. Each note has: TIME, SAY, DO, and what to WATCH FOR.
2. Start on time. Post the course site link in the chat.
3. Run the live demos as written. If a demo breaks, say so, and use the numbers on the slide. A broken demo you recover from is a lesson.
4. Ask the room to **predict before you run**. Wait for two answers.
5. Leave the last minutes for questions. If you do not know, say "good question, let us test it", or write it down for Kokil.
6. Finish by posting the practice page link, the reading, and the data rules for the week.

**Do not** reveal what the notebook will find (the bugs, the surprises). Students find those.

## Running the coding session (2 hours)

1. **Before:** the Desk opens the main room 10 minutes early and checks that the notebook link and data links in the chat work.
2. **Open (5 minutes):** the Lead says the plan, makes pairs, and sends people to rooms. Read the stuck protocol aloud (below).
3. **Time checks:** the Lead posts the time and the next exercise in the main chat at each boundary on the run sheet.
4. **Rooms:** visit each room every 15 to 20 minutes. Ask "what did you predict, and what happened?" before anything else.
5. **Desk:** answer chat messages and "Ask for help" in the main room, and tell the room who is on the way.
6. **Close (5 minutes):** everyone fills in their verification log. Two or three volunteers can share one thing they found.

### The stuck protocol (read it aloud at the start)

Students try these, in order, for no more than 5 minutes:

1. Read the last line of the error message. What is it telling you?
2. Re-read the instructions for the step. Did you skip a part?
3. Ask your partner, then ask an AI assistant to explain the message (never paste keys, passwords, or other people's data).
4. Still stuck? Click **Ask for help** or message the main chat. Say what you expected, what happened, and what you tried.

### The hint ladder (for you)

1. **Ask:** "What did you predict? What happened instead?"
2. **Point:** "Look at this line. What does it do?"
3. **Narrow:** "Check the number of rows before and after this step."
4. **Show the next step only**, not the whole answer.
5. **Offer the safety net:** a partner, the saved result, or the next exercise, and follow up afterwards.

The private answer keys list the hints for each bug hunt in order. Ask Kokil for the link.

## When things go wrong

| Problem | What to do |
|---|---|
| A student is far behind | Offer the safety net (skip to the next required exercise, or pair them). Say it is fine. Check in at the next break |
| A student is far ahead | Point them to the stretch tasks, or ask them to help a neighbour explain a cell in their own words |
| An install or Colab problem | The Desk takes it. Try again in a fresh runtime. If it still fails, use the fallback the notebook names, and write it in the team chat |
| A key or login problem | Do not look at the key. Ask the student to re-enter it in Colab Secrets. If still stuck, use the saved data |
| Zoom or audio | The Desk handles it. Post the plan in the chat |
| A student is upset by content (Week 6 includes abusive language) | Say they can step away or work on another label. Do not ask them to explain |
| A student asks about their own research or ethics | You are not expected to advise. Say "that is a good question for your supervisor, and Kokil is the ethics contact for CACTUS" and note it |
| You made a mistake | Say so, fix it, and move on. Mistakes are things you check |

## Rules for the team

- **Data privacy:** never paste a student's data, a key, or anything personal into an AI chat or a public issue. Students' project data stays with them.
- **Public data only in public places.** Class data (the Week 5 and Week 6 files) is for course use only and lives on the class drive, not on this site.
- **No legal rulings.** On terms or ethics, say what the question is and send it to Kokil.
- **Answer keys stay private.** Do not post, forward, or screenshot them.
- **Be kind.** No shaming for not knowing. Pairs help each other first, and facilitators second.
- **Report problems as GitHub issues**, with no keys and no personal data. This also helps the next cohort.

## Where everything is, week by week

Slides open in the **presenter view**: press **N** for the script. Notebooks open in Colab.

| Week | Presenter slides | Practice page | Notebook |
|---|---|---|---|
| 1 | [Define your problem](https://kokiljaidka.github.io/CACTUS_fall2026/slides/week01_define_your_problem_presenter.html) | [Cactus Code Garden](https://kokiljaidka.github.io/CACTUS_fall2026/practice/week01_cactus_code_garden.html) | [First API calls](https://colab.research.google.com/github/kokiljaidka/CACTUS_fall2026/blob/main/notebooks/week01_first_api_calls.ipynb) |
| 2 | [Clean it, chart it](https://kokiljaidka.github.io/CACTUS_fall2026/slides/week02_clean_it_chart_it_presenter.html) | [Silent Changes](https://kokiljaidka.github.io/CACTUS_fall2026/practice/week02_silent_changes.html) | [Clean and chart](https://colab.research.google.com/github/kokiljaidka/CACTUS_fall2026/blob/main/notebooks/week02_clean_and_chart.ipynb) |
| 3 | [Verify and analyze](https://kokiljaidka.github.io/CACTUS_fall2026/slides/week03_verify_and_analyze_presenter.html) | [Planted-Effect Lab](https://kokiljaidka.github.io/CACTUS_fall2026/practice/week03_planted_effect_lab.html) | [Verify and analyze](https://colab.research.google.com/github/kokiljaidka/CACTUS_fall2026/blob/main/notebooks/week03_verify_and_analyze.ipynb) |
| 4 | [Collect your own data](https://kokiljaidka.github.io/CACTUS_fall2026/slides/week04_collect_your_own_data_presenter.html) | [Before You Collect](https://kokiljaidka.github.io/CACTUS_fall2026/practice/week04_before_you_collect.html) | [Collect your own data](https://colab.research.google.com/github/kokiljaidka/CACTUS_fall2026/blob/main/notebooks/week04_collect_your_own_data.ipynb) |
| 5 | [Analyze text](https://kokiljaidka.github.io/CACTUS_fall2026/slides/week05_analyze_text_presenter.html) | [What Counts as a Word?](https://kokiljaidka.github.io/CACTUS_fall2026/practice/week05_what_counts_as_a_word.html) | [Analyze text](https://colab.research.google.com/github/kokiljaidka/CACTUS_fall2026/blob/main/notebooks/week05_analyze_text.ipynb) |
| 6 | [AI as annotator](https://kokiljaidka.github.io/CACTUS_fall2026/slides/week06_ai_as_annotator_presenter.html) | [Can You Trust the Labeler?](https://kokiljaidka.github.io/CACTUS_fall2026/practice/week06_trust_the_labeler.html) | [AI as annotator](https://colab.research.google.com/github/kokiljaidka/CACTUS_fall2026/blob/main/notebooks/week06_ai_as_annotator.ipynb) |
| 7 | To build | To build | To build |
| 8 | To build | To build | To build |

Weeks 5 and 6 use class data that is shared privately (the class drive). Ask Kokil for the link.
