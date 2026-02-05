from typing import Literal, Optional
from datetime import datetime

from .._models import BaseModel
from .task_progress import TaskProgress
from .agent_api_reference import AgentAPIReference

__all__ = ["ScanResult", "KnowledgeBaseAPIReference", "ScanCategory"]


class KnowledgeBaseAPIReference(BaseModel):
    id: str

    name: str


class ScanResult(BaseModel):
    id: str

    agent: AgentAPIReference

    created_at: datetime

    grade: Optional[Literal["A", "B", "C", "D"]] = None

    knowledge_base: Optional[KnowledgeBaseAPIReference] = None

    project_id: str

    status: TaskProgress

    updated_at: datetime


class ScanCategory(BaseModel):
    id: str

    description: str

    owasp_id: Optional[str] = None

    title: str
