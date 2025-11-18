
from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .task_progress_param import TaskProgressParam

__all__ = ["KnowledgeBaseUpdateParams"]


class KnowledgeBaseUpdateParams(TypedDict, total=False):
    description: Optional[str]

    name: Optional[str]

    project_id: Optional[str]

    status: Optional[TaskProgressParam]
