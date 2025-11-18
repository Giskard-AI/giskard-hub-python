
from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["DatasetBulkDeleteParams"]


class DatasetBulkDeleteParams(TypedDict, total=False):
    dataset_ids: Required[SequenceNotStr[str]]
