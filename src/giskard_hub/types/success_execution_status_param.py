
from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SuccessExecutionStatusParam"]


class SuccessExecutionStatusParam(TypedDict, total=False):
    evaluation_id: Required[str]

    status: Literal["success"]
