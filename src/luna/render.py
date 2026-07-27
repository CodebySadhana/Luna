from __future__ import annotations

from .models import RunResult


def render_markdown(result: RunResult) -> str:
    return result.to_markdown()
