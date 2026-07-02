"""Scan domain types."""

import json
from enum import IntEnum
from typing import Any, Dict, List, Literal, Optional, TypeAlias, TypedDict, cast
from datetime import datetime
from typing_extensions import Required, deprecated

from pydantic import Field

from .chat import ChatMessage
from .agent import Agent, AgentInterface
from .common import TaskState, TaskProgress
from .._types import SequenceNotStr
from .._models import BaseModel
from .knowledge_base import KnowledgeBase, KnowledgeBaseReference

__all__ = [
    "ScanProbeAttemptReference",
    "Scan",
    "ScanCategory",
    "ScanAvailableProbe",
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
    agent: AgentInterface | Agent
    created_at: datetime
    grade: Optional[Literal["A", "B", "C", "D"]] = None
    knowledge_base: Optional[KnowledgeBaseReference | KnowledgeBase] = None
    project_id: str
    status: TaskProgress
    updated_at: datetime
    start_datetime: Optional[datetime] = None
    end_datetime: Optional[datetime] = None

    @property
    def state(self) -> TaskState:
        return self.status.state


class ScanCategory(BaseModel):
    id: str
    description: str
    owasp_id: Optional[str] = None
    title: str


class ScanAvailableProbe(BaseModel):
    id: str
    name: str
    desc: str
    tags: List[str]


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


def _attempt_input_to_messages(value: Any) -> List[ChatMessage]:
    """Best-effort conversion of an attempt input dict into ChatMessage list.

    Supports:
      - Chat-style: `{"messages": [{"role": ..., "content": ...}, ...]}`
      - Probe-style: `{"probe_text": "..."}` → single user message
      - Anything else: dump to JSON and wrap as a single user message
    """
    if isinstance(value, dict):
        d = cast(Dict[str, Any], value)
        msgs = d.get("messages")
        if isinstance(msgs, list):
            out: List[ChatMessage] = []
            for m in cast(List[Any], msgs):
                if isinstance(m, dict):
                    md = cast(Dict[str, Any], m)
                    role, content = md.get("role"), md.get("content")
                    if isinstance(role, str) and isinstance(content, str):
                        out.append(ChatMessage(role=role, content=content))
            if out:
                return out
        probe_text = d.get("probe_text")
        if isinstance(probe_text, str):
            return [ChatMessage(role="user", content=probe_text)]
    return [ChatMessage(role="user", content=json.dumps(value, ensure_ascii=False))]


def _attempt_output_to_message(value: Any) -> Optional[ChatMessage]:
    """Best-effort conversion of an attempt output dict into a single ChatMessage.

    Supports:
      - Chat-style: `{"response": {"role": ..., "content": ...}}`
      - Anything else: dump to JSON and wrap as a single assistant message
    """
    if value is None:
        return None
    if isinstance(value, dict):
        d = cast(Dict[str, Any], value)
        response = d.get("response")
        if isinstance(response, dict):
            r = cast(Dict[str, Any], response)
            role, content = r.get("role"), r.get("content")
            if isinstance(role, str) and isinstance(content, str):
                return ChatMessage(role=role, content=content)
    return ChatMessage(role="assistant", content=json.dumps(value, ensure_ascii=False))


class ScanProbeAttempt(BaseModel):
    id: str
    error: Optional[ScanProbeAttemptError] = None
    input: Dict[str, Any] = Field(default_factory=dict)
    output: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    probe_id: str = Field(alias="probe_result_id")
    reason: str
    review_status: ReviewStatus
    severity: Severity

    @property
    @deprecated("`ScanProbeAttempt.messages` is deprecated; read `attempt.input` and `attempt.output` directly.")
    def messages(self) -> List[ChatMessage]:
        """Deprecated flattened view: extracted user input(s) then assistant output.

        For chat-style probes (`input.messages`, `output.response`), returns the
        original chat turns. For non-chat probes the dicts are JSON-dumped into
        single text messages so call sites can still read `attempt.messages`.
        """
        out: List[ChatMessage] = list(_attempt_input_to_messages(self.input))
        assistant = _attempt_output_to_message(self.output)
        if assistant is not None:
            out.append(assistant)
        return out


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
    probe_ids: Optional[SequenceNotStr[str]]
    tags: Optional[SequenceNotStr[str]]


class ScanRetrieveParams(TypedDict, total=False):
    include: Optional[List[Literal["agent", "knowledge_base"]]]


class ScanBulkDeleteParams(TypedDict, total=False):
    scan_ids: Required[SequenceNotStr[str]]


class ScanProbeAttemptUpdateParams(TypedDict, total=False):
    review_status: Optional[ReviewStatus]
    severity: Optional[Severity]
    successful: Optional[bool]
