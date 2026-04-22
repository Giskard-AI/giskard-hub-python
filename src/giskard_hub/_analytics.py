from __future__ import annotations

import os
import atexit
import hashlib
import logging
from typing import Any

log = logging.getLogger(__name__)

_posthog_client: Any = None
_initialized = False

POSTHOG_PROJECT_API_KEY = "phc_z4TRoET597ASsuoDBa7zr5FWmUSjdCSyxazHyScLp2Nf"
POSTHOG_HOST = "https://eu.i.posthog.com"


def _get_client() -> Any:
    global _posthog_client, _initialized
    if _initialized:
        return _posthog_client

    _initialized = True
    try:
        from posthog import Posthog
        _posthog_client = Posthog(POSTHOG_PROJECT_API_KEY, host=POSTHOG_HOST, enable_exception_autocapture=True)
        atexit.register(_posthog_client.shutdown)
    except Exception:
        log.debug("PostHog analytics could not be initialized", exc_info=True)
        _posthog_client = None

    return _posthog_client


def make_distinct_id(api_key: str) -> str:
    return "sdk_" + hashlib.sha256(api_key.encode()).hexdigest()[:16]


def capture_event(distinct_id: str, event: str, properties: dict[str, Any] | None = None) -> None:
    client = _get_client()
    if client is None:
        return
    try:
        client.capture(distinct_id=distinct_id, event=event, properties=properties or {})
    except Exception:
        log.debug("PostHog capture failed", exc_info=True)


def capture_exception(exc: BaseException, distinct_id: str | None = None) -> None:
    client = _get_client()
    if client is None:
        return
    try:
        kwargs: dict[str, Any] = {}
        if distinct_id is not None:
            kwargs["distinct_id"] = distinct_id
        client.capture_exception(exc, **kwargs)
    except Exception:
        log.debug("PostHog capture_exception failed", exc_info=True)
