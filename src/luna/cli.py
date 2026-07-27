from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from .engine import LunaEngine
from .memory import MemoryStore
from .models import ContentBrief
from .providers import AnthropicProvider, MockProvider, OpenAIProvider
from .skills import discover_skill_packs, load_skill_pack, validate_skill_pack
from .workflows import load_workflow, list_workflows, validate_workflow


def _load_json(path: str | Path | None) -> dict[str, Any]:
    if path is None:
        return {}
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _provider(name: str):
    if name == "anthropic":
        provider = AnthropicProvider()
        return provider if provider.available() else MockProvider()
    if name == "openai":
        provider = OpenAIProvider()
        return provider if provider.available() else MockProvider()
    return MockProvider()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="luna", description="Luna: the editorial intelligence layer")
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="Run a workflow from a content brief")
    run.add_argument("--brief", required=True, help="Path to a content brief JSON file")
    run.add_argument("--memory", help="Path to a memory JSON file")
    run.add_argument("--analytics", help="Path to analytics feedback JSON file")
    run.add_argument("--workflow", default="content_lifecycle", help="Workflow name in workflows/")
    run.add_argument("--provider", choices=["mock", "anthropic", "openai"], default="mock")
    run.add_argument("--output", help="Optional output file path")
    run.add_argument("--json", action="store_true", help="Emit JSON instead of markdown")
    run.add_argument("--no-review", action="store_true", help="Skip the revision loop")
    run.add_argument("--pack", default="skills/content-intelligence", help="Skill pack path")

    validate = sub.add_parser("validate", help="Validate workflows, skill packs, and example files")
    validate.add_argument("--pack", default="skills/content-intelligence", help="Skill pack path")

    inspect = sub.add_parser("inspect", help="Inspect the configured workflows and skill pack")
    inspect.add_argument("--pack", default="skills/content-intelligence", help="Skill pack path")

    return parser


def cmd_run(args: argparse.Namespace) -> int:
    brief = ContentBrief.from_dict(_load_json(args.brief))
    memory_store = MemoryStore(args.memory) if args.memory else None
    analytics = _load_json(args.analytics) if args.analytics else {}
    engine = LunaEngine(provider=_provider(args.provider), memory_store=memory_store, skill_pack_path=args.pack)
    result = engine.run_workflow(brief, args.workflow, analytics_feedback=analytics, review=not args.no_review)
    output = result.to_json() if args.json else result.to_markdown()
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    pack = load_skill_pack(args.pack)
    validate_skill_pack(pack)
    workflow_names = list_workflows()
    for workflow_name in workflow_names:
        validate_workflow(load_workflow(workflow_name))
    sys.stdout.write(f"Validated {pack.name} and {len(workflow_names)} workflows.\n")
    return 0


def cmd_inspect(args: argparse.Namespace) -> int:
    pack = load_skill_pack(args.pack)
    packs = discover_skill_packs(Path(args.pack).parent.parent if Path(args.pack).parts[:1] == ("skills",) else Path("skills"))
    sys.stdout.write(f"Skill pack: {pack.name}\n")
    sys.stdout.write(f"Description: {pack.description}\n")
    sys.stdout.write(f"Workflows: {', '.join(list_workflows())}\n")
    sys.stdout.write(f"Discovered packs: {', '.join(p.name for p in packs)}\n")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "run":
        return cmd_run(args)
    if args.command == "validate":
        return cmd_validate(args)
    if args.command == "inspect":
        return cmd_inspect(args)
    parser.error("unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
