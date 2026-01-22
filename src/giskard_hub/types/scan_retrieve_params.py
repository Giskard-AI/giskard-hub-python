from __future__ import annotations

from typing import List, Literal, Optional, TypedDict

__all__ = ["ScanRetrieveParams"]


class ScanRetrieveParams(TypedDict, total=False):
    include: Optional[List[Literal["agent", "knowledge_base"]]]
