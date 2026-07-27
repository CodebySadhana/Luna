from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any

from .base import BaseProvider


class OpenAIProvider(BaseProvider):
    name = "openai"

    def __init__(self, model: str | None = None, api_key: str | None = None, base_url: str | None = None):
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-4.1")
        self.api_key = api_key or os.getenv("OPENAI_API_KEY", "")
        self.base_url = (base_url or os.getenv("OPENAI_BASE_URL", "https://api.openai.com")).rstrip("/")

    def available(self) -> bool:
        return bool(self.api_key)

    def generate(self, *, stage: str, prompt: str, context: dict[str, Any]) -> str:
        if not self.available():
            raise RuntimeError("OPENAI_API_KEY is not set")
        body = {
            "model": self.model,
            "input": [
                {"role": "system", "content": context.get("system", "")},
                {"role": "user", "content": prompt},
            ],
        }
        request = urllib.request.Request(
            f"{self.base_url}/v1/responses",
            data=json.dumps(body).encode("utf-8"),
            headers={
                "content-type": "application/json",
                "authorization": f"Bearer {self.api_key}",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except urllib.error.URLError as exc:
            raise RuntimeError(f"OpenAI request failed: {exc}") from exc
        if isinstance(payload.get("output_text"), str):
            return payload["output_text"].strip()
        chunks: list[str] = []
        for item in payload.get("output", []):
            for block in item.get("content", []):
                text = block.get("text") if isinstance(block, dict) else None
                if text:
                    chunks.append(text)
        return "\\n".join(chunks).strip()
