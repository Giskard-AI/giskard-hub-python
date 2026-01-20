
from __future__ import annotations

from typing import List

from .._models import BaseModel
from .audit_api_resource import AuditAPIResource
from .paginated_metadata import PaginatedMetadata

__all__ = ["PaginatedAPIResponseAuditAPIResource"]


class PaginatedAPIResponseAuditAPIResource(BaseModel):
    data: List[AuditAPIResource]

    metadata: PaginatedMetadata
