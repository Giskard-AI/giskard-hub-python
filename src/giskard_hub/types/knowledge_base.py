"""Knowledge base domain types."""

from typing import Dict, List, Literal, Optional, TypedDict
from datetime import datetime
from typing_extensions import Required

from pydantic import computed_field

from .common import TaskState, OrderByParam, TaskProgress, FilterValueParam, TaskProgressParam
from .._types import FileTypes, SequenceNotStr
from .._models import BaseModel

__all__ = [
    "KnowledgeBase",
    "KnowledgeBaseReference",
    "Topic",
    "KnowledgeBaseDocumentRow",
    "KnowledgeBaseDocumentDetail",
    "KnowledgeBaseListParams",
    "KnowledgeBaseCreateParams",
    "KnowledgeBaseUpdateParams",
    "KnowledgeBaseBulkDeleteParams",
    "KnowledgeBaseSearchDocumentsParams",
    "KnowledgeBaseDocumentOrderByParam",
    "KnowledgeBaseDocumentFiltersParam",
]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class Topic(BaseModel):
    id: str
    created_at: datetime
    knowledge_base_id: str
    name: str
    updated_at: datetime
    document_count: Optional[int] = None


class KnowledgeBaseReference(BaseModel):
    id: str
    name: str


class KnowledgeBase(BaseModel):
    id: str
    created_at: datetime
    description: Optional[str] = None
    filename: Optional[str] = None
    n_documents: int
    name: str
    project_id: str
    status: TaskProgress
    topics: List[Topic]
    updated_at: datetime

    @computed_field
    def state(self) -> TaskState:
        return self.status.state


class KnowledgeBaseDocumentRow(BaseModel):
    id: str
    created_at: datetime
    knowledge_base_id: str
    snippet: str
    updated_at: datetime
    topic_id: Optional[str] = None
    topic_name: Optional[str] = None


class KnowledgeBaseDocumentDetail(BaseModel):
    id: str
    content: str
    created_at: datetime
    knowledge_base_id: str
    updated_at: datetime
    topic_id: Optional[str] = None
    topic_name: Optional[str] = None


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class KnowledgeBaseListParams(TypedDict, total=False):
    project_id: Optional[str]


class KnowledgeBaseCreateParams(TypedDict, total=False):
    project_id: Required[str]
    name: Required[str]
    description: Optional[str]
    document_column: str
    topic_column: str
    file: Required[FileTypes]


class KnowledgeBaseUpdateParams(TypedDict, total=False):
    description: Optional[str]
    name: Optional[str]
    project_id: Optional[str]
    status: Optional[TaskProgressParam]


class KnowledgeBaseBulkDeleteParams(TypedDict, total=False):
    knowledge_base_ids: Required[SequenceNotStr[str]]


# ---------------------------------------------------------------------------
# Search params
# ---------------------------------------------------------------------------

KnowledgeBaseDocumentSortColumn = Literal["created_at", "updated_at", "topic_id"]
KnowledgeBaseDocumentFilterColumn = Literal["topic_id"]

KnowledgeBaseDocumentOrderByParam = OrderByParam[KnowledgeBaseDocumentSortColumn]
KnowledgeBaseDocumentFiltersParam = Dict[KnowledgeBaseDocumentFilterColumn, FilterValueParam]


class KnowledgeBaseSearchDocumentsParams(TypedDict, total=False):
    search: Optional[str]
    order_by: Optional[List[KnowledgeBaseDocumentOrderByParam]]
    filters: Optional[KnowledgeBaseDocumentFiltersParam]
    limit: int
    offset: int
