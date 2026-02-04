from typing import List

from .._models import BaseModel
from .paginated_metadata import PaginatedMetadata
from .audit_display_api_response import AuditDisplayAPIResponse

__all__ = ["APIResponseAuditDisplay"]


class APIResponseAuditDisplay(BaseModel):
    data: List[AuditDisplayAPIResponse]

    metadata: PaginatedMetadata
