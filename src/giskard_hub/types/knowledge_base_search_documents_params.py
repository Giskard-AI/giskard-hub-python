from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .knowledge_base_documents_search_filters import KnowledgeBaseDocumentsSearchFilters

__all__ = ["KnowledgeBaseSearchDocumentsParams"]


class KnowledgeBaseSearchDocumentsParams(TypedDict, total=False):
    filters: Optional[KnowledgeBaseDocumentsSearchFilters]
    """Search filters"""
