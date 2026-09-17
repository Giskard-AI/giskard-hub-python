# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from giskard_hub import HubClient, AsyncHubClient
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_login(self, client: HubClient) -> None:
        auth = client.auth.login()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_login_with_all_params(self, client: HubClient) -> None:
        auth = client.auth.login(
            login_hint="string",
            return_to="string",
        )
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_login(self, client: HubClient) -> None:
        response = client.auth.with_raw_response.login()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        auth = response.parse()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_login(self, client: HubClient) -> None:
        with client.auth.with_streaming_response.login() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            auth = response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_callback(self, client: HubClient) -> None:
        auth = client.auth.callback()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_callback_with_all_params(self, client: HubClient) -> None:
        auth = client.auth.callback(
            code="string",
            error="string",
            state="string",
        )
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_callback(self, client: HubClient) -> None:
        response = client.auth.with_raw_response.callback()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        auth = response.parse()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_callback(self, client: HubClient) -> None:
        with client.auth.with_streaming_response.callback() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            auth = response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_logout(self, client: HubClient) -> None:
        auth = client.auth.logout()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_logout(self, client: HubClient) -> None:
        response = client.auth.with_raw_response.logout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        auth = response.parse()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_logout(self, client: HubClient) -> None:
        with client.auth.with_streaming_response.logout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            auth = response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_keepalive(self, client: HubClient) -> None:
        auth = client.auth.keepalive()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_keepalive(self, client: HubClient) -> None:
        response = client.auth.with_raw_response.keepalive()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        auth = response.parse()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_keepalive(self, client: HubClient) -> None:
        with client.auth.with_streaming_response.keepalive() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            auth = response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_login(self, async_client: AsyncHubClient) -> None:
        auth = await async_client.auth.login()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_login_with_all_params(self, async_client: AsyncHubClient) -> None:
        auth = await async_client.auth.login(
            login_hint="string",
            return_to="string",
        )
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_login(self, async_client: AsyncHubClient) -> None:
        response = await async_client.auth.with_raw_response.login()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_login(self, async_client: AsyncHubClient) -> None:
        async with async_client.auth.with_streaming_response.login() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_callback(self, async_client: AsyncHubClient) -> None:
        auth = await async_client.auth.callback()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_callback_with_all_params(self, async_client: AsyncHubClient) -> None:
        auth = await async_client.auth.callback(
            code="string",
            error="string",
            state="string",
        )
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_callback(self, async_client: AsyncHubClient) -> None:
        response = await async_client.auth.with_raw_response.callback()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_callback(self, async_client: AsyncHubClient) -> None:
        async with async_client.auth.with_streaming_response.callback() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_logout(self, async_client: AsyncHubClient) -> None:
        auth = await async_client.auth.logout()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_logout(self, async_client: AsyncHubClient) -> None:
        response = await async_client.auth.with_raw_response.logout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_logout(self, async_client: AsyncHubClient) -> None:
        async with async_client.auth.with_streaming_response.logout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_keepalive(self, async_client: AsyncHubClient) -> None:
        auth = await async_client.auth.keepalive()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_keepalive(self, async_client: AsyncHubClient) -> None:
        response = await async_client.auth.with_raw_response.keepalive()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(object, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_keepalive(self, async_client: AsyncHubClient) -> None:
        async with async_client.auth.with_streaming_response.keepalive() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(object, auth, path=["response"])

        assert cast(Any, response.is_closed) is True
