from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["KnowledgeBaseDocumentRowAPIResource"]


class KnowledgeBaseDocumentRowAPIResource(BaseModel):
    id: str
    """ID of the document"""

    created_at: datetime
    """Date of creation"""

    knowledge_base_id: str
    """Knowledge base ID"""

    preview: str
    """Document preview"""

    updated_at: datetime
    """Date of the last modification"""

    topic_id: Optional[str] = None
    """Topic ID"""

    topic_name: Optional[str] = None
    """Topic name"""
