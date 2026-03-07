from .._models import BaseModel

__all__ = ["UserAPIReference"]


class UserAPIReference(BaseModel):
    id: str

    name: str
