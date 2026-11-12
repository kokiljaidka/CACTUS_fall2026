# Practice pages: facilitator guide

What each level teaches, where students tend to stall, and a question to ask instead of giving the answer. Use it when a student asks for help during the puzzle page or the practice page.

**The rule:** ask a question before you give an answer. Every level has a hint button, so check whether the student has used it. If they are still stuck after the nudge question, show them the next step, not the whole solution.

Answers for the Week 2 bug-hunt levels are in the private answer key (`week02_practice_key.md`), not here.

## Before the session

- Do the page yourself once, start to finish, in under 40 minutes (Week 1) or 20 minutes (Week 2).
- Try the wrong choices on purpose and read the feedback messages.
- Use tap as well as drag. Some students will only tap, and that is fine.

## Week 1: Cactus Code Garden (17 levels)

Students work through the 16 puzzles in about 30 to 35 minutes, then the Colab bridge. If a pair is far behind at 35 minutes, they skip to level 16 (their project row) and the bridge.

| Level | Teaches | Common stall | Ask this |
|---|---|---|---|
| 1 Water the cactus | Exact steps in order | Not predicting; counting squares wrongly | "Count the squares with your finger. How many to the right? How many up?" |
| 2 Around the rocks | Order matters; the computer cannot guess a detour | Walking into a rock | "Which is the first square the cactus cannot enter? What would you do before that?" |
| 3 Name the boxes | Variables as named boxes | Filling in the order they appear, not by name | "Read the print line. Which word comes from `city`?" |
| 4 Quotes matter | Types: text vs number | "Why is `1 + 2` fine but `"1" + "2"` gives 12?" | "Which pieces have quotes? What does + do to text?" |
| 5 One row as a dictionary | A row is labeled slots | Putting a value under the wrong label | "Which label describes this value?" |
| 6 Counting from zero | Index starts at 0 | Expecting the first item to be 1 | "Point at the first item. What number is on it?" |
| 7 Set the dials | Function parameters; `q`, `gl`, `hl` | Mixing up what each dial takes | "What does each dial control: what, where, or which language?" |
| 8 Order of the dials | Arguments match by position | Swapped result still looks plausible | "In the definition, which parameter comes first?" |
| 9 Say it once | Repeat blocks | Hitting the block limit; forgetting to set the count | "What is the smallest piece that repeats? How many times?" |
| 10 The staircase | Spotting a repeating pattern | Trying to build the whole path step by step | "Write the path as steps. Is there a pair that keeps coming back?" |
| 11 For each comment | Loops that build on a value | Choosing `count = 1` | "What is `count` after the first comment? After the second?" |
| 12 to 14 Read the response | Following a path into nested data | Starting in the middle; counting from 1 | "Start from the outside. Which label holds the results? Then which item?" |
| 15 Put the steps in order | Decomposition | Guessing the order | "What does each step need that an earlier step produces?" |
| 16 Your project row | Turning your own project into a dictionary | Spending ten minutes on perfect field names | "What would one real row of your data look like? Add three fields; you can change them later." |
| 17 Colab bridge | Real code with checks | `NameError` in Task 2 if Step 3 was not run; the Task 3 check fails until the line is pasted (by design) | "Read the last line of the error. Which earlier cell does it need?" |

**Watch for:**
- Students who finish early: ask them to explain level 11 or 14 to their partner.
- Students who feel slow: say that levels 6, 11 and 12 to 14 are the ones people stall on.
- Level 16 is the bridge to the project card. If a student's row does not match their card, that is useful: help them fix one of the two.

## Week 2: Silent Changes (5 levels, about 20 minutes)

Students do this between the learning session and the coding session. It may be done alone.

| Level | Teaches | Common stall | Ask this |
|---|---|---|---|
| 1 Clean the café table | Each step's effect on the row count; tempting steps that damage the data | Adding every card; not seeing why a card is a trap; leaving the prediction box empty | "For each row this removes: would you say out loud why it should go?" |
| 2 to 4 Find the bug | A result can run without error and still be misleading | Clicking a line that looks "technical"; picking a check that does not test the doubt | See the ladder below |
| 5 Colab bridge | Writing the pipeline as real code, with a check | Pasting into the wrong cell; counts that do not match | "Compare your steps with the ones on the page, one at a time. Where do the counts first differ?" |

**Level 1, what students should see in the output:** two steps remove rows, two only change types, and values that could not be read are flagged as blank rather than dropped or invented. If a student's final row count is not 25, they have used a tempting step. Ask them what that step did to the count.

**The ladder for levels 2 to 4 (use in order, one rung at a time):**

1. "Which line decides which rows or numbers the answer is based on?"
2. "What does that line assume about each row or group?"
3. "What could you count or compare that would show whether that assumption holds?"
4. Only then: point at the line and say "look at what this does to the number of rows (or to the group sizes)."

The matching check is on the page. If a student picks the wrong check, the message explains why it would not catch the problem, so you do not have to.

**Watch for:**
- Students who treat the AI code as correct because it ran. Say: "It ran. Is that the same as right?"
- Students who rush. The prediction box and the waterfall table are the point.
- The live Exercise 2 in the coding session has **different** bugs. If a student asks, say they will see them there. Do not describe them.

## Week 3: Planted-Effect Lab (4 levels and a bridge, about 20 minutes)

Students do this between the learning session and the coding session. The numbers are random, so every student's run differs, and that is the point.

| Level | Teaches | Common stall | Ask this |
|---|---|---|---|
| 1 One study | One estimate is noisy; the interval is the honest statement of that | Expecting the estimate to equal the truth; treating a miss as a mistake in the code | "If you ran it again, would you get the same number? What does that tell you?" |
| 2 Run it 100 times | Roughly 95 in 100 intervals contain the truth; a bigger sample tightens the estimates | Not finding the sample size that gets the count of far-off estimates to 10 or fewer | "What happens to the spread when you double the sample? How far could you go?" |
| 3 Who gets the treatment? | A confounder can flip the sign of a naive comparison; adjusting recovers the truth | Not seeing why the naive estimate goes negative | "Who is more likely to attend tutoring? How does that change who ends up in each group?" |
| 4 What does each answer claim? | Certainty, size and cause need separate evidence | Choosing "ignores randomization" for any answer (the study was randomized) | "Does it claim more than one small study can give? Does it treat 'significant' as 'large'?" |
| 5 Colab bridge | The same simulation as real code, checked by the 95-in-100 rule | `NameError` if imports are missing; counts far from 95 when the sample is tiny | "Run it three times. What range of counts do you get? Is it near 95?" |

**Watch for:**
- Students who treat the "right" answer to a prediction as the point. The point is that results vary.
- The confounding level uses a tutoring story, not the notebook's label story, so the notebook's Exercise 3 still has something to discover. Do not tell students what the notebook's naive estimate will look like.
- A very small sample (10 to 20) can occasionally give an odd run in the bridge. Rerun before concluding there is a bug.

## Week 4: Before You Collect (4 levels and a bridge, about 20 minutes)

Students do this between the learning session and the coding session. It is mostly judgment, so expect disagreement, and welcome it.

| Level | Teaches | Common stall | Ask this |
|---|---|---|---|
| 1 Keep, change, or drop | Collect only what the question needs; change what identifies people | "Keep everything, just in case" | "Does the question need this field? If it does, can it be changed so it does not identify someone?" |
| 2 Who could be found? | Removing the username is not enough; details combine | Stopping when the username is gone | "What could someone learn by combining the time, the place and the text?" |
| 3 Plan the pull | A limit is a plan: page size and pause; save raw first | Using a tiny page size, or no pause | "How many requests does that need? How many are you allowed?" |
| 4 Should you collect it? | Public versus private, consent, terms, sensitivity | Wanting a yes or no; arguing about the law | "Is it public? Did people agree to this use? Do the terms allow it? When unsure, who do you ask?" |
| 5 Colab bridge | A collection stub that saves raw first, with a log | A `NotImplementedError`: they have not changed the one function that talks to the platform | "Which function needs your platform's request? For Route B use `sample_api`." |

**Watch for:**
- Facilitators giving legal or ethical rulings. Say you do not know and ask Kokil or the ethics office.
- Students quoting real people from their own data in the breakout room. Ask them to describe it without names.
- The limits on the page are invented. Students need their platform's real limits from the access guide.
