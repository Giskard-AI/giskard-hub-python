from __future__ import annotations

from typing import Any, Dict, Optional
from typing_extensions import TypedDict

from giskard_hub._types import SequenceNotStr

__all__ = ["KnowledgeBaseSearchDocumentsParams"]


class KnowledgeBaseSearchDocumentsParams(TypedDict, total=False):
    search: Optional[str]

    order_by: SequenceNotStr[Dict[str, Any]]

    filters: Dict[str, Dict[str, Any]]

    limit: int

    offset: int
