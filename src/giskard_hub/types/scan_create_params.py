from __future__ import annotations

from typing import Optional, TypedDict
from typing_extensions import Required

from .._types import SequenceNotStr

__all__ = ["ScanCreateParams"]


class ScanCreateParams(TypedDict, total=False):
    agent_id: Required[str]

    project_id: Required[str]

    knowledge_base_id: Optional[str]

    tags: Optional[SequenceNotStr[str]]
