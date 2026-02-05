from .._models import BaseModel

__all__ = ["DatasetReference"]


class DatasetReference(BaseModel):
    id: str

    name: str
