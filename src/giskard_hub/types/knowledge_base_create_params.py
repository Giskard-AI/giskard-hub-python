from __future__ import annotations

from typing import Optional, TypedDict
from typing_extensions import Required

from .._types import FileTypes

__all__ = ["KnowledgeBaseCreateParams"]


class KnowledgeBaseCreateParams(TypedDict, total=False):
    project_id: Required[str]

    name: Required[str]

    description: Optional[str]

    document_column: str

    topic_column: str

    file: Required[FileTypes]
