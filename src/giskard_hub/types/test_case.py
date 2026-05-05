"""Test case domain types."""

from typing import Any, Dict, List, Literal, Iterable, Optional, TypeAlias, TypedDict, cast
from datetime import datetime
from typing_extensions import Required, deprecated

from pydantic import Field

from .chat import ChatMessage
from .user import UserReference
from .check import Interaction, InteractionParam
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


def _first_interaction_messages(interactions: Optional[List[Interaction]]) -> List[ChatMessage]:
    """Extract chat messages from `interactions[0].input["messages"]`.

    Returns an empty list if there are no interactions or the input is not
    shaped as `{"messages": [...]}`. Used by both `TestCase.messages` (the
    deprecated public accessor) and `helpers._evaluate_local` (an internal
    consumer that needs the same view without tripping the deprecation).
    """
    if not interactions:
        return []
    raw_messages = interactions[0].input.get("messages")
    if not isinstance(raw_messages, list):
        return []
    out: List[ChatMessage] = []
    for entry in cast(List[Any], raw_messages):
        if isinstance(entry, dict):
            entry_d = cast(Dict[str, Any], entry)
            role, content = entry_d.get("role"), entry_d.get("content")
            if isinstance(role, str) and isinstance(content, str):
                out.append(ChatMessage(role=role, content=content))
    return out


class TestCase(BaseModel):
    __test__ = False
    id: str
    comments: List[TestCaseComment] = Field(default_factory=list)  # pyright: ignore[reportUnknownVariableType]
    created_at: datetime
    dataset_id: str
    interactions: Optional[List[Interaction]] = None
    tags: List[str] = Field(default_factory=list)
    updated_at: datetime
    status: TestCaseStatus = "active"

    @property
    @deprecated("`TestCase.messages` is deprecated; read `interactions[i].input` instead.")
    def messages(self) -> List[ChatMessage]:
        """Deprecated flattened view of the first interaction's input messages.

        Returns the input messages from `interactions[0].input["messages"]`
        when present, falling back to an empty list otherwise. Prefer reading
        `test_case.interactions` directly.
        """
        return _first_interaction_messages(self.interactions)


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
