
from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ResultSearchParams"]


class ResultSearchParams(TypedDict, total=False):
    include: Optional[List[Literal["test_case"]]]

    limit: Optional[int]

    offset: Optional[int]
