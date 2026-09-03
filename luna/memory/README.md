# Luna's Memory

Luna without memory is a very opinionated stranger. She'll ask who your
audience is every single time, and every answer she gives will be a first
draft.

Memory is what makes the second month better than the first.

## Where it lives

Plain markdown, in your repo, edited by hand or by Luna:

```
luna/memory/
├── brand.md         who you are, what you're for, what you're not
├── audience.md      who they are, what they say, what they want
├── voice.md         how you sound, and how you don't
├── wins.md          what worked, and the mechanism
├── losses.md        what failed, and why — the more valuable file
├── patterns.md      what has held up across three or more instances
├── experiments.md   what's being tested right now
└── competitors.md   who else is in this space and what they're doing
```

Start them with `templates/`. Nothing here needs to be complete on day one.

**Why markdown and not a database:** you need to read it, correct it, and
paste it into any agent. A database would make Luna's memory something you
query instead of something you own.

## The five record types

Every memory entry is one of these. The type is not decoration — it sets how
much confidence the entry earns.

### WIN
Something worked. Record **the mechanism, not the number**.

> ❌ "The notes post got 40k views."
> ✅ "The notes post worked because it named a private habit ('you reread your
> own message after sending it'). Recognition hooks have now outperformed
> instructional hooks three times."

### LOSS
Something failed. **This is the most valuable file in the system** and the one
everyone skips. Wins are over-explained and over-fitted; losses are specific.

> "Carousel on pricing psychology: 900 views, 2 saves. Best guess: the audience
> doesn't set prices, they get quoted them. Wrong problem, not a wrong format."

### PATTERN
Three or more instances pointing the same way. Requires evidence, and the
instances get listed.

> "Posts naming a specific dollar amount outperform posts saying 'expensive'
> — 3 of 3 so far. n is small. Keep testing."

### HYPOTHESIS
Something Luna believes might be true. **Explicitly unproven**, with a test
attached.

> "Hypothesis: this audience saves more than it shares because the content is
> reference material, not identity material. Test: publish one identity-shaped
> piece this month and compare share rate."

### EXPERIMENT
Something being tested right now, with the expectation **written before**
publishing.

> "Testing: hook as a question vs. as a statement, same piece, two platforms.
> Expect the statement to win on watch-through. If the question wins, my model
> of this audience's skepticism is wrong."

## The loop

```
OBSERVE → HYPOTHESIZE → CREATE → PUBLISH → MEASURE → LEARN → UPDATE MEMORY
   ↑                                                              │
   └──────────────────────────────────────────────────────────────┘
```

The update step is the one that gets skipped, and skipping it is what keeps
an operator making the same mistake for a year.

## Rules

**Never write a number Luna wasn't given.** Every metric in memory traces to
something the user reported. No estimates, no "approximately," no filling in a
plausible figure.

**Record the mechanism, not the outcome.** "It worked" is not reusable. "It
worked because X" is.

**Losses need equal weight to wins.** If `wins.md` is three times longer than
`losses.md`, the memory is a highlight reel and it will make Luna
overconfident.

**Date everything.** Audience truths expire. A pattern from eight months ago
is a hypothesis again.

**Prune.** A memory file nobody reads is not memory. When a pattern is
disproven, delete it — don't archive it with a note.

## How Luna uses it

At the start of any run, she reads what is relevant to the task — not all of
it. `/luna-hook` reads `voice.md` and `audience.md`. `/luna-postmortem` reads
`wins.md`, `losses.md`, and `patterns.md`.

At the end of any run that produced a result, she proposes an update. She
**shows you the diff before writing it.** Memory that changes without your
seeing it is memory you can't trust.

## Privacy

This is your data, in your repo. Nothing here syncs anywhere. Don't put
customer PII or anything you wouldn't want in a git history in these files —
if the repo is public, memory is public.
