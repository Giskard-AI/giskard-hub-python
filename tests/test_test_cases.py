"""Tests for `TestCasesResource` argument validation (sync + async)."""

import pytest

from giskard_hub import HubClient, AsyncHubClient


@pytest.fixture
def hub() -> HubClient:
    return HubClient(api_key="test", base_url="http://localhost")


@pytest.fixture
def async_hub() -> AsyncHubClient:
    return AsyncHubClient(api_key="test", base_url="http://localhost")


def test_create_rejects_both_messages_and_input_data(hub: HubClient) -> None:
    with pytest.raises(ValueError, match="Cannot provide both 'messages' and 'input_data'"):
        hub.test_cases.create(
            dataset_id="d",
            messages=[{"role": "user", "content": "x"}],
            input_data=[{"role": "user", "content": "x"}],
        )


def test_create_rejects_neither(hub: HubClient) -> None:
    with pytest.raises(ValueError, match="Must provide either 'messages' or 'input_data'"):
        hub.test_cases.create(dataset_id="d")


@pytest.mark.asyncio
async def test_async_create_rejects_both(async_hub: AsyncHubClient) -> None:
    with pytest.raises(ValueError, match="Cannot provide both 'messages' and 'input_data'"):
        await async_hub.test_cases.create(
            dataset_id="d",
            messages=[{"role": "user", "content": "x"}],
            input_data=[{"role": "user", "content": "x"}],
        )


@pytest.mark.asyncio
async def test_async_create_rejects_neither(async_hub: AsyncHubClient) -> None:
    with pytest.raises(ValueError, match="Must provide either 'messages' or 'input_data'"):
        await async_hub.test_cases.create(dataset_id="d")
