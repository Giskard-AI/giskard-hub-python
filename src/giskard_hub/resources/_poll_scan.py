"""Polling client for local-agent scan execution.

The SDK polls ``GET /v2/scans/{scan_id}/invocations?status=pending`` for
invocation requests from LIDAR, executes the local agent callable, and
POSTs the response back via
``POST /v2/scans/{scan_id}/invocations/{id}/respond``.

All communication is plain HTTP — no WebSocket, no long-lived connections.
"""

import asyncio
import inspect
import logging
import time
from typing import Any, Awaitable, Callable

import httpx

from ..types.chat import ChatMessage

logger = logging.getLogger(__name__)

AgentCallable = Callable[[list[ChatMessage]], Any]
AsyncAgentCallable = Callable[[list[ChatMessage]], Any | Awaitable[Any]]

_TERMINAL_STATES = frozenset({"finished", "error", "canceled"})


def _normalize_output(value: Any) -> dict[str, object]:
    """Turn the agent return value into a dict matching the Hub protocol."""
    from ._helpers_types import normalize_agent_output

    output = normalize_agent_output(value)
    return output.to_dict()


def run_poll_scan(
    base_url: str,
    api_key: str,
    scan_id: str,
    agent: AgentCallable,
    http_client: httpx.Client,
    poll_interval: float = 0.5,
) -> None:
    """Synchronous polling loop for local scan execution.

    Blocks until the scan finishes, is cancelled, or errors.
    Works in Jupyter notebooks without event-loop conflicts.
    """
    headers = {"X-API-Key": api_key}
    invocations_url = f"{base_url}/v2/scans/{scan_id}/invocations"

    while True:
        resp = http_client.get(
            invocations_url,
            params={"status": "pending"},
            headers=headers,
        )
        resp.raise_for_status()
        payload = resp.json()["data"]

        for inv in payload["invocations"]:
            _process_invocation_sync(
                inv, agent, base_url, scan_id, headers, http_client
            )

        if payload["scan_status"] in _TERMINAL_STATES:
            break

        time.sleep(poll_interval)


def _process_invocation_sync(
    inv: dict[str, Any],
    agent: AgentCallable,
    base_url: str,
    scan_id: str,
    headers: dict[str, str],
    http_client: httpx.Client,
) -> None:
    invocation_id = inv["id"]
    messages = [
        ChatMessage(role=m.get("role", "user"), content=m.get("content", ""))
        for m in inv.get("messages", [])
    ]

    try:
        result = agent(messages)
        output = _normalize_output(result)
        body: dict[str, Any] = {"output": output}
    except Exception as exc:
        logger.error("Agent invocation failed: %s", exc)
        body = {"error": {"message": str(exc)}}

    resp = http_client.post(
        f"{base_url}/v2/scans/{scan_id}/invocations/{invocation_id}/respond",
        json=body,
        headers=headers,
    )
    resp.raise_for_status()


async def arun_poll_scan(
    base_url: str,
    api_key: str,
    scan_id: str,
    agent: AsyncAgentCallable,
    http_client: httpx.AsyncClient,
    poll_interval: float = 0.5,
) -> None:
    """Async polling loop for local scan execution."""
    headers = {"X-API-Key": api_key}
    invocations_url = f"{base_url}/v2/scans/{scan_id}/invocations"

    while True:
        resp = await http_client.get(
            invocations_url,
            params={"status": "pending"},
            headers=headers,
        )
        resp.raise_for_status()
        payload = resp.json()["data"]

        await asyncio.gather(
            *(
                _process_invocation_async(
                    inv, agent, base_url, scan_id, headers, http_client
                )
                for inv in payload["invocations"]
            )
        )

        if payload["scan_status"] in _TERMINAL_STATES:
            break

        await asyncio.sleep(poll_interval)


async def _process_invocation_async(
    inv: dict[str, Any],
    agent: AsyncAgentCallable,
    base_url: str,
    scan_id: str,
    headers: dict[str, str],
    http_client: httpx.AsyncClient,
) -> None:
    invocation_id = inv["id"]
    messages = [
        ChatMessage(role=m.get("role", "user"), content=m.get("content", ""))
        for m in inv.get("messages", [])
    ]

    try:
        result = agent(messages)
        if inspect.isawaitable(result):
            result = await result
        output = _normalize_output(result)
        body: dict[str, Any] = {"output": output}
    except Exception as exc:
        logger.error("Agent invocation failed: %s", exc)
        body = {"error": {"message": str(exc)}}

    resp = await http_client.post(
        f"{base_url}/v2/scans/{scan_id}/invocations/{invocation_id}/respond",
        json=body,
        headers=headers,
    )
    resp.raise_for_status()
