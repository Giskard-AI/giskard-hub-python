"""Evaluation domain types."""

from typing import Dict, List, Union, Literal, Iterable, Optional, TypeAlias, TypedDict
from datetime import datetime  # noqa: I001
from typing_extensions import Required

from .chat import ChatMessageParam
from .agent import Agent, AgentOutput, MinimalAgent, AgentReference, AgentOutputParam, MinimalAgentParam
from .check import CheckResult
from .common import TaskState, OrderByParam, TaskProgress, FilterValueParam
from .._types import SequenceNotStr
from .dataset import Dataset, DatasetSubset, DatasetReference, DatasetSubsetParam
from .._models import BaseModel
from .test_case import TestCase, TestCaseReference

__all__ = [
    "Metric",
    "Evaluation",
    "EvaluationReference",
    "EvaluationListParams",
    "EvaluationCreateParams",
    "EvaluationUpdateParams",
    "EvaluationRetrieveParams",
    "EvaluationRunSingleParams",
    "EvaluationCreateLocalParams",
    "EvaluationBulkDeleteParams",
    "Criterion",
    "CriterionEvaluationDataset",
    "FailureCategory",
    "FailureCategoryParam",
    "TestCaseEvaluation",
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
    agent: AgentReference | MinimalAgent | Agent
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
# Test case evaluation
# ---------------------------------------------------------------------------


class FailureCategoryResult(BaseModel):
    category: Optional[FailureCategory] = None
    error: Optional[str] = None
    status: Optional[TaskState] = None


class TestCaseEvaluationReference(BaseModel):
    id: str


class TestCaseEvaluation(BaseModel):
    __test__ = False
    id: str
    created_at: datetime
    updated_at: datetime
    error: Optional[str] = None
    evaluation_id: str
    failure_category: Optional[FailureCategoryResult] = None
    output: Optional[AgentOutput] = None
    results: List[CheckResult]
    state: TaskState
    test_case: TestCaseReference | TestCase
    hidden: bool
    test_case_exists: Optional[bool] = None


# ---------------------------------------------------------------------------
# Evaluation params
# ---------------------------------------------------------------------------


class EvaluationListParams(TypedDict, total=False):
    project_id: Required[str]
    include: Optional[List[Literal["agent", "dataset"]]]


class EvaluationCreateParams(TypedDict, total=False):
    agent_id: Required[str]
    project_id: Required[str]
    criteria: Optional[DatasetSubsetParam]
    name: str
    old_evaluation_id: Optional[str]
    run_count: Optional[int]
    scheduled_evaluation_id: Optional[str]


class EvaluationUpdateParams(TypedDict, total=False):
    name: Required[str]


class EvaluationRetrieveParams(TypedDict, total=False):
    include: Optional[List[Literal["agent", "dataset"]]]


class EvaluationRunSingleParams(TypedDict, total=False):
    checks: Required[Iterable[Dict[str, object]]]
    messages: Required[Iterable[ChatMessageParam]]
    model_output: Required[AgentOutputParam]
    model_description: str
    project_id: Optional[str]


class CriterionEvaluationDataset(TypedDict, total=False):
    evaluation_id: Required[str]
    target_type: Literal["evaluation"]


Criterion: TypeAlias = Union[DatasetSubsetParam, CriterionEvaluationDataset]


class EvaluationCreateLocalParams(TypedDict, total=False):
    criteria: Required[Iterable[Criterion]]
    model: Required[MinimalAgentParam]
    name: Optional[str]


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
    include: Optional[List[Literal["test_case"]]]


class ResultRetrieveParams(TypedDict, total=False):
    include: Optional[List[Literal["test_case"]]]


class ResultSearchParams(TypedDict, total=False):
    search: Optional[str]
    order_by: Optional[List[ResultOrderByParam]]
    filters: Optional[ResultFiltersParam]
    limit: int
    offset: int
    include: Optional[List[Literal["test_case"]]]


class ResultUpdateParams(TypedDict, total=False):
    failure_category: Optional[FailureCategoryParam]


class ResultUpdateVisibilityParams(TypedDict, total=False):
    hidden: Required[bool]
    set_test_case_draft: Optional[bool]


class ResultSubmitLocalOutputParams(TypedDict, total=False):
    error: Optional[str]
    output: Optional[AgentOutputParam]
