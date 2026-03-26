"""Agent domain types."""

from typing import Any, Dict, Iterable, Optional, TypedDict, cast
from datetime import datetime
from typing_extensions import Required

from pydantic import Field, AliasChoices, model_validator

from .chat import Header, ChatMessage, HeaderParam, ChatMessageParam
from .._types import SequenceNotStr
from .._models import BaseModel
from .execution import ExecutionError, ExecutionErrorParam

__all__ = [
    "Agent",
    "AgentReference",
    "AgentOutput",
    "AgentOutputParam",
    "MinimalAgent",
    "MinimalAgentParam",
    "DetectStateful",
    "DivergenceWarning",
    "AgentListParams",
    "AgentCreateParams",
    "AgentUpdateParams",
    "AgentBulkDeleteParams",
    "AgentTestConnectionParams",
    "AgentGenerateCompletionParams",
    "AgentAutofillDescriptionParams",
    "AgentDetectStatefulParams",
]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class Agent(BaseModel):
    id: str
    created_at: datetime
    description: Optional[str] = None
    headers: Dict[str, str] = Field(default_factory=dict)
    name: str
    project_id: str
    stateful: Optional[bool] = None
    supported_languages: list[str]
    updated_at: datetime
    url: str

    @model_validator(mode="before")
    @classmethod
    def _normalize_headers(cls, data: Any) -> Any:  # noqa: ANN401
        if not isinstance(data, dict):
            return data

        d = cast(Dict[str, Any], data)
        raw_headers = d.get("headers")

        # Already a mapping or missing: nothing to do
        if raw_headers is None or isinstance(raw_headers, dict):
            return d

        # Convert list of Header models or dicts into a dict[str, str]
        if isinstance(raw_headers, list):
            headers_dict: Dict[str, str] = {}
            for item in cast(list[Any], raw_headers):
                if isinstance(item, Header):
                    headers_dict[item.name] = item.value
                elif isinstance(item, dict):
                    item_typed = cast(Dict[str, Any], item)
                    name = item_typed.get("name")
                    value = item_typed.get("value")
                    if isinstance(name, str) and isinstance(value, str):
                        headers_dict[name] = value

            return {**d, "headers": headers_dict}

        return d


class AgentReference(BaseModel):
    id: str
    name: str


class AgentOutput(BaseModel):
    response: Optional[ChatMessage] = Field(
        default=None,
        validation_alias=AliasChoices("response", "message"),
    )
    error: Optional[ExecutionError] = None
    metadata: Optional[Dict[str, object]] = None


class AgentOutputParam(TypedDict, total=False):
    response: Required[Optional[ChatMessageParam]]
    error: Optional[ExecutionErrorParam]
    metadata: Dict[str, object]


class MinimalAgent(BaseModel):
    name: str
    description: Optional[str] = None


class MinimalAgentParam(TypedDict, total=False):
    name: Required[str]
    description: Optional[str]


class DivergenceWarning(BaseModel):
    message: str
    severity: str


class DetectStateful(BaseModel):
    stateful: bool
    warnings: Optional[list[DivergenceWarning]] = None


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class AgentListParams(TypedDict, total=False):
    project_id: Optional[str]


class AgentCreateParams(TypedDict, total=False):
    headers: Required[Iterable[HeaderParam]]
    name: Required[str]
    project_id: Required[str]
    supported_languages: Required[SequenceNotStr[str]]
    url: Required[str]
    description: Optional[str]
    stateful: Optional[bool]


class AgentUpdateParams(TypedDict, total=False):
    description: Optional[str]
    headers: Optional[Iterable[HeaderParam]]
    name: Optional[str]
    supported_languages: Optional[SequenceNotStr[str]]
    url: Optional[str]


class AgentBulkDeleteParams(TypedDict, total=False):
    agent_ids: Required[SequenceNotStr[str]]


class AgentTestConnectionParams(TypedDict, total=False):
    url: Required[str]
    headers: Dict[str, str]


class AgentGenerateCompletionParams(TypedDict, total=False):
    messages: Required[Iterable[ChatMessageParam]]


class AgentAutofillDescriptionParams(TypedDict, total=False):
    pass


class AgentDetectStatefulParams(TypedDict, total=False):
    pass
