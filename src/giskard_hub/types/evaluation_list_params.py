from __future__ import annotations

from typing import List, Optional, Literal, TypedDict
from typing_extensions import Required

__all__ = ["EvaluationListParams"]


class EvaluationListParams(TypedDict, total=False):
    project_id: Required[str]

    include: Optional[List[Literal["agent", "dataset"]]]
