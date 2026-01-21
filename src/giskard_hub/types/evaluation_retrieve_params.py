from __future__ import annotations

from typing import List, Optional, Literal, TypedDict

__all__ = ["EvaluationRetrieveParams"]


class EvaluationRetrieveParams(TypedDict, total=False):
    include: Optional[List[Literal["agent", "dataset"]]]
