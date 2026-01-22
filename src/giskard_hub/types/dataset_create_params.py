from __future__ import annotations

from typing import Optional, TypedDict
from typing_extensions import Required

__all__ = ["DatasetCreateParams"]


class DatasetCreateParams(TypedDict, total=False):
    name: Required[str]

    project_id: Required[str]

    description: Optional[str]
