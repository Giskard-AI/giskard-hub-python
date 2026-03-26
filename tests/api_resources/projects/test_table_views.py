from __future__ import annotations

import os
from typing import Any, List, cast

import pytest

from giskard_hub import HubClient, AsyncHubClient
from tests.utils import assert_matches_type
from giskard_hub.types import TableView

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTableViews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubClient) -> None:
        table_view = client.projects.table_views.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="test_cases",
            name="My View",
            settings={"columns": ["name", "status"]},
        )
        assert_matches_type(TableView, table_view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubClient) -> None:
        response = client.projects.table_views.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="test_cases",
            name="My View",
            settings={"columns": ["name", "status"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        table_view = response.parse()
        assert_matches_type(TableView, table_view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubClient) -> None:
        with client.projects.table_views.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="test_cases",
            name="My View",
            settings={"columns": ["name", "status"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            table_view = response.parse()
            assert_matches_type(TableView, table_view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubClient) -> None:
        table_view = client.projects.table_views.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="test_cases",
        )
        assert_matches_type(list[TableView], table_view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubClient) -> None:
        response = client.projects.table_views.with_raw_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="test_cases",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        table_view = response.parse()
        assert_matches_type(list[TableView], table_view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubClient) -> None:
        with client.projects.table_views.with_streaming_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="test_cases",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            table_view = response.parse()
            assert_matches_type(list[TableView], table_view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubClient) -> None:
        table_view = client.projects.table_views.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TableView, table_view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubClient) -> None:
        table_view = client.projects.table_views.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="Updated View",
            settings={"columns": ["name", "status", "priority"]},
        )
        assert_matches_type(TableView, table_view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubClient) -> None:
        response = client.projects.table_views.with_raw_response.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        table_view = response.parse()
        assert_matches_type(TableView, table_view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubClient) -> None:
        with client.projects.table_views.with_streaming_response.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            table_view = response.parse()
            assert_matches_type(TableView, table_view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubClient) -> None:
        table_view = client.projects.table_views.delete(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert table_view is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubClient) -> None:
        response = client.projects.table_views.with_raw_response.delete(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        table_view = response.parse()
        assert table_view is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubClient) -> None:
        with client.projects.table_views.with_streaming_response.delete(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            table_view = response.parse()
            assert table_view is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTableViews:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubClient) -> None:
        table_view = await async_client.projects.table_views.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="test_cases",
            name="My View",
            settings={"columns": ["name", "status"]},
        )
        assert_matches_type(TableView, table_view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubClient) -> None:
        response = await async_client.projects.table_views.with_raw_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="test_cases",
            name="My View",
            settings={"columns": ["name", "status"]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        table_view = await response.parse()
        assert_matches_type(TableView, table_view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubClient) -> None:
        async with async_client.projects.table_views.with_streaming_response.create(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="test_cases",
            name="My View",
            settings={"columns": ["name", "status"]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            table_view = await response.parse()
            assert_matches_type(TableView, table_view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubClient) -> None:
        table_view = await async_client.projects.table_views.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="test_cases",
        )
        assert_matches_type(list[TableView], table_view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubClient) -> None:
        response = await async_client.projects.table_views.with_raw_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="test_cases",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        table_view = await response.parse()
        assert_matches_type(list[TableView], table_view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubClient) -> None:
        async with async_client.projects.table_views.with_streaming_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_type="test_cases",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            table_view = await response.parse()
            assert_matches_type(list[TableView], table_view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubClient) -> None:
        table_view = await async_client.projects.table_views.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TableView, table_view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubClient) -> None:
        table_view = await async_client.projects.table_views.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="Updated View",
            settings={"columns": ["name", "status", "priority"]},
        )
        assert_matches_type(TableView, table_view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubClient) -> None:
        response = await async_client.projects.table_views.with_raw_response.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        table_view = await response.parse()
        assert_matches_type(TableView, table_view, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubClient) -> None:
        async with async_client.projects.table_views.with_streaming_response.update(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            table_view = await response.parse()
            assert_matches_type(TableView, table_view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubClient) -> None:
        table_view = await async_client.projects.table_views.delete(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert table_view is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubClient) -> None:
        response = await async_client.projects.table_views.with_raw_response.delete(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        table_view = await response.parse()
        assert table_view is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubClient) -> None:
        async with async_client.projects.table_views.with_streaming_response.delete(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            table_view = await response.parse()
            assert table_view is None

        assert cast(Any, response.is_closed) is True
