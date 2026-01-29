from typing import Dict, Union, Optional

from .._models import BaseModel
from ..types.agent import Agent
from ..types.dataset import Dataset
from .evaluation_api_resource import EvaluationAPIResource

__all__ = ["APIResponseEvaluationAPIResource", "IncludedItem"]


class IncludedItem(BaseModel):
    data: Union[Agent, Dataset]


class APIResponseEvaluationAPIResource(BaseModel):
    data: EvaluationAPIResource

    included: Optional[Dict[str, Dict[str, IncludedItem]]] = None
