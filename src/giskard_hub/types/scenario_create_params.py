from __future__ import annotations

from typing import Any, Dict, Optional, TypedDict
from typing_extensions import Required

__all__ = ["ScenarioCreateParams"]


class ScenarioCreateParams(TypedDict, total=False):
    name: Required[str]

    description: Optional[str]

    config: Optional[Dict[str, Any]]

    agent_id: Optional[str]
