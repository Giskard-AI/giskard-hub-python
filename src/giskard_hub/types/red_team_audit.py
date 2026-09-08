"""Red team audit domain types."""

from typing import List, Literal, Optional, TypeAlias, TypedDict
from datetime import datetime
from typing_extensions import Required

from .._types import FileTypes, SequenceNotStr
from .._models import BaseModel

__all__ = [
    "RedTeamAudit",
    "RedTeamAuditContent",
    "RedTeamAuditDownloadType",
    "RedTeamAuditEvaluationUploadStatus",
    "RedTeamAuditFinding",
    "RedTeamAuditLogChunk",
    "RedTeamAuditLogStream",
    "RedTeamAuditLogs",
    "RedTeamAuditOverallAssessment",
    "RedTeamAuditRemediation",
    "RedTeamAuditScanType",
    "RedTeamAuditStatus",
    "RedTeamAuditCreateParams",
    "RedTeamAuditListParams",
    "RedTeamAuditImportParams",
    "RedTeamAuditLogsParams",
    "RedTeamAuditDownloadParams",
]


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

RedTeamAuditStatus: TypeAlias = Literal[
    "queued",
    "running",
    "uploading",
    "finished",
    "error",
    "canceled",
    "timed_out",
]

RedTeamAuditScanType: TypeAlias = Literal["vulnerability", "garak", "deepteam", "lidar"]

RedTeamAuditEvaluationUploadStatus: TypeAlias = Literal["not_started", "uploaded", "skipped", "error"]

RedTeamAuditDownloadType: TypeAlias = Literal["report", "logs", "run-archive"]

RedTeamAuditLogStream: TypeAlias = Literal["stdout", "stderr", "system"]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class RedTeamAuditOverallAssessment(BaseModel):
    headline: str
    body: str


class RedTeamAuditFinding(BaseModel):
    external_id: str
    position: int
    title: str
    severity: Optional[str] = None
    likelihood: Optional[str] = None
    impact: Optional[str] = None
    taxonomy_codes: List[str]
    description: str
    remediation_ids: List[str]
    result_urls: List[str]


class RedTeamAuditRemediation(BaseModel):
    external_id: str
    position: int
    recommendation: str
    priority: Optional[str] = None


class RedTeamAuditContent(BaseModel):
    trust_level: str
    trust_level_grade: str
    overall_assessment: RedTeamAuditOverallAssessment
    findings: List[RedTeamAuditFinding]
    remediations: List[RedTeamAuditRemediation]


class RedTeamAuditLogChunk(BaseModel):
    sequence: int
    timestamp: datetime
    stream: RedTeamAuditLogStream
    text: str


class RedTeamAuditLogs(BaseModel):
    next_cursor: int
    state: RedTeamAuditStatus
    logs_truncated: bool = False
    chunks: List[RedTeamAuditLogChunk]


class RedTeamAudit(BaseModel):
    id: str
    project_id: str
    target_agent_id: str
    input_evaluation_ids: List[str]
    output_evaluation_id: Optional[str] = None
    output_evaluation_name: Optional[str] = None
    name: Optional[str] = None
    status: RedTeamAuditStatus
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime] = None
    run_deadline: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    last_heartbeat_at: Optional[datetime] = None
    last_log_at: Optional[datetime] = None
    runner: Optional[str] = None
    error: Optional[str] = None
    logs_truncated: bool
    evaluation_upload_status: RedTeamAuditEvaluationUploadStatus
    evaluation_upload_error: Optional[str] = None
    evaluation_uploaded_count: int
    trust_level: Optional[str] = None
    trust_level_grade: Optional[str] = None
    has_pdf: bool = False
    has_audit_content: bool = False
    has_intermediate_archive: bool = False


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class RedTeamAuditCreateParams(TypedDict, total=False):
    project_id: Required[str]
    target_agent_id: Required[str]
    input_evaluation_ids: SequenceNotStr[str]
    name: Optional[str]
    scan_types: Optional[List[RedTeamAuditScanType]]


class RedTeamAuditListParams(TypedDict, total=False):
    project_id: Optional[str]


class RedTeamAuditImportParams(TypedDict, total=False):
    project_id: Required[str]
    target_agent_id: Required[str]
    content: Required[FileTypes]
    name: Optional[str]
    report: Optional[FileTypes]


class RedTeamAuditLogsParams(TypedDict, total=False):
    after: int
    limit: int


class RedTeamAuditDownloadParams(TypedDict, total=False):
    type: RedTeamAuditDownloadType
