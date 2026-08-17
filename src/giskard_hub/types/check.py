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

from .common import JsonValue, TaskState
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
    "AnswerRelevanceParams",
    "AnswerRelevanceParamsParam",
    "ConformityParams",
    "ConformityParamsParam",
    "ContradictionParams",
    "ContradictionParamsParam",
    "EqualsParams",
    "EqualsParamsParam",
    "GreaterThanParams",
    "GreaterThanParamsParam",
    "GreaterThanEqualsParams",
    "GreaterThanEqualsParamsParam",
    "GroundednessParams",
    "GroundednessParamsParam",
    "HubConformityParams",
    "HubConformityParamsParam",
    "HubCorrectnessParams",
    "HubCorrectnessParamsParam",
    "HubGroundednessParams",
    "HubGroundednessParamsParam",
    "HubMetadataParams",
    "HubMetadataParamsParam",
    "JsonValidParams",
    "JsonValidParamsParam",
    "LessThanParams",
    "LessThanParamsParam",
    "LessThanEqualsParams",
    "LessThanEqualsParamsParam",
    "LLMJudgeParams",
    "LLMJudgeParamsParam",
    "NotEqualsParams",
    "NotEqualsParamsParam",
    "ReadabilityParams",
    "ReadabilityParamsParam",
    "RegexMatchingParams",
    "RegexMatchingParamsParam",
    "SemanticSimilarityParams",
    "SemanticSimilarityParamsParam",
    "StringMatchingParams",
    "StringMatchingParamsParam",
    "ToxicityParams",
    "ToxicityParamsParam",
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

ExpectedValue: TypeAlias = Union[bool, int, float, str]
NormalizationForm: TypeAlias = Literal["NFC", "NFD", "NFKC", "NFKD"]
MatchMode: TypeAlias = Literal["any", "all", "none"]
ReadabilityMetric: TypeAlias = Literal[
    "flesch_reading_ease",
    "flesch_kincaid_grade",
    "gunning_fog",
    "automated_readability_index",
    "coleman_liau_index",
    "dale_chall_readability_score",
]
ToxicityCategory: TypeAlias = Literal["hate_speech", "harassment", "threats", "self_harm", "sexual_content", "violence"]


class HubConformityParams(BaseModel):
    rules: List[str]
    text_key: Optional[str] = None
    type: Optional[Literal["hub_conformity"]] = None


class HubCorrectnessParams(BaseModel):
    reference: str
    text_key: Optional[str] = None
    type: Optional[Literal["hub_correctness"]] = None


class HubGroundednessParams(BaseModel):
    context: str
    text_key: Optional[str] = None
    type: Optional[Literal["hub_groundedness"]] = None


class JsonPathRule(BaseModel):
    expected_value: ExpectedValue
    expected_value_type: Literal["string", "number", "boolean"]
    json_path: str


class HubMetadataParams(BaseModel):
    json_path_rules: List[JsonPathRule]
    metadata_key: Optional[str] = None
    type: Optional[Literal["hub_metadata"]] = None


class ConformityParams(BaseModel):
    rule: str
    type: Optional[Literal["conformity"]] = None


class GroundednessParams(BaseModel):
    answer: Optional[str] = None
    answer_key: Optional[str] = None
    context: Optional[Union[str, List[str]]] = None
    context_key: Optional[str] = None
    type: Optional[Literal["groundedness"]] = None


class StringMatchingParams(BaseModel):
    keyword: Optional[str] = None
    keyword_key: Optional[str] = None
    text: Optional[str] = None
    text_key: Optional[str] = None
    normalization_form: Optional[NormalizationForm] = None
    case_sensitive: Optional[bool] = None
    type: Optional[Literal["string_matching"]] = None


class RegexMatchingParams(BaseModel):
    pattern: Optional[str] = None
    pattern_key: Optional[str] = None
    text: Optional[str] = None
    text_key: Optional[str] = None
    match_timeout_seconds: Optional[float] = None
    type: Optional[Literal["regex_matching"]] = None


class _ComparisonParams(BaseModel):
    key: Optional[str] = None
    expected_value: Optional[ExpectedValue] = None
    expected_value_key: Optional[str] = None
    normalization_form: Optional[NormalizationForm] = None
    match: Optional[MatchMode] = None


class EqualsParams(_ComparisonParams):
    type: Optional[Literal["equals"]] = None


class NotEqualsParams(_ComparisonParams):
    type: Optional[Literal["not_equals"]] = None


class GreaterThanParams(_ComparisonParams):
    type: Optional[Literal["greater_than"]] = None


class GreaterThanEqualsParams(_ComparisonParams):
    type: Optional[Literal["greater_than_equals"]] = None


class LessThanParams(_ComparisonParams):
    type: Optional[Literal["less_than"]] = None


class LessThanEqualsParams(_ComparisonParams):
    type: Optional[Literal["less_than_equals"]] = None


class SemanticSimilarityParams(BaseModel):
    reference_text: Optional[str] = None
    reference_text_key: Optional[str] = None
    actual_answer_key: Optional[str] = None
    threshold: Optional[float] = None
    type: Optional[Literal["semantic_similarity"]] = None


class ContradictionParams(BaseModel):
    answer: Optional[str] = None
    answer_key: Optional[str] = None
    context: Optional[Union[str, List[str]]] = None
    context_key: Optional[str] = None
    type: Optional[Literal["contradiction"]] = None


class ToxicityParams(BaseModel):
    categories: Optional[List[ToxicityCategory]] = None
    output: Optional[str] = None
    output_key: Optional[str] = None
    type: Optional[Literal["toxicity"]] = None


class AnswerRelevanceParams(BaseModel):
    question: Optional[str] = None
    question_key: Optional[str] = None
    answer: Optional[str] = None
    answer_key: Optional[str] = None
    context: Optional[str] = None
    include_history: Optional[bool] = None
    type: Optional[Literal["answer_relevance"]] = None


class JsonValidParams(BaseModel):
    key: Optional[str] = None
    parse: Optional[bool] = None
    expected_schema: Optional[Dict[str, Any]] = None
    type: Optional[Literal["json_valid"]] = None


class ReadabilityParams(BaseModel):
    key: Optional[str] = None
    metric: Optional[ReadabilityMetric] = None
    min_score: Optional[float] = None
    max_score: Optional[float] = None
    type: Optional[Literal["readability"]] = None


class LLMJudgeParams(BaseModel):
    prompt: Optional[str] = None
    prompt_path: Optional[str] = None
    type: Optional[Literal["llm_judge"]] = None


CheckType: TypeAlias = Union[
    AnswerRelevanceParams,
    ConformityParams,
    ContradictionParams,
    EqualsParams,
    GreaterThanParams,
    GreaterThanEqualsParams,
    GroundednessParams,
    HubConformityParams,
    HubCorrectnessParams,
    HubGroundednessParams,
    HubMetadataParams,
    JsonValidParams,
    LessThanParams,
    LessThanEqualsParams,
    LLMJudgeParams,
    NotEqualsParams,
    ReadabilityParams,
    RegexMatchingParams,
    SemanticSimilarityParams,
    StringMatchingParams,
    ToxicityParams,
]


# ---------------------------------------------------------------------------
# Check parameter TypedDicts (used in requests)
# ---------------------------------------------------------------------------


class HubConformityParamsParam(TypedDict, total=False):
    rules: Required[SequenceNotStr[str]]
    text_key: str
    type: Literal["hub_conformity"]


class HubCorrectnessParamsParam(TypedDict, total=False):
    reference: Required[str]
    text_key: str
    type: Literal["hub_correctness"]


class HubGroundednessParamsParam(TypedDict, total=False):
    context: Required[str]
    text_key: str
    type: Literal["hub_groundedness"]


class JsonPathRuleParam(TypedDict, total=False):
    expected_value: Required[ExpectedValue]
    expected_value_type: Required[Literal["string", "number", "boolean"]]
    json_path: Required[str]


class HubMetadataParamsParam(TypedDict, total=False):
    json_path_rules: Required[Iterable[JsonPathRuleParam]]
    metadata_key: str
    type: Literal["hub_metadata"]


class ConformityParamsParam(TypedDict, total=False):
    rule: Required[str]
    type: Literal["conformity"]


class GroundednessParamsParam(TypedDict, total=False):
    answer: str
    answer_key: str
    context: Union[str, SequenceNotStr[str]]
    context_key: str
    type: Literal["groundedness"]


class StringMatchingParamsParam(TypedDict, total=False):
    keyword: str
    keyword_key: str
    text: str
    text_key: str
    normalization_form: NormalizationForm
    case_sensitive: bool
    type: Literal["string_matching"]


class RegexMatchingParamsParam(TypedDict, total=False):
    pattern: str
    pattern_key: str
    text: str
    text_key: str
    match_timeout_seconds: float
    type: Literal["regex_matching"]


class _ComparisonParamsParam(TypedDict, total=False):
    key: str
    expected_value: ExpectedValue
    expected_value_key: str
    normalization_form: NormalizationForm
    match: MatchMode


class EqualsParamsParam(_ComparisonParamsParam, total=False):
    type: Literal["equals"]


class NotEqualsParamsParam(_ComparisonParamsParam, total=False):
    type: Literal["not_equals"]


class GreaterThanParamsParam(_ComparisonParamsParam, total=False):
    type: Literal["greater_than"]


class GreaterThanEqualsParamsParam(_ComparisonParamsParam, total=False):
    type: Literal["greater_than_equals"]


class LessThanParamsParam(_ComparisonParamsParam, total=False):
    type: Literal["less_than"]


class LessThanEqualsParamsParam(_ComparisonParamsParam, total=False):
    type: Literal["less_than_equals"]


class SemanticSimilarityParamsParam(TypedDict, total=False):
    reference_text: str
    reference_text_key: str
    actual_answer_key: str
    threshold: float
    type: Literal["semantic_similarity"]


class ContradictionParamsParam(TypedDict, total=False):
    answer: str
    answer_key: str
    context: Union[str, SequenceNotStr[str]]
    context_key: str
    type: Literal["contradiction"]


class ToxicityParamsParam(TypedDict, total=False):
    categories: SequenceNotStr[ToxicityCategory]
    output: str
    output_key: str
    type: Literal["toxicity"]


class AnswerRelevanceParamsParam(TypedDict, total=False):
    question: str
    question_key: str
    answer: str
    answer_key: str
    context: str
    include_history: bool
    type: Literal["answer_relevance"]


class JsonValidParamsParam(TypedDict, total=False):
    key: str
    parse: bool
    expected_schema: Dict[str, Any]
    type: Literal["json_valid"]


class ReadabilityParamsParam(TypedDict, total=False):
    key: str
    metric: ReadabilityMetric
    min_score: float
    max_score: float
    type: Literal["readability"]


class LLMJudgeParamsParam(TypedDict, total=False):
    prompt: str
    prompt_path: str
    type: Literal["llm_judge"]


CheckTypeParam: TypeAlias = Union[
    AnswerRelevanceParamsParam,
    ConformityParamsParam,
    ContradictionParamsParam,
    EqualsParamsParam,
    GreaterThanParamsParam,
    GreaterThanEqualsParamsParam,
    GroundednessParamsParam,
    HubConformityParamsParam,
    HubCorrectnessParamsParam,
    HubGroundednessParamsParam,
    HubMetadataParamsParam,
    JsonValidParamsParam,
    LessThanParamsParam,
    LessThanEqualsParamsParam,
    LLMJudgeParamsParam,
    NotEqualsParamsParam,
    ReadabilityParamsParam,
    RegexMatchingParamsParam,
    SemanticSimilarityParamsParam,
    StringMatchingParamsParam,
    ToxicityParamsParam,
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
    identifier: str
    check_id: str
    enabled: bool
    params: Dict[str, Any]
    override_spec: Dict[str, Any]


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
    # Same shape as `CheckConfigParam`: name the check by its `identifier`
    # (e.g. "hub_correctness") and pass its config in `params`. The API resolves
    # the identifier server-side.
    identifier: Required[str]
    enabled: bool
    params: Dict[str, Any]


class InteractionResultData(BaseModel):
    interaction_position: int
    input: Optional[JsonValue] = None
    output: Optional[JsonValue] = None
    state: str = ""
    check_results: List[CheckResult] = Field(default_factory=list)  # pyright: ignore[reportUnknownVariableType]
    error: Optional[str] = None
    checks: Optional[List[InteractionCheckConfig]] = None


class Interaction(BaseModel):
    position: int
    input: Dict[str, Any]
    output: Optional[Dict[str, Any]] = None
    simulator_config: Optional[Dict[str, Any]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    id: Optional[str] = None
    checks: Optional[List[InteractionCheckConfig]] = None


class InteractionParam(TypedDict, total=False):
    position: int
    input: Required[JsonValue]
    output: Optional[JsonValue]
    checks: Optional[Iterable[InteractionCheckConfigParam]]
