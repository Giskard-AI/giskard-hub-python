"""Connect a local Python callable to Giskard Hub as a live agent.

The Hub WebSocket at ``/_api/v2/local-agents/connect`` creates an agent when
this session connects and deletes it when the socket closes. Hub workers invoke
the agent through a tenant-scoped call bridge; this client receives those calls
and runs ``handler``.
"""

from __future__ import annotations

import json
import inspect
from typing import Any, cast
from urllib.parse import urlparse, urlencode, urlunparse
from collections.abc import Callable
from typing_extensions import TypeAlias

import websockets
from websockets.sync.client import connect as sync_websocket_connect

from .._exceptions import HubClientError

LocalAgentHandler: TypeAlias = Callable[[dict[str, Any]], object]

_CONNECT_PATH = "/_api/v2/local-agents/connect"
_DEFAULT_AGENT_NAME = "Local agent"


def build_local_agent_connect_url(
    hub_url: str,
    *,
    name: str = _DEFAULT_AGENT_NAME,
    project_id: str | None = None,
    description: str | None = None,
) -> str:
    """Build the Hub WebSocket URL used to register a local agent.

    Parameters
    ----------
    hub_url:
        Hub origin (``https://app.example.com``), an SDK base URL that already
        includes ``/_api``, or a full ``ws(s)://`` URL.
    name:
        Display name created in Hub on connect.
    project_id:
        Project that should own the agent. Hub picks the first writable project
        when omitted.
    description:
        Optional agent description.

    Returns
    -------
    str
        WebSocket URL including query parameters.
    """
    parsed = urlparse(hub_url)
    if parsed.scheme in {"ws", "wss"} and parsed.path.rstrip("/"):
        return hub_url

    scheme = "wss" if parsed.scheme in {"https", "wss"} else "ws"
    query = urlencode(
        {
            key: value
            for key, value in {
                "name": name,
                "project_id": project_id,
                "description": description,
            }.items()
            if value
        }
    )
    return urlunparse((scheme, parsed.netloc, _CONNECT_PATH, "", query, ""))


def local_agent_connect_headers(api_key: str, tenant_host: str | None = None) -> dict[str, str]:
    """Return the WebSocket headers Hub expects for a local-agent session."""
    headers = {"X-API-Key": api_key}
    if tenant_host:
        headers["X-Forwarded-Host"] = tenant_host
    return headers


def _decode_json_object(raw: str | bytes) -> dict[str, Any]:
    if isinstance(raw, bytes):
        raw = raw.decode("utf-8")
    message: object = json.loads(raw)
    if not isinstance(message, dict):
        raise HubClientError("Hub local-agent message must be a JSON object")
    return cast(dict[str, Any], message)


def _handshake_or_raise(message: dict[str, Any]) -> dict[str, Any]:
    if message.get("type") == "error":
        raise HubClientError(str(message.get("message") or "Hub rejected the local agent connection"))
    if message.get("type") != "connected":
        raise HubClientError(f"Unexpected Hub handshake: {message!r}")
    return message


def _error_reply(call_id: object, message: str) -> dict[str, Any]:
    return {"type": "error", "id": call_id, "message": message}


def _call_reply(message: dict[str, Any]) -> tuple[object, dict[str, Any]] | dict[str, Any] | None:
    """Return (call_id, payload), an error reply, or None for non-call messages."""
    msg_type = message.get("type")
    if msg_type == "connected":
        return None
    if msg_type == "error":
        raise HubClientError(str(message.get("message") or "Hub local-agent error"))
    if msg_type != "call":
        return None

    call_id = message.get("id")
    payload: object = message.get("payload")
    if not isinstance(payload, dict):
        return _error_reply(call_id, "Hub call payload must be a JSON object.")
    return call_id, cast(dict[str, Any], payload)


async def invoke_local_agent_handler(handler: LocalAgentHandler, payload: dict[str, Any]) -> dict[str, Any]:
    """Run a local agent handler and require a JSON-object result.

    Parameters
    ----------
    handler:
        Sync or async callable that receives the Hub request body.
    payload:
        JSON object posted by Hub (playground, eval, scan, or ART).

    Returns
    -------
    dict
        JSON object sent back to Hub as the agent output.

    Raises
    ------
    TypeError
        If the handler does not return a dict.
    """
    result: object = handler(payload)
    if inspect.isawaitable(result):
        result = await result
    if not isinstance(result, dict):
        raise TypeError("Local agent handler must return a dict")
    return cast(dict[str, Any], result)


def invoke_local_agent_handler_sync(handler: LocalAgentHandler, payload: dict[str, Any]) -> dict[str, Any]:
    """Run a synchronous local agent handler and require a JSON-object result.

    Parameters
    ----------
    handler:
        Callable that receives the Hub request body. Async handlers are not
        supported on the synchronous client.
    payload:
        JSON object posted by Hub (playground, eval, scan, or ART).

    Returns
    -------
    dict
        JSON object sent back to Hub as the agent output.

    Raises
    ------
    TypeError
        If the handler is async or does not return a dict.
    """
    result: object = handler(payload)
    if inspect.isawaitable(result):
        close = getattr(result, "close", None)
        if callable(close):
            close()
        raise TypeError("Async local agent handlers require AsyncHubClient.connect_local_agent")
    if not isinstance(result, dict):
        raise TypeError("Local agent handler must return a dict")
    return cast(dict[str, Any], result)


async def handle_hub_local_agent_message(
    message: dict[str, Any],
    handler: LocalAgentHandler,
) -> dict[str, Any] | None:
    """Translate one Hub WebSocket message into a reply, if needed.

    Parameters
    ----------
    message:
        Decoded JSON message from Hub.
    handler:
        Local callable that serves agent invocations.

    Returns
    -------
    dict or None
        Reply to send, or ``None`` when the message is informational.
    """
    parsed = _call_reply(message)
    if parsed is None or isinstance(parsed, dict):
        return parsed
    call_id, payload = parsed
    try:
        output = await invoke_local_agent_handler(handler, payload)
    except Exception as exc:
        return _error_reply(call_id, str(exc))
    return {"type": "result", "id": call_id, "output": output}


def handle_hub_local_agent_message_sync(
    message: dict[str, Any],
    handler: LocalAgentHandler,
) -> dict[str, Any] | None:
    """Synchronous variant of :func:`handle_hub_local_agent_message`."""
    parsed = _call_reply(message)
    if parsed is None or isinstance(parsed, dict):
        return parsed
    call_id, payload = parsed
    try:
        output = invoke_local_agent_handler_sync(handler, payload)
    except Exception as exc:
        return _error_reply(call_id, str(exc))
    return {"type": "result", "id": call_id, "output": output}


async def connect_local_agent(
    *,
    hub_url: str,
    api_key: str,
    handler: LocalAgentHandler,
    name: str = _DEFAULT_AGENT_NAME,
    project_id: str | None = None,
    description: str | None = None,
    tenant_host: str | None = None,
) -> dict[str, Any]:
    """Connect ``handler`` to Hub until the session is closed.

    Hub creates a read-only local agent on connect and deletes it on disconnect.
    Evaluations and other workers in the same tenant reach the handler through
    that live session.

    Parameters
    ----------
    hub_url:
        Hub origin, for example ``https://app.llm.localhost``.
    api_key:
        Tenant API key (sent as ``X-API-Key``).
    handler:
        Sync or async callable ``payload -> dict``. For chat agents, Hub sends
        ``{"messages": [...]}`` and expects
        ``{"response": {"role": "assistant", "content": "..."}}``.
    name:
        Agent name shown in Hub.
    project_id:
        Project UUID. When omitted, Hub uses the first project the key can
        create agents in.
    description:
        Optional description stored on the Hub agent.
    tenant_host:
        Optional tenant hostname sent as ``X-Forwarded-Host`` when ``hub_url``
        is not the tenant host.

    Returns
    -------
    dict
        The Hub ``connected`` handshake (includes ``agent_id`` and
        ``project_id``) after the session ends.

    Example
    -------
    ::

        from giskard_hub import connect_local_agent


        async def echo(payload: dict) -> dict:
            text = payload["messages"][-1]["content"]
            return {"response": {"role": "assistant", "content": text}}


        await connect_local_agent(
            hub_url="https://app.llm.localhost",
            api_key="...",
            handler=echo,
        )
    """
    uri = build_local_agent_connect_url(hub_url, name=name, project_id=project_id, description=description)
    handshake: dict[str, Any] | None = None
    async with websockets.connect(
        uri, additional_headers=local_agent_connect_headers(api_key, tenant_host)
    ) as websocket:
        handshake = _handshake_or_raise(_decode_json_object(await websocket.recv()))
        async for raw in websocket:
            reply = await handle_hub_local_agent_message(_decode_json_object(raw), handler)
            if reply is not None:
                await websocket.send(json.dumps(reply))
    return handshake or {}


def connect_local_agent_sync(
    *,
    hub_url: str,
    api_key: str,
    handler: LocalAgentHandler,
    name: str = _DEFAULT_AGENT_NAME,
    project_id: str | None = None,
    description: str | None = None,
    tenant_host: str | None = None,
) -> dict[str, Any]:
    """Synchronous variant of :func:`connect_local_agent`.

    Async handlers are not supported; use :func:`connect_local_agent` or
    ``AsyncHubClient.connect_local_agent`` instead.
    """
    uri = build_local_agent_connect_url(hub_url, name=name, project_id=project_id, description=description)
    handshake: dict[str, Any] | None = None
    with sync_websocket_connect(uri, additional_headers=local_agent_connect_headers(api_key, tenant_host)) as websocket:
        handshake = _handshake_or_raise(_decode_json_object(websocket.recv()))
        for raw in websocket:
            reply = handle_hub_local_agent_message_sync(_decode_json_object(raw), handler)
            if reply is not None:
                websocket.send(json.dumps(reply))
    return handshake or {}
