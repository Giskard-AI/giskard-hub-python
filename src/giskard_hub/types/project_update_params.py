from __future__ import annotations

from typing import Iterable, Optional, TypedDict

from .evaluations.failure_category_param import FailureCategoryParam

__all__ = ["ProjectUpdateParams"]


class ProjectUpdateParams(TypedDict, total=False):
    description: Optional[str]

    failure_categories: Optional[Iterable[FailureCategoryParam]]

    name: Optional[str]
