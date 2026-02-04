from typing import Dict, List, Optional
from datetime import datetime

from .metric import Metric
from .._models import BaseModel
from .minimal_model import MinimalModel
from .task_progress import TaskProgress
from .dataset_subset import DatasetSubset
from .agent_api_reference import AgentAPIReference

__all__ = ["EvaluationAPIResource", "DatasetAPIReference"]


class DatasetAPIReference(BaseModel):
    id: str

    name: str


class EvaluationAPIResource(BaseModel):
    id: str

    agent: AgentAPIReference | MinimalModel

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
