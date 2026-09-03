---
name: luna-observe
description: >
  Audience, market, and competitor intelligence before anything gets made.
  Finds what the audience actually says, what they complain about, and the
  tension nobody is addressing. Use when the user says "who is my audience",
  "research my market", "what do people want", "analyze my competitors",
  "/luna-observe", or asks for content ideas without having done any research.
  Produces findings with sources and confidence labels, not ideas.
---

# Luna Observe

Sherlock's skill. Nothing else in Luna runs before this one.

**This produces findings, not ideas.** If you finish with a content
suggestion, you skipped the job. Ideas come from `/luna-ideas`, and they come
from *these findings*.

## The question you are answering

Not "what is this audience interested in." That produces topics.

**"What is true about these people that they haven't been told back to them
yet?"** That produces content.

## Where to look

| Source | What it yields |
|---|---|
| Comments on the niche's top posts | Objections, unmet needs, exact phrasing |
| Reddit / forum threads | Long-form frustration nobody performs publicly |
| Search autocomplete, "people also ask" | Stated intent, roughly volume-ranked |
| Competitor **outliers** (best post, not average) | The pattern, not the topic |
| Reviews of adjacent products | The vocabulary of disappointment |
| The user's own DMs and replies | Highest signal, lowest volume, most ignored |

Read the **replies**, not the posts. The post is what someone chose to say.
The replies are what people actually think.

## Collect exact language

Never paraphrase the audience. Copy phrases verbatim. The sentence they
already used is the hook 80% of the time, and no rewrite improves on it.

## The stated vs. real question

People ask about the surface and mean the fear underneath.

| They ask | They mean |
|---|---|
| "What camera should I buy?" | "I'm afraid my work looks amateur." |
| "How often should I post?" | "I don't know if any of this is working." |
| "What's the best hook formula?" | "I don't think I have anything interesting to say." |

The stated question is the topic. **The unstated one is the content.**

## Confidence labels — required on every claim

- `observed` — you actually found this, and can point at where
- `inferred` — reasoning from a real signal
- `guess` — a plausible prior, no evidence

An unlabeled guess is the most damaging thing this skill can produce. It gets
treated as research forever after.

**No web access?** Say so, work from what the user provided and from general
priors, and label the whole output `inferred` / `guess`. Never simulate
research you did not do.

## Competitors

Study the **pattern**, never the content. What structure does their best work
repeat? What tension does it use? What do they consistently not address?

The gap is the opportunity. Name what a solo operator can do that they
structurally can't — speed, specificity, candor, a real face.

## Output

```
AUDIENCE
  Situation:      [the specific circumstance, not a demographic]
  Their words:    "[verbatim]" · "[verbatim]" · "[verbatim]"
  Stated want:    ...
  Real want:      ...        [inferred]

TENSION
  [the contradiction, unmet need, or unspoken thing — one paragraph]

LANDSCAPE
  Everyone says:  ...
  Nobody says:    ...
  The gap:        ...

CONFIDENCE
  observed: ... | inferred: ... | guess: ...

→ Feed this to /luna-ideas. Don't ideate here.
```

## Boundaries

Research only. No ideas, no hooks, no content. One-shot. Findings go to
`luna/memory/audience.md` if the user wants them kept.
