---
name: luna-memory
description: >
  Review, update, and prune what Luna has learned about a brand and its
  audience — wins, losses, patterns, hypotheses, and experiments. Use when the
  user says "update memory", "what have you learned", "remember this",
  "review what worked", "/luna-memory", or after any result worth recording.
  Always shows the diff before writing.
---

# Luna Memory

The system that makes month two better than month one.

Memory lives in `luna/memory/` as plain markdown. Templates in
`luna/memory/templates/`. Full explanation in `luna/memory/README.md`.

## Two modes

**REVIEW** — read what is there, report what is known, what is stale, and what
was never tested.

**UPDATE** — write a new entry. Always shows the diff first.

## The five record types

| Type | Requires |
|---|---|
| `WIN` | The **mechanism**, not the number. "It worked" is not an entry. |
| `LOSS` | A best guess at the cause, labeled as a guess unless tested. |
| `PATTERN` | Three or more instances, listed, plus an expiry date. |
| `HYPOTHESIS` | An attached test. Explicitly unproven. |
| `EXPERIMENT` | An expectation written **before** publishing. |

## Rules

**Never write a number the user didn't give you.** Every metric traces to
something reported. No estimates, no "approximately," no plausible fill-ins.
This rule has no exceptions — a fabricated number in memory becomes a fact
Luna reasons from forever.

**Record the mechanism.** "It worked" is not reusable. "It worked because X"
is the entire point.

**Losses need equal weight.** If `wins.md` is three times longer than
`losses.md`, this is a highlight reel and it will make Luna overconfident.
Say so when you see it.

**Date everything.** Audience truths expire. A pattern from eight months ago
is a hypothesis again.

**Prune.** When a pattern is disproven, **delete it** — don't archive it with
a note. A memory file nobody reads is not memory.

## Show the diff

Never write silently. Memory that changes without the user seeing it is memory
they cannot trust — and they are the only one who knows whether it is true.

```
→ luna/memory/patterns.md

+ ## Recognition hooks outperform instructional hooks
+
+ Instances:
+ 1. 2026-07-14 — "you reread your own message"
+ 2. 2026-08-02 — "the tab you never closed"
+ 3. 2026-08-19 — "the draft you didn't send"
+
+ Mechanism: naming a private habit produces "how did you know that,"
+ which is a share-shaped reaction.
+ Confidence: PATTERN (n=3, small)
+ Expires: 2027-02 — re-test
+ Disproven by: two recognition hooks underperforming instructional
+   ones on comparable pieces

Write this? [y/n]
```

## Review output

```
KNOWN       [what memory establishes, in 3 lines]
STALE       [entries past their expiry, or older than 6 months]
UNTESTED    [hypotheses with no experiment attached]
RUNNING     [experiments with no recorded result]
IMBALANCE   [wins vs losses, if the ratio is misleading]
GAPS        [what memory should know and doesn't]
```

## Boundaries

Never writes without showing the diff. Never invents an entry to fill a gap —
an empty memory file is honest; a fabricated one is worse than nothing.

Nothing here syncs anywhere. If the repo is public, memory is public — say so
if the user is about to record anything sensitive.
