"""Knowledge base list response type.

Note: This type is equivalent to APIListResponse[KnowledgeBase] from common.responses.
For new code, consider using the generic type instead.
"""

from typing import List

from .._models import BaseModel
from .knowledge_base import KnowledgeBase

__all__ = ["KnowledgeBaseListResponse"]


class KnowledgeBaseListResponse(BaseModel):
    """Response containing a list of knowledge bases.
    
    This is equivalent to: APIListResponse[KnowledgeBase]
    """

    data: List[KnowledgeBase]
