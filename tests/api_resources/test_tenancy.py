# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from giskard_hub import HubClient, AsyncHubClient
from tests.utils import assert_matches_type
from giskard_hub.types import HealthStatus, FindTenantResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTenancy:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_discovery(self, client: HubClient) -> None:
        tenancy = client.tenancy.discovery()
        assert_matches_type(dict, tenancy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_discovery(self, client: HubClient) -> None:
        response = client.tenancy.with_raw_response.discovery()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        tenancy = response.parse()
        assert_matches_type(dict, tenancy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_discovery(self, client: HubClient) -> None:
        with client.tenancy.with_streaming_response.discovery() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            tenancy = response.parse()
            assert_matches_type(dict, tenancy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_health(self, client: HubClient) -> None:
        tenancy = client.tenancy.health()
        assert_matches_type(HealthStatus, tenancy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_health(self, client: HubClient) -> None:
        response = client.tenancy.with_raw_response.health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        tenancy = response.parse()
        assert_matches_type(HealthStatus, tenancy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_health(self, client: HubClient) -> None:
        with client.tenancy.with_streaming_response.health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            tenancy = response.parse()
            assert_matches_type(HealthStatus, tenancy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_find_tenant(self, client: HubClient) -> None:
        tenancy = client.tenancy.find_tenant(
            email="user@example.com",
            turnstile_token="token",
        )
        assert_matches_type(FindTenantResponse, tenancy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_find_tenant(self, client: HubClient) -> None:
        response = client.tenancy.with_raw_response.find_tenant(
            email="user@example.com",
            turnstile_token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        tenancy = response.parse()
        assert_matches_type(FindTenantResponse, tenancy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_find_tenant(self, client: HubClient) -> None:
        with client.tenancy.with_streaming_response.find_tenant(
            email="user@example.com",
            turnstile_token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            tenancy = response.parse()
            assert_matches_type(FindTenantResponse, tenancy, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTenancy:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_discovery(self, async_client: AsyncHubClient) -> None:
        tenancy = await async_client.tenancy.discovery()
        assert_matches_type(dict, tenancy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_discovery(self, async_client: AsyncHubClient) -> None:
        response = await async_client.tenancy.with_raw_response.discovery()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        tenancy = response.parse()
        assert_matches_type(dict, tenancy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_discovery(self, async_client: AsyncHubClient) -> None:
        async with async_client.tenancy.with_streaming_response.discovery() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            tenancy = await response.parse()
            assert_matches_type(dict, tenancy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_health(self, async_client: AsyncHubClient) -> None:
        tenancy = await async_client.tenancy.health()
        assert_matches_type(HealthStatus, tenancy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_health(self, async_client: AsyncHubClient) -> None:
        response = await async_client.tenancy.with_raw_response.health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        tenancy = response.parse()
        assert_matches_type(HealthStatus, tenancy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_health(self, async_client: AsyncHubClient) -> None:
        async with async_client.tenancy.with_streaming_response.health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            tenancy = await response.parse()
            assert_matches_type(HealthStatus, tenancy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_find_tenant(self, async_client: AsyncHubClient) -> None:
        tenancy = await async_client.tenancy.find_tenant(
            email="user@example.com",
            turnstile_token="token",
        )
        assert_matches_type(FindTenantResponse, tenancy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_find_tenant(self, async_client: AsyncHubClient) -> None:
        response = await async_client.tenancy.with_raw_response.find_tenant(
            email="user@example.com",
            turnstile_token="token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        tenancy = response.parse()
        assert_matches_type(FindTenantResponse, tenancy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_find_tenant(self, async_client: AsyncHubClient) -> None:
        async with async_client.tenancy.with_streaming_response.find_tenant(
            email="user@example.com",
            turnstile_token="token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            tenancy = await response.parse()
            assert_matches_type(FindTenantResponse, tenancy, path=["response"])

        assert cast(Any, response.is_closed) is True
