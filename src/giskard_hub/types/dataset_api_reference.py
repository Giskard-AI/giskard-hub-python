from .._models import BaseModel

__all__ = ["DatasetAPIReference"]


class DatasetAPIReference(BaseModel):
    id: str

    name: str
