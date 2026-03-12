"""Chat message and header types."""

from typing import Dict, Optional, TypedDict
from typing_extensions import Required

from .._models import BaseModel

__all__ = [
    "ChatMessage",
    "ChatMessageParam",
    "ChatMessageWithMetadata",
    "ChatMessageWithMetadataParam",
    "Header",
    "HeaderParam",
]


class ChatMessage(BaseModel):
    content: str
    role: str


class ChatMessageParam(TypedDict, total=False):
    content: Required[str]
    role: Required[str]


class ChatMessageWithMetadata(BaseModel):
    content: str
    role: str
    metadata: Optional[Dict[str, object]] = None


class ChatMessageWithMetadataParam(TypedDict, total=False):
    content: Required[str]
    role: Required[str]
    metadata: Optional[Dict[str, object]]


class Header(BaseModel):
    name: str
    value: str


class HeaderParam(TypedDict, total=False):
    name: Required[str]
    value: Required[str]
