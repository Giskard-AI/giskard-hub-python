
from typing_extensions import Literal, TypeAlias

__all__ = ["ReviewStatus"]

ReviewStatus: TypeAlias = Literal["pending", "ignored", "acknowledged", "corrected"]
