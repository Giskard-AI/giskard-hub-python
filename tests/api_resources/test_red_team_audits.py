# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from giskard_hub import HubClient, AsyncHubClient
from tests.utils import assert_matches_type
from giskard_hub.types import CreditEstimate

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRedTeamAudits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_estimate(self, client: HubClient) -> None:
        estimate = client.red_team_audits.estimate()
        assert_matches_type(CreditEstimate, estimate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_estimate_with_all_params(self, client: HubClient) -> None:
        estimate = client.red_team_audits.estimate(
            mode="light",
        )
        assert_matches_type(CreditEstimate, estimate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_estimate(self, client: HubClient) -> None:
        response = client.red_team_audits.with_raw_response.estimate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        estimate = response.parse()
        assert_matches_type(CreditEstimate, estimate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_estimate(self, client: HubClient) -> None:
        with client.red_team_audits.with_streaming_response.estimate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            estimate = response.parse()
            assert_matches_type(CreditEstimate, estimate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRedTeamAudits:
    parametrize = pytest.mark.parametrize(
        "async_client",
        [False, True, {"http_client": "aiohttp"}],
        indirect=True,
        ids=["loose", "strict", "aiohttp"],
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_estimate(self, async_client: AsyncHubClient) -> None:
        estimate = await async_client.red_team_audits.estimate()
        assert_matches_type(CreditEstimate, estimate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_estimate_with_all_params(self, async_client: AsyncHubClient) -> None:
        estimate = await async_client.red_team_audits.estimate(
            mode="regular",
        )
        assert_matches_type(CreditEstimate, estimate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_estimate(self, async_client: AsyncHubClient) -> None:
        response = await async_client.red_team_audits.with_raw_response.estimate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        estimate = response.parse()
        assert_matches_type(CreditEstimate, estimate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_estimate(self, async_client: AsyncHubClient) -> None:
        async with async_client.red_team_audits.with_streaming_response.estimate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            estimate = await response.parse()
            assert_matches_type(CreditEstimate, estimate, path=["response"])

        assert cast(Any, response.is_closed) is True
