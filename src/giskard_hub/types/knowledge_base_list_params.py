from __future__ import annotations

from typing import Optional, TypedDict

__all__ = ["KnowledgeBaseListParams"]


class KnowledgeBaseListParams(TypedDict, total=False):
    project_id: Optional[str]
