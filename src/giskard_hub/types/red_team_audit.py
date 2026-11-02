"""Red team audit types exposed by the SDK."""

from typing import TypeAlias, TypedDict
from typing_extensions import Literal

__all__ = [
    "RedTeamAuditCoverageMode",
    "RedTeamAuditEstimateParams",
]

RedTeamAuditCoverageMode: TypeAlias = Literal["regular", "light"]


class RedTeamAuditEstimateParams(TypedDict, total=False):
    mode: RedTeamAuditCoverageMode
