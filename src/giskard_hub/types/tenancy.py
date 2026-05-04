"""Tenancy types."""

from typing import Dict, List, TypedDict
from typing_extensions import Required

from .._models import BaseModel

__all__ = [
    "HealthStatus",
    "FindTenantRequest",
    "FindTenantResponse",
    "FindTenantTenantInfo",
]


class HealthStatus(BaseModel):
    status: str
    version: str
    services: Dict[str, str]


class FindTenantTenantInfo(BaseModel):
    slug: str
    host: str


class FindTenantResponse(BaseModel):
    tenants: List[FindTenantTenantInfo]


class FindTenantRequest(TypedDict, total=False):
    email: Required[str]
    turnstile_token: Required[str]
