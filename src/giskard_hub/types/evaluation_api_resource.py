from typing import Dict, List, Union, Optional, TypeAlias
from datetime import datetime

from .metric import Metric
from .._models import BaseModel
from .minimal_model import MinimalModel
from .task_progress import TaskProgress
from .dataset_subset import DatasetSubset
from .agent_api_reference import AgentAPIReference

__all__ = ["EvaluationAPIResource", "Agent", "Dataset"]

Agent: TypeAlias = Union[AgentAPIReference, MinimalModel]


class Dataset(BaseModel):
    id: str

    name: str


class EvaluationAPIResource(BaseModel):
    id: str

    agent: Agent

    created_at: datetime

    criteria: Optional[DatasetSubset] = None

    dataset: Dataset

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
