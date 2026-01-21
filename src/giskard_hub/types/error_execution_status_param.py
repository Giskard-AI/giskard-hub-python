from __future__ import annotations

from typing import Literal, TypedDict
from typing_extensions import Required

__all__ = ["ErrorExecutionStatusParam"]


class ErrorExecutionStatusParam(TypedDict, total=False):
    error_message: Required[str]

    status: Literal["error"]
