"""Agent domain types."""

from typing import Any, Dict, List, Iterable, Optional, TypedDict, cast
from datetime import datetime
from typing_extensions import Required, deprecated

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
    "AgentDetectStatefulness",
    "AgentInterface",
    "GenerateCompletionOutput",
    "AgentListParams",
    "AgentCreateParams",
    "AgentUpdateParams",
    "AgentBulkDeleteParams",
    "AgentTestConnectionParams",
    "AgentGenerateCompletionParams",
    "AgentAutofillDescriptionParams",
    "AgentDetectStatefulnessParams",
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
    supported_languages: list[str]
    updated_at: datetime
    url: str
    auto_bindings: Optional[List[Dict[str, Any]]] = None
    input_schema: Optional[Dict[str, Any]] = None
    output_schema: Optional[Dict[str, Any]] = None

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


class AgentDetectStatefulness(BaseModel):
    stateful: bool


class AgentInterface(BaseModel):
    id: str
    name: str = ""
    input_schema: Dict[str, Any] = Field(default_factory=dict)
    output_schema: Dict[str, Any] = Field(default_factory=dict)


class GenerateCompletionOutput(BaseModel):
    """Result of `agents.generate_completion`.

    The `output` field is the raw structured output of the agent
    (matching its `output_schema`). Helper accessors are provided to keep
    older code that read `response` / `message` working.
    """

    output: Optional[Dict[str, Any]] = None
    error: Optional[ExecutionError] = None
    metadata: Optional[Dict[str, Any]] = None
    forwarded: Optional[Dict[str, Any]] = None

    def _extract_response(self) -> Optional[ChatMessage]:
        if self.output is None:
            return None
        response = self.output.get("response")
        if isinstance(response, dict):
            r = cast(Dict[str, Any], response)
            role, content = r.get("role"), r.get("content")
            if isinstance(role, str) and isinstance(content, str):
                return ChatMessage(role=role, content=content)
        return None

    @property
    @deprecated(
        "`GenerateCompletionOutput.response` is deprecated; read "
        "`output['response']` from the structured `output` dict instead."
    )
    def response(self) -> Optional[ChatMessage]:
        """Deprecated accessor for the `response` chat message."""
        return self._extract_response()

    @property
    @deprecated(
        "`GenerateCompletionOutput.message` is deprecated; read "
        "`output['response']` from the structured `output` dict instead."
    )
    def message(self) -> Optional[ChatMessage]:
        """Deprecated alias for `response`."""
        return self._extract_response()


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
    auto_bindings: Optional[Dict[str, str]]
    input_schema: Optional[Dict[str, Any]]
    output_schema: Optional[Dict[str, Any]]


class AgentUpdateParams(TypedDict, total=False):
    description: Optional[str]
    headers: Optional[Iterable[HeaderParam]]
    name: Optional[str]
    supported_languages: Optional[SequenceNotStr[str]]
    url: Optional[str]
    auto_bindings: Optional[Dict[str, str]]
    input_schema: Optional[Dict[str, Any]]
    output_schema: Optional[Dict[str, Any]]


class AgentBulkDeleteParams(TypedDict, total=False):
    agent_ids: Required[SequenceNotStr[str]]


class AgentTestConnectionParams(TypedDict, total=False):
    url: Required[str]
    project_id: Required[str]
    headers: Iterable[HeaderParam]
    agent_id: Optional[str]
    input_schema: Optional[Dict[str, Any]]


class AgentGenerateCompletionParams(TypedDict, total=False):
    input: Required[Dict[str, Any]]
    metadata: Optional[Dict[str, Any]]
    forwarded: Optional[Dict[str, Any]]


class AgentAutofillDescriptionParams(TypedDict, total=False):
    pass


class AgentDetectStatefulnessParams(TypedDict, total=False):
    pass
