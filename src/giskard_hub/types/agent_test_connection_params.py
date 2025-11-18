
from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["AgentTestConnectionParams"]


class AgentTestConnectionParams(TypedDict, total=False):
    url: Required[str]

    headers: Dict[str, str]
