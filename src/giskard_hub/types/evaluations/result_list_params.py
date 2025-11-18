
from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ResultListParams"]


class ResultListParams(TypedDict, total=False):
    include: Optional[List[Literal["test_case"]]]
