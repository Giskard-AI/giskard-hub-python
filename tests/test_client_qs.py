from __future__ import annotations

from urllib.parse import unquote

from giskard_hub import HubClient, AsyncHubClient


def test_hubclient_uses_repeat_array_query_params() -> None:
    client = HubClient(base_url="http://example.com", api_key="test")
    try:
        assert unquote(client.qs.stringify({"include": ["agent", "dataset"]})) == "include=agent&include=dataset"
        assert unquote(client.qs.stringify({"include": ["dataset", "agent"]})) == "include=dataset&include=agent"
    finally:
        client.close()


async def test_asynchubclient_uses_repeat_array_query_params() -> None:
    client = AsyncHubClient(base_url="http://example.com", api_key="test")
    try:
        assert unquote(client.qs.stringify({"include": ["agent", "dataset"]})) == "include=agent&include=dataset"
        assert unquote(client.qs.stringify({"include": ["dataset", "agent"]})) == "include=dataset&include=agent"
    finally:
        await client.close()
