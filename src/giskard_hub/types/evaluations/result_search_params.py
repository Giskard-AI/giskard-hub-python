from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional, TypedDict

from giskard_hub._types import SequenceNotStr

__all__ = ["ResultSearchParams"]


class ResultSearchParams(TypedDict, total=False):
    search: Optional[str]

    order_by: SequenceNotStr[Dict[str, Any]]

    filters: Dict[str, Dict[str, Any]]

    limit: int

    offset: int

    include: Optional[List[Literal["test_case"]]]
