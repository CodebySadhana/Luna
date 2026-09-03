# Changelog

## 1.0.0 — 2026-09-03

Complete rewrite. Luna becomes a marketing intelligence agent.

### The change

The previous version was a pip-installable Python package: an engine, provider
adapters for OpenAI / Anthropic / mock, and a fifteen-stage linear pipeline,
under a generic "Chief Content Strategist" framing with placeholder specialist
files.

It has been replaced by an agent-portable instruction distribution with no
runtime, modelled on
[ponytail](https://github.com/DietrichGebert/ponytail)'s architecture.

The intelligence was in the prompts the whole time. The pipeline was
infrastructure built to look like a product.

### Added

- **Luna's soul** — identity, the 12-rung ladder, twelve principles, voice,
  the scoring framework, and the orchestration layer (`luna/soul/`)
- **The ten minds** — Miranda, Harvey, Sherlock, Midge, Blair, David, Spencer,
  Olivia, Elle, Tony, each with operating instructions and failure modes
  (`luna/minds/`)
- **21 skills** — `/luna` plus twenty specialists, from `/luna-observe`
  through `/luna-postmortem` (`skills/`)
- **Platform intelligence** — eight platforms reasoned from constraints and
  posture, with an explicit disclaimer that no ranking algorithm is known
  (`luna/platforms/`)
- **The memory system** — WIN / LOSS / PATTERN / HYPOTHESIS / EXPERIMENT in
  plain markdown, with templates (`luna/memory/`)
- **Seven illustrative examples**, led by the before/after flex (`examples/`)
- **Benchmark methodology** — four objectively measurable tasks, explicitly
  **not yet run**, with no fabricated results (`benchmarks/`)
- **Multi-agent portability** — Claude Code, Claude Skills, OpenCode, Cursor,
  Gemini CLI, Kimi, and any agent that reads `AGENTS.md`
- **Adapter generator** — `scripts/sync_adapters.py` writes all 44 host
  adapter files from the skills, so no agent can run stale rules
- **Integrity tests** — enforcing first-names-only on the ten minds, and that
  no unlabelled performance number can ship

### Removed

- `src/luna/` — the Python engine, CLI, and provider adapters
- `skills/content-intelligence/` — superseded; its specialist files were
  two-line stubs
- `workflows/`, `prompts/`, `integrations/`, `tests/` (old), `build_backend.py`,
  `pyproject.toml`, `Makefile`, `ARCHITECTURE.md`, `.env.example`
- Fabricated citation markers in the old README, and an incorrect author
  attribution in the plugin manifest

### Notes

Luna is no longer installable with `pip`. There is nothing to install — copy
`AGENTS.md`, or install the plugin. That is the point.
