from typing import Optional

from .._types import Omit, omit
from .._models import BaseModel
from .knowledge_base_documents_search_filters import KnowledgeBaseDocumentsSearchFilters

__all__ = ["SearchKnowledgeBaseDocumentsAPIRequest"]


class SearchKnowledgeBaseDocumentsAPIRequest(BaseModel):
    filters: Optional[KnowledgeBaseDocumentsSearchFilters] | Omit = omit
    """Search filters"""
