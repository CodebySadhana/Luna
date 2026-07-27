# Luna architecture

Luna is split into seven visible layers.

The **core orchestration engine** lives in `src/luna/engine.py`. It loads a workflow, builds state from a brief and memory snapshot, and executes stages in order.

The **skill pack** lives in `skills/content-intelligence`. It defines the Chief Content Strategist role, the specialist contracts, the memory vocabulary, and the stage sequence. The same pack is the basis for the Claude Code project skill and the Codex plugin manifest.

The **provider adapters** live in `src/luna/providers`. They are isolated from the engine so the framework remains model-agnostic. The local `MockProvider` keeps the repo runnable without API keys, while the Anthropic and OpenAI adapters are drop-in HTTP clients.

The **tool adapters** live in `src/luna/tools.py`. They provide local research, analytics, memory, and publication-handoff helpers that can be replaced later with real tools or remote services.

The **workflows** live in `workflows/`. They are plain JSON so they can be inspected, versioned, and reused by both code and prompts.

The **memory system** lives in `src/luna/memory.py`. It persists durable brand facts, winning hooks, failed hooks, campaigns, analytics summaries, and evergreen ideas in a single JSON file with atomic writes.

The **platform integration files** live at the repo root and under `.claude*`, `.codex-plugin`, and `.agents`. They stay thin and only point back to the shared skill pack and workflows, so Claude Code, Codex, and future agents all see the same behavior.

## Why it ports cleanly

Claude Code skills are reusable markdown instructions, and Anthropic documents that they can load dynamically with invocation control, subagents, and dynamic context injection. Luna uses that model directly by keeping the working instructions in the skill pack instead of burying them in code. citeturn295316search3

Anthropic's prompt engineering guidance emphasizes clarity, examples, XML-like structure when needed, and agentic decomposition. Luna applies that by keeping each specialist narrow and by making every stage's input and output explicit. citeturn904852search23turn904852search9

Anthropic's evaluation guidance recommends defining measurable success criteria and then testing against them. Luna mirrors that with deterministic validation, a smoke test, and a workflow that produces reviewable artifacts instead of opaque chat. citeturn904852search1turn904852search5

Prompt caching and context management are first-class concerns in long-running agentic work. Luna keeps the repeated context in stable files so it can be cached and reused, and it keeps the high-entropy runtime state in memory and workflow artifacts rather than rebuilding everything from scratch each turn. citeturn273123search3turn295316search2

The same design also fits retrieval-based content work because the shared memory file and review artifacts can carry source attribution, campaign history, and analytics signals forward into later runs. That makes the framework more like a content operating system than a single prompt. citeturn904852search14turn904852search6
