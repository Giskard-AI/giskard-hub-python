from ..._models import BaseModel

__all__ = ["FailureCategory"]


class FailureCategory(BaseModel):
    description: str

    identifier: str

    title: str
