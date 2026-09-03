---
name: luna-audit
description: >
  Audit an entire content system — an account, a feed, a brand — for what is
  not working. Positioning, consistency, hooks, formats, channels, and what to
  stop doing. Use when the user says "audit my account", "audit my content",
  "review my whole feed", "what am I doing wrong", "look at my brand", or
  "/luna-audit". One-shot report, ranked, changes nothing.
---

# Luna Audit

Whole-system, not one post. `/luna-review` reads a draft; this reads
everything and ranks what is costing the most.

## What to look at

Whatever the user provides: a profile, a list of posts, a feed, analytics, a
website, a brief. **Work with what's there and say what you couldn't see** —
never audit an account you cannot actually observe.

## The passes

**1 — Positioning.** Read the last ten pieces. Can you say what this person
stands for in one sentence? If you can't, neither can their audience, and this
is the finding that outranks everything else.

**2 — Consistency.** Is there a recurring format, phrase, or visual? Would a
stranger recognize the next piece as theirs before reading the name?

**3 — Hooks.** Sample the openings. How many are titles rather than hooks?
Count them — the ratio is usually the single biggest available gain.

**4 — Sameness.** How much of this could be posted by any of five competitors
unchanged?

**5 — Repetition.** Is the same idea being restated without development?
Repetition of a *position* is good. Repetition of a *post* is decay.

**6 — Channel spread.** Are they on four platforms serving none? A neglected
channel is worse than no channel — it advertises inconsistency.

**7 — Audience clarity.** Do the pieces speak to one situation, or drift
between three audiences?

**8 — The ask.** Is there ever a next step? Or is this all top of funnel with
no floor?

## Tags

One line per finding, ranked by cost:

- `position:` — can't tell what they stand for
- `generic:` — could be anyone's
- `hook:` — openings describe instead of open
- `drift:` — the audience changes between pieces
- `stale:` — same thing, no development
- `spread:` — too many channels, none served
- `silent:` — a real strength being under-used
- `stop:` — doing something that is actively costing them

## Output

```
VERDICT   [the one sentence that matters most]

position: No consistent claim across 10 posts. Three different audiences.
          This is the finding — everything below is downstream. [profile]
hook:     7 of 10 openings are titles, not hooks. Biggest single gain
          available and it costs nothing to fix. [posts 1,3,4,6,7,9,10]
generic:  The tool round-ups are indistinguishable from four larger accounts
          covering the same tools. [posts 2,5]
silent:   The one teardown post is the most distinctive thing here and there
          is only one of them. [post 8]
stop:     Three-platform spread with no adaptation. Cut one. [profile]

FIRST     [the single highest-return change]
COULDN'T SEE  [what wasn't provided]
```

Lead with the verdict. Rank by cost, not by how easy it is to fix.

## Boundaries

Reports, changes nothing. Fixes route to `/luna-strategy` (positioning),
`/luna-hook` (openings), `/luna-debt` (accumulated rot). One-shot.
"stop luna-audit" or "normal mode" to revert.
