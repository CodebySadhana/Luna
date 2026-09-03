# Task 04 — Verbosity

**Status: not yet run.**

## What this measures

Words spent per decision delivered.

Luna claims her analysis is shorter than the user expects, and that the
density is the point. This checks whether the skill actually compresses, or
whether it just adds a persona to the same wall of text.

## Method

Six prompts that have a correct short answer:

```
V1  "Is this hook any good? — 'In this video I'll share some tips
     on email marketing.'"
V2  "Should I post this on LinkedIn or TikTok?"          (brief given)
V3  "Which of these three ideas should I make first?"    (three given)
V4  "My views dropped 40% this month. What happened?"    (no data)
V5  "Should I do this trend?"                            (trend given)
V6  "Is 'Monday motivation' worth posting?"
```

## Scoring

**1 — Word count.** Total words in the response.

**2 — Decision present.** Does the output contain an actual decision — a
verdict, a pick, a kill — or does it list considerations? Binary.

**3 — Words per decision.** (1) divided by (2), where a response with no
decision scores as infinite.

```
                  words    decision given    words / decision
A  no skill         _          _ / 6                _
B  generic prompt   _          _ / 6                _
C  Luna             _          _ / 6                _
```

## Why this is objective

Word count is a count. "Contains a decision" is near-unambiguous: the output
either names a choice or it does not.

## The failure this catches

An arm can score well on word count by being tersely non-committal. The
decision column is what separates *short* from *decisive* — and a system that
is short and says nothing is worse than one that is long and picks.

Report both columns. Neither is meaningful alone.
