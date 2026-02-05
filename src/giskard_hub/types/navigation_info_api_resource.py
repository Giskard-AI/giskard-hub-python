from typing import Optional

from .._models import BaseModel

__all__ = ["NavigationInfoAPIResource"]


class NavigationInfoAPIResource(BaseModel):
    next_document_id: Optional[str] = None
    """ID of the next document"""

    previous_document_id: Optional[str] = None
    """ID of the previous document"""
