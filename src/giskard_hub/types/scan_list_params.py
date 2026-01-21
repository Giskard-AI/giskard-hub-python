from __future__ import annotations

from typing import List, Optional, Literal, TypedDict

__all__ = ["ScanListParams"]


class ScanListParams(TypedDict, total=False):
    include: Optional[List[Literal["agent", "knowledge_base"]]]

    project_id: Optional[str]
