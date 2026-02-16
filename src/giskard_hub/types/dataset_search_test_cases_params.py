"""Dataset search test cases parameters."""

from __future__ import annotations

from typing import Any, Dict, Optional, TypedDict

from .._types import SequenceNotStr

__all__ = ["DatasetSearchTestCasesParams"]


class DatasetSearchTestCasesParams(TypedDict, total=False):
    """Parameters for searching dataset test cases."""

    search: Optional[str]

    order_by: SequenceNotStr[Dict[str, Any]]

    filters: Dict[str, Dict[str, Any]]

    limit: int

    offset: int
