# Architecture

## The shape

Luna has **no runtime**. There is no engine, no orchestrator process, no API
client, no database. Every file is either an instruction, an adapter generated
from an instruction, or a test that guards one.

This is deliberate. An earlier version of this repository shipped a Python
package with provider adapters and a fifteen-stage pipeline. It was deleted,
because the intelligence was in the prompts the whole time and the pipeline
was infrastructure built to look like a product.

```
Luna/
├── AGENTS.md            the compact ruleset — the portable core
│
├── skills/              THE SOURCE OF TRUTH. 21 skills.
│   ├── luna/            the mode itself
│   └── luna-*/          twenty specialists
│
├── luna/                the deep reference the skills point into
│   ├── soul/            identity, ladder, principles, voice, scoring,
│   │                    orchestration
│   ├── minds/           the ten minds
│   ├── platforms/       eight platforms, reasoned from constraints
│   └── memory/          the learning loop + templates
│
├── commands/            GENERATED  Claude Code, Gemini CLI
├── .opencode/command/   GENERATED  OpenCode
├── .cursor/rules/       GENERATED  Cursor
├── .agents/rules/       GENERATED  agent-rules hosts
│
├── examples/            illustrative walkthroughs
├── benchmarks/          method, not results — nothing has been run
├── tests/               structural + integrity guards
├── docs/
└── scripts/             one generator
```

## The layers

**1 — Skills** decide *what Luna does*. One skill per job, each with
frontmatter that tells the host when to fire, a body of real instruction, and
a `## Boundaries` section that stops it bleeding into its neighbours.

**2 — `luna/`** is the deep reference. Skills stay readable by pointing here
instead of restating the ladder in twenty-one files. A skill is what to do;
`luna/` is why, and how the ten minds think.

**3 — Adapters** are generated. They contain no behavior of their own — only
the skill's description, a pointer to the skill file, and the invariants that
must survive even when a host loads a `.toml` prompt and never reads
`SKILL.md`.

**4 — Tests** guard what a reader can't check by eye: adapter drift, dead
commands, placeholder text, broken links, surnames on the minds, and any
number that isn't labelled.

## Why the adapters are generated

21 skills × 2 command formats + 2 rule files = 44 files that must agree with
21 sources.

Hand-maintained, they drift within a month — and drift here means one agent
silently runs last month's rules. `scripts/sync_adapters.py` writes all 44,
and `--check` fails CI when any is stale.

Edit a skill. Run the script. Every host is current.

## Where behavior lives

| Question | File |
|---|---|
| What does Luna do on this task? | `skills/<name>/SKILL.md` |
| Should this exist at all? | `luna/soul/ladder.md` |
| What does Luna refuse? | `luna/soul/principles.md`, `AGENTS.md` |
| How does she sound? | `luna/soul/voice.md` |
| Which minds run, in what order? | `luna/soul/orchestration.md` |
| How is an idea scored? | `luna/soul/scoring.md` |
| How does this platform behave? | `luna/platforms/<platform>.md` |
| What has she learned? | `luna/memory/` |

## Adding a skill

1. `skills/luna-<name>/SKILL.md` with `name`, a `description` containing
   "Use when" and `/luna-<name>`, a real body, and `## Boundaries`.
2. `python scripts/sync_adapters.py`
3. `python -m unittest discover -s tests`

The tests will tell you what you missed. No manifest to edit — the plugin
points at the directory.
