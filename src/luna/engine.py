from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .memory import MemoryStore
from .models import ContentBrief, RunResult, StageArtifact, WorkflowState
from .render import render_markdown
from .skills import load_skill_pack, validate_skill_pack
from .specialists import SPECIALISTS
from .tools import ToolHub
from .workflows import load_workflow, validate_workflow


@dataclass(slots=True)
class LunaEngine:
    provider: Any | None = None
    memory_store: MemoryStore | None = None
    skill_pack_path: str | Path = Path("skills/content-intelligence")

    def load_state(self, brief: ContentBrief, analytics_feedback: dict[str, Any] | None = None) -> WorkflowState:
        memory = self.memory_store.load() if self.memory_store else {}
        return WorkflowState(brief=brief, memory=memory, analytics_feedback=analytics_feedback or {})

    def run_workflow(
        self,
        brief: ContentBrief,
        workflow_name: str = "content_lifecycle",
        *,
        analytics_feedback: dict[str, Any] | None = None,
        review: bool = True,
    ) -> RunResult:
        workflow = load_workflow(workflow_name)
        validate_workflow(workflow)
        pack = load_skill_pack(self.skill_pack_path)
        validate_skill_pack(pack)
        state = self.load_state(brief, analytics_feedback)
        tools = ToolHub(memory_store=self.memory_store)
        artifacts: list[StageArtifact] = []
        for stage in workflow.stages:
            func = SPECIALISTS.get(stage.specialist)
            if func is None:
                raise KeyError(f"unknown specialist: {stage.specialist}")
            artifact = func(state, tools, self.provider)
            state.artifacts[stage.id] = artifact
            artifacts.append(artifact)
            if stage.id == "review_loop" and review and artifact.needs_revision:
                revision = SPECIALISTS["revise"](state, tools, self.provider)
                state.artifacts["revise"] = revision
                artifacts.append(revision)
                hook = state.artifacts.get("hook_generation")
                if hook and revision.payload.get("revised_hook"):
                    hook.payload["best_hook"] = revision.payload["revised_hook"]
                    hook.payload["hooks"] = [revision.payload["revised_hook"]] + hook.payload.get("hooks", [])[1:]
                draft = state.artifacts.get("draft_generation")
                if draft and revision.payload.get("revised_draft"):
                    draft.payload["body"] = revision.payload["revised_draft"]
        memory_patch = state.artifacts.get("memory_update").payload.get("memory_patch", {}) if state.artifacts.get("memory_update") else {}
        if self.memory_store and memory_patch:
            self.memory_store.apply_patch(memory_patch)
        return RunResult(workflow=workflow.name, brief=brief, artifacts=artifacts, memory_patch=memory_patch)

    def run_markdown(
        self,
        brief: ContentBrief,
        workflow_name: str = "content_lifecycle",
        *,
        analytics_feedback: dict[str, Any] | None = None,
        review: bool = True,
    ) -> str:
        return render_markdown(self.run_workflow(brief, workflow_name, analytics_feedback=analytics_feedback, review=review))
