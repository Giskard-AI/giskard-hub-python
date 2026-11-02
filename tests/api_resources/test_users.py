# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from giskard_hub import HubClient, AsyncHubClient
from tests.utils import assert_matches_type
from giskard_hub.types import HubApiKey

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_api_key(self, client: HubClient) -> None:
        api_key = client.users.retrieve_api_key()
        assert_matches_type(HubApiKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_api_key(self, client: HubClient) -> None:
        response = client.users.with_raw_response.retrieve_api_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(HubApiKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_api_key(self, client: HubClient) -> None:
        with client.users.with_streaming_response.retrieve_api_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(HubApiKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_rotate_api_key(self, client: HubClient) -> None:
        api_key = client.users.rotate_api_key()
        assert_matches_type(HubApiKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_rotate_api_key(self, client: HubClient) -> None:
        response = client.users.with_raw_response.rotate_api_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(HubApiKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_rotate_api_key(self, client: HubClient) -> None:
        with client.users.with_streaming_response.rotate_api_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(HubApiKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client",
        [False, True, {"http_client": "aiohttp"}],
        indirect=True,
        ids=["loose", "strict", "aiohttp"],
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_api_key(self, async_client: AsyncHubClient) -> None:
        api_key = await async_client.users.retrieve_api_key()
        assert_matches_type(HubApiKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_api_key(self, async_client: AsyncHubClient) -> None:
        response = await async_client.users.with_raw_response.retrieve_api_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(HubApiKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_api_key(self, async_client: AsyncHubClient) -> None:
        async with async_client.users.with_streaming_response.retrieve_api_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(HubApiKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_rotate_api_key(self, async_client: AsyncHubClient) -> None:
        api_key = await async_client.users.rotate_api_key()
        assert_matches_type(HubApiKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_rotate_api_key(self, async_client: AsyncHubClient) -> None:
        response = await async_client.users.with_raw_response.rotate_api_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(HubApiKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_rotate_api_key(self, async_client: AsyncHubClient) -> None:
        async with async_client.users.with_streaming_response.rotate_api_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(HubApiKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True
