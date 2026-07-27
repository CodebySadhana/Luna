from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .memory import MemoryStore
from .models import ContentBrief, WorkflowState


def _bullets(items: list[str]) -> list[str]:
    return [item for item in items if str(item).strip()]


@dataclass(slots=True)
class ResearchTool:
    def plan(self, brief: ContentBrief, memory: dict[str, Any]) -> dict[str, Any]:
        known = memory.get("brand", {}).get("mission", "")
        return {
            "search_angles": _bullets([
                f"What proof would make {brief.audience} trust the idea faster?",
                f"Which competing stories already own {brief.topic}?",
                f"What language does the audience use when they describe {brief.goal}?",
            ]),
            "known_context": known,
        }


@dataclass(slots=True)
class AnalyticsTool:
    def summarize(self, feedback: dict[str, Any]) -> dict[str, Any]:
        metrics = feedback.get("metrics", {})
        return {
            "best_signal": feedback.get("best_signal", ""),
            "weak_signal": feedback.get("weak_signal", ""),
            "metrics": metrics,
        }


@dataclass(slots=True)
class PublicationTool:
    def package(self, state: WorkflowState) -> dict[str, Any]:
        hook = state.artifacts.get("hook_generation")
        draft = state.artifacts.get("draft_generation")
        seo = state.artifacts.get("seo_metadata")
        return {
            "title": hook.payload.get("best_hook", "") if hook else "",
            "draft": draft.payload.get("body", "") if draft else "",
            "seo": seo.payload if seo else {},
            "handoff_note": "Ready for upload, schedule, and final asset assembly.",
        }


@dataclass(slots=True)
class ToolHub:
    memory_store: MemoryStore | None = None
    research: ResearchTool = field(default_factory=ResearchTool)
    analytics: AnalyticsTool = field(default_factory=AnalyticsTool)
    publication: PublicationTool = field(default_factory=PublicationTool)

    def memory_snapshot(self) -> dict[str, Any]:
        return self.memory_store.load() if self.memory_store else {}
