from typing_extensions import Literal

__all__ = ["TaskStatus"]

TaskStatus = Literal["open", "in_progress", "completed"]
