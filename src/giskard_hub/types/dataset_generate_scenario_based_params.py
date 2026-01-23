from __future__ import annotations

from typing import Any, Dict, Optional, TypedDict
from typing_extensions import Required

__all__ = ["DatasetGenerateScenarioBasedParams"]


class DatasetGenerateScenarioBasedParams(TypedDict, total=False):
    agent_id: Required[str]

    project_id: Required[str]

    scenario_id: Required[str]

    dataset_name: Optional[str]

    description: Optional[str]

    n_examples: Optional[int]

    scenario_config: Optional[Dict[str, Any]]
