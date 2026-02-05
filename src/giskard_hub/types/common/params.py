"""Common parameter type definitions."""

from __future__ import annotations

from typing import TypeVar, TypedDict
from typing_extensions import Required

from ..._types import SequenceNotStr

__all__ = [
    "BulkDeleteParams",
]

T = TypeVar("T")


class BulkDeleteParams(TypedDict, total=False):
    """Generic bulk delete parameters.

    Note: The actual field name (e.g., 'agent_ids', 'dataset_ids') should be
    defined in resource-specific implementations.
    """

    ids: Required[SequenceNotStr[str]]
