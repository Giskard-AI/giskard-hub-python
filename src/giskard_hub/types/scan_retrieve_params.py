from __future__ import annotations

from typing import List, Optional, Literal, TypedDict

__all__ = ["ScanRetrieveParams"]


class ScanRetrieveParams(TypedDict, total=False):
    include: Optional[List[Literal["agent", "knowledge_base"]]]
