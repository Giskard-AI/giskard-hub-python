
from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ExecutionErrorParam"]


class ExecutionErrorParam(TypedDict, total=False):
    message: Required[str]

    details: Dict[str, object]
