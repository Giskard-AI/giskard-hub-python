from typing import Optional, Literal

from .._models import BaseModel

__all__ = ["SuccessExecutionStatus"]


class SuccessExecutionStatus(BaseModel):
    evaluation_id: str

    status: Optional[Literal["success"]] = None
