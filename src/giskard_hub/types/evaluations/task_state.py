
from typing_extensions import Literal, TypeAlias

__all__ = ["TaskState"]

TaskState: TypeAlias = Literal["skipped", "finished", "error", "running", "canceled"]
