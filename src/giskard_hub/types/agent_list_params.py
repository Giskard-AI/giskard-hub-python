from __future__ import annotations

from typing import Optional, TypedDict

__all__ = ["AgentListParams"]


class AgentListParams(TypedDict, total=False):
    project_id: Optional[str]
