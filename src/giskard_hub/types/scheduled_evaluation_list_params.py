
from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ScheduledEvaluationListParams"]


class ScheduledEvaluationListParams(TypedDict, total=False):
    project_id: Required[str]
