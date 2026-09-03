---
name: luna-ideas
description: >
  Generate content ideas grounded in an actual audience insight, then rank them
  and kill the weak ones. Use when the user says "give me content ideas", "what
  should I post", "I need ideas for this week", "help me come up with content",
  or "/luna-ideas". Returns three ranked concepts with reasons, never ten
  unranked ones.
---

# Luna Ideas

Midge's skill. Turns a tension into things that could exist.

## Before you generate anything

**Insight before ideation.** Ideas from a blank page reflect the model's
priors — they are the same ideas everyone else in this niche is already
making.

Check for an insight. If there isn't one:

- `luna/memory/audience.md` exists? Use it.
- User gave context? Use it.
- Neither? **Ask one question**, not five: *"Who is this for, and what have
  they told you they're stuck on?"*

Then generate. Never generate first and hope the audience fits.

## An insight is not an idea

| Insight | Idea |
|---|---|
| People are embarrassed they never set the tool up | "I audited 50 people's setups. 43 had never opened settings." |
| Founders think posting more will fix it | "I tripled my posting for 60 days. Here's the graph nobody shows you." |
| Nobody admits they don't read the docs | "The five features in this tool that everyone pays for and nobody uses" |

The idea has a **shape** (what you actually see), a **proof**, and a **reason
to watch**.

## The angle set

When an insight goes flat, run it through these before abandoning it:

| Angle | Shape |
|---|---|
| **Inversion** | The advice everyone gives, argued against |
| **Confession** | What I did wrong, specifically, with the cost |
| **Teardown** | A real example, examined in public |
| **Receipts** | The claim, then the proof, in that order |
| **The unspoken** | What everyone here knows and nobody posts |
| **Before / after** | The gap does the talking |
| **Constraint** | The same result with something essential removed |
| **The list that turns** | Four expected items, then one that undoes them |

## Format is half the idea

The same insight as a talking head, a teardown, a side-by-side, a confession,
or a chart is five different pieces with five different ceilings. Choose the
format deliberately, and choose one the operator can actually make this week.

## Ranking is the job

**Ten ideas is homework, not a deliverable.** Generate widely, then cut hard.

Deliver **three**. Ranked. With the reason for the order.

If the user explicitly asks for ten: give ten, ranked, with the bottom half
marked `cut` and one line each on why. Never hand over a flat list — an
unranked list transfers the hard decision back to the person who asked you to
make it.

## Output

```
INSIGHT   [the tension these come from — one line]

01  [concept]
    Shape:   [what the viewer actually sees]
    Format:  [medium and length]
    Angle:   [from the angle set]
    Why 1st: [what it beats and why]

02  [concept]     ... same fields

03  [concept]     ... same fields

CUT   [what you generated and killed, one line each — the cuts are
       information, they show what's already been considered]
```

## Boundaries

Concepts, not copy. Hooks come from `/luna-hook`, scripts from
`/luna-script`, and scoring from `/luna-score`.

Ideas that are fun to make but not good to watch get cut. That's the most
common failure and it is always the maker's taste, not the audience's.
