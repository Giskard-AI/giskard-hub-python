from __future__ import annotations

from typing import TypedDict
from typing_extensions import Required

from .._types import SequenceNotStr

__all__ = ["EvaluationBulkDeleteParams"]


class EvaluationBulkDeleteParams(TypedDict, total=False):
    evaluation_ids: Required[SequenceNotStr[str]]
