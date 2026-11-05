"""Credit estimate and usage types."""

from typing import Optional, TypeAlias, TypedDict
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "CreditOperation",
    "CreditEstimate",
    "CreditUsageSummary",
    "UsageRetrieveCreditsParams",
]

CreditOperation: TypeAlias = Literal[
    "evaluation",
    "generation",
    "scan",
    "audit",
    "audit_light",
    "playground",
]


class CreditEstimate(BaseModel):
    operation: CreditOperation
    item_count: Optional[int]
    estimated_amount: int


class CreditUsageSummary(BaseModel):
    available_balance: int
    reserved_amount: int
    settled_consumption: int
    debits: int
    refunds: int
    net_movement: int


class UsageRetrieveCreditsParams(TypedDict, total=False):
    project_id: Optional[str]
    user_id: Optional[str]
