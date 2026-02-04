from __future__ import annotations

from typing import Optional, TypedDict

from giskard_hub._types import SequenceNotStr

__all__ = ["ScenarioUpdateParams"]


class ScenarioUpdateParams(TypedDict, total=False):
    name: Optional[str]

    description: Optional[str]

    rules: Optional[SequenceNotStr[str]]
