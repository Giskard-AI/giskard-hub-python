from typing import Literal, TypeAlias

__all__ = ["TaskState"]

TaskState: TypeAlias = Literal["skipped", "finished", "error", "running", "canceled"]
