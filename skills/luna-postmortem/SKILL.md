---
name: luna-postmortem
description: >
  Analyze what happened after a post or campaign — the win or the flop — and
  turn it into something that changes the next decision. Use when the user says
  "why did this flop", "why did this do so well", "postmortem", "analyze what
  happened", "this didn't work", or "/luna-postmortem". Ends with a memory
  entry.
---

# Luna Postmortem

The loop-closing skill. Without it, an operator makes the same mistake for a
year and calls it consistency.

## The only question

**What did we believe, what happened, and what do we believe now?**

If the third answer is identical to the first, the postmortem produced
nothing — and you say that out loud rather than manufacturing a lesson.

## Wins are harder to analyze than losses

Everyone over-explains a win. The story is always available afterward, and it
is usually wrong.

A win has more possible causes than a loss, and variance explains more of it
than anyone wants to accept. Be more skeptical of a success than a failure.

**"It might have been variance"** is a legitimate, often correct conclusion.

## The sequence

Work down. Stop at the first real failure — everything below it is
uninformative, because nobody reached it.

```
1  DISTRIBUTION   Did it get served at all?
                  Almost no views = the platform, not the content.
2  HOOK           Served but not watched. The first two seconds failed.
3  RETENTION      Watched then dropped. The middle didn't earn itself.
4  IDEA           Watched fully, no response. They saw it. They didn't care.
5  ASK            Everything worked, nobody acted. The CTA or the offer.
```

Most operators diagnose at 4 when the failure was at 2. The distinction
matters: a hook failure means rewrite the line, an idea failure means the
concept was dead.

## Wrong lessons to avoid

- **"Post more."** Volume is not a finding.
- **"The algorithm changed."** Unknowable. Ends the investigation.
- **"People don't want value anymore."** Almost never true.
- **"Do more of what worked"** — without naming *what* worked and why.
- Generalizing from one post. See the labels in `/luna-analytics`.

## Output

```
PIECE       [what it was, when]
EXPECTED    [what was predicted — say plainly if nothing was written down]
HAPPENED    [what the user reported. No invented numbers.]
DELTA       [the gap, and whether it's meaningful or within noise]

FAILED AT   distribution / hook / retention / idea / ask
            [or: succeeded, and here is the mechanism]
MECHANISM   [why]
CONFIDENCE  OBSERVATION / PATTERN / HYPOTHESIS

BELIEF      before: ...
            after:  ...
            (if unchanged, say so — that's an honest result)

MEMORY      → wins.md / losses.md / patterns.md
            [the actual entry, written out]
NEXT TEST   [the one experiment this suggests]
```

## The memory entry is the deliverable

A postmortem that doesn't update memory was entertainment. Write the entry
out, and show it before saving.

## Boundaries

One-shot. Never invents metrics. If the user provided no numbers, run it
qualitatively and label the whole thing as such.
