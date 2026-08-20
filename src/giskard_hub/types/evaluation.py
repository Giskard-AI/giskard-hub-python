"""Evaluation domain types."""

from typing import (
    Any,
    Dict,
    List,
    Union,
    Literal,
    Iterable,
    Optional,
    TypedDict,
)
from datetime import datetime  # noqa: I001
from typing_extensions import Required, deprecated

from .agent import AgentOutput, AgentInterface, AgentOutputParam, MinimalAgentParam
from .check import CheckResult, FlatCheckSpecParam, InteractionResultData
from .common import JsonValue, TaskState, OrderByParam, TaskProgress, FilterValueParam
from .._types import SequenceNotStr
from .dataset import Dataset, DatasetSubset, DatasetReference, DatasetSubsetParam
from .._models import BaseModel
from .scenario import Scenario, ScenarioReference

__all__ = [
    "Metric",
    "Evaluation",
    "EvaluationReference",
    "EvaluationListParams",
    "EvaluationCreateParams",
    "EvaluationUpdateParams",
    "EvaluationRetrieveParams",
    "EvaluationRunInteractionChecksParams",
    "EvaluationCreateLocalParams",
    "EvaluationUploadParams",
    "EvaluationBulkDeleteParams",
    "FailureCategory",
    "FailureCategoryParam",
    "ScenarioEvaluation",
    "TestCaseEvaluation",
    "ScenarioEvaluationReference",
    "TestCaseEvaluationReference",
    "ResultListParams",
    "ResultRetrieveParams",
    "ResultSearchParams",
    "ResultOrderByParam",
    "ResultFiltersParam",
    "ResultUpdateParams",
    "ResultUpdateVisibilityParams",
    "ResultSubmitLocalOutputParams",
]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class Metric(BaseModel):
    name: str
    display_name: Optional[str] = None
    errored: Optional[int] = None
    failed: Optional[int] = None
    passed: Optional[int] = None
    total: Optional[int] = None
    success_rate: Optional[float] = None


class EvaluationReference(BaseModel):
    id: str
    name: str


class Evaluation(BaseModel):
    id: str
    agent: AgentInterface
    created_at: datetime
    criteria: Optional[DatasetSubset] = None
    dataset: Dataset | DatasetReference
    failure_categories: Dict[str, int]
    local: bool
    metrics: List[Metric]
    name: str
    old_evaluation_id: Optional[str] = None
    project_id: str
    scheduled_evaluation_id: Optional[str] = None
    status: TaskProgress
    tags: List[Metric]
    updated_at: datetime
    is_upload: bool = False

    @property
    def state(self) -> TaskState:
        return self.status.state


# ---------------------------------------------------------------------------
# Failure category
# ---------------------------------------------------------------------------


class FailureCategory(BaseModel):
    description: str
    identifier: str
    title: str


class FailureCategoryParam(TypedDict, total=False):
    description: Required[str]
    identifier: Required[str]
    title: Required[str]


# ---------------------------------------------------------------------------
# Scenario evaluation
# ---------------------------------------------------------------------------


class FailureCategoryResult(BaseModel):
    category: Optional[FailureCategory] = None
    error: Optional[str] = None
    status: Optional[TaskState] = None


class DivergenceWarning(BaseModel):
    turn: int
    expected: str
    actual: str


class ScenarioEvaluationReference(BaseModel):
    id: str


TestCaseEvaluationReference = ScenarioEvaluationReference


class ScenarioEvaluation(BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    error: Optional[str] = None
    evaluation_id: str
    failure_category: Optional[FailureCategoryResult] = None
    output: Optional[Union[AgentOutput, JsonValue]] = None
    results: List[CheckResult]
    state: TaskState
    scenario: ScenarioReference | Scenario
    hidden: bool
    scenario_exists: Optional[bool] = None
    interaction_results: Optional[List[InteractionResultData]] = None

    @property
    @deprecated("`.test_case` is deprecated; read `.scenario` instead.")
    def test_case(self) -> ScenarioReference | Scenario:
        """Deprecated alias for `scenario`."""
        return self.scenario

    @property
    @deprecated("`.test_case_exists` is deprecated; read `.scenario_exists` instead.")
    def test_case_exists(self) -> Optional[bool]:
        """Deprecated alias for `scenario_exists`."""
        return self.scenario_exists


class TestCaseEvaluation(ScenarioEvaluation):
    __test__ = False


# ---------------------------------------------------------------------------
# Evaluation params
# ---------------------------------------------------------------------------


class EvaluationListParams(TypedDict, total=False):
    project_id: Required[str]


class EvaluationCreateParams(TypedDict, total=False):
    project_id: Required[str]
    agent_id: Optional[str]
    criteria: Optional[DatasetSubsetParam]
    name: str
    old_evaluation_id: Optional[str]
    run_count: Optional[int]
    scheduled_evaluation_id: Optional[str]


class EvaluationUpdateParams(TypedDict, total=False):
    name: Required[str]


class EvaluationRetrieveParams(TypedDict, total=False):
    pass


class EvaluationRunInteractionChecksParams(TypedDict, total=False):
    project_id: Required[str]
    input_data: Required[Dict[str, Any]]
    model_output: Required[Dict[str, Any]]
    checks: Required[Iterable[FlatCheckSpecParam]]


class EvaluationCreateLocalParams(TypedDict, total=False):
    criteria: Required[DatasetSubsetParam]
    model: Required[MinimalAgentParam]
    name: Optional[str]


class EvaluationUploadParams(TypedDict, total=False):
    project_id: Required[str]
    payload: Required[Dict[str, Any]]
    agent_id: Optional[str]
    name: Optional[str]
    auto_classify_failures: Optional[bool]


class EvaluationBulkDeleteParams(TypedDict, total=False):
    evaluation_ids: Required[SequenceNotStr[str]]


# ---------------------------------------------------------------------------
# Result params
# ---------------------------------------------------------------------------


ResultSortColumn = Literal["failure_category_name", "id", "sample_success", "status", "visibility"]
ResultFilterColumn = Literal["failure_category_name", "metrics", "sample_success", "status", "tags", "visibility"]

ResultOrderByParam = OrderByParam[ResultSortColumn]
ResultFiltersParam = Dict[ResultFilterColumn, FilterValueParam]


class ResultListParams(TypedDict, total=False):
    include: Optional[List[Literal["scenario", "test_case"]]]


class ResultRetrieveParams(TypedDict, total=False):
    include: Optional[List[Literal["scenario", "test_case"]]]


class ResultSearchParams(TypedDict, total=False):
    search: Optional[str]
    order_by: Optional[List[ResultOrderByParam]]
    filters: Optional[ResultFiltersParam]
    limit: int
    offset: int
    include: Optional[List[Literal["scenario", "test_case"]]]


class ResultUpdateParams(TypedDict, total=False):
    failure_category: Optional[FailureCategoryParam]


class ResultUpdateVisibilityParams(TypedDict, total=False):
    hidden: Required[bool]
    set_scenario_draft: Optional[bool]


class ResultSubmitLocalOutputParams(TypedDict, total=False):
    error: Optional[str]
    output: Optional[AgentOutputParam]
