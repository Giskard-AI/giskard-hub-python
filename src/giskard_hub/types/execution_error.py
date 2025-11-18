
from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ExecutionError"]


class ExecutionError(BaseModel):
    message: str

    details: Optional[Dict[str, object]] = None
