from typing import List

from .._models import BaseModel
from .audit_api_resource import AuditAPIResource
from .paginated_metadata import PaginatedMetadata

__all__ = ["APIResponseAudit"]


class APIResponseAudit(BaseModel):
    data: List[AuditAPIResource]

    metadata: PaginatedMetadata
