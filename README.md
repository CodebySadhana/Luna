# Luna

Luna is the editorial intelligence layer that turns content chaos into a repeatable operating system for research, creation, distribution, and improvement. It is model-agnostic, file-backed, and built to work cleanly in Claude Code and Codex without hiding important behavior behind magic.

Luna is built around one core role: **Chief Content Strategist**. That strategist routes work to narrow specialists for research, audience synthesis, trend intelligence, positioning, hook engineering, script writing, visual direction, SEO, distribution, analytics, repurposing, monetization, brand voice, and memory updates.

The repository follows the same discipline Anthropic documents for building with Claude: skills are reusable markdown instructions, Claude Code skills follow the Agent Skills open standard and extend it with invocation control, subagent execution, and dynamic context injection, prompt engineering should favor clarity and explicit structure, evaluations should be tied to measurable success criteria, prompt caching should be used to reduce repeated context cost, and RAG-style retrieval should preserve attribution when answers come from documents. citeturn295316search3turn904852search23turn904852search1turn273123search3turn904852search14

## What Luna does

Luna reads a content brief, executes a lifecycle from goal intake through memory update, and produces a full strategy packet: research angles, audience insight, positioning, hooks, draft copy, visual direction, SEO metadata, publication handoff notes, analytics review, and a memory patch for future runs.

The repository is intentionally simple. The engine is separate from the skill packs, provider adapters, tool adapters, workflows, and memory store, so any one layer can be replaced without rewriting the rest.

## Repository layout

The code lives in `src/luna`. The canonical content-intelligence skill pack lives in `skills/content-intelligence`. Claude Code gets a project skill under `.claude/skills/luna-chief-content-strategist`, while Codex gets a plugin manifest under `.codex-plugin/plugin.json`. Platform-specific files stay thin and point back to the shared workflow and skill assets.

## Install

```bash
git clone <this repo>
cd luna
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Run

Generate the sample content packet:

```bash
luna run --brief examples/content_brief.json --memory examples/memory.json --analytics examples/analytics_feedback.json
```

Write the output to a file:

```bash
luna run --brief examples/content_brief.json --memory examples/memory.json --output out.md
```

Validate the repo:

```bash
luna validate
```

## Claude Code setup

Open the repository root in Claude Code. The project skill is already committed at `.claude/skills/luna-chief-content-strategist/SKILL.md`, and the shared instructions in `CLAUDE.md` keep the repo aligned with the Luna operating model.

If you prefer the plugin path, `.claude-plugin/plugin.json` points Claude-capable environments at the shared `skills/` and `workflows/` directories.

## Codex setup

Use the repository root as the working directory. The Codex manifest is committed at `.codex-plugin/plugin.json`, and it points at the same shared skills, workflows, and hooks. No second copy of the logic is required.

## Extending Luna

To add a new content skill pack, copy `skills/content-intelligence` into a new folder, change the manifest name, and keep the same small skill contract: brief in, stage output out, memory patch back. The engine only cares that the pack exposes predictable stage names and a manifest that validates.

## Verification

```bash
make lint
make test
make smoke
```
