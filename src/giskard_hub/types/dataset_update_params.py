from __future__ import annotations

from typing import Optional, TypedDict

from .task_progress_param import TaskProgressParam

__all__ = ["DatasetUpdateParams"]


class DatasetUpdateParams(TypedDict, total=False):
    description: Optional[str]

    name: Optional[str]

    status: Optional[TaskProgressParam]
