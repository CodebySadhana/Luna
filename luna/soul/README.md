# Luna's Soul

The deep architecture that makes Luna work. These files are the source of truth for Luna's behavior across all host agents.

## The files

| File | What it covers |
|---|---|
| **[personality.md](personality.md)** | Who Luna is when no specific task frames her behavior |
| **[identity.md](identity.md)** | What she does, who she's for, what she refuses |
| **[voice.md](voice.md)** | How she talks — before/after examples, rules, certainty calibration |
| **[principles.md](principles.md)** | The twelve rules she lives by, with the mechanisms behind each |
| **[ladder.md](ladder.md)** | The 12-rung decision framework that every idea runs through |
| **[scoring.md](scoring.md)** | The Luna Score: how to argue with an idea before it costs anything |
| **[orchestration.md](orchestration.md)** | Which minds activate for which requests, and in what order |

## How they work together

```
personality.md     → sets the baseline tone and posture
       ↓
identity.md        → clarifies what she does and who she's for
       ↓
voice.md           → specifies HOW to say it
       ↓
principles.md      → establishes the RULES that constrain behavior
       ↓
ladder.md          → the DECISION FRAMEWORK for every task
       ↓
scoring.md         → structured way to JUDGE an idea
       ↓
orchestration.md   → which of the TEN MINDS to activate
```

Every interaction Luna has runs through this stack. The skills (`../skills/`) implement these rules. The adapters (`.opencode/`, `.cursor/`, `AGENTS.md`, etc.) inject this soul into each host environment.

## If something feels off

- **Luna sounds wrong** → check voice.md
- **Luna won't kill a bad idea** → check principles.md or ladder.md
- **Luna activated the wrong mind** → check orchestration.md
- **Luna scored something incorrectly** → check scoring.md
- **Luna's positioning is unclear** → check identity.md
- **Luna's tone shifted** → check personality.md

## The hierarchy

Everything flows from personality. Everything else is specification. If personality contradicts another file, check whether the other file is still current.
