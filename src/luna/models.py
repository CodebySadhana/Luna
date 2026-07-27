from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


def _listify(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    if isinstance(value, tuple):
        return [str(item) for item in value]
    if isinstance(value, str):
        return [piece.strip() for piece in value.split(",") if piece.strip()]
    return [str(value)]


@dataclass(slots=True)
class ContentBrief:
    project_name: str
    topic: str
    goal: str
    audience: str
    primary_platform: str
    secondary_platforms: list[str] = field(default_factory=list)
    offer: str = ""
    tone: str = ""
    content_pillars: list[str] = field(default_factory=list)
    brand_voice: str = ""
    visual_style: str = ""
    call_to_action: str = ""
    constraints: list[str] = field(default_factory=list)
    reference_links: list[str] = field(default_factory=list)
    success_metric: str = ""
    notes: str = ""

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ContentBrief":
        return cls(
            project_name=str(data.get("project_name", "Luna")),
            topic=str(data.get("topic", "")),
            goal=str(data.get("goal", "")),
            audience=str(data.get("audience", "")),
            primary_platform=str(data.get("primary_platform", "")),
            secondary_platforms=_listify(data.get("secondary_platforms")),
            offer=str(data.get("offer", "")),
            tone=str(data.get("tone", "")),
            content_pillars=_listify(data.get("content_pillars")),
            brand_voice=str(data.get("brand_voice", "")),
            visual_style=str(data.get("visual_style", "")),
            call_to_action=str(data.get("call_to_action", "")),
            constraints=_listify(data.get("constraints")),
            reference_links=_listify(data.get("reference_links")),
            success_metric=str(data.get("success_metric", "")),
            notes=str(data.get("notes", "")),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class StageArtifact:
    stage: str
    specialist: str
    summary: str
    payload: dict[str, Any] = field(default_factory=dict)
    prompt: str = ""
    needs_revision: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class WorkflowState:
    brief: ContentBrief
    memory: dict[str, Any] = field(default_factory=dict)
    analytics_feedback: dict[str, Any] = field(default_factory=dict)
    artifacts: dict[str, StageArtifact] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def previous(self, stage: str) -> StageArtifact | None:
        return self.artifacts.get(stage)


@dataclass(slots=True)
class RunResult:
    workflow: str
    brief: ContentBrief
    artifacts: list[StageArtifact]
    memory_patch: dict[str, Any] = field(default_factory=dict)

    def artifact(self, stage: str) -> StageArtifact | None:
        for artifact in self.artifacts:
            if artifact.stage == stage:
                return artifact
        return None

    def to_dict(self) -> dict[str, Any]:
        return {
            "workflow": self.workflow,
            "brief": self.brief.to_dict(),
            "artifacts": [artifact.to_dict() for artifact in self.artifacts],
            "memory_patch": self.memory_patch,
        }

    def to_json(self, *, indent: int = 2) -> str:
        import json

        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    def to_markdown(self) -> str:
        lines: list[str] = [
            f"# Luna run: {self.brief.project_name}",
            "",
            f"**Workflow:** {self.workflow}",
            f"**Topic:** {self.brief.topic}",
            f"**Goal:** {self.brief.goal}",
            f"**Audience:** {self.brief.audience}",
            f"**Primary platform:** {self.brief.primary_platform}",
            "",
        ]
        for artifact in self.artifacts:
            lines.append(artifact.payload.get("body", f"### {artifact.stage}\n{artifact.summary}"))
            lines.append("")
        if self.memory_patch:
            lines.extend(["## Memory update", ""])
            for key, value in self.memory_patch.items():
                lines.append(f"- **{key}**: {value}")
        return "\n".join(lines).rstrip() + "\n"
