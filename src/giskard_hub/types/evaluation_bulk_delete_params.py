
from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["EvaluationBulkDeleteParams"]


class EvaluationBulkDeleteParams(TypedDict, total=False):
    evaluation_ids: Required[SequenceNotStr[str]]
