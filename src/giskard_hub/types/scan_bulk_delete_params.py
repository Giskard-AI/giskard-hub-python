from __future__ import annotations

from typing import TypedDict
from typing_extensions import Required

from .._types import SequenceNotStr

__all__ = ["ScanBulkDeleteParams"]


class ScanBulkDeleteParams(TypedDict, total=False):
    scan_ids: Required[SequenceNotStr[str]]
