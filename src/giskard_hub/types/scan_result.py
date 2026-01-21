from typing import Optional, Literal
from datetime import datetime

from .._models import BaseModel
from .task_progress import TaskProgress
from .agent_api_reference import AgentAPIReference

__all__ = ["ScanResult", "KnowledgeBase"]


class KnowledgeBase(BaseModel):
    id: str

    name: str


class ScanResult(BaseModel):
    id: str

    agent: AgentAPIReference

    created_at: datetime

    grade: Optional[Literal["A", "B", "C", "D"]] = None

    knowledge_base: Optional[KnowledgeBase] = None

    project_id: str

    status: TaskProgress

    updated_at: datetime
