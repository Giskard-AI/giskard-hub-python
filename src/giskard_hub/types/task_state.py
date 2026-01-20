
from __future__ import annotations

from typing_extensions import Literal

__all__ = ["TaskState"]

TaskState = Literal["pending", "running", "completed", "failed", "cancelled"]
