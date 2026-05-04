"""Test case domain types."""

from typing import List, Literal, Iterable, Optional, TypeAlias, TypedDict
from datetime import datetime
from typing_extensions import Required

from pydantic import Field

from .chat import ChatMessage, ChatMessageParam, ChatMessageWithMetadataParam
from .user import UserReference
from .agent import AgentOutput
from .check import CheckConfig, TestCaseCheckConfigParam, Interaction, InteractionParam
from .._types import SequenceNotStr
from .._models import BaseModel

__all__ = [
    "TestCase",
    "TestCaseReference",
    "TestCaseComment",
    "TestCaseStatus",
    "BulkMoveTestCasesParams",
    "TestCaseCreateParams",
    "TestCaseUpdateParams",
    "TestCaseBulkDeleteParams",
    "TestCaseBulkUpdateParams",
    "CommentAddParams",
    "CommentEditParams",
]

TestCaseStatus: TypeAlias = Literal["active", "draft"]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class TestCaseComment(BaseModel):
    __test__ = False
    id: str
    content: str = Field(alias="comment")
    created_at: datetime
    updated_at: datetime
    user: UserReference


class TestCaseReference(BaseModel):
    __test__ = False
    id: str


class TestCase(BaseModel):
    __test__ = False
    id: str
    comments: List[TestCaseComment]
    created_at: datetime
    dataset_id: str
    interactions: Optional[List[Interaction]] = None
    tags: List[str]
    updated_at: datetime
    status: TestCaseStatus


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class TestCaseCreateParams(TypedDict, total=False):
    dataset_id: Required[str]
    interactions: Optional[Iterable[InteractionParam]]
    status: Optional[TestCaseStatus]
    tags: SequenceNotStr[str]
    source_probe_attempt_id: Optional[str]


class TestCaseUpdateParams(TypedDict, total=False):
    dataset_id: Optional[str]
    interactions: Optional[Iterable[InteractionParam]]
    tags: Optional[SequenceNotStr[str]]
    status: Optional[TestCaseStatus]


class TestCaseBulkDeleteParams(TypedDict, total=False):
    test_case_ids: Required[SequenceNotStr[str]]


class TestCaseBulkUpdateParams(TypedDict, total=False):
    ids: Required[SequenceNotStr[str]]
    disabled_checks: Optional[SequenceNotStr[str]]
    enabled_checks: Optional[SequenceNotStr[str]]
    added_tags: Optional[SequenceNotStr[str]]
    removed_tags: Optional[SequenceNotStr[str]]
    status: Optional[TestCaseStatus]


class BulkMoveTestCasesParams(TypedDict, total=False):
    test_case_ids: Required[SequenceNotStr[str]]
    dataset_id: Required[str]
    duplicate: Optional[bool]


# ---------------------------------------------------------------------------
# Comment params
# ---------------------------------------------------------------------------


class CommentAddParams(TypedDict, total=False):
    comment: Required[str]


class CommentEditParams(TypedDict, total=False):
    comment: Required[str]
