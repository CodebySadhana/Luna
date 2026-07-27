from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

WORKFLOW_DIR = Path(__file__).resolve().parents[2] / "workflows"


@dataclass(slots=True)
class WorkflowStage:
    id: str
    specialist: str
    purpose: str


@dataclass(slots=True)
class WorkflowDefinition:
    name: str
    description: str
    stages: list[WorkflowStage]

    def stage_ids(self) -> list[str]:
        return [stage.id for stage in self.stages]


def load_workflow(name: str, base_dir: str | Path = WORKFLOW_DIR) -> WorkflowDefinition:
    path = Path(base_dir) / f"{name}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    stages = [WorkflowStage(**stage) for stage in data["stages"]]
    return WorkflowDefinition(name=data["name"], description=data["description"], stages=stages)


def list_workflows(base_dir: str | Path = WORKFLOW_DIR) -> list[str]:
    return sorted(path.stem for path in Path(base_dir).glob("*.json"))


def validate_workflow(definition: WorkflowDefinition) -> None:
    if not definition.name:
        raise ValueError("workflow name is required")
    if not definition.stages:
        raise ValueError(f"workflow {definition.name} has no stages")
    seen: set[str] = set()
    for stage in definition.stages:
        if stage.id in seen:
            raise ValueError(f"duplicate stage id: {stage.id}")
        seen.add(stage.id)
