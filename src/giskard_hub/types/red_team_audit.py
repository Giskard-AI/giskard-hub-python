"""Red team audit types exposed by the SDK."""

from typing import Any, Dict, List, Literal, Optional, TypeAlias, TypedDict
from datetime import date, datetime
from typing_extensions import Required

from pydantic import Field

from .._types import FileTypes, SequenceNotStr
from .._models import BaseModel

__all__ = [
    "RedTeamAuditCoverageMode",
    "RedTeamAuditStatus",
    "RedTeamAuditScanType",
    "RedTeamAuditEvaluationUploadStatus",
    "RedTeamAuditLogStream",
    "RedTeamAuditImpactGrade",
    "RedTeamAuditRiskModelSurface",
    "RedTeamAudit",
    "RedTeamAuditLogChunk",
    "RedTeamAuditLogs",
    "RedTeamAuditOverallAssessment",
    "RedTeamAuditFindingEvidence",
    "RedTeamAuditFinding",
    "RedTeamAuditRemediation",
    "RedTeamAuditCoverage",
    "RedTeamAuditRiskModelScope",
    "RedTeamAuditRiskModelAssumption",
    "RedTeamAuditRiskModelMeta",
    "RedTeamAuditRiskModelMission",
    "RedTeamAuditRiskModelBusinessAsset",
    "RedTeamAuditRiskModelSupportingAsset",
    "RedTeamAuditRiskModelFearedEvent",
    "RedTeamAuditRiskModelRiskOrigin",
    "RedTeamAuditRiskModelScenario",
    "RedTeamAuditRiskModel",
    "RedTeamAuditContent",
    "RedTeamAuditCreateParams",
    "RedTeamAuditListParams",
    "RedTeamAuditUploadParams",
    "RedTeamAuditRetrieveLogsParams",
    "RedTeamAuditEstimateParams",
]


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

RedTeamAuditCoverageMode: TypeAlias = Literal["regular", "light"]

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

RedTeamAuditLogStream: TypeAlias = Literal["stdout", "stderr", "system"]

RedTeamAuditImpactGrade: TypeAlias = Literal["G1", "G2", "G3", "G4"]

RedTeamAuditRiskModelSurface: TypeAlias = Literal[
    "public_chat",
    "ai_api",
    "client_visible_session",
    "public_upload",
    "public_retrieval",
    "public_output",
]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class RedTeamAudit(BaseModel):
    id: str
    project_id: str
    target_agent_id: str
    input_evaluation_ids: List[str]
    output_evaluation_id: Optional[str] = None
    output_evaluation_name: Optional[str] = None
    output_dataset_id: Optional[str] = None
    output_dataset_name: Optional[str] = None
    name: Optional[str] = None
    mode: RedTeamAuditCoverageMode
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


class RedTeamAuditOverallAssessment(BaseModel):
    headline: str
    body: str


class RedTeamAuditFindingEvidence(BaseModel):
    thread_id: str
    reason: str
    highlighted: bool
    result_url: Optional[str] = None
    excerpt_sequences: List[int]


class RedTeamAuditFinding(BaseModel):
    external_id: str
    position: int
    source_report_id: Optional[str] = None
    risk_model_wave: Optional[str] = None
    title: str
    display_title: Optional[str] = None
    technical_description: str
    report_description: str
    reproduction_steps: str
    associated_scenarios: List[str]
    taxonomy_codes: List[str]
    impact: Optional[str] = None
    impact_rationale: str
    likelihood: Optional[str] = None
    likelihood_rationale: str
    severity: Optional[str] = None
    evidence: List[RedTeamAuditFindingEvidence]
    remediation_ids: List[str]


class RedTeamAuditRemediation(BaseModel):
    external_id: str
    position: int
    recommendation: str
    priority: Optional[str] = None
    finding_ids: List[str]


class RedTeamAuditCoverage(BaseModel):
    mode: RedTeamAuditCoverageMode
    scenarios_total: int
    covered_scenario_ids: List[str] = Field(default_factory=list)
    uncovered_scenario_ids: List[str] = Field(default_factory=list)


class RedTeamAuditRiskModelScope(BaseModel):
    in_: List[str] = Field(alias="in")
    out: List[str]


class RedTeamAuditRiskModelAssumption(BaseModel):
    text: str
    source: str


class RedTeamAuditRiskModelMeta(BaseModel):
    updated: date
    based_on: List[str]
    scope: RedTeamAuditRiskModelScope
    assumptions: List[RedTeamAuditRiskModelAssumption]


class RedTeamAuditRiskModelMission(BaseModel):
    id: str
    name: str


class RedTeamAuditRiskModelBusinessAsset(BaseModel):
    id: str
    name: str
    why: str


class RedTeamAuditRiskModelSupportingAsset(BaseModel):
    id: str
    name: str
    supports: List[str]
    notes: str = ""


class RedTeamAuditRiskModelFearedEvent(BaseModel):
    id: str
    description: str
    asset_ids: List[str]
    impact: RedTeamAuditImpactGrade


class RedTeamAuditRiskModelRiskOrigin(BaseModel):
    id: str
    name: str
    target_objective: str


class RedTeamAuditRiskModelScenario(BaseModel):
    id: str
    title: str
    origin_id: str
    feared_event_id: str
    surface: RedTeamAuditRiskModelSurface
    dedup_key: str
    rationale: str


class RedTeamAuditRiskModel(BaseModel):
    schema_version: Literal[1]
    wave: str
    meta: RedTeamAuditRiskModelMeta
    missions: List[RedTeamAuditRiskModelMission]
    business_assets: List[RedTeamAuditRiskModelBusinessAsset]
    supporting_assets: List[RedTeamAuditRiskModelSupportingAsset]
    feared_events: List[RedTeamAuditRiskModelFearedEvent]
    risk_origins: List[RedTeamAuditRiskModelRiskOrigin]
    scenarios: List[RedTeamAuditRiskModelScenario]


class RedTeamAuditContent(BaseModel):
    report: Dict[str, Any]
    generated_at: Optional[datetime] = None
    trust_level: str
    trust_level_grade: str
    overall_assessment: RedTeamAuditOverallAssessment
    conclusion: Optional[str] = None
    risk_model: Optional[RedTeamAuditRiskModel] = None
    attack_counts: Dict[str, int] = Field(default_factory=dict)
    coverage: Optional[RedTeamAuditCoverage] = None
    findings: List[RedTeamAuditFinding]
    remediations: List[RedTeamAuditRemediation]


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class RedTeamAuditCreateParams(TypedDict, total=False):
    project_id: Required[str]
    target_agent_id: Required[str]
    input_evaluation_ids: SequenceNotStr[str]
    name: Optional[str]
    scan_types: Optional[List[RedTeamAuditScanType]]
    mode: RedTeamAuditCoverageMode


class RedTeamAuditListParams(TypedDict, total=False):
    project_id: Optional[str]


class RedTeamAuditUploadParams(TypedDict, total=False):
    project_id: Required[str]
    target_agent_id: Required[str]
    content: Required[FileTypes]
    name: Optional[str]
    report: FileTypes
    risk_model: FileTypes


class RedTeamAuditRetrieveLogsParams(TypedDict, total=False):
    after: int
    limit: int


class RedTeamAuditEstimateParams(TypedDict, total=False):
    mode: RedTeamAuditCoverageMode
