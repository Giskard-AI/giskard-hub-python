
from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = [
    "ScheduledEvaluationListLatestRunsResponse",
    "Data",
    "DataLatestRun",
    "DataScheduledEvaluation",
    "IncludedIncludedItem",
]


class DataLatestRun(BaseModel):
    id: str

    name: str


class DataScheduledEvaluation(BaseModel):
    id: str

    name: str


class Data(BaseModel):
    latest_runs: List[DataLatestRun]

    scheduled_evaluation: DataScheduledEvaluation


class IncludedIncludedItem(BaseModel):
    data: object


class ScheduledEvaluationListLatestRunsResponse(BaseModel):
    data: List[Data]

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
