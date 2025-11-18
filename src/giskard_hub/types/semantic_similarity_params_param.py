
from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SemanticSimilarityParamsParam"]


class SemanticSimilarityParamsParam(TypedDict, total=False):
    reference: Required[str]

    threshold: float

    type: Literal["semantic_similarity"]
