from typing import List

from .._models import BaseModel
from .knowledge_base import KnowledgeBase

__all__ = ["KnowledgeBaseListResponse"]


class KnowledgeBaseListResponse(BaseModel):
    data: List[KnowledgeBase]
