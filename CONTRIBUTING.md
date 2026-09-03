# Contributing to Luna

The best contributions are **sharper instructions**, not more files.

Luna is a set of opinions. A skill that says one true thing beats a skill that
covers everything, and 21 sharp skills beat 60 vague ones. Adding surface area
is the easy contribution and usually the wrong one.

## What helps most

1. **A sharper principle.** Something Luna believes that is wrong, or is
   stated too softly to change behavior.
2. **A better example.** `examples/` is where people decide whether Luna is
   real. A walkthrough where her reasoning visibly beats the obvious answer is
   worth more than a new command.
3. **Platform intelligence that reflects reality.** Platforms change. If
   something in `luna/platforms/` is out of date, fix it — and say how you
   know.
4. **A benchmark run.** `benchmarks/` has four specified tasks and zero
   results. Running one honestly is the single most valuable thing anyone
   could contribute right now.
5. **A host adapter.** If Luna works in an agent not listed in
   `docs/agent-portability.md`, add the row — at the tier it actually works
   at, not the tier you wish it worked at.

## The non-negotiables

Pull requests violating these will be closed. Both are enforced by
`tests/test_integrity.py`.

### 1. First names only

The ten minds are **Miranda, Harvey, Sherlock, Midge, Blair, David, Spencer,
Olivia, Elle, Tony** — and nothing more specific. No surnames, no plot
references, no visual descriptions that trace back to a rights holder.

They are archetypes: the authority of a CMO, the observation of a detective.
Keep them that way.

### 2. Never invent a number

No performance figure, engagement rate, benchmark result, or trend statistic
that was not actually measured or actually reported by a user.

This is the rule Luna enforces on every user, so the repository has to hold to
it. A hedged fabrication — "engagement is typically around 3%" — is still a
fabrication. It gets read, remembered, and repeated as fact.

If you have real numbers: publish the model, date, temperature, run count, and
the failures alongside them.

## Voice

Contributions should sound like Luna. Short, sharp, certain. Verdict first.

- No hedge stacks ("you might want to consider possibly")
- No "in today's fast-paced digital landscape"
- No emoji in strategic output
- Confident about mechanisms, uncertain about outcomes

If a paragraph would survive with every noun swapped, delete it.

## Adding a skill

Only if it does something the existing 21 don't. "Like `/luna-ideas` but for
LinkedIn" is a platform note, not a skill.

1. Create `skills/luna-<name>/SKILL.md`:
   - `name` matching the directory exactly
   - `description` containing **"Use when"** and **`/luna-<name>`** — without
     these the host will never fire it
   - A real body. Not a stub — the tests require substance.
   - A `## Boundaries` section saying what it does *not* do
2. `python scripts/sync_adapters.py`
3. `python -m unittest discover -s tests`

The tests will tell you what you missed.

## Never edit a generated file

These are written by `scripts/sync_adapters.py`, and your changes will be
overwritten:

```
commands/*.toml
.opencode/command/*.md
.cursor/rules/luna.mdc
.agents/rules/luna.md
```

Edit `skills/*/SKILL.md` or `AGENTS.md`, then run the script.

## Before opening a PR

```bash
python scripts/sync_adapters.py
python -m unittest discover -s tests -v
```

Stdlib only. If a change needs a dependency, it probably needs a rethink.

## What gets rejected

- New dependencies
- A runtime, an engine, or a pipeline — Luna ships instructions, and the
  Python package that used to live here was deleted for exactly this reason
- Skills that generate volume without ranking
- Anything promising reach, virality, or algorithm knowledge
- Growth tactics that require deceiving an audience
- Enterprise features. The audience is one person with a phone.
