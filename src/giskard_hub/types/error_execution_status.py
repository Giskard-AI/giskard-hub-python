from typing import Literal, Optional

from .._models import BaseModel

__all__ = ["ErrorExecutionStatus"]


class ErrorExecutionStatus(BaseModel):
    error_message: str

    status: Optional[Literal["error"]] = None
