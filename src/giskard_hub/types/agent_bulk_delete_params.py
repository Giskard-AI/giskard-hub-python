
from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AgentBulkDeleteParams"]


class AgentBulkDeleteParams(TypedDict, total=False):
    agent_ids: Required[SequenceNotStr[str]]
