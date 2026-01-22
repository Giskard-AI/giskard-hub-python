from __future__ import annotations

from typing import Dict, TypedDict
from typing_extensions import Required

__all__ = ["AgentTestConnectionParams"]


class AgentTestConnectionParams(TypedDict, total=False):
    url: Required[str]

    headers: Dict[str, str]
