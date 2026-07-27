from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {".md", ".json", ".toml", ".py"}
FORBIDDEN = ["TO" + "DO", "FIX" + "ME", "local" + "Storage", "session" + "Storage"]


def iter_files() -> list[Path]:
    paths: list[Path] = []
    for folder in ["src", "tests", "scripts", "skills", "workflows", "prompts", ".claude", ".claude-plugin", ".codex-plugin", ".agents"]:
        base = ROOT / folder
        if base.exists():
            paths.extend(p for p in base.rglob("*") if p.is_file())
    paths.extend([ROOT / "README.md", ROOT / "ARCHITECTURE.md", ROOT / "CLAUDE.md", ROOT / "AGENTS.md", ROOT / "pyproject.toml", ROOT / "Makefile", ROOT / ".env.example"])
    return [path for path in paths if path.exists()]


def check_text(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        raise ValueError(f"{path} is empty")
    if text.endswith("\n\n\n"):
        raise ValueError(f"{path} has too many trailing blank lines")
    for token in FORBIDDEN:
        if token in text:
            raise ValueError(f"{path} contains forbidden token {token}")
    for line_no, line in enumerate(text.splitlines(), start=1):
        if line.rstrip() != line:
            raise ValueError(f"{path}:{line_no} has trailing whitespace")
        if "\t" in line and path.suffix in {".md", ".json"}:
            raise ValueError(f"{path}:{line_no} has a tab character")
    if path.suffix == ".json":
        json.loads(text)


def compile_python() -> None:
    result = subprocess.run([sys.executable, "-m", "compileall", "src", "scripts", "tests"], cwd=ROOT, check=False, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stdout + result.stderr)


def main() -> int:
    for path in iter_files():
        if path.suffix in TEXT_EXTENSIONS or path.name in {"Makefile"}:
            check_text(path)
    compile_python()
    print(f"Linted {len(iter_files())} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
