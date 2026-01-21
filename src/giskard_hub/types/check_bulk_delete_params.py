from __future__ import annotations

from typing import TypedDict
from typing_extensions import Required

from .._types import SequenceNotStr

__all__ = ["CheckBulkDeleteParams"]


class CheckBulkDeleteParams(TypedDict, total=False):
    check_ids: Required[SequenceNotStr[str]]
