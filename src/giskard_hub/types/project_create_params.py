from __future__ import annotations

from typing import Optional, TypedDict
from typing_extensions import Required

__all__ = ["ProjectCreateParams"]


class ProjectCreateParams(TypedDict, total=False):
    name: Required[str]

    description: Optional[str]
