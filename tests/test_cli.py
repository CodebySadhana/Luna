from __future__ import annotations

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import json
import tempfile
from pathlib import Path
import unittest

from luna.cli import main


class CLITests(unittest.TestCase):
    def test_run_command_writes_output(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            brief = temp / "brief.json"
            memory = temp / "memory.json"
            output = temp / "out.md"
            brief.write_text(json.dumps({
                "project_name": "Luna Editorial",
                "topic": "Turn content chaos into a repeatable operating system",
                "goal": "Build a premium content strategy packet",
                "audience": "founders and creators",
                "primary_platform": "instagram",
            }), encoding="utf-8")
            exit_code = main(["run", "--brief", str(brief), "--memory", str(memory), "--output", str(output)])
            self.assertEqual(exit_code, 0)
            text = output.read_text(encoding="utf-8")
            self.assertIn("# Luna run:", text)


if __name__ == "__main__":
    unittest.main()
