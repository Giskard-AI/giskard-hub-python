
from __future__ import annotations

from typing import List

from .._models import BaseModel
from .action_type import ActionType

__all__ = ["ListFilterValueActionType"]


class ListFilterValueActionType(BaseModel):
    values: List[ActionType]
