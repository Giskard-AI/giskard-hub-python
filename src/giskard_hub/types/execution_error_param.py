from __future__ import annotations

from typing import Dict, TypedDict
from typing_extensions import Required

__all__ = ["ExecutionErrorParam"]


class ExecutionErrorParam(TypedDict, total=False):
    message: Required[str]

    details: Dict[str, object]
