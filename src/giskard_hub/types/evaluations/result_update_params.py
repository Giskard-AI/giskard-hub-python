from __future__ import annotations

from typing import Optional, TypedDict

from .failure_category_param import FailureCategoryParam

__all__ = ["ResultUpdateParams"]


class ResultUpdateParams(TypedDict, total=False):
    failure_category: Optional[FailureCategoryParam]
