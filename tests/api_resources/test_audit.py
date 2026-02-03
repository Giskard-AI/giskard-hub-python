# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from giskard_hub import HubClient, AsyncHubClient
from tests.utils import assert_matches_type
from giskard_hub.types import (
    APIResponseAudit,
    APIResponseAuditDisplay,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAudit:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: HubClient) -> None:
        audit = client.audit.search()
        assert_matches_type(APIResponseAudit, audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: HubClient) -> None:
        audit = client.audit.search(
            filters={"action": "created"},
            limit=10,
            offset=0,
        )
        assert_matches_type(APIResponseAudit, audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: HubClient) -> None:
        response = client.audit.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        audit = response.parse()
        assert_matches_type(APIResponseAudit, audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: HubClient) -> None:
        with client.audit.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            audit = response.parse()
            assert_matches_type(APIResponseAudit, audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_entities(self, client: HubClient) -> None:
        audit = client.audit.list_entities(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="project",
        )
        assert_matches_type(APIResponseAuditDisplay, audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_entities_with_all_params(self, client: HubClient) -> None:
        audit = client.audit.list_entities(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="project",
            limit=10,
            offset=0,
        )
        assert_matches_type(APIResponseAuditDisplay, audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_entities(self, client: HubClient) -> None:
        response = client.audit.with_raw_response.list_entities(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        audit = response.parse()
        assert_matches_type(APIResponseAuditDisplay, audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_entities(self, client: HubClient) -> None:
        with client.audit.with_streaming_response.list_entities(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            audit = response.parse()
            assert_matches_type(APIResponseAuditDisplay, audit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAudit:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHubClient) -> None:
        audit = await async_client.audit.search()
        assert_matches_type(APIResponseAudit, audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHubClient) -> None:
        audit = await async_client.audit.search(
            filters={"action": "created"},
            limit=10,
            offset=0,
        )
        assert_matches_type(APIResponseAudit, audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHubClient) -> None:
        response = await async_client.audit.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        audit = await response.parse()
        assert_matches_type(APIResponseAudit, audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHubClient) -> None:
        async with async_client.audit.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            audit = await response.parse()
            assert_matches_type(APIResponseAudit, audit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_entities(self, async_client: AsyncHubClient) -> None:
        audit = await async_client.audit.list_entities(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="project",
        )
        assert_matches_type(APIResponseAuditDisplay, audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_entities_with_all_params(self, async_client: AsyncHubClient) -> None:
        audit = await async_client.audit.list_entities(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="project",
            limit=10,
            offset=0,
        )
        assert_matches_type(APIResponseAuditDisplay, audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_entities(self, async_client: AsyncHubClient) -> None:
        response = await async_client.audit.with_raw_response.list_entities(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        audit = await response.parse()
        assert_matches_type(APIResponseAuditDisplay, audit, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_entities(self, async_client: AsyncHubClient) -> None:
        async with async_client.audit.with_streaming_response.list_entities(
            entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            audit = await response.parse()
            assert_matches_type(APIResponseAuditDisplay, audit, path=["response"])

        assert cast(Any, response.is_closed) is True
