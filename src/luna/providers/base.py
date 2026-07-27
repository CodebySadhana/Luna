from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseProvider(ABC):
    name = "base"

    def available(self) -> bool:
        return True

    @abstractmethod
    def generate(self, *, stage: str, prompt: str, context: dict[str, Any]) -> str:
        raise NotImplementedError
