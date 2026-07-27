from __future__ import annotations

import json
import tempfile
from pathlib import Path
from typing import Any

DEFAULT_MEMORY: dict[str, Any] = {
    "brand": {
        "mission": "Luna turns content chaos into a repeatable operating system.",
        "positioning": "editorial intelligence layer",
        "north_star": "faster research, sharper strategy, better hooks, stronger brand consistency, measurable performance",
    },
    "audience": [],
    "offers": [],
    "content_pillars": [],
    "vocabulary": [],
    "visual_style": {},
    "winning_hooks": [],
    "failed_hooks": [],
    "analytics": [],
    "campaigns": [],
    "evergreen_ideas": [],
    "notes": [],
}


def _merge(current: Any, patch: Any) -> Any:
    if isinstance(current, dict) and isinstance(patch, dict):
        merged = dict(current)
        for key, value in patch.items():
            merged[key] = _merge(merged.get(key), value)
        return merged
    if isinstance(current, list) and isinstance(patch, list):
        merged = list(current)
        for item in patch:
            if item not in merged:
                merged.append(item)
        return merged
    return patch if patch is not None else current


class MemoryStore:
    def __init__(self, path: str | Path):
        self.path = Path(path)

    def load(self) -> dict[str, Any]:
        if not self.path.exists():
            return json.loads(json.dumps(DEFAULT_MEMORY))
        return json.loads(self.path.read_text(encoding="utf-8"))

    def save(self, data: dict[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
        with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8", dir=str(self.path.parent)) as handle:
            handle.write(payload)
            temp_path = Path(handle.name)
        temp_path.replace(self.path)

    def apply_patch(self, patch: dict[str, Any]) -> dict[str, Any]:
        current = self.load()
        merged = _merge(current, patch)
        self.save(merged)
        return merged

    def summary(self) -> str:
        memory = self.load()
        brand = memory.get("brand", {})
        return (
            f"{brand.get('mission', '')} | {brand.get('positioning', '')} | "
            f"{brand.get('north_star', '')}"
        ).strip(" |")
