from __future__ import annotations

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import tempfile
from pathlib import Path
import unittest

from luna.engine import LunaEngine
from luna.memory import MemoryStore
from luna.models import ContentBrief


class EngineTests(unittest.TestCase):
    def test_run_workflow_produces_expected_stages(self) -> None:
        brief = ContentBrief.from_dict({
            "project_name": "Luna Editorial",
            "topic": "Turn content chaos into a repeatable operating system",
            "goal": "Build a premium content strategy packet",
            "audience": "founders and creators",
            "primary_platform": "instagram",
            "secondary_platforms": ["linkedin"],
            "offer": "Luna framework",
            "tone": "premium, sharp",
            "content_pillars": ["editorial systems", "hook engineering"],
            "brand_voice": "clear, stylish",
            "visual_style": "minimal editorial",
            "call_to_action": "download the template",
            "success_metric": "saves",
        })
        with tempfile.TemporaryDirectory() as temp_dir:
            memory = MemoryStore(Path(temp_dir) / "memory.json")
            engine = LunaEngine(memory_store=memory)
            result = engine.run_workflow(brief)
            self.assertEqual(result.workflow, "content_lifecycle")
            self.assertIsNotNone(result.artifact("hook_generation"))
            self.assertIsNotNone(result.artifact("publication_handoff"))
            self.assertIn("winning_hooks", result.memory_patch)
            self.assertTrue((Path(temp_dir) / "memory.json").exists())

    def test_markdown_render_contains_sections(self) -> None:
        brief = ContentBrief.from_dict({
            "project_name": "Luna Editorial",
            "topic": "Turn content chaos into a repeatable operating system",
            "goal": "Build a premium content strategy packet",
            "audience": "founders and creators",
            "primary_platform": "instagram",
        })
        engine = LunaEngine()
        markdown = engine.run_markdown(brief)
        self.assertIn("## Hook engineering", markdown)
        self.assertIn("## Publication handoff", markdown)


if __name__ == "__main__":
    unittest.main()
