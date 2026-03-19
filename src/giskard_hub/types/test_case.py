"""Test case domain types."""

from typing import List, Literal, Iterable, Optional, TypedDict
from datetime import datetime
from typing_extensions import Required

from pydantic import Field

from .chat import ChatMessage, ChatMessageParam, ChatMessageWithMetadataParam
from .user import UserReference
from .agent import AgentOutput
from .check import CheckConfig, TestCaseCheckConfigParam
from .._types import SequenceNotStr
from .._models import BaseModel

__all__ = [
    "TestCase",
    "TestCaseReference",
    "TestCaseComment",
    "BulkMoveTestCasesParams",
    "TestCaseCreateParams",
    "TestCaseUpdateParams",
    "TestCaseBulkDeleteParams",
    "TestCaseBulkUpdateParams",
    "CommentAddParams",
    "CommentEditParams",
]


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
    checks: List[CheckConfig]
    comments: List[TestCaseComment]
    created_at: datetime
    dataset_id: str
    demo_output: Optional[AgentOutput] = None
    messages: List[ChatMessage]
    tags: List[str]
    updated_at: datetime
    status: Literal["active", "draft"]


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class TestCaseCreateParams(TypedDict, total=False):
    dataset_id: Required[str]
    messages: Required[Iterable[ChatMessageParam]]
    checks: Iterable[TestCaseCheckConfigParam]
    demo_output: Optional[ChatMessageWithMetadataParam]
    status: Optional[Literal["active", "draft"]]
    tags: SequenceNotStr[str]


class TestCaseUpdateParams(TypedDict, total=False):
    checks: Optional[Iterable[TestCaseCheckConfigParam]]
    dataset_id: Optional[str]
    demo_output: Optional[ChatMessageWithMetadataParam]
    messages: Optional[Iterable[ChatMessageParam]]
    tags: Optional[SequenceNotStr[str]]
    status: Optional[Literal["active", "draft"]]


class TestCaseBulkDeleteParams(TypedDict, total=False):
    test_case_ids: Required[SequenceNotStr[str]]


class TestCaseBulkUpdateParams(TypedDict, total=False):
    ids: Required[SequenceNotStr[str]]
    disabled_checks: Optional[SequenceNotStr[str]]
    enabled_checks: Optional[SequenceNotStr[str]]
    added_tags: Optional[SequenceNotStr[str]]
    removed_tags: Optional[SequenceNotStr[str]]
    status: Optional[Literal["active", "draft"]]


class BulkMoveTestCasesParams(TypedDict, total=False):
    chat_test_case_ids: Required[SequenceNotStr[str]]
    dataset_id: Required[str]
    duplicate: Optional[bool]


# ---------------------------------------------------------------------------
# Comment params
# ---------------------------------------------------------------------------


class CommentAddParams(TypedDict, total=False):
    comment: Required[str]


class CommentEditParams(TypedDict, total=False):
    comment: Required[str]
