from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["NotificationPreferencesAPIResource"]


class NotificationPreferencesAPIResource(BaseModel):
    email_notifications: Optional[bool] = None

    push_notifications: Optional[bool] = None

    evaluation_notifications: Optional[bool] = None

    scan_notifications: Optional[bool] = None
