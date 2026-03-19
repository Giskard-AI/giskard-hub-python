"""Polling client for local-agent scan execution."""

import time
import asyncio
import inspect
import logging
from typing import Any, Callable, Awaitable

import httpx

from ..types.chat import ChatMessage

logger = logging.getLogger(__name__)

_TERMINAL_STATES = frozenset({"finished", "error", "canceled"})


def _normalize_output(value: Any) -> dict[str, object]:
    from ._helpers_types import normalize_agent_output

    return normalize_agent_output(value).to_dict()


def run_poll_scan(
    base_url: str,
    api_key: str,
    scan_id: str,
    agent: Callable[[list[ChatMessage]], Any],
    http_client: httpx.Client,
    poll_interval: float = 0.5,
) -> None:
    """Poll for invocations, call the local agent, submit responses.

    Blocks until the scan reaches a terminal state.
    """
    headers = {"X-API-Key": api_key}
    url = f"{base_url}/v2/scans/{scan_id}/invocations"

    while True:
        resp = http_client.get(url, params={"status": "pending"}, headers=headers)
        resp.raise_for_status()
        data = resp.json()["data"]

        for inv in data["invocations"]:
            messages = [ChatMessage(role=m["role"], content=m.get("content", "")) for m in inv["messages"]]
            try:
                body: dict[str, Any] = {"output": _normalize_output(agent(messages))}
            except Exception as exc:
                logger.error("Agent invocation failed: %s", exc)
                body = {"error": {"message": str(exc)}}

            http_client.post(f"{url}/{inv['id']}/respond", json=body, headers=headers).raise_for_status()

        if data["scan_status"] in _TERMINAL_STATES:
            break

        time.sleep(poll_interval)


async def arun_poll_scan(
    base_url: str,
    api_key: str,
    scan_id: str,
    agent: Callable[[list[ChatMessage]], Any | Awaitable[Any]],
    http_client: httpx.AsyncClient,
    poll_interval: float = 0.5,
) -> None:
    """Async version of the polling loop."""
    headers = {"X-API-Key": api_key}
    url = f"{base_url}/v2/scans/{scan_id}/invocations"

    while True:
        resp = await http_client.get(url, params={"status": "pending"}, headers=headers)
        resp.raise_for_status()
        data = resp.json()["data"]

        async def _process(inv: dict[str, Any]) -> None:
            messages = [ChatMessage(role=m["role"], content=m.get("content", "")) for m in inv["messages"]]
            try:
                result = agent(messages)
                if inspect.isawaitable(result):
                    result = await result
                body: dict[str, Any] = {"output": _normalize_output(result)}
            except Exception as exc:
                logger.error("Agent invocation failed: %s", exc)
                body = {"error": {"message": str(exc)}}

            (await http_client.post(f"{url}/{inv['id']}/respond", json=body, headers=headers)).raise_for_status()

        await asyncio.gather(*(_process(inv) for inv in data["invocations"]))

        if data["scan_status"] in _TERMINAL_STATES:
            break

        await asyncio.sleep(poll_interval)
