"""Common response type definitions.

This module provides generic response wrappers used throughout the API.
These generic types can replace many resource-specific API response classes.
"""

from __future__ import annotations

from typing import Dict, List, Generic, TypeVar, Optional
from typing_extensions import override

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

    @override
    def __repr__(self) -> str:
        return f"APIResponse[{type(self.data).__name__}](data={self.data!r})"


class APIResponseWithIncluded(BaseModel, Generic[T, TIncluded]):
    """Generic API response wrapper with included related resources.

    Used when the API returns a resource along with related data
    in an 'included' field.

    TIncluded is the type at included[main_resource_id][included_resource_name], typically:
        - APIResponse[Resource]               for a single included resource
        - List[APIResponse[Resource]]         for a list of included resources
    """

    data: T

    included: Optional[Dict[str, Dict[str, TIncluded]]] = None


class APIPaginatedMetadata(BaseModel):
    """Pagination metadata for paginated responses."""

    count: int

    offset: int

    limit: int

    total: int


class APIPaginatedResponse(BaseModel, Generic[T, TIncluded]):
    """Generic API response wrapper for paginated lists.

    Includes pagination metadata alongside the data.

    TIncluded is the type at included[main_resource_id][included_resource_name], typically:
        - APIResponse[Resource]               for a single included resource
        - List[APIResponse[Resource]]         for a list of included resources
    """

    data: List[T]

    included: Optional[Dict[str, Dict[str, TIncluded]]] = None

    metadata: APIPaginatedMetadata
