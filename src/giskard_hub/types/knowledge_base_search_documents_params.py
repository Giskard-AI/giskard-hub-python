from __future__ import annotations

from typing import Dict, List, Literal, Optional
from typing_extensions import TypedDict

from .filter_param import FilterValueParam
from .order_by_param import OrderByParam

__all__ = [
    "KnowledgeBaseSearchDocumentsParams",
    "KnowledgeBaseDocumentOrderByParam",
    "KnowledgeBaseDocumentFiltersParam",
]

KnowledgeBaseDocumentSortColumn = Literal["created_at", "updated_at", "topic_id"]
KnowledgeBaseDocumentFilterColumn = Literal["topic_id"]

KnowledgeBaseDocumentOrderByParam = OrderByParam[KnowledgeBaseDocumentSortColumn]
KnowledgeBaseDocumentFiltersParam = Dict[KnowledgeBaseDocumentFilterColumn, FilterValueParam]


class KnowledgeBaseSearchDocumentsParams(TypedDict, total=False):
    search: Optional[str]

    order_by: Optional[List[KnowledgeBaseDocumentOrderByParam]]

    filters: Optional[KnowledgeBaseDocumentFiltersParam]

    limit: int

    offset: int
