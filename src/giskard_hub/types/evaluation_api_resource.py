from typing import Dict, List, Optional
from datetime import datetime

from ..types import Metric, MinimalAgent, TaskProgress, DatasetSubset, AgentAPIReference, DatasetAPIReference
from .._models import BaseModel

__all__ = ["EvaluationAPIResource"]


class EvaluationAPIResource(BaseModel):
    id: str

    agent: AgentAPIReference | MinimalAgent

    created_at: datetime

    criteria: Optional[DatasetSubset] = None

    dataset: DatasetAPIReference

    failure_categories: Dict[str, int]

    local: bool

    metrics: List[Metric]

    name: str

    old_evaluation_id: Optional[str] = None

    project_id: str

    scheduled_evaluation_id: Optional[str] = None

    status: TaskProgress

    tags: List[Metric]

    updated_at: datetime
