# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from giskard_hub import HubClient, AsyncHubClient
from tests.utils import assert_matches_type
from giskard_hub.types import (
    APIResponseNone,
    APIResponseKnowledgeBase,
    KnowledgeBaseListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowledgeBases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubClient) -> None:
        knowledge_base = client.knowledge_bases.create(
            data={
                "name": "name",
                "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            file=b"raw file contents",
        )
        assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubClient) -> None:
        knowledge_base = client.knowledge_bases.create(
            data={
                "name": "name",
                "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "description": "description",
                "document_column": "document_column",
                "topic_column": "topic_column",
            },
            file=b"raw file contents",
        )
        assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubClient) -> None:
        response = client.knowledge_bases.with_raw_response.create(
            data={
                "name": "name",
                "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubClient) -> None:
        with client.knowledge_bases.with_streaming_response.create(
            data={
                "name": "name",
                "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: HubClient) -> None:
        knowledge_base = client.knowledge_bases.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: HubClient) -> None:
        response = client.knowledge_bases.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: HubClient) -> None:
        with client.knowledge_bases.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `knowledge_base_id` but received ''",
        ):
            client.knowledge_bases.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubClient) -> None:
        knowledge_base = client.knowledge_bases.update(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubClient) -> None:
        knowledge_base = client.knowledge_bases.update(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status={
                "total": 0,
                "current": 0,
                "error": "error",
                "state": "skipped",
            },
        )
        assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubClient) -> None:
        response = client.knowledge_bases.with_raw_response.update(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubClient) -> None:
        with client.knowledge_bases.with_streaming_response.update(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `knowledge_base_id` but received ''",
        ):
            client.knowledge_bases.with_raw_response.update(
                knowledge_base_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubClient) -> None:
        knowledge_base = client.knowledge_bases.list()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubClient) -> None:
        knowledge_base = client.knowledge_bases.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubClient) -> None:
        response = client.knowledge_bases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubClient) -> None:
        with client.knowledge_bases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubClient) -> None:
        knowledge_base = client.knowledge_bases.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseNone, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubClient) -> None:
        response = client.knowledge_bases.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(APIResponseNone, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubClient) -> None:
        with client.knowledge_bases.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(APIResponseNone, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `knowledge_base_id` but received ''",
        ):
            client.knowledge_bases.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bulk_delete(self, client: HubClient) -> None:
        knowledge_base = client.knowledge_bases.bulk_delete(
            knowledge_base_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(APIResponseNone, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_bulk_delete(self, client: HubClient) -> None:
        response = client.knowledge_bases.with_raw_response.bulk_delete(
            knowledge_base_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(APIResponseNone, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_bulk_delete(self, client: HubClient) -> None:
        with client.knowledge_bases.with_streaming_response.bulk_delete(
            knowledge_base_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(APIResponseNone, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKnowledgeBases:
    parametrize = pytest.mark.parametrize(
        "async_client",
        [False, True, {"http_client": "aiohttp"}],
        indirect=True,
        ids=["loose", "strict", "aiohttp"],
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubClient) -> None:
        knowledge_base = await async_client.knowledge_bases.create(
            data={
                "name": "name",
                "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            file=b"raw file contents",
        )
        assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubClient) -> None:
        knowledge_base = await async_client.knowledge_bases.create(
            data={
                "name": "name",
                "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "description": "description",
                "document_column": "document_column",
                "topic_column": "topic_column",
            },
            file=b"raw file contents",
        )
        assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubClient) -> None:
        response = await async_client.knowledge_bases.with_raw_response.create(
            data={
                "name": "name",
                "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubClient) -> None:
        async with async_client.knowledge_bases.with_streaming_response.create(
            data={
                "name": "name",
                "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHubClient) -> None:
        knowledge_base = await async_client.knowledge_bases.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHubClient) -> None:
        response = await async_client.knowledge_bases.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHubClient) -> None:
        async with async_client.knowledge_bases.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `knowledge_base_id` but received ''",
        ):
            await async_client.knowledge_bases.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubClient) -> None:
        knowledge_base = await async_client.knowledge_bases.update(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubClient) -> None:
        knowledge_base = await async_client.knowledge_bases.update(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status={
                "total": 0,
                "current": 0,
                "error": "error",
                "state": "skipped",
            },
        )
        assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubClient) -> None:
        response = await async_client.knowledge_bases.with_raw_response.update(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubClient) -> None:
        async with async_client.knowledge_bases.with_streaming_response.update(
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(APIResponseKnowledgeBase, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `knowledge_base_id` but received ''",
        ):
            await async_client.knowledge_bases.with_raw_response.update(
                knowledge_base_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubClient) -> None:
        knowledge_base = await async_client.knowledge_bases.list()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubClient) -> None:
        knowledge_base = await async_client.knowledge_bases.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubClient) -> None:
        response = await async_client.knowledge_bases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubClient) -> None:
        async with async_client.knowledge_bases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubClient) -> None:
        knowledge_base = await async_client.knowledge_bases.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseNone, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubClient) -> None:
        response = await async_client.knowledge_bases.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(APIResponseNone, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubClient) -> None:
        async with async_client.knowledge_bases.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(APIResponseNone, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `knowledge_base_id` but received ''",
        ):
            await async_client.knowledge_bases.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncHubClient) -> None:
        knowledge_base = await async_client.knowledge_bases.bulk_delete(
            knowledge_base_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(APIResponseNone, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncHubClient) -> None:
        response = await async_client.knowledge_bases.with_raw_response.bulk_delete(
            knowledge_base_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(APIResponseNone, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncHubClient) -> None:
        async with async_client.knowledge_bases.with_streaming_response.bulk_delete(
            knowledge_base_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(APIResponseNone, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True
