from __future__ import annotations

from typing import TypedDict
from typing_extensions import Required

from .._types import SequenceNotStr

__all__ = ["TaskBulkDeleteParams"]


class TaskBulkDeleteParams(TypedDict, total=False):
    task_ids: Required[SequenceNotStr[str]]
