"""Scenario domain types (dataset items evaluated against agents)."""

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
    "Scenario",
    "ScenarioReference",
    "ScenarioComment",
    "ScenarioSchemaValidation",
    "ScenarioStatus",
    "BulkMoveScenariosParams",
    "ScenarioCreateParams",
    "ScenarioUpdateParams",
    "ScenarioBulkDeleteParams",
    "ScenarioBulkUpdateParams",
    "ScenarioCommentAddParams",
    "ScenarioCommentEditParams",
]

ScenarioStatus: TypeAlias = Literal["active", "draft"]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class ScenarioComment(BaseModel):
    id: str
    content: str = Field(alias="comment")
    created_at: datetime
    updated_at: datetime
    user: UserReference


class ScenarioReference(BaseModel):
    id: str


class ScenarioSchemaValidation(BaseModel):
    input_valid: bool = True
    output_valid: bool = True


def _first_interaction_messages(interactions: Optional[List[Interaction]]) -> List[ChatMessage]:
    """Extract chat messages from `interactions[0].input["messages"]`.

    Returns an empty list if there are no interactions or the input is not
    shaped as `{"messages": [...]}`. Used by the deprecated `Scenario.messages`
    accessor and `helpers._evaluate_local` (an internal consumer that needs the
    same view without tripping the deprecation).
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


class Scenario(BaseModel):
    id: str
    comments: List[ScenarioComment] = Field(default_factory=list)  # pyright: ignore[reportUnknownVariableType]
    created_at: datetime
    dataset_id: str
    interactions: Optional[List[Interaction]] = None
    tags: List[str] = Field(default_factory=list)
    updated_at: datetime
    status: ScenarioStatus = "active"
    schema_validation: ScenarioSchemaValidation = Field(default_factory=ScenarioSchemaValidation)

    @property
    @deprecated("`.messages` is deprecated; read `interactions[i].input` instead.")
    def messages(self) -> List[ChatMessage]:
        """Deprecated flattened view of the first interaction's input messages."""
        return _first_interaction_messages(self.interactions)


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class ScenarioCreateParams(TypedDict, total=False):
    dataset_id: Required[str]
    interactions: Optional[Iterable[InteractionParam]]
    status: Optional[ScenarioStatus]
    tags: SequenceNotStr[str]
    source_probe_attempt_id: Optional[str]


class ScenarioUpdateParams(TypedDict, total=False):
    dataset_id: Optional[str]
    interactions: Optional[Iterable[InteractionParam]]
    tags: Optional[SequenceNotStr[str]]
    status: Optional[ScenarioStatus]


class ScenarioBulkDeleteParams(TypedDict, total=False):
    scenario_ids: Required[SequenceNotStr[str]]


class ScenarioBulkUpdateParams(TypedDict, total=False):
    ids: Required[SequenceNotStr[str]]
    disabled_checks: Optional[SequenceNotStr[str]]
    enabled_checks: Optional[SequenceNotStr[str]]
    added_tags: Optional[SequenceNotStr[str]]
    removed_tags: Optional[SequenceNotStr[str]]
    status: Optional[ScenarioStatus]


class BulkMoveScenariosParams(TypedDict, total=False):
    scenario_ids: Required[SequenceNotStr[str]]
    dataset_id: Required[str]
    duplicate: Optional[bool]


# ---------------------------------------------------------------------------
# Comment params
# ---------------------------------------------------------------------------


class ScenarioCommentAddParams(TypedDict, total=False):
    comment: Required[str]


class ScenarioCommentEditParams(TypedDict, total=False):
    comment: Required[str]
