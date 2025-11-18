
from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .failure_category_param import FailureCategoryParam

__all__ = ["ResultUpdateParams"]


class ResultUpdateParams(TypedDict, total=False):
    evaluation_id: Required[str]

    failure_category: Optional[FailureCategoryParam]
