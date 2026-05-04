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


# Mirrors the backend
_IDENTIFIER_TO_KIND: Dict[str, str] = {
    "correctness": "hub_correctness",
    "conformity": "hub_conformity",
    "groundedness": "hub_groundedness",
    "string_match": "string_matching",
    "metadata": "hub_metadata",
    "semantic_similarity": "semantic_similarity",
}


def _extract_check_params(check: Dict[str, Any]) -> Dict[str, Any]:
    spec: Any = check.get("spec") or {}
    if isinstance(spec, BaseModel):
        return spec.model_dump(exclude={"kind"}, exclude_none=True)
    if isinstance(spec, dict):
        return {k: v for k, v in cast(Dict[str, Any], spec).items() if k != "kind"}
    return {}


def _check_param_to_spec(identifier: Optional[str], params: Any) -> Dict[str, Any]:
    """Build a `spec` dict, deriving `kind` from `params["type"]` then `identifier`."""
    if isinstance(params, BaseModel):
        params_dict: Dict[str, Any] = params.model_dump(exclude_none=True)
    elif isinstance(params, dict):
        params_dict = dict(cast(Dict[str, Any], params))
    else:
        params_dict = {}
    type_from_params = params_dict.pop("type", None)
    type_str = type_from_params or identifier or ""
    if not type_str:
        raise ValueError(
            "Cannot derive check kind: provide 'identifier' or include 'type' in 'params', "
            "or pass 'spec' directly with an explicit 'kind'."
        )
    kind = _IDENTIFIER_TO_KIND.get(type_str, type_str)
    return {"kind": kind, **params_dict}


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


def _check_params_to_api(  # pyright: ignore[reportUnusedFunction]
    checks: Iterable[CheckConfigParam],
) -> list[Dict[str, Any]]:
    return [
        {
            "identifier": check["identifier"],
            "enabled": check.get("enabled", True),
            **(
                {"spec": _check_param_to_spec(check["identifier"], check.get("params", {}))}
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
