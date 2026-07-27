from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "src"))

from luna.skills import load_skill_pack, validate_skill_pack


def main() -> int:
    pack = load_skill_pack(ROOT / "skills" / "content-intelligence")
    validate_skill_pack(pack)
    print(f"Validated skill pack: {pack.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
