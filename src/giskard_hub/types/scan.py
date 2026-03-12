"""Scan domain types."""

from typing import Dict, List, Literal, Optional, TypeAlias, TypedDict
from datetime import datetime
from typing_extensions import Required

from .chat import ChatMessageWithMetadata
from .agent import AgentReference
from .common import TaskProgress
from .._types import SequenceNotStr
from .._models import BaseModel

__all__ = [
    "ScanResult",
    "ScanCategory",
    "KnowledgeBaseAPIReference",
    "ScanListParams",
    "ScanCreateParams",
    "ScanRetrieveParams",
    "ScanBulkDeleteParams",
    "Severity",
    "ReviewStatus",
    "ScanProbeResult",
    "ScanProbeAttempt",
    "AttemptUpdateParams",
]


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

Severity: TypeAlias = Literal[0, 10, 20, 30]
ReviewStatus: TypeAlias = Literal["pending", "ignored", "acknowledged", "corrected"]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class KnowledgeBaseAPIReference(BaseModel):
    id: str
    name: str


class ScanResult(BaseModel):
    id: str
    agent: AgentReference
    created_at: datetime
    grade: Optional[Literal["A", "B", "C", "D"]] = None
    knowledge_base: Optional[KnowledgeBaseAPIReference] = None
    project_id: str
    status: TaskProgress
    updated_at: datetime


class ScanCategory(BaseModel):
    id: str
    description: str
    owasp_id: Optional[str] = None
    title: str


class ScanProbeMetric(BaseModel):
    count: int
    severity: Severity


class ScanProbeResult(BaseModel):
    id: str
    metrics: Optional[List[ScanProbeMetric]] = None
    probe_category: str
    probe_description: str
    probe_lidar_id: str
    probe_name: str
    probe_tags: List[str]
    scan_result_id: str
    status: TaskProgress


class ScanProbeAttemptError(BaseModel):
    message: str


class ScanProbeAttempt(BaseModel):
    id: str
    error: Optional[ScanProbeAttemptError] = None
    messages: List[ChatMessageWithMetadata]
    metadata: Dict[str, object]
    probe_result_id: str
    reason: str
    review_status: ReviewStatus
    severity: Severity


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class ScanListParams(TypedDict, total=False):
    include: Optional[List[Literal["agent", "knowledge_base"]]]
    project_id: Optional[str]


class ScanCreateParams(TypedDict, total=False):
    agent_id: Required[str]
    project_id: Required[str]
    knowledge_base_id: Optional[str]
    tags: Optional[SequenceNotStr[str]]


class ScanRetrieveParams(TypedDict, total=False):
    include: Optional[List[Literal["agent", "knowledge_base"]]]


class ScanBulkDeleteParams(TypedDict, total=False):
    scan_ids: Required[SequenceNotStr[str]]


class AttemptUpdateParams(TypedDict, total=False):
    review_status: Optional[ReviewStatus]
    severity: Optional[Severity]
    successful: Optional[bool]
