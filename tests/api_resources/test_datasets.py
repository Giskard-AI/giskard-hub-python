# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, List, cast

import pytest

from giskard_hub import HubClient, AsyncHubClient
from tests.utils import assert_matches_type
from giskard_hub.types import (
    Dataset,
    TestCase,
    APIResponse,
    APIPaginatedResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubClient) -> None:
        dataset = client.datasets.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubClient) -> None:
        dataset = client.datasets.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
        )
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubClient) -> None:
        response = client.datasets.with_raw_response.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubClient) -> None:
        with client.datasets.with_streaming_response.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: HubClient) -> None:
        dataset = client.datasets.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: HubClient) -> None:
        response = client.datasets.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: HubClient) -> None:
        with client.datasets.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `dataset_id` but received ''",
        ):
            client.datasets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubClient) -> None:
        dataset = client.datasets.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubClient) -> None:
        dataset = client.datasets.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            name="name",
            status={
                "total": 0,
                "current": 0,
                "error": "error",
                "state": "skipped",
            },
        )
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubClient) -> None:
        response = client.datasets.with_raw_response.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubClient) -> None:
        with client.datasets.with_streaming_response.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `dataset_id` but received ''",
        ):
            client.datasets.with_raw_response.update(
                dataset_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubClient) -> None:
        dataset = client.datasets.list()
        assert_matches_type(APIResponse[List[Dataset]], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubClient) -> None:
        dataset = client.datasets.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[List[Dataset]], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubClient) -> None:
        response = client.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(APIResponse[List[Dataset]], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubClient) -> None:
        with client.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(APIResponse[List[Dataset]], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubClient) -> None:
        dataset = client.datasets.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[None], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubClient) -> None:
        response = client.datasets.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(APIResponse[None], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubClient) -> None:
        with client.datasets.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(APIResponse[None], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `dataset_id` but received ''",
        ):
            client.datasets.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bulk_delete(self, client: HubClient) -> None:
        dataset = client.datasets.bulk_delete(
            dataset_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(APIResponse[None], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_bulk_delete(self, client: HubClient) -> None:
        response = client.datasets.with_raw_response.bulk_delete(
            dataset_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(APIResponse[None], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_bulk_delete(self, client: HubClient) -> None:
        with client.datasets.with_streaming_response.bulk_delete(
            dataset_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(APIResponse[None], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_scenario_based(self, client: HubClient) -> None:
        dataset = client.datasets.generate_scenario_based(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            scenario_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_scenario_based_with_all_params(self, client: HubClient) -> None:
        dataset = client.datasets.generate_scenario_based(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            scenario_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            n_examples=10,
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
        )
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_generate_scenario_based(self, client: HubClient) -> None:
        response = client.datasets.with_raw_response.generate_scenario_based(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            scenario_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_generate_scenario_based(self, client: HubClient) -> None:
        with client.datasets.with_streaming_response.generate_scenario_based(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            scenario_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_document_based(self, client: HubClient) -> None:
        dataset = client.datasets.generate_document_based(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_generate_document_based_with_all_params(self, client: HubClient) -> None:
        dataset = client.datasets.generate_document_based(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            description="description",
            n_examples=0,
            topic_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_generate_document_based(self, client: HubClient) -> None:
        response = client.datasets.with_raw_response.generate_document_based(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_generate_document_based(self, client: HubClient) -> None:
        with client.datasets.with_streaming_response.generate_document_based(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_tags(self, client: HubClient) -> None:
        dataset = client.datasets.list_tags(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[List[str]], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_tags(self, client: HubClient) -> None:
        response = client.datasets.with_raw_response.list_tags(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(APIResponse[List[str]], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_tags(self, client: HubClient) -> None:
        with client.datasets.with_streaming_response.list_tags(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(APIResponse[List[str]], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_tags(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `dataset_id` but received ''",
        ):
            client.datasets.with_raw_response.list_tags(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_test_cases(self, client: HubClient) -> None:
        dataset = client.datasets.list_test_cases(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[List[TestCase]], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_test_cases(self, client: HubClient) -> None:
        response = client.datasets.with_raw_response.list_test_cases(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(APIResponse[List[TestCase]], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_test_cases(self, client: HubClient) -> None:
        with client.datasets.with_streaming_response.list_test_cases(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(APIResponse[List[TestCase]], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_test_cases(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `dataset_id` but received ''",
        ):
            client.datasets.with_raw_response.list_test_cases(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_test_cases(self, client: HubClient) -> None:
        result = client.datasets.search_test_cases(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIPaginatedResponse[TestCase, None], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_test_cases_with_all_params(self, client: HubClient) -> None:
        result = client.datasets.search_test_cases(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filters={
                "status": {
                    "selected_options": ["active", "draft"],
                    "match_logic": "any",
                },
                "tags": {
                    "selected_options": ["tag1", "tag2"],
                    "match_logic": "any",
                },
                "checks": {
                    "selected_options": ["check1", "check2"],
                    "match_logic": "any",
                },
            },
            order_by=[
                {
                    "field": "created_at",
                    "order": "desc",
                }
            ],
            limit=10,
            offset=0,
        )
        assert_matches_type(APIPaginatedResponse[TestCase, None], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search_test_cases(self, client: HubClient) -> None:
        response = client.datasets.with_raw_response.search_test_cases(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        result = response.parse()
        assert_matches_type(APIPaginatedResponse[TestCase, None], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search_test_cases(self, client: HubClient) -> None:
        with client.datasets.with_streaming_response.search_test_cases(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            result = response.parse()
            assert_matches_type(APIPaginatedResponse[TestCase, None], result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_search_test_cases(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `dataset_id` but received ''",
        ):
            client.datasets.with_raw_response.search_test_cases(
                "",
            )


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize(
        "async_client",
        [False, True, {"http_client": "aiohttp"}],
        indirect=True,
        ids=["loose", "strict", "aiohttp"],
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubClient) -> None:
        dataset = await async_client.datasets.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubClient) -> None:
        dataset = await async_client.datasets.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
        )
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubClient) -> None:
        response = await async_client.datasets.with_raw_response.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubClient) -> None:
        async with async_client.datasets.with_streaming_response.create(
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHubClient) -> None:
        dataset = await async_client.datasets.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHubClient) -> None:
        response = await async_client.datasets.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHubClient) -> None:
        async with async_client.datasets.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `dataset_id` but received ''",
        ):
            await async_client.datasets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubClient) -> None:
        dataset = await async_client.datasets.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubClient) -> None:
        dataset = await async_client.datasets.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            name="name",
            status={
                "total": 0,
                "current": 0,
                "error": "error",
                "state": "skipped",
            },
        )
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubClient) -> None:
        response = await async_client.datasets.with_raw_response.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubClient) -> None:
        async with async_client.datasets.with_streaming_response.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `dataset_id` but received ''",
        ):
            await async_client.datasets.with_raw_response.update(
                dataset_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubClient) -> None:
        dataset = await async_client.datasets.list()
        assert_matches_type(APIResponse[List[Dataset]], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubClient) -> None:
        dataset = await async_client.datasets.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[List[Dataset]], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubClient) -> None:
        response = await async_client.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(APIResponse[List[Dataset]], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubClient) -> None:
        async with async_client.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(APIResponse[List[Dataset]], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubClient) -> None:
        dataset = await async_client.datasets.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[None], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubClient) -> None:
        response = await async_client.datasets.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(APIResponse[None], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubClient) -> None:
        async with async_client.datasets.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(APIResponse[None], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `dataset_id` but received ''",
        ):
            await async_client.datasets.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncHubClient) -> None:
        dataset = await async_client.datasets.bulk_delete(
            dataset_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(APIResponse[None], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncHubClient) -> None:
        response = await async_client.datasets.with_raw_response.bulk_delete(
            dataset_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(APIResponse[None], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncHubClient) -> None:
        async with async_client.datasets.with_streaming_response.bulk_delete(
            dataset_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(APIResponse[None], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_scenario_based(self, async_client: AsyncHubClient) -> None:
        dataset = await async_client.datasets.generate_scenario_based(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            scenario_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_scenario_based_with_all_params(self, async_client: AsyncHubClient) -> None:
        dataset = await async_client.datasets.generate_scenario_based(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            scenario_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            n_examples=10,
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
        )
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_generate_scenario_based(self, async_client: AsyncHubClient) -> None:
        response = await async_client.datasets.with_raw_response.generate_scenario_based(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            scenario_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_generate_scenario_based(self, async_client: AsyncHubClient) -> None:
        async with async_client.datasets.with_streaming_response.generate_scenario_based(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            scenario_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_document_based(self, async_client: AsyncHubClient) -> None:
        dataset = await async_client.datasets.generate_document_based(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_generate_document_based_with_all_params(self, async_client: AsyncHubClient) -> None:
        dataset = await async_client.datasets.generate_document_based(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_name="dataset_name",
            description="description",
            n_examples=0,
            topic_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_generate_document_based(self, async_client: AsyncHubClient) -> None:
        response = await async_client.datasets.with_raw_response.generate_document_based(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_generate_document_based(self, async_client: AsyncHubClient) -> None:
        async with async_client.datasets.with_streaming_response.generate_document_based(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            knowledge_base_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(APIResponse[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_tags(self, async_client: AsyncHubClient) -> None:
        dataset = await async_client.datasets.list_tags(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[List[str]], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_tags(self, async_client: AsyncHubClient) -> None:
        response = await async_client.datasets.with_raw_response.list_tags(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(APIResponse[List[str]], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_tags(self, async_client: AsyncHubClient) -> None:
        async with async_client.datasets.with_streaming_response.list_tags(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(APIResponse[List[str]], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_tags(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `dataset_id` but received ''",
        ):
            await async_client.datasets.with_raw_response.list_tags(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_test_cases(self, async_client: AsyncHubClient) -> None:
        dataset = await async_client.datasets.list_test_cases(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[List[TestCase]], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_test_cases(self, async_client: AsyncHubClient) -> None:
        response = await async_client.datasets.with_raw_response.list_test_cases(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(APIResponse[List[TestCase]], dataset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_test_cases(self, async_client: AsyncHubClient) -> None:
        async with async_client.datasets.with_streaming_response.list_test_cases(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(APIResponse[List[TestCase]], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_test_cases(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `dataset_id` but received ''",
        ):
            await async_client.datasets.with_raw_response.list_test_cases(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_test_cases(self, async_client: AsyncHubClient) -> None:
        result = await async_client.datasets.search_test_cases(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIPaginatedResponse[TestCase, None], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_test_cases_with_all_params(self, async_client: AsyncHubClient) -> None:
        result = await async_client.datasets.search_test_cases(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filters={
                "status": {
                    "selected_options": ["active", "draft"],
                    "match_logic": "any",
                },
                "tags": {
                    "selected_options": ["tag1", "tag2"],
                    "match_logic": "any",
                },
                "checks": {
                    "selected_options": ["check1", "check2"],
                    "match_logic": "any",
                },
            },
            order_by=[
                {
                    "field": "created_at",
                    "order": "desc",
                }
            ],
            limit=10,
            offset=0,
        )
        assert_matches_type(APIPaginatedResponse[TestCase, None], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search_test_cases(self, async_client: AsyncHubClient) -> None:
        response = await async_client.datasets.with_raw_response.search_test_cases(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        result = await response.parse()
        assert_matches_type(APIPaginatedResponse[TestCase, None], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search_test_cases(self, async_client: AsyncHubClient) -> None:
        async with async_client.datasets.with_streaming_response.search_test_cases(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            result = await response.parse()
            assert_matches_type(APIPaginatedResponse[TestCase, None], result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_search_test_cases(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `dataset_id` but received ''",
        ):
            await async_client.datasets.with_raw_response.search_test_cases(
                "",
            )
