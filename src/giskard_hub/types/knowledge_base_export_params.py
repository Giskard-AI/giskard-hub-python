from typing import Optional
from typing_extensions import TypedDict

__all__ = ["KnowledgeBaseExportParams"]


class KnowledgeBaseExportParams(TypedDict, total=False):
    format: Optional[str]
    """Export format"""
