"""User types."""

from typing import List, Optional

from .._models import BaseModel

__all__ = ["User", "UserReference", "GroupReference"]


class GroupReference(BaseModel):
    id: str
    name: str


class UserReference(BaseModel):
    id: str
    name: str


class User(BaseModel):
    id: str
    email: str
    name: Optional[str] = None
    groups: List[GroupReference] = []
