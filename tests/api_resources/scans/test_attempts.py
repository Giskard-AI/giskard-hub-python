# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from giskard_hub import HubClient, AsyncHubClient
from tests.utils import assert_matches_type
from giskard_hub.types import APIResponse
from giskard_hub.types.scans import ScanProbeAttempt

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttempts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubClient) -> None:
        attempt = client.scans.attempts.update(
            probe_attempt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[ScanProbeAttempt], attempt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubClient) -> None:
        attempt = client.scans.attempts.update(
            probe_attempt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            review_status="pending",
            severity=0,
            successful=True,
        )
        assert_matches_type(APIResponse[ScanProbeAttempt], attempt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubClient) -> None:
        response = client.scans.attempts.with_raw_response.update(
            probe_attempt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        attempt = response.parse()
        assert_matches_type(APIResponse[ScanProbeAttempt], attempt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubClient) -> None:
        with client.scans.attempts.with_streaming_response.update(
            probe_attempt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            attempt = response.parse()
            assert_matches_type(APIResponse[ScanProbeAttempt], attempt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `probe_attempt_id` but received ''",
        ):
            client.scans.attempts.with_raw_response.update(
                probe_attempt_id="",
            )


class TestAsyncAttempts:
    parametrize = pytest.mark.parametrize(
        "async_client",
        [False, True, {"http_client": "aiohttp"}],
        indirect=True,
        ids=["loose", "strict", "aiohttp"],
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubClient) -> None:
        attempt = await async_client.scans.attempts.update(
            probe_attempt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[ScanProbeAttempt], attempt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubClient) -> None:
        attempt = await async_client.scans.attempts.update(
            probe_attempt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            review_status="pending",
            severity=0,
            successful=True,
        )
        assert_matches_type(APIResponse[ScanProbeAttempt], attempt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubClient) -> None:
        response = await async_client.scans.attempts.with_raw_response.update(
            probe_attempt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        attempt = await response.parse()
        assert_matches_type(APIResponse[ScanProbeAttempt], attempt, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubClient) -> None:
        async with async_client.scans.attempts.with_streaming_response.update(
            probe_attempt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            attempt = await response.parse()
            assert_matches_type(APIResponse[ScanProbeAttempt], attempt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `probe_attempt_id` but received ''",
        ):
            await async_client.scans.attempts.with_raw_response.update(
                probe_attempt_id="",
            )
