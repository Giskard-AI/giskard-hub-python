"""Auth domain types."""

from typing import Optional, TypedDict

__all__ = [
    "AuthLoginParams",
    "AuthCallbackParams",
]


class AuthLoginParams(TypedDict, total=False):
    login_hint: Optional[str]
    return_to: Optional[str]


class AuthCallbackParams(TypedDict, total=False):
    code: Optional[str]
    error: Optional[str]
    state: Optional[str]
