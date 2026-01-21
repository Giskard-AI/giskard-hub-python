from __future__ import annotations

from typing import Literal, TypedDict
from typing_extensions import Required

__all__ = ["SuccessExecutionStatusParam"]


class SuccessExecutionStatusParam(TypedDict, total=False):
    evaluation_id: Required[str]

    status: Literal["success"]
