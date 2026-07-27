from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any

from .base import BaseProvider


class AnthropicProvider(BaseProvider):
    name = "anthropic"

    def __init__(self, model: str | None = None, api_key: str | None = None, base_url: str | None = None, version: str = "2023-06-01"):
        self.model = model or os.getenv("ANTHROPIC_MODEL", "claude-sonnet-5-20250929")
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY", "")
        self.base_url = (base_url or os.getenv("ANTHROPIC_BASE_URL", "https://api.anthropic.com")).rstrip("/")
        self.version = version

    def available(self) -> bool:
        return bool(self.api_key)

    def generate(self, *, stage: str, prompt: str, context: dict[str, Any]) -> str:
        if not self.available():
            raise RuntimeError("ANTHROPIC_API_KEY is not set")
        body = {
            "model": self.model,
            "max_tokens": int(context.get("max_tokens", 1200)),
            "system": context.get("system", ""),
            "messages": [{"role": "user", "content": prompt}],
        }
        request = urllib.request.Request(
            f"{self.base_url}/v1/messages",
            data=json.dumps(body).encode("utf-8"),
            headers={
                "content-type": "application/json",
                "x-api-key": self.api_key,
                "anthropic-version": self.version,
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except urllib.error.URLError as exc:
            raise RuntimeError(f"Anthropic request failed: {exc}") from exc
        parts: list[str] = []
        for block in payload.get("content", []):
            if isinstance(block, dict) and block.get("type") == "text":
                parts.append(block.get("text", ""))
        return "\\n".join(parts).strip()
