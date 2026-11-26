"""User types."""

from typing import Optional

from .._models import BaseModel

__all__ = ["TaskUser", "User", "UserReference", "GroupReference"]


class GroupReference(BaseModel):
    id: str
    name: str


class UserReference(BaseModel):
    id: str
    name: str


class TaskUser(BaseModel):
    """User embedded on a task.

    Matches ``TaskUserAPIResource``: an id and a display name.
    """

    id: str
    name: Optional[str] = None


User = TaskUser
