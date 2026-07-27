from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"

BRIEF = ROOT / "examples" / "content_brief.json"
ANALYTICS = ROOT / "examples" / "analytics_feedback.json"
MEMORY = ROOT / "examples" / "memory.json"


def main() -> int:
    with tempfile.TemporaryDirectory() as temp_dir:
        output = Path(temp_dir) / "out.md"
        command = [
            sys.executable,
            "-m",
            "luna",
            "run",
            "--brief",
            str(BRIEF),
            "--memory",
            str(MEMORY),
            "--analytics",
            str(ANALYTICS),
            "--output",
            str(output),
        ]
        env = dict(os.environ)
        env["PYTHONPATH"] = str(SRC) + (os.pathsep + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")
        subprocess.run(command, cwd=ROOT, check=True, env=env)
        text = output.read_text(encoding="utf-8")
        required = ["# Luna run:", "## Goal intake", "## Hook engineering", "## Publication handoff", "## Memory update"]
        missing = [needle for needle in required if needle not in text]
        if missing:
            raise RuntimeError(f"smoke test missing: {missing}")
    print("Smoke test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
