from __future__ import annotations

from typing import Any, Dict, Optional, TypedDict
from typing_extensions import Required

__all__ = ["ScenarioPreviewParams"]


class ScenarioPreviewParams(TypedDict, total=False):
    config: Required[Dict[str, Any]]

    sample_size: Optional[int]
