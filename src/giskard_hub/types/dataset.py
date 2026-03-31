"""Dataset domain types."""

from typing import Any, Dict, List, Literal, Iterable, Optional, TypedDict
from datetime import datetime
from typing_extensions import Required

from .common import TaskState, OrderByParam, TaskProgress, FilterValueParam, TaskProgressParam
from .._types import FileTypes, SequenceNotStr
from .._models import BaseModel

__all__ = [
    "Dataset",
    "DatasetReference",
    "DatasetSubset",
    "DatasetSubsetParam",
    "DatasetListParams",
    "DatasetCreateParams",
    "DatasetImportParams",
    "DatasetUpdateParams",
    "DatasetBulkDeleteParams",
    "DatasetSearchTestCasesParams",
    "TestCaseOrderByParam",
    "TestCaseFiltersParam",
    "DatasetGenerateAdversarialParams",
    "DatasetGenerateDocumentBasedParams",
    "DatasetGenerateScenarioBasedParams",
]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class Dataset(BaseModel):
    id: str
    created_at: datetime
    description: Optional[str] = None
    name: str
    project_id: str
    status: TaskProgress
    tags: List[str]
    updated_at: datetime

    @property
    def state(self) -> TaskState:
        return self.status.state


class DatasetReference(BaseModel):
    id: str
    name: str


class DatasetSubset(BaseModel):
    dataset_id: str
    tags: Optional[List[str]] = None
    target_type: Optional[Literal["dataset"]] = None


class DatasetSubsetParam(TypedDict, total=False):
    dataset_id: Required[str]
    tags: Optional[SequenceNotStr[str]]
    target_type: Literal["dataset"]


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class DatasetListParams(TypedDict, total=False):
    project_id: Optional[str]


class DatasetCreateParams(TypedDict, total=False):
    name: Required[str]
    project_id: Required[str]
    description: Optional[str]


class DatasetImportParams(TypedDict, total=False):
    file: Required[FileTypes]
    project_id: Required[str]
    dataset_id: Optional[str]
    name: Optional[str]


class DatasetUpdateParams(TypedDict, total=False):
    description: Optional[str]
    name: Optional[str]
    status: Optional[TaskProgressParam]


class DatasetBulkDeleteParams(TypedDict, total=False):
    dataset_ids: Required[SequenceNotStr[str]]


# ---------------------------------------------------------------------------
# Search params
# ---------------------------------------------------------------------------

TestCaseSortColumn = Literal["created_at", "id", "status", "updated_at"]
TestCaseFilterColumn = Literal["metrics", "status", "tags"]

TestCaseOrderByParam = OrderByParam[TestCaseSortColumn]
TestCaseFiltersParam = Dict[TestCaseFilterColumn, FilterValueParam]


class DatasetSearchTestCasesParams(TypedDict, total=False):
    search: Optional[str]
    order_by: Optional[List[TestCaseOrderByParam]]
    filters: Optional[TestCaseFiltersParam]
    limit: int
    offset: int


# ---------------------------------------------------------------------------
# Generation params
# ---------------------------------------------------------------------------


class Category(TypedDict, total=False):
    desc: Required[str]
    name: Required[str]
    id: Optional[str]


class DatasetGenerateAdversarialParams(TypedDict, total=False):
    agent_id: Required[str]
    project_id: Required[str]
    categories: Iterable[Category]
    dataset_name: str
    description: Optional[str]
    n_examples_per_category: int


class DatasetGenerateDocumentBasedParams(TypedDict, total=False):
    agent_id: Required[str]
    knowledge_base_id: Required[str]
    project_id: Required[str]
    dataset_name: str
    description: Optional[str]
    n_examples: int
    topic_ids: SequenceNotStr[str]


class DatasetGenerateScenarioBasedParams(TypedDict, total=False):
    agent_id: Required[str]
    project_id: Required[str]
    scenario_id: Required[str]
    dataset_name: Optional[str]
    n_examples: int
    scenario_config: Optional[Dict[str, Any]]
