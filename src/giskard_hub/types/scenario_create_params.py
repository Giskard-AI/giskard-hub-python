from __future__ import annotations

from typing import TypedDict
from typing_extensions import Required

from giskard_hub._types import SequenceNotStr

__all__ = ["ScenarioCreateParams"]


class ScenarioCreateParams(TypedDict, total=False):
    name: Required[str]

    description: Required[str]

    rules: SequenceNotStr[str]
