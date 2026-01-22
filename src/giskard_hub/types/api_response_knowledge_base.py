from typing import Dict, Optional

from .._models import BaseModel
from .knowledge_base import KnowledgeBase

__all__ = ["APIResponseKnowledgeBase", "IncludedIncludedItem"]


class IncludedIncludedItem(BaseModel):
    data: object


class APIResponseKnowledgeBase(BaseModel):
    data: KnowledgeBase

    included: Optional[Dict[str, Dict[str, IncludedIncludedItem]]] = None
