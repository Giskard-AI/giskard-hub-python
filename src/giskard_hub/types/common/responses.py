"""Common response type definitions.

This module provides generic response wrappers used throughout the API.
These generic types can replace many resource-specific API response classes.
"""

from __future__ import annotations

from typing import Dict, Generic, List, Literal, Optional, TypeVar, Union

from ..._models import BaseModel

__all__ = [
    "APIResponse",
    "APIListResponse",
    "APIPaginatedResponse",
    "APIResponseWithIncluded",
]

T = TypeVar("T")
TIncluded = TypeVar("TIncluded")


class APIResponse(BaseModel, Generic[T]):
    """Generic API response wrapper for single resource.
    
    Usage:
        APIResponse[Agent] instead of APIResponseAgent
        APIResponse[Dataset] instead of APIResponseDataset
    """

    data: T


class APIListResponse(BaseModel, Generic[T]):
    """Generic API response wrapper for list of resources.
    
    Usage:
        APIListResponse[Agent] instead of AgentListResponse
        APIListResponse[TestCase] instead of APIResponseListTestCase
    """

    data: List[T]


class APIPaginatedMetadata(BaseModel):
    """Pagination metadata for paginated responses."""

    current_page: int
    
    per_page: int
    
    total_count: int
    
    total_pages: int


class APIPaginatedResponse(BaseModel, Generic[T]):
    """Generic API response wrapper for paginated lists.
    
    Includes pagination metadata alongside the data.
    """

    data: List[T]
    
    metadata: APIPaginatedMetadata


class APIResponseWithIncluded(BaseModel, Generic[T, TIncluded]):
    """Generic API response wrapper with included related resources.
    
    Used when the API returns a resource along with related data
    in an 'included' field (following JSON:API spec pattern).
    """

    data: T
    
    included: Optional[Dict[str, Dict[str, TIncluded]]] = None
