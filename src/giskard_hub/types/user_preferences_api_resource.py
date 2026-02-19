from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .notification_preferences_api_resource import NotificationPreferencesAPIResource

__all__ = ["UserPreferencesAPIResource"]


class UserPreferencesAPIResource(BaseModel):
    user_id: str

    notifications: Optional[NotificationPreferencesAPIResource] = None
