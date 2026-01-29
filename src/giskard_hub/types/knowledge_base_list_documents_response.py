from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["KnowledgeBaseListDocumentsResponse", "Data"]


class Data(BaseModel):
    id: str

    content: str

    created_at: datetime

    embedding: List[float]

    knowledge_base_id: str

    topic_id: Optional[str] = None

    updated_at: datetime


class KnowledgeBaseListDocumentsResponse(BaseModel):
    data: List[Data]
