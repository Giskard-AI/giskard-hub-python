from typing import Dict, Optional

from .._models import BaseModel
from .scheduled_evaluation import ScheduledEvaluation

__all__ = ["APIResponseScheduledEvaluation", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class APIResponseScheduledEvaluation(BaseModel):
    data: ScheduledEvaluation

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
