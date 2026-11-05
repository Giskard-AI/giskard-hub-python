# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from giskard_hub import HubClient, AsyncHubClient
from tests.utils import assert_matches_type
from giskard_hub.types import CreditUsageSummary

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_credits(self, client: HubClient) -> None:
        usage = client.usage.retrieve_credits()
        assert_matches_type(CreditUsageSummary, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_credits_with_all_params(self, client: HubClient) -> None:
        usage = client.usage.retrieve_credits(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CreditUsageSummary, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_credits(self, client: HubClient) -> None:
        response = client.usage.with_raw_response.retrieve_credits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        usage = response.parse()
        assert_matches_type(CreditUsageSummary, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_credits(self, client: HubClient) -> None:
        with client.usage.with_streaming_response.retrieve_credits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            usage = response.parse()
            assert_matches_type(CreditUsageSummary, usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client",
        [False, True, {"http_client": "aiohttp"}],
        indirect=True,
        ids=["loose", "strict", "aiohttp"],
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_credits(self, async_client: AsyncHubClient) -> None:
        usage = await async_client.usage.retrieve_credits()
        assert_matches_type(CreditUsageSummary, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_credits_with_all_params(self, async_client: AsyncHubClient) -> None:
        usage = await async_client.usage.retrieve_credits(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CreditUsageSummary, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_credits(self, async_client: AsyncHubClient) -> None:
        response = await async_client.usage.with_raw_response.retrieve_credits()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        usage = response.parse()
        assert_matches_type(CreditUsageSummary, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_credits(self, async_client: AsyncHubClient) -> None:
        async with async_client.usage.with_streaming_response.retrieve_credits() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(CreditUsageSummary, usage, path=["response"])

        assert cast(Any, response.is_closed) is True
