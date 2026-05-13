"""Unit tests for `giskard_hub._analytics`.

These tests rely on `monkeypatch` to reset module-level state between tests
(`_posthog_client`, `_initialized`, `_explicitly_disabled`) and the opt-out
environment variables, and to inject a fake `posthog` module when exercising
lazy initialization.
"""

import sys
from types import SimpleNamespace
from typing import Any
from unittest.mock import MagicMock

import pytest

from giskard_hub import _analytics


@pytest.fixture(autouse=True)
def _reset_analytics_state(  # pyright: ignore[reportUnusedFunction]
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(_analytics, "_posthog_client", None)
    monkeypatch.setattr(_analytics, "_initialized", False)
    monkeypatch.setattr(_analytics, "_explicitly_disabled", False)
    for var in _analytics._DISABLING_ENV_VARS:
        monkeypatch.delenv(var, raising=False)


# ---------------------------------------------------------------------------
# _is_true_str
# ---------------------------------------------------------------------------


class TestIsTrueStr:
    def test_none_is_false(self) -> None:
        assert _analytics._is_true_str(None) is False

    def test_empty_is_false(self) -> None:
        assert _analytics._is_true_str("") is False

    @pytest.mark.parametrize("value", ["1", "true", "yes", "on", "t", "y"])
    def test_truthy_values(self, value: str) -> None:
        assert _analytics._is_true_str(value) is True

    @pytest.mark.parametrize("value", ["TRUE", "Yes", "On", "T", "Y"])
    def test_case_insensitive(self, value: str) -> None:
        assert _analytics._is_true_str(value) is True

    @pytest.mark.parametrize("value", ["0", "false", "no", "off", "f", "n", "anything"])
    def test_falsy_values(self, value: str) -> None:
        assert _analytics._is_true_str(value) is False

    def test_whitespace_stripped(self) -> None:
        assert _analytics._is_true_str("  true  ") is True


# ---------------------------------------------------------------------------
# _should_disable
# ---------------------------------------------------------------------------


class TestShouldDisable:
    def test_default_is_false(self) -> None:
        assert _analytics._should_disable() is False

    def test_explicitly_disabled(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(_analytics, "_explicitly_disabled", True)
        assert _analytics._should_disable() is True

    @pytest.mark.parametrize(
        "var",
        [
            "DO_NOT_TRACK",
            "GISKARD_TELEMETRY_DISABLED",
            "GISKARD_HUB_TELEMETRY_DISABLED",
        ],
    )
    def test_env_disabled(self, monkeypatch: pytest.MonkeyPatch, var: str) -> None:
        monkeypatch.setenv(var, "1")
        assert _analytics._should_disable() is True

    def test_ci_env_var_does_not_disable(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("CI", "true")
        assert _analytics._should_disable() is False

    def test_env_disabled_evaluated_dynamically(self, monkeypatch: pytest.MonkeyPatch) -> None:
        # Setting the opt-out env var after module import must take effect immediately.
        assert _analytics._should_disable() is False
        monkeypatch.setenv("DO_NOT_TRACK", "1")
        assert _analytics._should_disable() is True


# ---------------------------------------------------------------------------
# make_distinct_id
# ---------------------------------------------------------------------------


class TestMakeDistinctId:
    def test_is_deterministic(self) -> None:
        assert _analytics.make_distinct_id("key") == _analytics.make_distinct_id("key")

    def test_different_keys_yield_different_ids(self) -> None:
        assert _analytics.make_distinct_id("a") != _analytics.make_distinct_id("b")

    def test_has_hub_prefix(self) -> None:
        assert _analytics.make_distinct_id("abc").startswith("hub_")

    def test_does_not_leak_raw_key(self) -> None:
        assert "my-secret-key" not in _analytics.make_distinct_id("my-secret-key")

    def test_id_length(self) -> None:
        # "hub_" + 16 hex chars
        assert len(_analytics.make_distinct_id("abc")) == len("hub_") + 16


# ---------------------------------------------------------------------------
# _get_client
# ---------------------------------------------------------------------------


def _install_fake_posthog(monkeypatch: pytest.MonkeyPatch, posthog_cls: Any) -> None:
    """Replace `posthog` in sys.modules so `from posthog import Posthog` picks up `posthog_cls`."""
    monkeypatch.setitem(sys.modules, "posthog", SimpleNamespace(Posthog=posthog_cls))


class TestGetClient:
    def test_returns_constructed_client(self, monkeypatch: pytest.MonkeyPatch) -> None:
        fake = MagicMock(return_value=MagicMock())
        _install_fake_posthog(monkeypatch, fake)
        client = _analytics._get_client()
        assert client is fake.return_value
        fake.assert_called_once()

    def test_initialization_is_idempotent(self, monkeypatch: pytest.MonkeyPatch) -> None:
        fake = MagicMock(return_value=MagicMock())
        _install_fake_posthog(monkeypatch, fake)
        _analytics._get_client()
        _analytics._get_client()
        fake.assert_called_once()

    def test_returns_none_when_posthog_init_fails(self, monkeypatch: pytest.MonkeyPatch) -> None:
        fake = MagicMock(side_effect=RuntimeError("boom"))
        _install_fake_posthog(monkeypatch, fake)
        assert _analytics._get_client() is None

    def test_passes_hardening_kwargs(self, monkeypatch: pytest.MonkeyPatch) -> None:
        fake = MagicMock(return_value=MagicMock())
        _install_fake_posthog(monkeypatch, fake)
        _analytics._get_client()
        kwargs = fake.call_args.kwargs
        assert kwargs["enable_exception_autocapture"] is False
        assert kwargs["timeout"] == 2
        assert kwargs["max_retries"] == 0

    def test_passes_disabled_when_should_disable(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("DO_NOT_TRACK", "1")
        fake = MagicMock(return_value=MagicMock())
        _install_fake_posthog(monkeypatch, fake)
        _analytics._get_client()
        kwargs = fake.call_args.kwargs
        assert kwargs["disabled"] is True
        assert kwargs["disable_geoip"] is True

    def test_passes_enabled_when_telemetry_on(self, monkeypatch: pytest.MonkeyPatch) -> None:
        fake = MagicMock(return_value=MagicMock())
        _install_fake_posthog(monkeypatch, fake)
        _analytics._get_client()
        kwargs = fake.call_args.kwargs
        assert kwargs["disabled"] is False
        assert kwargs["disable_geoip"] is False

    def test_does_not_register_atexit(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Regression: explicit atexit.register was removed to avoid hanging at process exit."""
        import atexit

        register_calls: list[Any] = []

        def fake_register(fn: Any, *_a: Any, **_kw: Any) -> None:
            register_calls.append(fn)

        monkeypatch.setattr(atexit, "register", fake_register)
        fake = MagicMock(return_value=MagicMock(shutdown=MagicMock()))
        _install_fake_posthog(monkeypatch, fake)
        _analytics._get_client()
        # The PostHog constructor is mocked, so it cannot register its own atexit either.
        # We only need to verify that *our* module no longer registers `client.shutdown`.
        assert fake.return_value.shutdown not in register_calls


# ---------------------------------------------------------------------------
# capture_event
# ---------------------------------------------------------------------------


class TestCaptureEvent:
    def test_noop_when_env_disabled(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("DO_NOT_TRACK", "1")
        fake = MagicMock(return_value=MagicMock())
        _install_fake_posthog(monkeypatch, fake)
        _analytics.capture_event("user", "evt")
        # Client is never instantiated when disabled before the first capture.
        fake.assert_not_called()

    def test_noop_when_explicitly_disabled(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(_analytics, "_explicitly_disabled", True)
        fake = MagicMock(return_value=MagicMock())
        _install_fake_posthog(monkeypatch, fake)
        _analytics.capture_event("user", "evt")
        fake.assert_not_called()

    def test_calls_client_capture(self, monkeypatch: pytest.MonkeyPatch) -> None:
        mock_client = MagicMock()
        monkeypatch.setattr(_analytics, "_posthog_client", mock_client)
        monkeypatch.setattr(_analytics, "_initialized", True)
        _analytics.capture_event("uid", "my_event", {"a": 1})
        mock_client.capture.assert_called_once_with(distinct_id="uid", event="my_event", properties={"a": 1})

    def test_default_properties_is_empty_dict(self, monkeypatch: pytest.MonkeyPatch) -> None:
        mock_client = MagicMock()
        monkeypatch.setattr(_analytics, "_posthog_client", mock_client)
        monkeypatch.setattr(_analytics, "_initialized", True)
        _analytics.capture_event("uid", "my_event")
        mock_client.capture.assert_called_once_with(distinct_id="uid", event="my_event", properties={})

    def test_swallows_client_exception(self, monkeypatch: pytest.MonkeyPatch) -> None:
        mock_client = MagicMock()
        mock_client.capture.side_effect = RuntimeError("network blocked")
        monkeypatch.setattr(_analytics, "_posthog_client", mock_client)
        monkeypatch.setattr(_analytics, "_initialized", True)
        # Must not raise.
        _analytics.capture_event("uid", "my_event")

    def test_noop_when_get_client_returns_none(self, monkeypatch: pytest.MonkeyPatch) -> None:
        fake = MagicMock(side_effect=RuntimeError("import failure"))
        _install_fake_posthog(monkeypatch, fake)
        # Must not raise even though client construction fails.
        _analytics.capture_event("uid", "my_event")


# ---------------------------------------------------------------------------
# disable_telemetry
# ---------------------------------------------------------------------------


class TestDisableTelemetry:
    def test_flips_explicit_flag(self) -> None:
        assert _analytics._explicitly_disabled is False
        _analytics.disable_telemetry()
        assert _analytics._explicitly_disabled is True

    def test_subsequent_capture_is_noop(self, monkeypatch: pytest.MonkeyPatch) -> None:
        mock_client = MagicMock()
        monkeypatch.setattr(_analytics, "_posthog_client", mock_client)
        monkeypatch.setattr(_analytics, "_initialized", True)
        _analytics.disable_telemetry()
        _analytics.capture_event("uid", "evt")
        mock_client.capture.assert_not_called()

    def test_flips_existing_client_disabled_attribute(self, monkeypatch: pytest.MonkeyPatch) -> None:
        mock_client = MagicMock()
        mock_client.disabled = False
        monkeypatch.setattr(_analytics, "_posthog_client", mock_client)
        _analytics.disable_telemetry()
        assert mock_client.disabled is True

    def test_no_existing_client_is_fine(self) -> None:
        # _posthog_client is None per autouse reset; should not raise.
        _analytics.disable_telemetry()
        assert _analytics._explicitly_disabled is True
