"""Prompt preset domain types."""

from typing import Any, Dict, List, Optional, TypedDict
from datetime import datetime
from typing_extensions import Required

from pydantic import Field

from .._types import SequenceNotStr
from .._models import BaseModel

__all__ = [
    "PromptPreset",
    "PromptPresetPreview",
    "PromptPresetCreateParams",
    "PromptPresetUpdateParams",
    "PromptPresetPreviewParams",
]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class PromptPreset(BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime
    name: str
    description: Optional[str] = None
    rules: SequenceNotStr[str]


class PromptPresetPreview(BaseModel):
    inputs: List[Dict[str, Any]] = Field(default_factory=list)  # pyright: ignore[reportUnknownVariableType]
    generated_rules: Optional[List[str]] = None


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class PromptPresetCreateParams(TypedDict, total=False):
    name: Required[str]
    description: Required[str]
    rules: SequenceNotStr[str]


class PromptPresetUpdateParams(TypedDict, total=False):
    name: Optional[str]
    description: Optional[str]
    rules: Optional[SequenceNotStr[str]]


class PromptPresetPreviewParams(TypedDict, total=False):
    description: Required[str]
    rules: SequenceNotStr[str]
