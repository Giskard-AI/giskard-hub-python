
from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ErrorExecutionStatusParam"]


class ErrorExecutionStatusParam(TypedDict, total=False):
    error_message: Required[str]

    status: Literal["error"]
