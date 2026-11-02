"""Project domain types."""

from typing import List, Iterable, Optional, TypedDict
from datetime import datetime
from typing_extensions import Required

from .._types import SequenceNotStr
from .._models import BaseModel
from .evaluation import FailureCategory, FailureCategoryParam

__all__ = [
    "Project",
    "ProjectOnboarding",
    "ProjectCreateParams",
    "ProjectUpdateParams",
    "ProjectBulkDeleteParams",
    "ProjectOnboardingUpdateDismissalParams",
]


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class Project(BaseModel):
    id: str
    created_at: datetime
    description: str
    failure_categories: List[FailureCategory]
    name: str
    updated_at: datetime


class ProjectOnboarding(BaseModel):
    agent_connected: bool
    playground_tried: bool
    audit_launched: bool
    dismissed: bool
    restarted_at: Optional[datetime] = None


# ---------------------------------------------------------------------------
# Params
# ---------------------------------------------------------------------------


class ProjectCreateParams(TypedDict, total=False):
    name: Required[str]
    description: Optional[str]


class ProjectUpdateParams(TypedDict, total=False):
    description: Optional[str]
    failure_categories: Optional[Iterable[FailureCategoryParam]]
    name: Optional[str]


class ProjectBulkDeleteParams(TypedDict, total=False):
    project_ids: Required[SequenceNotStr[str]]


class ProjectOnboardingUpdateDismissalParams(TypedDict, total=False):
    dismissed: Required[bool]
