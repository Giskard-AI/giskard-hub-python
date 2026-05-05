"""Scenario domain types."""

from typing import Any, Dict, List, Optional, TypedDict
from datetime import datetime
from typing_extensions import Required, deprecated

from pydantic import Field

from .._types import SequenceNotStr
from .._models import BaseModel

__all__ = [
    "Scenario",
    "ScenarioPreview",
    "ScenarioCreateParams",
    "ScenarioUpdateParams",
    "ScenarioPreviewParams",
]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class Scenario(BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    name: str
    description: Optional[str] = None
    rules: SequenceNotStr[str]


class ScenarioPreview(BaseModel):
    inputs: List[Dict[str, Any]] = Field(default_factory=list)  # pyright: ignore[reportUnknownVariableType]
    generated_rules: Optional[List[str]] = None

    @property
    @deprecated("`ScenarioPreview.conversation` is deprecated; read `inputs` instead.")
    def conversation(self) -> List[Dict[str, Any]]:
        """Deprecated alias for `inputs`."""
        return self.inputs


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class ScenarioCreateParams(TypedDict, total=False):
    name: Required[str]
    description: Required[str]
    rules: SequenceNotStr[str]


class ScenarioUpdateParams(TypedDict, total=False):
    name: Optional[str]
    description: Optional[str]
    rules: Optional[SequenceNotStr[str]]


class ScenarioPreviewParams(TypedDict, total=False):
    description: Required[str]
    rules: SequenceNotStr[str]
