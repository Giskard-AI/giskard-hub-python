
from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SemanticSimilarityParams"]


class SemanticSimilarityParams(BaseModel):
    reference: str

    threshold: Optional[float] = None

    type: Optional[Literal["semantic_similarity"]] = None
