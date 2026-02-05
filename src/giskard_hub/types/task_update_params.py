from __future__ import annotations

from typing import Union, Optional, TypeAlias, TypedDict

from .task_status import TaskStatus
from .task_priority import TaskPriority

__all__ = ["TaskUpdateParams", "RelatedEntityParam"]


class DatasetReferenceParam(TypedDict, total=False):
    type: str

    dataset_id: str


class EvaluationReferenceParam(TypedDict, total=False):
    type: str

    evaluation_id: str


class ScanReferenceParam(TypedDict, total=False):
    type: str

    scan_id: str


class ProbeResultReferenceParam(TypedDict, total=False):
    type: str

    probe_result_id: str


class ProbeAttemptReferenceParam(TypedDict, total=False):
    type: str

    probe_attempt_id: str


class ChatTestCaseReferenceParam(TypedDict, total=False):
    type: str

    test_case_id: str


class ChatTestCaseEvaluationReferenceParam(TypedDict, total=False):
    type: str

    evaluation_id: str


RelatedEntityParam: TypeAlias = Union[
    DatasetReferenceParam,
    EvaluationReferenceParam,
    ScanReferenceParam,
    ProbeResultReferenceParam,
    ProbeAttemptReferenceParam,
    ChatTestCaseReferenceParam,
    ChatTestCaseEvaluationReferenceParam,
]


class TaskUpdateParams(TypedDict, total=False):
    assignee_id: Optional[str]

    description: Optional[str]

    name: Optional[str]

    priority: Optional[TaskPriority]

    related_entity: Optional[RelatedEntityParam]

    status: Optional[TaskStatus]
