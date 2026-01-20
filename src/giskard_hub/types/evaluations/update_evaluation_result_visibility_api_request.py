
from __future__ import annotations

from .._models import BaseModel

__all__ = ["UpdateEvaluationResultVisibilityAPIRequest"]


class UpdateEvaluationResultVisibilityAPIRequest(BaseModel):
    hidden: bool
