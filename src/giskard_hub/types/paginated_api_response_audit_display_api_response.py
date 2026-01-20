
from __future__ import annotations

from typing import List

from .._models import BaseModel
from .audit_display_api_response import AuditDisplayAPIResponse
from .paginated_metadata import PaginatedMetadata

__all__ = ["PaginatedAPIResponseAuditDisplayAPIResponse"]


class PaginatedAPIResponseAuditDisplayAPIResponse(BaseModel):
    data: List[AuditDisplayAPIResponse]

    metadata: PaginatedMetadata
