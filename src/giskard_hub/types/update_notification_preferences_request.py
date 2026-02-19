from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["UpdateNotificationPreferencesRequest"]


class UpdateNotificationPreferencesRequest(TypedDict, total=False):
    email_notifications: Optional[bool]

    push_notifications: Optional[bool]

    evaluation_notifications: Optional[bool]

    scan_notifications: Optional[bool]
