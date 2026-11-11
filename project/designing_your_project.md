# Designing your project

Over 8 weeks you will turn a rough idea into working code on your own data. This guide helps you shape that idea. Your question decides what data you need and what you will do with it, so it is worth spending time on now. It does not have to be polished. We will revise it together.

**What to hand in:** a one-page project card (template at the end). A first draft is due after Week 1, and you will update it as you go.

---

## Step 1: Pick a case study

A case study is a specific topic in a specific context. "Social media" is too broad. "How Singapore, Hong Kong, and Taiwan users talk about AI chatbots on Reddit" is a case study.

Ask yourself:
- What do I already care about, or study, or have data on?
- Who is it about, where, and in what period?

## Step 2: Write one main question and 2–3 sub-questions

Raise **one main research question** and **two to three sub-questions** that break it into parts you can actually answer. For example:

> **Main question:** Can we gauge mental health through social media behavior?
> - What are the main reasons people use social media, and why?
> - What language behaviors on social media are predictive of low mental health?
> - How do motivations for social media use moderate the relationship between frequency of use and mental health?

There is no single right way to break a main question into sub-questions. The structures below are **starting templates, not a checklist**. Pick the one that fits your case study, mix elements from more than one, or use a different structure if your topic calls for it.

| Structure | Shape | Best for | Example |
|---|---|---|---|
| **Predictors → Consequences → Moderators** | *Main:* How does X affect Y?<br>1. What predicts or drives X?<br>2. What are the effects of X on Y?<br>3. For whom, or under what conditions, is the relationship stronger or weaker? | A specific behavior or exposure with a clear downstream outcome | *Main:* How does algorithmically curated content affect body image among teenage girls?<br>1. What factors predict exposure to appearance-focused content?<br>2. What are the mental-health consequences of that exposure?<br>3. Does it differ by age, platform literacy, or prior body-image concerns? |
| **Mechanism / Mediation** | *Main:* Does X affect Y, and through what pathway?<br>1. Is X associated with Y?<br>2. What mechanism (mediator) explains the link?<br>3. Does the mechanism hold across contexts, platforms, or populations? | Questions about *how or why* an effect happens, not just whether | *Main:* Does passive Instagram use affect loneliness?<br>1. Is passive use associated with loneliness?<br>2. Does social comparison mediate this?<br>3. Does the mediating role differ between active and passive users? |
| **Comparative / Contrastive** | *Main:* How does X differ between A and B?<br>1. What does X look like in A?<br>2. What does X look like in B?<br>3. What explains the difference? | Two platforms, populations, places, or time periods | *Main:* How does self-disclosure differ between WhatsApp and Instagram?<br>1. What does disclosure look like on each?<br>2. What affordance differences (persistence, visibility, audience) explain the gap? |
| **Debate / Reconciling mixed findings** | *Main:* Is X beneficial or harmful?<br>1. What supports the "risk" narrative?<br>2. What supports the "benefit" narrative?<br>3. Why are findings mixed (moderators, methods, populations)? | Topics where the literature is visibly split | *Main:* Is social media use harmful or helpful for adolescent mental health?<br>1. What does the "harm" literature find, and under what measures?<br>2. What does the "benefit" literature find?<br>3. Do the studies define or measure "use" differently? |
| **Multi-level / Stakeholder** | *Main:* What are the implications of X across levels?<br>1. Individual: how does X affect users?<br>2. Platform: what design features shape X?<br>3. Society or policy: what broader implications does X have? | Cases that span individual, platform, and policy angles (cyberbullying, misinformation) | *Main:* What does cyberbullying reveal about platform responsibility?<br>1. What individual harms result?<br>2. Which moderation features are or aren't effective?<br>3. What does regulation (for example Singapore's Online Safety Act) require? |
| **Problem → Cause → Intervention** | *Main:* How can X be reduced or addressed?<br>1. How prevalent or severe is X?<br>2. What causes or sustains X?<br>3. What interventions have been proposed or tested? | A specific harm and what might fix it | *Main:* How can problematic social media use be reduced among university students?<br>1. How common is it in this population?<br>2. What feedback loops (FOMO, variable reward, notifications) sustain it?<br>3. What interventions have evidence behind them? |

### A CACTUS example

Using the Starbucks comments dataset from Week 2, a **comparative** project might read:

> **Main:** How do online comments about Starbucks differ across Southeast and East Asian countries during a boycott period?
> 1. How much do comments in each country mention the boycott?
> 2. How does the tone (positive or negative language) differ between countries?
> 3. Do the differences hold in all languages, or only some?

Notice that each sub-question can be answered with something you will learn in this series (counting, sentiment, comparing groups).

## Step 3: Check that it is doable in 8 weeks

Go through this list. If you answer "no" or "not sure", that is fine. It tells you what to work on.

- [ ] **Data:** Do I have the data, or can I get it by Week 4? What does one row represent (a post, a comment, a user, a survey response)?
- [ ] **Size:** Is it big enough to say something, and small enough to handle on a laptop?
- [ ] **Measure:** For each sub-question, can I say what I would count, label, or compute?
- [ ] **Method:** Which week of this series teaches the tool I'd use?
- [ ] **Ethics:** Is the data public or do I have consent? Could anyone be identified? (We cover this in Week 4.)
- [ ] **Scope:** Could I answer this in a few weeks of part-time coding? If not, narrow it.

**Too big:** "How does social media affect society?"
**Better:** "How do Singapore and Taiwan Reddit users talk about AI-generated art?"

## Step 4: Use AI to sharpen it, not to decide it

AI can help you think, but you are the researcher. Try prompts like:

> Here is my main question and sub-questions: *(paste)*. Which of these structures (predictors→consequences→moderators, mechanism, comparative, ...) fits best, and why? What is missing? What could I not answer with the data I described?

Then check what it says. Does the suggestion fit your data? Is the structure a real match or just a plausible-sounding one? Write down what you accepted and what you rejected.

## Step 5: Fill in your project card

Copy this into a doc and fill it in. Keep each answer short.

```
PROJECT CARD
Name:                         Date:

Case study (topic, place, period):

Main research question:

Sub-question 1:
Sub-question 2:
Sub-question 3 (optional):

Structure I used (or "my own"):

Data
  What I have / will get:
  What one row is:
  Roughly how many rows:
  Where it comes from:
  Ethics or privacy concerns:

What I would measure or compute for each sub-question:
  1.
  2.
  3.

What could go wrong with my data, and how I'd check:

Which weeks of CACTUS help most:

How I'll use AI on this project (and how I'll check it):
```

## When to work on it

| When | What |
|---|---|
| After Week 1 | First draft: main question and sub-questions |
| After Week 2 | Add: what could go wrong in my data, and how I'd check |
| Week 3 | Revise with feedback; settle what you will measure |
| Week 4 | Data in hand (or a clear plan to get it) |
| Weeks 5–7 | Run your methods; revise the card when your plans change |
| Week 8 | Present your project |

Revising the question is normal. If the data can't answer it, change the question rather than forcing the data.
