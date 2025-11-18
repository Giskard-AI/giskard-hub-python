
from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ScheduledEvaluationBulkDeleteParams"]


class ScheduledEvaluationBulkDeleteParams(TypedDict, total=False):
    scheduled_evaluation_ids: Required[SequenceNotStr[str]]
