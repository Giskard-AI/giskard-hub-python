from __future__ import annotations

from typing import Literal, TypedDict
from typing_extensions import Required

__all__ = ["SemanticSimilarityParamsParam"]


class SemanticSimilarityParamsParam(TypedDict, total=False):
    reference: Required[str]

    threshold: float

    type: Literal["semantic_similarity"]
