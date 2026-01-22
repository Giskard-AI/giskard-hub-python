from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .task_progress import TaskProgress

__all__ = ["KnowledgeBase", "Topic"]


class Topic(BaseModel):
    id: str
    """ID of the object"""

    created_at: datetime
    """Date of creation"""

    knowledge_base_id: str

    name: str

    updated_at: datetime
    """Date of the last modification"""

    document_count: Optional[int] = None


class KnowledgeBase(BaseModel):
    id: str

    created_at: datetime

    description: Optional[str] = None

    filename: Optional[str] = None

    n_documents: int

    name: str

    project_id: str

    status: TaskProgress

    topics: List[Topic]

    updated_at: datetime
