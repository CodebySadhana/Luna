"""Every supported host must actually have the files it needs.

The portability doc makes a promise per host. These tests are what stop that
promise from drifting into a lie after a refactor.
"""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# host -> the files that make Luna work there. Mirrors docs/agent-portability.md.
HOSTS = {
    "Claude Code": [
        ".claude-plugin/plugin.json",
        ".claude-plugin/marketplace.json",
        "skills/luna/SKILL.md",
        "commands/luna.toml",
    ],
    "Claude Skills": ["skills/luna/SKILL.md"],
    "OpenCode": ["opencode.json", ".opencode/command/luna.md", "AGENTS.md"],
    "Cursor": [".cursor/rules/luna.mdc"],
    "Gemini CLI": ["gemini-extension.json", "AGENTS.md", "commands/luna.toml"],
    "Kimi": ["AGENTS.md"],
    "Generic agents": ["AGENTS.md", "skills/luna/SKILL.md"],
}

MANIFESTS = [
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    ".agents/plugins/marketplace.json",
    "gemini-extension.json",
    "opencode.json",
]


class TestHostFiles(unittest.TestCase):
    def test_every_host_has_its_files(self):
        for host, files in HOSTS.items():
            for relative in files:
                with self.subTest(host=host, file=relative):
                    self.assertTrue(
                        (ROOT / relative).exists(),
                        f"{host} needs {relative} and it is missing",
                    )


class TestManifests(unittest.TestCase):
    def test_manifests_are_valid_json(self):
        for relative in MANIFESTS:
            with self.subTest(manifest=relative):
                json.loads((ROOT / relative).read_text(encoding="utf-8"))

    def test_no_placeholder_urls(self):
        for relative in MANIFESTS:
            with self.subTest(manifest=relative):
                text = (ROOT / relative).read_text(encoding="utf-8")
                self.assertNotIn("example.com", text)

    def test_plugin_points_at_real_directories(self):
        plugin = json.loads(
            (ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")
        )
        for key in ("skills", "commands"):
            with self.subTest(key=key):
                target = ROOT / plugin[key].lstrip("./")
                self.assertTrue(target.is_dir(), f"plugin.json {key} -> {target}")

    def test_gemini_context_file_exists(self):
        manifest = json.loads(
            (ROOT / "gemini-extension.json").read_text(encoding="utf-8")
        )
        self.assertTrue((ROOT / manifest["contextFileName"]).exists())


class TestSharedCore(unittest.TestCase):
    """Core intelligence lives once. Adapters stay thin."""

    def test_agents_rule_matches_agents_md(self):
        canonical = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        copy = (ROOT / ".agents" / "rules" / "luna.md").read_text(encoding="utf-8")
        self.assertEqual(
            canonical,
            copy,
            "AGENTS.md and .agents/rules/luna.md have drifted — run "
            "python scripts/sync_adapters.py",
        )

    def test_cursor_rule_contains_agents_md(self):
        canonical = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        rule = (ROOT / ".cursor" / "rules" / "luna.mdc").read_text(encoding="utf-8")
        self.assertIn(canonical, rule)
        self.assertIn("alwaysApply: true", rule)

    def test_adapters_hold_no_unique_behaviour(self):
        """An adapter longer than the skill means logic forked into a host."""
        for command in (ROOT / ".opencode" / "command").glob("*.md"):
            skill = ROOT / "skills" / command.stem / "SKILL.md"
            with self.subTest(command=command.name):
                self.assertLess(
                    len(command.read_text(encoding="utf-8")),
                    len(skill.read_text(encoding="utf-8")),
                    f"{command.name} is bigger than its skill — behaviour has "
                    f"leaked into a host adapter",
                )


class TestSoulIsComplete(unittest.TestCase):
    def test_soul_files(self):
        for name in (
            "identity",
            "principles",
            "voice",
            "ladder",
            "scoring",
            "orchestration",
        ):
            with self.subTest(file=name):
                self.assertTrue((ROOT / "luna" / "soul" / f"{name}.md").exists())

    def test_ten_minds(self):
        minds = sorted((ROOT / "luna" / "minds").glob("*.md"))
        self.assertEqual(len(minds), 10, "Luna has exactly ten minds")

    def test_platform_intelligence(self):
        platforms = {p.stem for p in (ROOT / "luna" / "platforms").glob("*.md")}
        for required in (
            "instagram",
            "tiktok",
            "youtube",
            "youtube-shorts",
            "linkedin",
            "x",
            "pinterest",
            "reddit",
        ):
            with self.subTest(platform=required):
                self.assertIn(required, platforms)

    def test_memory_templates(self):
        templates = {p.stem for p in (ROOT / "luna" / "memory" / "templates").glob("*.md")}
        for required in ("brand", "audience", "wins", "losses", "patterns", "experiments"):
            with self.subTest(template=required):
                self.assertIn(required, templates)


if __name__ == "__main__":
    unittest.main()
