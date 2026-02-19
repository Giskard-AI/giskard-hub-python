from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CreatePlaygroundChat"]


class CreatePlaygroundChat(TypedDict, total=False):
    project_id: str

    name: str

    agent_id: Optional[str]

    description: Optional[str]
