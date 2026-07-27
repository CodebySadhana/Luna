from __future__ import annotations

from typing import Any

from .base import BaseProvider


class MockProvider(BaseProvider):
    name = "mock"

    def available(self) -> bool:
        return True

    def generate(self, *, stage: str, prompt: str, context: dict[str, Any]) -> str:
        fallback = context.get("fallback", "")
        return str(fallback or prompt)
