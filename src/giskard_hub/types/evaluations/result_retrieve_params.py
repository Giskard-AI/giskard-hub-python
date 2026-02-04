from __future__ import annotations

from typing import List, Literal, Optional, TypedDict

__all__ = ["ResultRetrieveParams"]


class ResultRetrieveParams(TypedDict, total=False):
    include: Optional[List[Literal["test_case"]]]
