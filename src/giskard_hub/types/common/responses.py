"""Common response type definitions.

This module provides generic response wrappers used throughout the API.
These generic types can replace many resource-specific API response classes.
"""

from __future__ import annotations

from typing import Dict, List, Generic, Literal, TypeVar, Optional

from ..._models import BaseModel

__all__ = ["APIResponse", "APIPaginatedResponse", "APIResponseWithIncluded", "APIPaginatedMetadata"]

T = TypeVar("T")
TIncluded = TypeVar("TIncluded")


class APIResponse(BaseModel, Generic[T]):
    """Generic API response wrapper for single resource.

    Usage:
        APIResponse[Agent] instead of APIResponseAgent
        APIResponse[Dataset] instead of APIResponseDataset
    """

    data: T


class APIResponseWithIncluded(BaseModel, Generic[T, TIncluded]):
    """Generic API response wrapper with included related resources.

    Used when the API returns a resource along with related data
    in an 'included' field (following JSON:API spec pattern).
    """

    data: T

    included: Optional[Dict[str, Dict[str, Dict[Literal["data"], TIncluded]]]] = None


class APIPaginatedMetadata(BaseModel):
    """Pagination metadata for paginated responses."""

    count: int

    offset: int

    limit: int

    total: int


class APIPaginatedResponse(BaseModel, Generic[T, TIncluded]):
    """Generic API response wrapper for paginated lists.

    Includes pagination metadata alongside the data.
    """

    data: List[T]

    included: Optional[Dict[str, Dict[str, Dict[Literal["data"], TIncluded]]]] = None

    metadata: APIPaginatedMetadata
