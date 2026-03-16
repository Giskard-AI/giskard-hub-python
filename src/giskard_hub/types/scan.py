"""Scan domain types."""

from enum import IntEnum
from typing import Dict, List, Literal, Optional, TypeAlias, TypedDict
from datetime import datetime
from typing_extensions import Required

from pydantic import Field

from .chat import ChatMessageWithMetadata
from .agent import Agent, AgentReference
from .common import TaskState, TaskProgress
from .._types import SequenceNotStr
from .._models import BaseModel
from .knowledge_base import KnowledgeBase, KnowledgeBaseReference

__all__ = [
    "ScanProbeAttemptReference",
    "Scan",
    "ScanCategory",
    "ScanListParams",
    "ScanCreateParams",
    "ScanRetrieveParams",
    "ScanBulkDeleteParams",
    "Severity",
    "ReviewStatus",
    "ScanProbe",
    "ScanProbeAttempt",
    "ScanProbeAttemptUpdateParams",
]


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------


class Severity(IntEnum):
    SAFE = 0
    MINOR = 10
    MAJOR = 20
    CRITICAL = 30


ReviewStatus: TypeAlias = Literal["pending", "ignored", "acknowledged", "corrected"]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class Scan(BaseModel):
    id: str
    agent: AgentReference | Agent
    created_at: datetime
    grade: Optional[Literal["A", "B", "C", "D"]] = None
    knowledge_base: Optional[KnowledgeBaseReference | KnowledgeBase] = None
    project_id: str
    status: TaskProgress
    updated_at: datetime

    @property
    def state(self) -> TaskState:
        return self.status.state


class ScanCategory(BaseModel):
    id: str
    description: str
    owasp_id: Optional[str] = None
    title: str


class ScanProbeMetric(BaseModel):
    count: int
    severity: Severity


class ScanProbe(BaseModel):
    id: str
    metrics: Optional[List[ScanProbeMetric]] = None
    category: str = Field(alias="probe_category")
    description: str = Field(alias="probe_description")
    probe_lidar_id: str
    name: str = Field(alias="probe_name")
    tags: List[str] = Field(alias="probe_tags")
    scan_id: str = Field(alias="scan_result_id")
    status: TaskProgress

    @property
    def state(self) -> TaskState:
        return self.status.state


class ScanProbeAttemptError(BaseModel):
    message: str


class ScanProbeAttemptReference(BaseModel):
    id: str


class ScanProbeAttempt(BaseModel):
    id: str
    error: Optional[ScanProbeAttemptError] = None
    messages: List[ChatMessageWithMetadata]
    metadata: Dict[str, object]
    probe_id: str = Field(alias="probe_result_id")
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


class ScanProbeAttemptUpdateParams(TypedDict, total=False):
    review_status: Optional[ReviewStatus]
    severity: Optional[Severity]
    successful: Optional[bool]
