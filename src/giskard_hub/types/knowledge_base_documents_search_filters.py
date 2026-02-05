from typing import Optional

from .._types import Omit, SequenceNotStr, omit
from .._models import BaseModel
from .sort_by_literal import SortByLiteral

__all__ = ["KnowledgeBaseDocumentsSearchFilters"]


class KnowledgeBaseDocumentsSearchFilters(BaseModel):
    ascending: Optional[bool] | Omit = omit
    """Sort order"""

    sort_by: Optional[SortByLiteral] | Omit = omit
    """Sort by field"""

    topic_ids: Optional[SequenceNotStr[str]] | Omit = omit
    """Filter by topic IDs"""
