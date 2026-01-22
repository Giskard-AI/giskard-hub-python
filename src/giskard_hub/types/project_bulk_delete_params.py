from __future__ import annotations

from typing import TypedDict
from typing_extensions import Required

from .._types import SequenceNotStr

__all__ = ["ProjectBulkDeleteParams"]


class ProjectBulkDeleteParams(TypedDict, total=False):
    project_ids: Required[SequenceNotStr[str]]
