from .._models import BaseModel

__all__ = ["ProjectReference"]


class ProjectReference(BaseModel):
    id: str

    name: str
