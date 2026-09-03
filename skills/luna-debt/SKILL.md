---
name: luna-debt
description: >
  Find content debt — the accumulated rot that quietly costs an operator:
  stale messaging, repetitive content, neglected channels, outdated audience
  assumptions, dead workflows, unfinished drafts, broken links. Use when the
  user says "content debt", "what's rotting", "what should I stop doing",
  "clean up my content", "/luna-debt", or "what did we defer". One-shot ledger.
---

# Luna Debt

Ponytail tracks deliberate code shortcuts. Luna tracks the marketing
equivalent: **decisions that were right once and were never revisited.**

Content debt is invisible because nothing breaks. The feed still posts, the
bio still reads fine, the channel still exists. It just quietly stops working.

## The debt types

| Type | What it looks like |
|---|---|
| `stale` | Messaging written for who they were 18 months ago |
| `repeat` | The same idea restated with no development |
| `neglect` | A channel that exists and hasn't been served in months |
| `assume` | An audience belief nobody has re-checked |
| `backlog` | Drafts, half-ideas, and recorded footage that will never ship |
| `manual` | A weekly task done by hand that shouldn't be |
| `broken` | Dead links, old bio, outdated pinned post, wrong pricing |
| `inconsistent` | Two channels saying different things about the same thing |
| `orphan` | A format started, promised as a series, and abandoned |

## Where to scan

- Bio, pinned post, link-in-bio, website above the fold — the most-read and
  least-updated surfaces an operator owns
- `luna/memory/` — patterns with an expiry date that has passed, hypotheses
  never tested, experiments left RUNNING
- The last 3 months of posts, for `repeat` and `orphan`
- Every channel with a profile — when was the last post?
- Anything the user calls "I keep meaning to"

## Memory rot

If `luna/memory/` exists, check it specifically:

- `PATTERN` entries past their **Expires** date → now hypotheses again
- `HYPOTHESIS` entries with no experiment → will never be tested
- `EXPERIMENT` entries stuck at RUNNING → the result was never recorded
- `wins.md` far longer than `losses.md` → a highlight reel, not memory

Flag anything with no re-check trigger as `no-trigger`. **Those are what
silently rot.**

## Output

One row per item, grouped by type, ranked by cost:

```
stale:   Bio still says "helping teams scale" — audience shifted to solo
         founders eight months ago. Most-read text they own. [profile]
neglect: Pinterest, last pin 5 months ago. Either serve it or delete it —
         an abandoned profile advertises inconsistency. [pinterest]
assume:  "This audience won't watch anything over 60s" — recorded once,
         never re-tested. [memory/patterns.md]  no-trigger
orphan:  "Teardown Tuesday" promised weekly, ran 3 times, stopped in March.
         The audience noticed even if the metrics didn't. [feed]
backlog: 14 drafts. Realistically 2 will ship. Delete the other 12 —
         a backlog you won't clear is a weekly tax on attention.
manual:  Analytics copied by hand into a sheet every Sunday. [workflow]

12 items, 4 with no re-check trigger.
```

Nothing found: `No debt. Clean ledger.`

## The hardest recommendation

**Deletion.** Most operators would rather keep a dead channel and a 40-item
backlog than admit those things are finished. Say it plainly:

> "Delete it. It isn't a plan, it's a to-do list you feel bad about."

## Boundaries

Reads and reports, changes nothing. To persist: ask, then write
`CONTENT-DEBT.md`. One-shot. "stop luna-debt" or "normal mode" to revert.
