"""Check, spec, and annotation types."""

from typing import (
    Any,
    Dict,
    List,
    Union,
    Literal,
    Iterable,
    Optional,
    TypeAlias,
    TypedDict,
    cast,
)
from datetime import datetime
from typing_extensions import Required

import pydantic
from pydantic import Field

from .common import TaskState
from .._types import SequenceNotStr
from .._models import BaseModel

__all__ = [
    "Check",
    "CheckResult",
    "CheckConfig",
    "CheckConfigParam",
    "CheckSource",
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
    "Annotation",
    "OutputAnnotation",
    "ContextAnnotation",
    "TestCaseCheckConfigParam",
    "CheckListParams",
    "CheckCreateParams",
    "CheckUpdateParams",
    "CheckBulkDeleteParams",
    "Interaction",
    "InteractionParam",
    "InteractionCheckConfig",
    "InteractionCheckConfigParam",
    "InteractionResultData",
    "FlatCheckSpec",
    "FlatCheckSpecParam",
]

CheckSource: TypeAlias = Literal["builtin", "project"]


# ---------------------------------------------------------------------------
# Check parameter models (BaseModel)
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
    expected_value: Union[bool, int, float, str]
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
# Check parameter TypedDicts (used in requests)
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
    expected_value: Required[Union[bool, int, float, str]]
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
# Annotations
# ---------------------------------------------------------------------------


class _BaseAnnotation(BaseModel):
    end_char_index: int
    label: str
    start_char_index: int
    text: str


class OutputAnnotation(_BaseAnnotation):
    type: Literal["output"]


class ContextAnnotation(_BaseAnnotation):
    type: Literal["context"]


Annotation: TypeAlias = Union[OutputAnnotation, ContextAnnotation]


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
    source: CheckSource = "project"
    updated_at: datetime
    spec: Dict[str, Any] = {}

    @pydantic.model_validator(mode="before")
    @classmethod
    def _convert_spec(cls, data: Any) -> Any:  # noqa: ANN401
        if not isinstance(data, dict):
            return data
        d = cast(Dict[str, Any], data)
        if "params" in d:
            return d
        return {**d, "params": _extract_check_params(d)}


class CheckResult(BaseModel):
    name: str
    display_name: Optional[str] = None
    status: TaskState
    passed: Optional[bool] = None
    error: Optional[str] = None
    reason: Optional[str] = None
    annotations: Optional[List[Annotation]] = None
    details: Optional[Dict[str, Any]] = None
    spec: Optional[Dict[str, Any]] = None
    target: Optional[str] = None
    reference_text: Optional[str] = None


# ---------------------------------------------------------------------------
# Test case check config
# ---------------------------------------------------------------------------


class TestCaseCheckConfigParam(TypedDict, total=False):
    identifier: Required[str]
    enabled: bool
    spec: Optional[Dict[str, Any]]
    position: int


# ---------------------------------------------------------------------------
# User-facing check config
# ---------------------------------------------------------------------------


def _extract_check_params(check: Dict[str, Any]) -> Dict[str, Any]:
    """Strip `kind` from `spec` to derive the user-facing `params` dict."""
    spec: Any = check.get("spec") or {}
    if isinstance(spec, BaseModel):
        return spec.model_dump(exclude={"kind"}, exclude_none=True)
    if isinstance(spec, dict):
        return {k: v for k, v in cast(Dict[str, Any], spec).items() if k != "kind"}
    return {}


class CheckConfig(BaseModel):
    identifier: str
    enabled: Optional[bool] = None
    spec: Optional[Dict[str, Any]] = None
    position: int
    params: Dict[str, Any] = {}

    @pydantic.model_validator(mode="before")
    @classmethod
    def _convert_spec(cls, data: Any) -> Any:  # noqa: ANN401
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


# ---------------------------------------------------------------------------
# Check params
# ---------------------------------------------------------------------------


class CheckListParams(TypedDict, total=False):
    project_id: Required[str]
    filter_builtin: bool


class CheckCreateParams(TypedDict, total=False):
    description: Optional[str]
    identifier: Required[str]
    name: Required[str]
    project_id: Required[str]
    spec: Required[Dict[str, Any]]


class CheckUpdateParams(TypedDict, total=False):
    description: Optional[str]
    identifier: Optional[str]
    name: Optional[str]
    spec: Optional[Dict[str, Any]]


class CheckBulkDeleteParams(TypedDict, total=False):
    check_ids: Required[SequenceNotStr[str]]


# ---------------------------------------------------------------------------
# Interaction types
# ---------------------------------------------------------------------------


# Back-compat re-export. The canonical home is
# `giskard_hub.resources._check_helpers.IDENTIFIER_TO_KIND`.
def __getattr__(name: str) -> Any:
    if name == "_IDENTIFIER_TO_KIND":
        import warnings

        from ..resources._check_helpers import IDENTIFIER_TO_KIND

        warnings.warn(
            "Importing `_IDENTIFIER_TO_KIND` from `giskard_hub.types.check` is "
            "deprecated; import `IDENTIFIER_TO_KIND` from "
            "`giskard_hub.resources._check_helpers` instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return IDENTIFIER_TO_KIND
    raise AttributeError(f"module 'giskard_hub.types.check' has no attribute {name!r}")


class FlatCheckSpec(BaseModel):
    check_id: Optional[str] = None
    identifier: Optional[str] = None
    override_spec: Optional[Dict[str, Any]] = None
    target: Optional[str] = None


class FlatCheckSpecParam(TypedDict, total=False):
    check_id: Optional[str]
    identifier: Optional[str]
    override_spec: Optional[Dict[str, Any]]
    target: Optional[str]


class InteractionCheckConfig(BaseModel):
    check_id: str
    name: Optional[str] = None
    target: Optional[str] = None
    enabled: bool = True
    override_spec: Optional[Dict[str, Any]] = None
    position: int = 0
    spec: Optional[Dict[str, Any]] = None


class InteractionCheckConfigParam(TypedDict, total=False):
    check_id: Required[str]
    name: Optional[str]
    target: Optional[str]
    enabled: bool
    override_spec: Optional[Dict[str, Any]]
    position: int
    spec: Optional[Dict[str, Any]]


class InteractionResultData(BaseModel):
    interaction_position: int
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
    state: str = ""
    check_results: List[CheckResult] = Field(default_factory=list)  # pyright: ignore[reportUnknownVariableType]
    error: Optional[str] = None
    checks: Optional[List[InteractionCheckConfig]] = None


class Interaction(BaseModel):
    position: int
    input: Dict[str, Any]
    input_bindings: Optional[Dict[str, str]] = None
    output: Optional[Dict[str, Any]] = None
    simulator_config: Optional[Dict[str, Any]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    id: Optional[str] = None
    checks: Optional[List[InteractionCheckConfig]] = None


class InteractionParam(TypedDict, total=False):
    position: Required[int]
    input: Required[Dict[str, Any]]
    input_bindings: Optional[Dict[str, str]]
    output: Optional[Dict[str, Any]]
    simulator_config: Optional[Dict[str, Any]]
    test_case_id: Optional[str]
    checks: Optional[Iterable[InteractionCheckConfigParam]]
