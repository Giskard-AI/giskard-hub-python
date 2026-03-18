"""WebSocket client for local-agent scan execution.

This module provides both sync and async functions that connect to the Hub's
``/v2/scans/{scan_id}/ws`` WebSocket endpoint, receive agent invocation
requests from LIDAR (running on the Hub), execute the local agent callable,
and send the response back.
"""

import asyncio
import inspect
import json
import logging
import os
import ssl
from typing import Any, Awaitable, Callable
from urllib.parse import urlencode, urlparse, urlunparse

import httpx

from ..types.chat import ChatMessage

logger = logging.getLogger(__name__)


def _ssl_context_from_httpx(http_client: httpx.Client | httpx.AsyncClient | None) -> ssl.SSLContext | None:
    """Derive an ``ssl.SSLContext`` that mirrors the httpx client's TLS config.

    Walks the internal transport chain
    (``httpx.Client._transport._pool._ssl_context``) to extract the exact
    ``ssl.SSLContext`` that httpx uses.  This means ``verify=False`` on the
    httpx client automatically disables verification for the WebSocket too,
    and custom CA bundles are preserved.

    Returns ``None`` (use system defaults) when extraction fails.
    """
    if http_client is None:
        return None

    # httpx.Client._transport → HTTPTransport._pool → httpcore.ConnectionPool._ssl_context
    try:
        ctx = http_client._transport._pool._ssl_context  # type: ignore[union-attr]
        if isinstance(ctx, ssl.SSLContext):
            return ctx
    except AttributeError:
        pass

    # Fallback: check common CA-bundle environment variables.
    for env_var in ("SSL_CERT_FILE", "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE"):
        ca_path = os.environ.get(env_var)
        if ca_path:
            return ssl.create_default_context(cafile=ca_path)

    return None


def _http_to_ws_url(http_url: str) -> str:
    """Convert an HTTP(S) URL to a WS(S) URL."""
    parsed = urlparse(http_url)
    if parsed.scheme == "https":
        scheme = "wss"
    elif parsed.scheme == "http":
        scheme = "ws"
    else:
        scheme = parsed.scheme
    return urlunparse(parsed._replace(scheme=scheme))


def _build_ws_url(base_url: str, scan_id: str, api_key: str) -> str:
    """Build the full WebSocket URL for a local scan session."""
    ws_base = _http_to_ws_url(base_url.rstrip("/"))
    query = urlencode({"api_key": api_key})
    return f"{ws_base}/v2/scans/{scan_id}/ws?{query}"


AgentCallable = Callable[[list[ChatMessage]], Any]
AsyncAgentCallable = Callable[[list[ChatMessage]], Any | Awaitable[Any]]


def _normalize_output(value: Any) -> dict:
    """Turn the agent return value into a dict matching the Hub protocol."""
    from ._helpers_types import normalize_agent_output

    output: AgentOutput = normalize_agent_output(value)
    return output.to_dict()


async def _arun_ws_scan(
    base_url: str,
    api_key: str,
    scan_id: str,
    agent: AsyncAgentCallable,
    on_progress: Callable[[dict], Any] | None = None,
    ssl_context: ssl.SSLContext | bool | None = None,
) -> dict | None:
    """Async implementation of the WebSocket scan loop.

    Returns the ``complete`` message payload, or ``None`` if the connection
    closed before completion.
    """
    try:
        from websockets.asyncio.client import connect
    except ImportError as exc:
        raise ImportError(
            "The 'websockets' package is required for local scan execution. "
            "Install it with: pip install 'giskard-hub[websockets]' or pip install websockets"
        ) from exc

    url = _build_ws_url(base_url, scan_id, api_key)
    logger.info("Connecting to scan WebSocket: %s", url.split("?")[0])

    connect_kwargs: dict[str, Any] = {}
    if ssl_context is not None:
        connect_kwargs["ssl"] = ssl_context

    async with connect(url, **connect_kwargs) as ws:
        async for raw_msg in ws:
            try:
                msg = json.loads(raw_msg)
            except json.JSONDecodeError:
                logger.warning("Non-JSON WebSocket message received, ignoring")
                continue

            msg_type = msg.get("type")

            if msg_type == "invoke":
                request_id = msg["request_id"]
                messages = [
                    ChatMessage(
                        role=m.get("role", "user"),
                        content=m.get("content", ""),
                    )
                    for m in msg.get("messages", [])
                ]

                try:
                    result = agent(messages)
                    if inspect.isawaitable(result):
                        result = await result
                    output = _normalize_output(result)
                    await ws.send(
                        json.dumps(
                            {
                                "type": "response",
                                "request_id": request_id,
                                "output": output,
                            }
                        )
                    )
                except Exception as exc:
                    logger.error("Agent invocation failed: %s", exc)
                    await ws.send(
                        json.dumps(
                            {
                                "type": "error",
                                "request_id": request_id,
                                "error": {"message": str(exc)},
                            }
                        )
                    )

            elif msg_type == "progress":
                if on_progress:
                    status = msg.get("status", {})
                    cb_result = on_progress(status)
                    if inspect.isawaitable(cb_result):
                        await cb_result

            elif msg_type == "complete":
                logger.info(
                    "Scan %s completed with grade: %s",
                    scan_id,
                    msg.get("grade"),
                )
                return msg

            elif msg_type == "error":
                error_msg = msg.get("message", "Unknown server error")
                raise RuntimeError(f"Scan error from Hub: {error_msg}")

            else:
                logger.warning("Unknown WebSocket message type: %s", msg_type)

    return None


def run_ws_scan(
    base_url: str,
    api_key: str,
    scan_id: str,
    agent: AgentCallable,
    on_progress: Callable[[dict], Any] | None = None,
    ssl_context: ssl.SSLContext | bool | None = None,
) -> dict | None:
    """Synchronous wrapper around the async WebSocket scan loop.

    Works correctly even when called from an environment that already has
    a running event loop (e.g. Jupyter notebooks) by executing the async
    code in a dedicated thread with its own event loop.
    """
    import concurrent.futures

    def _run_in_thread() -> dict | None:
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(
                _arun_ws_scan(
                    base_url, api_key, scan_id, agent, on_progress,
                    ssl_context=ssl_context,
                )
            )
        finally:
            loop.close()

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
        future = pool.submit(_run_in_thread)
        return future.result()
