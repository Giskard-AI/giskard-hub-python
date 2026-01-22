from __future__ import annotations

from typing import Dict, Optional, TypedDict
from typing_extensions import Required

__all__ = ["ChatMessageWithMetadataParam"]


class ChatMessageWithMetadataParam(TypedDict, total=False):
    content: Required[str]

    role: Required[str]

    metadata: Optional[Dict[str, object]]
