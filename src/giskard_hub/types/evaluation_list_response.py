from typing import Dict, List, Union, Optional

from .._models import BaseModel
from ..types.agent import Agent
from ..types.dataset import Dataset
from .evaluation_api_resource import EvaluationAPIResource

__all__ = ["EvaluationListResponse", "IncludedItem"]


class IncludedItem(BaseModel):
    data: Union[Agent, Dataset]


class EvaluationListResponse(BaseModel):
    data: List[EvaluationAPIResource]

    included: Optional[Dict[str, Dict[str, IncludedItem]]] = None
