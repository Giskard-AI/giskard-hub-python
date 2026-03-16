"""Execution status and error types."""

from typing import Dict, Literal, Optional, TypedDict
from typing_extensions import Required

from .._models import BaseModel

__all__ = [
    "ExecutionError",
    "ExecutionErrorParam",
    "ErrorExecutionStatus",
    "ErrorExecutionStatusParam",
    "SuccessExecutionStatus",
    "SuccessExecutionStatusParam",
]


class ExecutionError(BaseModel):
    message: str
    details: Optional[Dict[str, object]] = None


class ExecutionErrorParam(TypedDict, total=False):
    message: Required[str]
    details: Dict[str, object]


class ErrorExecutionStatus(BaseModel):
    error_message: str
    status: Literal["error"]


class ErrorExecutionStatusParam(TypedDict, total=False):
    error_message: Required[str]
    status: Literal["error"]


class SuccessExecutionStatus(BaseModel):
    evaluation_id: str
    status: Literal["success"]


class SuccessExecutionStatusParam(TypedDict, total=False):
    evaluation_id: Required[str]
    status: Literal["success"]
