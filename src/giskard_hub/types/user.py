from typing import Optional

from .._models import BaseModel

__all__ = ["User", "UserReference"]


class UserReference(BaseModel):
    id: str

    name: str


class User(BaseModel):
    id: str

    email: str

    name: Optional[str] = None
