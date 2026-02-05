from __future__ import annotations

from typing import Union, Optional, TypeAlias, TypedDict
from typing_extensions import Required

from .task_status import TaskStatus
from .task_priority import TaskPriority

__all__ = ["TaskCreateParams", "RelatedEntityParam"]


class DatasetReferenceParam(TypedDict, total=False):
    type: Required[str]

    dataset_id: Required[str]


class EvaluationReferenceParam(TypedDict, total=False):
    type: Required[str]

    evaluation_id: Required[str]


class ScanReferenceParam(TypedDict, total=False):
    type: Required[str]

    scan_id: Required[str]


class ProbeResultReferenceParam(TypedDict, total=False):
    type: Required[str]

    probe_result_id: Required[str]


class ProbeAttemptReferenceParam(TypedDict, total=False):
    type: Required[str]

    probe_attempt_id: Required[str]


class ChatTestCaseReferenceParam(TypedDict, total=False):
    type: Required[str]

    test_case_id: Required[str]


class ChatTestCaseEvaluationReferenceParam(TypedDict, total=False):
    type: Required[str]

    evaluation_id: Required[str]


RelatedEntityParam: TypeAlias = Union[
    DatasetReferenceParam,
    EvaluationReferenceParam,
    ScanReferenceParam,
    ProbeResultReferenceParam,
    ProbeAttemptReferenceParam,
    ChatTestCaseReferenceParam,
    ChatTestCaseEvaluationReferenceParam,
]


class TaskCreateParams(TypedDict, total=False):
    name: Required[str]

    project_id: Required[str]

    assignee_id: Optional[str]

    description: Optional[str]

    priority: Optional[TaskPriority]

    related_entity: Optional[RelatedEntityParam]

    status: Optional[TaskStatus]
