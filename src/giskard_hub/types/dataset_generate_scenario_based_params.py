
from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["DatasetGenerateScenarioBasedParams", "Scenario"]


class DatasetGenerateScenarioBasedParams(TypedDict, total=False):
    agent_id: Required[str]

    project_id: Required[str]

    scenarios: Required[Iterable[Scenario]]

    dataset_name: str

    description: Optional[str]

    n_examples_per_scenario: int
    """Number of examples to generate for each scenario"""


class Scenario(TypedDict, total=False):
    desc: Required[str]

    name: Required[str]

    id: Optional[str]
