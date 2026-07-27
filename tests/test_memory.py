from __future__ import annotations

import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import tempfile
from pathlib import Path
import unittest

from luna.memory import MemoryStore


class MemoryTests(unittest.TestCase):
    def test_apply_patch_merges_lists_and_dicts(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "memory.json"
            store = MemoryStore(path)
            store.apply_patch({"winning_hooks": ["hook one"], "brand": {"mission": "new mission"}})
            store.apply_patch({"winning_hooks": ["hook one", "hook two"], "brand": {"positioning": "editorial intelligence layer"}})
            data = store.load()
            self.assertEqual(data["brand"]["mission"], "new mission")
            self.assertEqual(data["brand"]["positioning"], "editorial intelligence layer")
            self.assertEqual(data["winning_hooks"], ["hook one", "hook two"])

    def test_summary_uses_brand_fields(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "memory.json"
            store = MemoryStore(path)
            summary = store.summary()
            self.assertIn("Luna turns content chaos", summary)


if __name__ == "__main__":
    unittest.main()
