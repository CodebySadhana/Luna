"""Structural tests for the skill pack.

Luna ships instructions, not a runtime — so the thing that can actually break
is structure: a skill whose frontmatter drifts from its directory, a command
with no adapter for one host, a placeholder that shipped.
"""

import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import sync_adapters  # noqa: E402

SKILLS = sorted(p for p in (ROOT / "skills").glob("*/SKILL.md"))


class TestSkillFrontmatter(unittest.TestCase):
    def test_skills_exist(self):
        self.assertGreaterEqual(len(SKILLS), 20, "expected the full skill pack")

    def test_frontmatter_parses(self):
        for skill in SKILLS:
            with self.subTest(skill=skill.parent.name):
                name, description = sync_adapters.parse_skill(skill)
                self.assertTrue(name)
                self.assertTrue(description)

    def test_name_matches_directory(self):
        for skill in SKILLS:
            with self.subTest(skill=skill.parent.name):
                name, _ = sync_adapters.parse_skill(skill)
                self.assertEqual(name, skill.parent.name)

    def test_every_skill_is_namespaced(self):
        for skill in SKILLS:
            with self.subTest(skill=skill.parent.name):
                self.assertTrue(
                    skill.parent.name == "luna"
                    or skill.parent.name.startswith("luna-"),
                    f"{skill.parent.name} is not in the luna namespace",
                )

    def test_description_carries_triggers(self):
        """A description with no trigger phrases will never fire on its own."""
        for skill in SKILLS:
            with self.subTest(skill=skill.parent.name):
                _, description = sync_adapters.parse_skill(skill)
                self.assertTrue(
                    any(
                        form in description
                        for form in ("Use when", "Use on", "Trigger:")
                    ),
                    "description must tell the host when to invoke the skill",
                )
                self.assertIn(
                    f"/{skill.parent.name}",
                    description,
                    "description must name its own slash command",
                )

    def test_description_length(self):
        """Too short to route on, or long enough to crowd the context window."""
        for skill in SKILLS:
            with self.subTest(skill=skill.parent.name):
                _, description = sync_adapters.parse_skill(skill)
                self.assertGreater(len(description), 80)
                self.assertLess(len(description), 1200)

    def test_body_is_not_a_stub(self):
        for skill in SKILLS:
            with self.subTest(skill=skill.parent.name):
                body = re.sub(
                    r"^---\n.*?\n---\n", "", skill.read_text(encoding="utf-8"),
                    flags=re.DOTALL,
                )
                self.assertGreater(
                    len(body.split()), 200, "skill body is too thin to be useful"
                )


class TestSkillBoundaries(unittest.TestCase):
    def test_every_skill_declares_boundaries(self):
        """Without a boundary section, skills bleed into each other."""
        for skill in SKILLS:
            with self.subTest(skill=skill.parent.name):
                text = skill.read_text(encoding="utf-8")
                self.assertIn("## Boundaries", text)


class TestAdapterCoverage(unittest.TestCase):
    """Every skill must reach every host. A missing adapter is a dead command."""

    def test_claude_and_gemini_command(self):
        for skill in SKILLS:
            name = skill.parent.name
            with self.subTest(skill=name):
                self.assertTrue(
                    (ROOT / "commands" / f"{name}.toml").exists(),
                    f"missing commands/{name}.toml",
                )

    def test_opencode_command(self):
        for skill in SKILLS:
            name = skill.parent.name
            with self.subTest(skill=name):
                self.assertTrue(
                    (ROOT / ".opencode" / "command" / f"{name}.md").exists(),
                    f"missing .opencode/command/{name}.md",
                )

    def test_no_orphan_adapters(self):
        """An adapter whose skill was deleted keeps advertising a dead command."""
        names = {skill.parent.name for skill in SKILLS}
        for toml in (ROOT / "commands").glob("*.toml"):
            with self.subTest(adapter=toml.name):
                self.assertIn(toml.stem, names)
        for md in (ROOT / ".opencode" / "command").glob("*.md"):
            with self.subTest(adapter=md.name):
                self.assertIn(md.stem, names)

    def test_adapters_are_in_sync(self):
        """The generated adapters must match the skills they came from."""
        argv = sys.argv
        sys.argv = ["sync_adapters.py", "--check"]
        try:
            exit_code = sync_adapters.main()
        finally:
            sys.argv = argv
        self.assertEqual(
            exit_code, 0, "adapters are stale — run: python scripts/sync_adapters.py"
        )


if __name__ == "__main__":
    unittest.main()
