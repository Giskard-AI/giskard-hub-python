import os
import atexit
import hashlib
import logging
import threading
from typing import Any

log = logging.getLogger(__name__)

_posthog_client: Any = None
_initialized = False
_explicitly_disabled = False
_init_lock = threading.Lock()

POSTHOG_PROJECT_API_KEY = "phc_z4TRoET597ASsuoDBa7zr5FWmUSjdCSyxazHyScLp2Nf"
POSTHOG_HOST = "https://eu.i.posthog.com"

_DISABLING_ENV_VARS = [
    "DO_NOT_TRACK",
    "GISKARD_TELEMETRY_DISABLED",
    "GISKARD_HUB_TELEMETRY_DISABLED",
]
_CI_ENV_VARS = ["CI", "TF_BUILD"]
_TRUTHY_VALUES = {"1", "true", "yes", "on", "t", "y"}


def _is_true_str(value: str | None) -> bool:
    if value is None:
        return False
    return value.strip().lower() in _TRUTHY_VALUES


def _is_ci() -> bool:
    return any(_is_true_str(os.getenv(var)) for var in _CI_ENV_VARS)


def _should_disable() -> bool:
    if _explicitly_disabled:
        return True
    if _is_ci():
        return True
    return any(_is_true_str(os.getenv(var)) for var in _DISABLING_ENV_VARS)


def _get_client() -> Any:
    global _posthog_client, _initialized
    with _init_lock:
        if _initialized:
            return _posthog_client

        disabled = _should_disable()
        try:
            from posthog import Posthog

            _posthog_client = Posthog(
                POSTHOG_PROJECT_API_KEY,
                host=POSTHOG_HOST,
                enable_exception_autocapture=not disabled,
                disabled=disabled,
                disable_geoip=disabled,
            )
            atexit.register(_posthog_client.shutdown)
        except Exception:
            log.debug("PostHog analytics could not be initialized", exc_info=True)
            _posthog_client = None

        _initialized = True
        return _posthog_client


def disable_telemetry() -> None:
    """Disable telemetry for the remainder of this process.

    Overrides environment-variable settings. Useful for test harnesses or
    runtime opt-out from code.

    Notes
    -----
    Prefer setting one of the opt-out environment variables before importing
    giskard_hub, since that avoids importing the PostHog client at all:

    - DO_NOT_TRACK
    - GISKARD_TELEMETRY_DISABLED
    - GISKARD_HUB_TELEMETRY_DISABLED

    Any value matching (case-insensitive) `1`, `true`, `yes`, `on`, `t`, or `y` is
    treated as truthy.

    Examples
    --------
    >>> from giskard_hub import disable_telemetry
    >>> disable_telemetry()
    """
    global _explicitly_disabled
    with _init_lock:
        _explicitly_disabled = True
        if _posthog_client is not None:
            try:
                _posthog_client.disabled = True
            except Exception:
                log.debug("Failed to flip PostHog client to disabled", exc_info=True)


def make_distinct_id(api_key: str) -> str:
    return "hub_" + hashlib.sha256(api_key.encode()).hexdigest()[:16]


def capture_event(distinct_id: str, event: str, properties: dict[str, Any] | None = None) -> None:
    if _should_disable():
        return
    client = _get_client()
    if client is None:
        return
    try:
        client.capture(distinct_id=distinct_id, event=event, properties=properties or {})
    except Exception:
        log.debug("PostHog capture failed", exc_info=True)


def capture_exception(exc: BaseException, distinct_id: str | None = None) -> None:
    if _should_disable():
        return
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
