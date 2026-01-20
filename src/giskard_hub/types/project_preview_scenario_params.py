
from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProjectPreviewScenarioParams"]


class ProjectPreviewScenarioParams(TypedDict, total=False):
    agent_id: Required[str]
