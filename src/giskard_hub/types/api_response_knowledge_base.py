from .._models import BaseModel
from .knowledge_base import KnowledgeBase

__all__ = ["APIResponseKnowledgeBase"]


class APIResponseKnowledgeBase(BaseModel):
    data: KnowledgeBase
