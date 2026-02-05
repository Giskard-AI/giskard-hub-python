"""Agent response wrapper.

Note: This type is equivalent to APIResponse[Agent] from common.responses.
For new code, consider using the generic type instead.
"""

from .agent import Agent
from .._models import BaseModel

__all__ = ["APIResponseAgent"]


class APIResponseAgent(BaseModel):
    """API response wrapper for a single agent.
    
    This is equivalent to: APIResponse[Agent]
    """

    data: Agent
