"""Check, assertion, and annotation types."""

from typing import List, Union, Literal, Iterable, Optional, TypeAlias, TypedDict
from datetime import datetime
from typing_extensions import Required

from .common import TaskState
from .._types import SequenceNotStr
from .._models import BaseModel

__all__ = [
    "Check",
    "CheckResult",
    "Assertion",
    "AssertionParam",
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


Assertion: TypeAlias = Union[
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


AssertionParam: TypeAlias = Union[
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
    type: Literal["output"]


# ---------------------------------------------------------------------------
# Check models
# ---------------------------------------------------------------------------


class Check(BaseModel):
    id: str
    assertions: Optional[List[Assertion]] = None
    built_in: bool
    created_at: datetime
    description: Optional[str] = None
    identifier: str
    name: str
    project_id: str
    updated_at: datetime


class CheckResult(BaseModel):
    annotations: Optional[List[OutputAnnotation]] = None
    display_name: Optional[str] = None
    error: Optional[str] = None
    name: str
    passed: Optional[bool] = None
    reason: Optional[str] = None
    status: TaskState


# ---------------------------------------------------------------------------
# Test case check config
# ---------------------------------------------------------------------------


class TestCaseCheckConfig(BaseModel):
    __test__ = False
    identifier: str
    assertions: Optional[List[Assertion]] = None
    enabled: Optional[bool] = None


class TestCaseCheckConfigParam(TypedDict, total=False):
    identifier: Required[str]
    assertions: Optional[Iterable[AssertionParam]]
    enabled: bool


# ---------------------------------------------------------------------------
# Check params
# ---------------------------------------------------------------------------


class CheckListParams(TypedDict, total=False):
    project_id: Required[str]
    filter_builtin: bool


class CheckCreateParams(TypedDict, total=False):
    assertions: Required[Iterable[AssertionParam]]
    description: Optional[str]
    identifier: Required[str]
    name: Required[str]
    project_id: Required[str]


class CheckUpdateParams(TypedDict, total=False):
    assertions: Optional[Iterable[AssertionParam]]
    description: Optional[str]
    identifier: Optional[str]
    name: Optional[str]


class CheckBulkDeleteParams(TypedDict, total=False):
    check_ids: Required[SequenceNotStr[str]]
