
from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SuccessExecutionStatus"]


class SuccessExecutionStatus(BaseModel):
    evaluation_id: str

    status: Optional[Literal["success"]] = None
