
from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["KnowledgeBaseBulkDeleteParams"]


class KnowledgeBaseBulkDeleteParams(TypedDict, total=False):
    knowledge_base_ids: Required[SequenceNotStr[str]]
