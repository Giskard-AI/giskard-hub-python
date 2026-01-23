from __future__ import annotations

from typing import Any, Dict, Optional, TypedDict

__all__ = ["ResultSearchParams"]


class ResultSearchParams(TypedDict, total=False):
    filters: Optional[Dict[str, Any]]

    limit: Optional[int]

    offset: Optional[int]
