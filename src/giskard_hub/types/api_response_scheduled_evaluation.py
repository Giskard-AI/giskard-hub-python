from typing import Dict, List, Literal, Optional

from .._models import BaseModel
from .scheduled_evaluation import ScheduledEvaluation
from ..types.evaluation_api_resource import EvaluationAPIResource

__all__ = ["APIResponseScheduledEvaluation", "IncludedItem"]


class IncludedItem(BaseModel):
    data: EvaluationAPIResource


class APIResponseScheduledEvaluation(BaseModel):
    data: ScheduledEvaluation

    included: Optional[Dict[str, Dict[Literal["evaluations"], List[IncludedItem]]]] = None
