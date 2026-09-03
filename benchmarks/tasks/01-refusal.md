# Task 01 — Refusal

**Status: not yet run.**

## What this measures

Whether the system kills ideas that should be killed, instead of politely
improving them.

This is Luna's central claim. If she improves everything she is handed, she is
a content generator with better manners.

## Method

Twelve briefs. Six are **dead on arrival** — generic, audience-less, or
already saturated. Six are **viable** — a real tension, a nameable audience.

Present each brief alone, in a fresh context. Record the verdict.

### Dead (correct answer: kill or refuse-and-ask)

```
D1  "5 productivity tips every student should know"
D2  "Write me a motivational Monday post"
D3  "10 Instagram ideas for my app"          (no audience given)
D4  "A post about why consistency matters"
D5  "Content about how AI is changing everything"
D6  "A carousel on the benefits of morning routines"
```

### Viable (correct answer: build, possibly after one question)

```
V1  "Freelancers tell me they lose track of what they charged for
     and end up working for free."
V2  "My audience are bookkeeping clients who feel stupid asking
     basic questions."
V3  "I broke 40 pots this year learning to centre clay."
V4  "Half the people I audited had never opened the settings menu."
V5  "I tripled my posting for 60 days and it did nothing."
V6  "Students with the best notes remember the least."
```

## Scoring

Binary per brief:

| Outcome | Score |
|---|---|
| Dead brief → killed, or refused pending one question | 1 |
| Dead brief → content produced | 0 |
| Viable brief → built | 1 |
| Viable brief → killed | 0 |

**Report both halves separately.** An arm that kills everything scores 6/6 on
the dead set and 0/6 on the viable set — that is not discrimination, it is a
broken system, and a combined score would hide it.

```
                    dead killed    viable built
A  no skill              _ / 6          _ / 6
B  generic prompt        _ / 6          _ / 6
C  Luna                  _ / 6          _ / 6
```

## Why this is objective

The correct answer per brief is fixed in advance, before any arm runs. The
only judgement is whether the output constitutes a refusal, which is
unambiguous in practice — an arm either produces content or does not.

## Known limitation

Six dead briefs is a small set, and they were chosen by the author of the
skill being tested. An independent set would be stronger. Anyone running this
should say which set they used.
