from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["KnowledgeBaseDocumentDetailAPIResource"]


class KnowledgeBaseDocumentDetailAPIResource(BaseModel):
    id: str
    """ID of the document"""

    content: str
    """Full document content"""

    created_at: datetime
    """Date of creation"""

    knowledge_base_id: str
    """Knowledge base ID"""

    updated_at: datetime
    """Date of the last modification"""

    topic_id: Optional[str] = None
    """Topic ID"""

    topic_name: Optional[str] = None
    """Topic name"""
