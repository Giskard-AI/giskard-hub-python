from __future__ import annotations

import json
from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from giskard_hub import HubClient, AsyncHubClient, connect_local_agent, connect_local_agent_sync
from giskard_hub._exceptions import HubClientError
from giskard_hub.lib.local_agent import (
    invoke_local_agent_handler,
    local_agent_connect_headers,
    build_local_agent_connect_url,
    handle_hub_local_agent_message,
    invoke_local_agent_handler_sync,
    handle_hub_local_agent_message_sync,
)

API_KEY = "test-key"


def test_build_url_from_https_origin() -> None:
    url = build_local_agent_connect_url(
        "https://app.llm.localhost",
        name="Demo",
        project_id="proj-1",
    )
    assert url.startswith("wss://app.llm.localhost/_api/v2/local-agents/connect")
    assert "name=Demo" in url
    assert "project_id=proj-1" in url


def test_build_url_from_http_origin() -> None:
    url = build_local_agent_connect_url("http://localhost:8000")
    assert url.startswith("ws://localhost:8000/_api/v2/local-agents/connect")


def test_build_url_from_sdk_base_url_with_api_suffix() -> None:
    url = build_local_agent_connect_url("https://app.llm.localhost/_api", name="Demo")
    assert url.startswith("wss://app.llm.localhost/_api/v2/local-agents/connect")
    assert "name=Demo" in url


def test_build_url_keeps_explicit_ws_path() -> None:
    raw = "wss://hub.example/_api/v2/local-agents/connect?name=x"
    assert build_local_agent_connect_url(raw) == raw


def test_connect_headers_include_tenant_host() -> None:
    assert local_agent_connect_headers("secret") == {"X-API-Key": "secret"}
    assert local_agent_connect_headers("secret", "app.llm.localhost") == {
        "X-API-Key": "secret",
        "X-Forwarded-Host": "app.llm.localhost",
    }


async def test_sync_and_async_handlers() -> None:
    async def async_handler(payload: dict[str, Any]) -> dict[str, Any]:
        return {"echo": payload["n"]}

    assert await invoke_local_agent_handler(lambda _payload: {"n": 1}, {"n": 0}) == {"n": 1}
    assert await invoke_local_agent_handler(async_handler, {"n": 2}) == {"echo": 2}


async def test_handler_must_return_dict() -> None:
    def not_a_dict(_payload: dict[str, Any]) -> Any:
        return "nope"

    with pytest.raises(TypeError, match="must return a dict"):
        await invoke_local_agent_handler(not_a_dict, {})


def test_sync_handler_rejects_async_callable() -> None:
    async def async_handler(payload: dict[str, Any]) -> dict[str, Any]:
        return payload

    with pytest.raises(TypeError, match="Async local agent handlers"):
        invoke_local_agent_handler_sync(async_handler, {})


async def test_call_message_runs_handler() -> None:
    reply = await handle_hub_local_agent_message(
        {"type": "call", "id": "abc", "payload": {"messages": [{"content": "hi"}]}},
        lambda payload: {
            "response": {
                "role": "assistant",
                "content": payload["messages"][0]["content"],
            }
        },
    )
    assert reply == {
        "type": "result",
        "id": "abc",
        "output": {"response": {"role": "assistant", "content": "hi"}},
    }


def test_sync_call_message_runs_handler() -> None:
    reply = handle_hub_local_agent_message_sync(
        {"type": "call", "id": "abc", "payload": {"messages": [{"content": "hi"}]}},
        lambda payload: {
            "response": {
                "role": "assistant",
                "content": payload["messages"][0]["content"],
            }
        },
    )
    assert reply == {
        "type": "result",
        "id": "abc",
        "output": {"response": {"role": "assistant", "content": "hi"}},
    }


async def test_call_message_reports_handler_error() -> None:
    def boom(_payload: dict[str, Any]) -> dict[str, Any]:
        raise RuntimeError("nope")

    reply = await handle_hub_local_agent_message({"type": "call", "id": "abc", "payload": {}}, boom)
    assert reply == {"type": "error", "id": "abc", "message": "nope"}


async def test_hub_error_message_raises() -> None:
    with pytest.raises(HubClientError, match="denied"):
        await handle_hub_local_agent_message({"type": "error", "message": "denied"}, lambda _payload: {})


class _FakeAsyncWs:
    def __init__(self, incoming: list[str]) -> None:
        self.sent: list[str] = []
        self._incoming = list(incoming)

    async def recv(self) -> str:
        return self._incoming.pop(0)

    def __aiter__(self) -> _FakeAsyncWs:
        return self

    async def __anext__(self) -> str:
        if not self._incoming:
            raise StopAsyncIteration
        return self._incoming.pop(0)

    async def send(self, data: str) -> None:
        self.sent.append(data)


class _AsyncCM:
    def __init__(self, websocket: _FakeAsyncWs) -> None:
        self._websocket = websocket

    async def __aenter__(self) -> _FakeAsyncWs:
        return self._websocket

    async def __aexit__(self, exc_type: object, exc: object, tb: object) -> bool:
        return False


class _FakeSyncWs:
    def __init__(self, incoming: list[str]) -> None:
        self.sent: list[str] = []
        self._incoming = list(incoming)

    def recv(self) -> str:
        return self._incoming.pop(0)

    def __iter__(self) -> _FakeSyncWs:
        return self

    def __next__(self) -> str:
        if not self._incoming:
            raise StopIteration
        return self._incoming.pop(0)

    def send(self, data: str) -> None:
        self.sent.append(data)


class _SyncCM:
    def __init__(self, websocket: _FakeSyncWs) -> None:
        self._websocket = websocket

    def __enter__(self) -> _FakeSyncWs:
        return self._websocket

    def __exit__(self, exc_type: object, exc: object, tb: object) -> bool:
        return False


def _echo(payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "response": {
            "role": "assistant",
            "content": payload["messages"][0]["content"],
        }
    }


async def test_connect_local_agent_roundtrip() -> None:
    incoming = [
        json.dumps({"type": "connected", "agent_id": "a1", "project_id": "p1"}),
        json.dumps({"type": "call", "id": "c1", "payload": {"messages": [{"content": "ping"}]}}),
    ]
    fake = _FakeAsyncWs(incoming)
    fake_ws_module = MagicMock()
    fake_ws_module.connect.return_value = _AsyncCM(fake)

    with patch("giskard_hub.lib.local_agent.websockets", fake_ws_module):
        hello = await connect_local_agent(
            hub_url="https://app.llm.localhost",
            api_key="secret",
            handler=_echo,
            name="Echo",
        )

    assert hello["agent_id"] == "a1"
    assert json.loads(fake.sent[0])["output"]["response"]["content"] == "ping"
    fake_ws_module.connect.assert_called_once()
    kwargs = fake_ws_module.connect.call_args.kwargs
    assert kwargs["additional_headers"]["X-API-Key"] == "secret"
    assert "local-agents/connect" in fake_ws_module.connect.call_args.args[0]


def test_connect_local_agent_sync_roundtrip() -> None:
    incoming = [
        json.dumps({"type": "connected", "agent_id": "a1", "project_id": "p1"}),
        json.dumps({"type": "call", "id": "c1", "payload": {"messages": [{"content": "ping"}]}}),
    ]
    fake = _FakeSyncWs(incoming)

    with patch("giskard_hub.lib.local_agent.sync_websocket_connect", return_value=_SyncCM(fake)) as connect:
        hello = connect_local_agent_sync(
            hub_url="http://localhost:8000",
            api_key="secret",
            handler=_echo,
            name="Echo",
            tenant_host="app.llm.localhost",
        )

    assert hello["agent_id"] == "a1"
    assert json.loads(fake.sent[0])["output"]["response"]["content"] == "ping"
    kwargs = connect.call_args.kwargs
    assert kwargs["additional_headers"]["X-API-Key"] == "secret"
    assert kwargs["additional_headers"]["X-Forwarded-Host"] == "app.llm.localhost"


def test_hub_client_connect_local_agent_uses_client_credentials() -> None:
    incoming = [
        json.dumps({"type": "connected", "agent_id": "a1", "project_id": "p1", "name": "Local echo"}),
    ]
    fake = _FakeSyncWs(incoming)
    client = HubClient(
        base_url="https://app.llm.localhost",
        api_key=API_KEY,
        tenant_host="tenant.example",
    )

    with patch("giskard_hub._client.run_local_agent_session_sync", wraps=connect_local_agent_sync) as wrapped:
        with patch("giskard_hub.lib.local_agent.sync_websocket_connect", return_value=_SyncCM(fake)):
            hello = client.connect_local_agent(handler=_echo, name="Local echo")

    assert hello["agent_id"] == "a1"
    kwargs = wrapped.call_args.kwargs
    assert kwargs["api_key"] == API_KEY
    assert kwargs["tenant_host"] == "tenant.example"
    assert kwargs["hub_url"].rstrip("/") == "https://app.llm.localhost/_api"


async def test_async_hub_client_connect_local_agent_uses_client_credentials() -> None:
    incoming = [
        json.dumps({"type": "connected", "agent_id": "a1", "project_id": "p1"}),
    ]
    fake = _FakeAsyncWs(incoming)
    fake_ws_module = MagicMock()
    fake_ws_module.connect.return_value = _AsyncCM(fake)
    client = AsyncHubClient(base_url="https://app.llm.localhost", api_key=API_KEY)

    with patch("giskard_hub.lib.local_agent.websockets", fake_ws_module):
        hello = await client.connect_local_agent(handler=_echo, name="Local echo")

    assert hello["agent_id"] == "a1"
    assert fake_ws_module.connect.call_args.kwargs["additional_headers"]["X-API-Key"] == API_KEY
