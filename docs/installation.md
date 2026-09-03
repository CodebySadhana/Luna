# Installation

Luna is a set of instructions. There is nothing to compile, no dependency to
install, and no API key to add.

## Claude Code

```bash
/plugin marketplace add CodebySadhana/Luna
/plugin install luna@luna
```

Then `/luna` to activate. `/luna-help` lists every command.

To update: `/plugin marketplace update luna` then `/reload-plugins`.

If `/plugin` is not recognised, your Claude Code is out of date:
`npm install -g @anthropic-ai/claude-code@latest`, then restart.

## Claude Skills

Upload any folder under `skills/` as a skill, or point an Agent-Skills
compatible client at the `skills/` directory. Start with `skills/luna/`.

## OpenCode

```bash
git clone https://github.com/CodebySadhana/Luna.git
cd Luna
opencode
```

`AGENTS.md` loads automatically as always-on instructions, and the 21 commands
in `.opencode/command/` are discovered on start. Type `/luna-hook` to check.

To use Luna on your own project instead, copy `AGENTS.md` and
`.opencode/command/` into it.

## Cursor

Copy `.cursor/rules/luna.mdc` into your project's `.cursor/rules/`.

It is set to `alwaysApply: true`, so Luna is active in every conversation in
that project. No command needed — describe the task.

## Gemini CLI

```bash
gemini extensions install https://github.com/CodebySadhana/Luna
```

Or clone the repo and work inside it — `gemini-extension.json` points
`contextFileName` at `AGENTS.md`, and the `commands/*.toml` files are picked
up automatically.

## Kimi

Copy `AGENTS.md` into your project root. Kimi CLI reads it as project
instructions.

This is instruction tier: the rules are always on, but there are no slash
commands. Say "write me a hook for this" rather than `/luna-hook`. For a
specific skill, paste the contents of its `SKILL.md`.

## Any other agent

If your agent reads `AGENTS.md` from a repo root — Codex, Zed, Amp, Jules, and
most others do — copy that one file into your project. That is the whole
install.

For a single task, paste the relevant `skills/luna-*/SKILL.md` into the
conversation.

## Setting up memory

Optional, and the thing that makes Luna better over time.

```bash
cp -r luna/memory/templates/* luna/memory/
```

Fill in `brand.md` and `audience.md` first — those two do most of the work.
The rest fill themselves in as you use `/luna-postmortem` and `/luna-memory`.

If your repo is public, your memory is public. Don't put client data in it.

## Verifying

```bash
python -m unittest discover -s tests -v
python scripts/sync_adapters.py --check
```

Stdlib only. No pip install, no dependencies.
