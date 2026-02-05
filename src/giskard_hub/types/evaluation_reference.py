from .._models import BaseModel

__all__ = ["EvaluationReference"]


class EvaluationReference(BaseModel):
    id: str

    name: str
