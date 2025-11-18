
from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["KnowledgeBaseListDocumentsResponse", "Data", "IncludedIncludedItem"]


class Data(BaseModel):
    id: str

    content: str

    created_at: datetime

    embedding: List[float]

    knowledge_base_id: str

    topic_id: Optional[str] = None

    updated_at: datetime


class IncludedIncludedItem(BaseModel):
    data: object


class KnowledgeBaseListDocumentsResponse(BaseModel):
    data: List[Data]

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
