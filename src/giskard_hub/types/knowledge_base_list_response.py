
from typing import Dict, List, Optional

from .._models import BaseModel
from .knowledge_base import KnowledgeBase

__all__ = ["KnowledgeBaseListResponse", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class KnowledgeBaseListResponse(BaseModel):
    data: List[KnowledgeBase]

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
