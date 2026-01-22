from __future__ import annotations

from typing import Optional, TypedDict

__all__ = ["DatasetListParams"]


class DatasetListParams(TypedDict, total=False):
    project_id: Optional[str]
