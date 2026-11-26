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
    "audit_attestation",
    "run_check",
    "playground",
]


class CreditEstimate(BaseModel):
    operation: CreditOperation
    item_count: Optional[int]
    estimated_amount: float


class CreditUsageSummary(BaseModel):
    available_balance: float
    reserved_amount: float
    settled_consumption: float
    debits: float
    refunds: float
    net_movement: float


class UsageRetrieveCreditsParams(TypedDict, total=False):
    project_id: Optional[str]
    user_id: Optional[str]
