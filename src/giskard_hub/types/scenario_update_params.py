from __future__ import annotations

from typing import Any, Dict, Optional, TypedDict

__all__ = ["ScenarioUpdateParams"]


class ScenarioUpdateParams(TypedDict, total=False):
    name: Optional[str]

    description: Optional[str]

    config: Optional[Dict[str, Any]]

    agent_id: Optional[str]
