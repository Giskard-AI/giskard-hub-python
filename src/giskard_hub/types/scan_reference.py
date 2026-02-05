from .._models import BaseModel

__all__ = ["ScanReference"]


class ScanReference(BaseModel):
    id: str

    name: str
