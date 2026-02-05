from .._models import BaseModel
from .knowledge_base_document_detail_api_resource import KnowledgeBaseDocumentDetailAPIResource

__all__ = ["APIResponseKnowledgeBaseDocumentDetailAPIResource"]


class APIResponseKnowledgeBaseDocumentDetailAPIResource(BaseModel):
    data: KnowledgeBaseDocumentDetailAPIResource
