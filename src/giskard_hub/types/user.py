from typing import Optional

from .._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    id: str

    email: str

    name: Optional[str] = None
