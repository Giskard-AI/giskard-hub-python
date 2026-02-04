from typing import Literal

__all__ = ["ActionType"]

ActionType = Literal[
    "created",
    "updated",
    "deleted",
    "published",
    "unpublished",
    "archived",
    "restored",
    "commented",
    "reviewed",
]
