from __future__ import annotations

from typing import Optional, TypedDict
from typing_extensions import Required

from .._types import FileTypes

__all__ = ["KnowledgeBaseCreateParams", "Data"]


class KnowledgeBaseCreateParams(TypedDict, total=False):
    data: Required[Data]

    file: Required[FileTypes]


class Data(TypedDict, total=False):
    name: Required[str]

    project_id: Required[str]

    description: Optional[str]

    document_column: str
    """Column name for document content"""

    topic_column: str
    """Column name for topic classification"""
