"""Check, assertion, and annotation types."""

from typing import Any, Dict, List, Union, Literal, Iterable, Optional, TypeAlias, TypedDict, cast
from datetime import datetime
from typing_extensions import Required

import pydantic

from .common import TaskState
from .._types import SequenceNotStr
from .._models import BaseModel

__all__ = [
    "Check",
    "CheckResult",
    "CheckConfig",
    "CheckConfigParam",
    "CheckType",
    "CheckTypeParam",
    "ConformityParams",
    "ConformityParamsParam",
    "CorrectnessParams",
    "CorrectnessParamsParam",
    "GroundednessParams",
    "GroundednessParamsParam",
    "StringMatchParams",
    "StringMatchParamsParam",
    "SemanticSimilarityParams",
    "SemanticSimilarityParamsParam",
    "MetadataParams",
    "MetadataParamsParam",
    "JsonPathRule",
    "JsonPathRuleParam",
    "OutputAnnotation",
    "TestCaseCheckConfig",
    "TestCaseCheckConfigParam",
    "CheckListParams",
    "CheckCreateParams",
    "CheckUpdateParams",
    "CheckBulkDeleteParams",
]


# ---------------------------------------------------------------------------
# Assertion parameter models (BaseModel – used in responses)
# ---------------------------------------------------------------------------


class ConformityParams(BaseModel):
    rules: List[str]
    type: Optional[Literal["conformity"]] = None


class CorrectnessParams(BaseModel):
    reference: str
    type: Optional[Literal["correctness"]] = None


class GroundednessParams(BaseModel):
    context: str
    type: Optional[Literal["groundedness"]] = None


class StringMatchParams(BaseModel):
    keyword: str
    type: Optional[Literal["string_match"]] = None


class SemanticSimilarityParams(BaseModel):
    reference: str
    threshold: Optional[float] = None
    type: Optional[Literal["semantic_similarity"]] = None


class JsonPathRule(BaseModel):
    expected_value: Union[bool, float, str]
    expected_value_type: Literal["string", "number", "boolean"]
    json_path: str


class MetadataParams(BaseModel):
    json_path_rules: List[JsonPathRule]
    type: Optional[Literal["metadata"]] = None


CheckType: TypeAlias = Union[
    CorrectnessParams,
    ConformityParams,
    GroundednessParams,
    StringMatchParams,
    MetadataParams,
    SemanticSimilarityParams,
]


# ---------------------------------------------------------------------------
# Assertion parameter TypedDicts (used in requests)
# ---------------------------------------------------------------------------


class ConformityParamsParam(TypedDict, total=False):
    rules: Required[SequenceNotStr[str]]
    type: Literal["conformity"]


class CorrectnessParamsParam(TypedDict, total=False):
    reference: Required[str]
    type: Literal["correctness"]


class GroundednessParamsParam(TypedDict, total=False):
    context: Required[str]
    type: Literal["groundedness"]


class StringMatchParamsParam(TypedDict, total=False):
    keyword: Required[str]
    type: Literal["string_match"]


class SemanticSimilarityParamsParam(TypedDict, total=False):
    reference: Required[str]
    threshold: float
    type: Literal["semantic_similarity"]


class JsonPathRuleParam(TypedDict, total=False):
    expected_value: Required[Union[bool, float, str]]
    expected_value_type: Required[Literal["string", "number", "boolean"]]
    json_path: Required[str]


class MetadataParamsParam(TypedDict, total=False):
    json_path_rules: Required[Iterable[JsonPathRuleParam]]
    type: Literal["metadata"]


CheckTypeParam: TypeAlias = Union[
    CorrectnessParamsParam,
    ConformityParamsParam,
    GroundednessParamsParam,
    StringMatchParamsParam,
    MetadataParamsParam,
    SemanticSimilarityParamsParam,
]


# ---------------------------------------------------------------------------
# Output annotation
# ---------------------------------------------------------------------------


class OutputAnnotation(BaseModel):
    end_char_index: int
    label: str
    start_char_index: int
    text: str
    type: Literal["output", "context"]


# ---------------------------------------------------------------------------
# Check models
# ---------------------------------------------------------------------------


class Check(BaseModel):
    id: str
    built_in: bool
    created_at: datetime
    description: Optional[str] = None
    identifier: str
    name: str
    params: Dict[str, Any] = {}
    project_id: str
    updated_at: datetime

    @pydantic.model_validator(mode="before")
    @classmethod
    def _convert_assertions(cls, data: Any) -> Any:  # noqa: ANN401
        if not isinstance(data, dict):
            return data
        d = cast(Dict[str, Any], data)
        if "params" in d:
            return d
        assertions: list[Any] = d.get("assertions") or []
        return {**d, "params": assertions[0] if assertions else {}}


class CheckResult(BaseModel):
    name: str
    display_name: Optional[str] = None
    status: TaskState
    passed: Optional[bool] = None
    error: Optional[str] = None
    reason: Optional[str] = None
    annotations: Optional[List[OutputAnnotation]] = None


# ---------------------------------------------------------------------------
# Test case check config
# ---------------------------------------------------------------------------


class TestCaseCheckConfig(BaseModel):
    __test__ = False
    identifier: str
    assertions: Optional[List[CheckType]] = None
    enabled: Optional[bool] = None


class TestCaseCheckConfigParam(TypedDict, total=False):
    identifier: Required[str]
    assertions: Optional[Iterable[CheckTypeParam]]
    enabled: bool


# ---------------------------------------------------------------------------
# User-facing check config (simplified format with params instead of assertions)
# ---------------------------------------------------------------------------


def _extract_check_params(check: Dict[str, Any]) -> Dict[str, Any]:
    """Extract params from the first assertion, stripping the ``type`` key."""
    assertions: list[Any] = check.get("assertions") or []
    if not assertions:
        return {}
    first: Any = assertions[0]
    if isinstance(first, BaseModel):
        return first.model_dump(exclude={"type"}, exclude_none=True)
    if isinstance(first, dict):
        return {k: v for k, v in cast(Dict[str, Any], first).items() if k != "type"}
    return {}


class CheckConfig(BaseModel):
    """Simplified check configuration with ``params`` instead of raw ``assertions``."""

    identifier: str
    enabled: Optional[bool] = None
    params: Dict[str, Any] = {}

    @pydantic.model_validator(mode="before")
    @classmethod
    def _convert_assertions(cls, data: Any) -> Any:  # noqa: ANN401
        if not isinstance(data, dict):
            return data
        d = cast(Dict[str, Any], data)
        if "params" in d:
            return d
        return {**d, "params": _extract_check_params(d)}


class CheckConfigParam(TypedDict, total=False):
    identifier: Required[str]
    enabled: bool
    params: Dict[str, Any]


def _check_params_to_api(  # pyright: ignore[reportUnusedFunction]
    checks: Iterable[CheckConfigParam],
) -> list[Dict[str, Any]]:
    """Convert user-facing CheckParam dicts to the API assertions format."""
    return [
        {
            "identifier": check["identifier"],
            "enabled": check.get("enabled", True),
            **(
                {"assertions": [{"type": check["identifier"], **check.get("params", {})}]}
                if check.get("params")
                else {}
            ),
        }
        for check in checks
    ]


# ---------------------------------------------------------------------------
# Check params
# ---------------------------------------------------------------------------


class CheckListParams(TypedDict, total=False):
    project_id: Required[str]
    filter_builtin: bool


class CheckCreateParams(TypedDict, total=False):
    assertions: Required[Iterable[CheckTypeParam]]
    description: Optional[str]
    identifier: Required[str]
    name: Required[str]
    project_id: Required[str]


class CheckUpdateParams(TypedDict, total=False):
    assertions: Optional[Iterable[CheckTypeParam]]
    description: Optional[str]
    identifier: Optional[str]
    name: Optional[str]


class CheckBulkDeleteParams(TypedDict, total=False):
    check_ids: Required[SequenceNotStr[str]]
