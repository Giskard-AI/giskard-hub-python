"""Common type definitions shared across resources.

This module provides generic types that can be used to replace
many resource-specific type definitions.
"""

from __future__ import annotations

from .responses import (
    APIResponse as APIResponse,
    APIListResponse as APIListResponse,
    APIPaginatedResponse as APIPaginatedResponse,
    APIPaginatedMetadata as APIPaginatedMetadata,
    APIResponseWithIncluded as APIResponseWithIncluded,
)

__all__ = [
    "APIResponse",
    "APIListResponse",
    "APIPaginatedResponse",
    "APIPaginatedMetadata",
    "APIResponseWithIncluded",
]
