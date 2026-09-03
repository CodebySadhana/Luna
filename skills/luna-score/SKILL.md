---
name: luna-score
description: >
  Score a content idea across attention, novelty, emotion, shareability, brand
  fit and more before it costs anything to make, then return MAKE IT / REWORK
  IT / KILL IT. Use when the user says "score this", "rate this idea", "is this
  worth making", "should I post this", "which of these is best", or
  "/luna-score". Heuristic judgment, explicitly not a prediction.
---

# Luna Score

A structured way to argue with an idea before it costs you anything.

## Say this every time

**This is not a prediction.** These are heuristic judgments about how an idea
is *built* — not forecasts of reach, engagement, or revenue. Nothing here has
been validated against outcome data. A 94 does not mean it will beat an 82.

The value is that it forces the weak dimension into the open. Two people who
disagree about an idea usually disagree about exactly one dimension. This
finds it in seconds.

Never drop this caveat to make the output look more authoritative.

## The dimensions

Score 0–100. Fourteen available — **use only the ones this format actually
depends on.** Padding the table with 90s you didn't think about is fake
precision.

| Dimension | The question |
|---|---|
| **Attention** | Is there a reason to stop in the first two seconds? |
| **Novelty** | Have they seen this exact thing this month? |
| **Emotion** | What is the feeling, and how strong? Name it. Mild interest scores low. |
| **Curiosity** | Is there an open loop they need closed? |
| **Shareability** | What does sharing this say about the sharer? |
| **Saveability** | Would someone come back to it? |
| **Retention** | Does the middle earn the end, or does the hook spend everything? |
| **Cultural timing** | Is this the right week? |
| **Audience relevance** | Does the named audience actually have this problem? |
| **Brand fit** | Would ten of these teach anyone what you stand for? |
| **Differentiation** | Could a competitor post this unchanged? |
| **Production feasibility** | Can one person make this well, this week? |
| **Distribution potential** | Is there a mechanism for it to travel, or just hope? |
| **Conversion potential** | Does it move anyone toward the thing you sell? Not every piece should. |

## Scoring discipline

- **Below 70 is normal.** A table of 90s means you're flattering the idea. A
  useful table has range.
- **The lowest score is the finding.** Lead with it. The 94s are noise.
- **Never score a dimension you didn't think about.** Omit it.
- **The total is a judgment, not an average.** A 30 on Attention caps the
  whole thing — nothing downstream of an unread post matters.

## Verdicts

| Range | Verdict |
|---|---|
| 85+ | **MAKE IT** — go, fix the weakest link first if it's cheap |
| 70–84 | **REWORK IT** — one dimension is dragging. Name it, fix that, re-score. |
| Below 70 | **KILL IT** — or salvage one element and start a new idea from it |

**Hard gates, which override the total:**
- Attention below 60 → **KILL**. Nothing survives not being seen.
- Differentiation below 50 → **KILL**. You're making someone else's content.

## Output

```
IDEA  "[the idea in one line]"

ATTENTION .............. 92
NOVELTY ................ 87
EMOTION ................ 74   <- recognition, not outrage. Lower ceiling.
CURIOSITY .............. 95
SHAREABILITY ........... 88
CULTURAL TIMING ........ 71
BRAND FIT .............. 94
DIFFERENTIATION ........ 90
PRODUCTION ............. 96

LUNA SCORE ............. 88 / 100
VERDICT ................ MAKE IT

Weakest link: cultural timing. Evergreen frame, no reason to publish this
specific week. Publish it, don't expect a spike, and don't blame the idea
if there isn't one.

Heuristic judgment, not a prediction.
```

## Scoring a batch

Rank them and **cut the bottom half**. Ten ideas where all ten are "worth
trying" is a menu, not a strategy.

The deliverable is: what to make first, what to make later, what to delete.

## Boundaries

Evaluates, doesn't fix. Route repairs to `/luna-hook` (rung 3), `/luna-ideas`
(rung 1–2), or `/luna-review` (a finished draft). One-shot.
