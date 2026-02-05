"""Dataset response wrapper.

Note: This type is equivalent to APIResponse[Dataset] from common.responses.
For new code, consider using the generic type instead.
"""

from .dataset import Dataset
from .._models import BaseModel

__all__ = ["APIResponseDataset"]


class APIResponseDataset(BaseModel):
    """API response wrapper for a single dataset.
    
    This is equivalent to: APIResponse[Dataset]
    """

    data: Dataset
