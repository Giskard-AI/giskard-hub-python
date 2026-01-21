from __future__ import annotations

from typing import Optional, TypedDict
from typing_extensions import Required

from .failure_category_param import FailureCategoryParam

__all__ = ["ResultUpdateParams"]


class ResultUpdateParams(TypedDict, total=False):
    evaluation_id: Required[str]

    failure_category: Optional[FailureCategoryParam]
