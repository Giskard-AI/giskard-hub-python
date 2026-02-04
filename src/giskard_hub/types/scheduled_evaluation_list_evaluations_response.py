from typing import Dict, List, Union, Optional

from ..types import Agent, Dataset
from .._models import BaseModel
from .evaluation_api_resource import EvaluationAPIResource

__all__ = ["ScheduledEvaluationListEvaluationsResponse", "IncludedItem"]


class IncludedItem(BaseModel):
    data: Union[Agent, Dataset]


class ScheduledEvaluationListEvaluationsResponse(BaseModel):
    data: List[EvaluationAPIResource]

    included: Optional[Dict[str, Dict[str, IncludedItem]]] = None
