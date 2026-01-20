
from __future__ import annotations

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SortByEvaluationResults"]


class SortByEvaluationResults(BaseModel):
    field: Literal["-id", "-status", "-failure_category_name", "-visibility", "-sample_success"]

    order: Literal["asc", "desc"]
