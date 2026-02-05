from typing import List

from .._models import BaseModel
from .paginated_metadata import PaginatedMetadata
from .knowledge_base_document_row_api_resource import KnowledgeBaseDocumentRowAPIResource

__all__ = ["PaginatedAPIResponseKnowledgeBaseDocumentRowAPIResource"]


class PaginatedAPIResponseKnowledgeBaseDocumentRowAPIResource(BaseModel):
    data: List[KnowledgeBaseDocumentRowAPIResource]

    metadata: PaginatedMetadata
