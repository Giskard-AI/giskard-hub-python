from typing import Generic, TypeVar
from typing_extensions import Required, TypedDict

__all__ = ["OrderByParam"]

T = TypeVar("T")


class OrderByParam(TypedDict, Generic[T], total=False):
    id: Required[T]
    """The column to sort by."""

    desc: bool
    """Sort in descending order. Defaults to True when omitted."""
