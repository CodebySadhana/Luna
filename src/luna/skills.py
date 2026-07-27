from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class SkillPack:
    path: Path
    manifest: dict[str, object]

    @property
    def name(self) -> str:
        return str(self.manifest.get("name", self.path.name))

    @property
    def description(self) -> str:
        return str(self.manifest.get("description", ""))


def load_skill_pack(path: str | Path) -> SkillPack:
    path = Path(path)
    manifest = json.loads((path / "manifest.json").read_text(encoding="utf-8"))
    return SkillPack(path=path, manifest=manifest)


def discover_skill_packs(root: str | Path) -> list[SkillPack]:
    packs: list[SkillPack] = []
    for path in Path(root).glob("*/manifest.json"):
        packs.append(load_skill_pack(path.parent))
    return sorted(packs, key=lambda pack: pack.name)


def validate_skill_pack(pack: SkillPack) -> None:
    required = ["SKILL.md", "manifest.json", "templates/content-brief.json", "templates/output-outline.md"]
    for relative in required:
        if not (pack.path / relative).exists():
            raise FileNotFoundError(f"missing {relative} in {pack.path}")
    specialists_dir = pack.path / "specialists"
    if not specialists_dir.exists():
        raise FileNotFoundError(f"missing specialists directory in {pack.path}")
    if not any(specialists_dir.glob("*.md")):
        raise FileNotFoundError(f"no specialist documents found in {specialists_dir}")
