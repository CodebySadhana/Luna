# Agent Portability

Luna is an agent-portable instruction distribution. `skills/` holds the core
behavior; everything host-specific is a thin adapter that makes those
instructions easy to load in a given agent.

**No agent gets its own copy of the logic.** Adapters are generated from the
skills by `scripts/sync_adapters.py`, and `tests/test_portability.py` fails
the build if one drifts or grows behavior of its own.

## Supported hosts

| Host | Files | Tier | Notes |
|---|---|---|---|
| **Claude Code** | `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `skills/`, `commands/` | Plugin | Full install. All 21 skills as `/luna-*` slash commands. |
| **Claude Skills** | `skills/*/SKILL.md` | Skill | Upload a skill folder directly, or point any Agent-Skills-compatible client at `skills/`. |
| **OpenCode** | `opencode.json`, `.opencode/command/*.md`, `AGENTS.md`, `skills/` | Command | `AGENTS.md` loads as always-on instructions; all 21 commands are auto-discovered from `.opencode/command/`. |
| **Cursor** | `.cursor/rules/luna.mdc` | Rule | Always-on project rule (`alwaysApply: true`), generated verbatim from `AGENTS.md`. |
| **Gemini CLI** | `gemini-extension.json`, `AGENTS.md`, `commands/*.toml`, `skills/` | Extension | `contextFileName` points at `AGENTS.md`; the `commands/*.toml` files are reused as-is. |
| **Kimi** | `AGENTS.md` | Instruction | Kimi CLI reads `AGENTS.md` from the repo root as project instructions. No slash commands at this tier — invoke by describing the task, or paste a `SKILL.md`. |
| **Generic agents** | `AGENTS.md` or `skills/*/SKILL.md` | Instruction | Any agent that reads `AGENTS.md` (Codex, Zed, Amp, Jules, and others) picks Luna up from the repo root with zero setup. |

## Tiers, honestly

- **Plugin / Extension** — installed, with working slash commands.
- **Command** — commands work, discovered from files.
- **Skill** — the skill loads; invocation depends on the client.
- **Instruction** — always-on rules, no slash commands. `/luna-hook` will not
  be recognised; say "write me a hook" instead and the rules still apply.

**Nothing is claimed above the tier it actually works at.** If a host is not
listed, Luna has not been set up for it — the `AGENTS.md` route almost
certainly still works, and a PR adding the row is welcome.

## The adapter rule

Keep adapters thin. When a host supports skills or commands, point it at
`skills/` and `commands/`. When a host only supports project instructions,
give it `AGENTS.md` — generated, never hand-edited.

**Never write behavior into an adapter.** A rule that exists only in the
Cursor file is a rule Claude Code users do not get. `test_portability.py`
enforces this by failing when an adapter grows larger than the skill it came
from.

## Regenerating

```bash
python scripts/sync_adapters.py           # rewrite the adapters
python scripts/sync_adapters.py --check   # CI: fail if stale
```

Edit `skills/*/SKILL.md` or `AGENTS.md`, then run it. Never edit a generated
file directly — the next sync overwrites it.

Generated: `commands/*.toml`, `.opencode/command/*.md`, `.cursor/rules/luna.mdc`,
`.agents/rules/luna.md`.

## Portable behavior

| File | What it carries |
|---|---|
| `AGENTS.md` | The compact always-on ruleset. The single source for every instruction-tier host. |
| `skills/luna/SKILL.md` | Marketing intelligence mode itself |
| `skills/luna-*/SKILL.md` | The twenty specialist skills |
| `luna/soul/` | Ladder, principles, voice, scoring, orchestration |
| `luna/minds/` | The ten minds |
| `luna/platforms/` | Per-platform reasoning |
| `luna/memory/` | The learning loop |
