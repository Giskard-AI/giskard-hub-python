# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, List, Union, cast

import pytest

from giskard_hub import HubClient, AsyncHubClient
from tests.utils import assert_matches_type
from giskard_hub.types import (
    Agent,
    Dataset,
    APIResponse,
    CheckAPIResource,
    EvaluationAPIResource,
    APIResponseWithIncluded,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubClient) -> None:
        evaluation = client.evaluations.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubClient) -> None:
        evaluation = client.evaluations.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            criteria={
                "dataset_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "tags": ["string"],
                "target_type": "dataset",
            },
            name="name",
            old_evaluation_id="old_evaluation_id",
            run_count=1,
            scheduled_evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubClient) -> None:
        response = client.evaluations.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubClient) -> None:
        with client.evaluations.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: HubClient) -> None:
        evaluation = client.evaluations.retrieve(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            APIResponseWithIncluded[EvaluationAPIResource, Union[Agent, Dataset]], evaluation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: HubClient) -> None:
        evaluation = client.evaluations.retrieve(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include=["agent"],
        )
        assert_matches_type(
            APIResponseWithIncluded[EvaluationAPIResource, Union[Agent, Dataset]], evaluation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: HubClient) -> None:
        response = client.evaluations.with_raw_response.retrieve(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(
            APIResponseWithIncluded[EvaluationAPIResource, Union[Agent, Dataset]], evaluation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: HubClient) -> None:
        with client.evaluations.with_streaming_response.retrieve(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(
                APIResponseWithIncluded[EvaluationAPIResource, Union[Agent, Dataset]], evaluation, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            client.evaluations.with_raw_response.retrieve(
                evaluation_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubClient) -> None:
        evaluation = client.evaluations.update(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubClient) -> None:
        response = client.evaluations.with_raw_response.update(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubClient) -> None:
        with client.evaluations.with_streaming_response.update(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            client.evaluations.with_raw_response.update(
                evaluation_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubClient) -> None:
        evaluation = client.evaluations.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            APIResponseWithIncluded[List[EvaluationAPIResource], Union[Agent, Dataset]], evaluation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubClient) -> None:
        evaluation = client.evaluations.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include=["agent"],
        )
        assert_matches_type(
            APIResponseWithIncluded[List[EvaluationAPIResource], Union[Agent, Dataset]], evaluation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubClient) -> None:
        response = client.evaluations.with_raw_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(
            APIResponseWithIncluded[List[EvaluationAPIResource], Union[Agent, Dataset]], evaluation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubClient) -> None:
        with client.evaluations.with_streaming_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(
                APIResponseWithIncluded[List[EvaluationAPIResource], Union[Agent, Dataset]],
                evaluation,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubClient) -> None:
        evaluation = client.evaluations.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[None], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubClient) -> None:
        response = client.evaluations.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(APIResponse[None], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubClient) -> None:
        with client.evaluations.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(APIResponse[None], evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            client.evaluations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bulk_delete(self, client: HubClient) -> None:
        evaluation = client.evaluations.bulk_delete(
            evaluation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(APIResponse[None], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_bulk_delete(self, client: HubClient) -> None:
        response = client.evaluations.with_raw_response.bulk_delete(
            evaluation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(APIResponse[None], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_bulk_delete(self, client: HubClient) -> None:
        with client.evaluations.with_streaming_response.bulk_delete(
            evaluation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(APIResponse[None], evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_local(self, client: HubClient) -> None:
        evaluation = client.evaluations.create_local(
            criteria=[{"dataset_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            model={"name": "name"},
        )
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_local_with_all_params(self, client: HubClient) -> None:
        evaluation = client.evaluations.create_local(
            criteria=[
                {
                    "dataset_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "tags": ["string"],
                    "target_type": "dataset",
                }
            ],
            model={
                "name": "name",
                "description": "description",
            },
            name="name",
        )
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_local(self, client: HubClient) -> None:
        response = client.evaluations.with_raw_response.create_local(
            criteria=[{"dataset_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            model={"name": "name"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_local(self, client: HubClient) -> None:
        with client.evaluations.with_streaming_response.create_local(
            criteria=[{"dataset_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            model={"name": "name"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_rerun_errored_results(self, client: HubClient) -> None:
        evaluation = client.evaluations.rerun_errored_results(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_rerun_errored_results(self, client: HubClient) -> None:
        response = client.evaluations.with_raw_response.rerun_errored_results(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_rerun_errored_results(self, client: HubClient) -> None:
        with client.evaluations.with_streaming_response.rerun_errored_results(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_rerun_errored_results(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            client.evaluations.with_raw_response.rerun_errored_results(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_single(self, client: HubClient) -> None:
        evaluation = client.evaluations.run_single(
            checks=[{"foo": "bar"}],
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            model_output={
                "response": {
                    "content": "content",
                    "role": "role",
                }
            },
        )
        assert_matches_type(APIResponse[List[CheckAPIResource]], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_single_with_all_params(self, client: HubClient) -> None:
        evaluation = client.evaluations.run_single(
            checks=[{"foo": "bar"}],
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            model_output={
                "response": {
                    "content": "content",
                    "role": "role",
                },
                "error": {
                    "message": "message",
                    "details": {"foo": "bar"},
                },
                "metadata": {"foo": "bar"},
            },
            model_description="model_description",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[List[CheckAPIResource]], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_single(self, client: HubClient) -> None:
        response = client.evaluations.with_raw_response.run_single(
            checks=[{"foo": "bar"}],
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            model_output={
                "response": {
                    "content": "content",
                    "role": "role",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(APIResponse[List[CheckAPIResource]], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_single(self, client: HubClient) -> None:
        with client.evaluations.with_streaming_response.run_single(
            checks=[{"foo": "bar"}],
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            model_output={
                "response": {
                    "content": "content",
                    "role": "role",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(APIResponse[List[CheckAPIResource]], evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvaluations:
    parametrize = pytest.mark.parametrize(
        "async_client",
        [False, True, {"http_client": "aiohttp"}],
        indirect=True,
        ids=["loose", "strict", "aiohttp"],
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubClient) -> None:
        evaluation = await async_client.evaluations.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubClient) -> None:
        evaluation = await async_client.evaluations.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            criteria={
                "dataset_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "tags": ["string"],
                "target_type": "dataset",
            },
            name="name",
            old_evaluation_id="old_evaluation_id",
            run_count=1,
            scheduled_evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubClient) -> None:
        response = await async_client.evaluations.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubClient) -> None:
        async with async_client.evaluations.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHubClient) -> None:
        evaluation = await async_client.evaluations.retrieve(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            APIResponseWithIncluded[EvaluationAPIResource, Union[Agent, Dataset]], evaluation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncHubClient) -> None:
        evaluation = await async_client.evaluations.retrieve(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include=["agent"],
        )
        assert_matches_type(
            APIResponseWithIncluded[EvaluationAPIResource, Union[Agent, Dataset]], evaluation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHubClient) -> None:
        response = await async_client.evaluations.with_raw_response.retrieve(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(
            APIResponseWithIncluded[EvaluationAPIResource, Union[Agent, Dataset]], evaluation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHubClient) -> None:
        async with async_client.evaluations.with_streaming_response.retrieve(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(
                APIResponseWithIncluded[EvaluationAPIResource, Union[Agent, Dataset]], evaluation, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            await async_client.evaluations.with_raw_response.retrieve(
                evaluation_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubClient) -> None:
        evaluation = await async_client.evaluations.update(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubClient) -> None:
        response = await async_client.evaluations.with_raw_response.update(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubClient) -> None:
        async with async_client.evaluations.with_streaming_response.update(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            await async_client.evaluations.with_raw_response.update(
                evaluation_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubClient) -> None:
        evaluation = await async_client.evaluations.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            APIResponseWithIncluded[List[EvaluationAPIResource], Union[Agent, Dataset]], evaluation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubClient) -> None:
        evaluation = await async_client.evaluations.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include=["agent"],
        )
        assert_matches_type(
            APIResponseWithIncluded[List[EvaluationAPIResource], Union[Agent, Dataset]], evaluation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubClient) -> None:
        response = await async_client.evaluations.with_raw_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(
            APIResponseWithIncluded[List[EvaluationAPIResource], Union[Agent, Dataset]], evaluation, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubClient) -> None:
        async with async_client.evaluations.with_streaming_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(
                APIResponseWithIncluded[List[EvaluationAPIResource], Union[Agent, Dataset]],
                evaluation,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubClient) -> None:
        evaluation = await async_client.evaluations.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[None], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubClient) -> None:
        response = await async_client.evaluations.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(APIResponse[None], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubClient) -> None:
        async with async_client.evaluations.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(APIResponse[None], evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            await async_client.evaluations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncHubClient) -> None:
        evaluation = await async_client.evaluations.bulk_delete(
            evaluation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(APIResponse[None], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncHubClient) -> None:
        response = await async_client.evaluations.with_raw_response.bulk_delete(
            evaluation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(APIResponse[None], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncHubClient) -> None:
        async with async_client.evaluations.with_streaming_response.bulk_delete(
            evaluation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(APIResponse[None], evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_local(self, async_client: AsyncHubClient) -> None:
        evaluation = await async_client.evaluations.create_local(
            criteria=[{"dataset_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            model={"name": "name"},
        )
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_local_with_all_params(self, async_client: AsyncHubClient) -> None:
        evaluation = await async_client.evaluations.create_local(
            criteria=[
                {
                    "dataset_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "tags": ["string"],
                    "target_type": "dataset",
                }
            ],
            model={
                "name": "name",
                "description": "description",
            },
            name="name",
        )
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_local(self, async_client: AsyncHubClient) -> None:
        response = await async_client.evaluations.with_raw_response.create_local(
            criteria=[{"dataset_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            model={"name": "name"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_local(self, async_client: AsyncHubClient) -> None:
        async with async_client.evaluations.with_streaming_response.create_local(
            criteria=[{"dataset_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}],
            model={"name": "name"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_rerun_errored_results(self, async_client: AsyncHubClient) -> None:
        evaluation = await async_client.evaluations.rerun_errored_results(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_rerun_errored_results(self, async_client: AsyncHubClient) -> None:
        response = await async_client.evaluations.with_raw_response.rerun_errored_results(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_rerun_errored_results(self, async_client: AsyncHubClient) -> None:
        async with async_client.evaluations.with_streaming_response.rerun_errored_results(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(APIResponse[EvaluationAPIResource], evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_rerun_errored_results(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            await async_client.evaluations.with_raw_response.rerun_errored_results(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_single(self, async_client: AsyncHubClient) -> None:
        evaluation = await async_client.evaluations.run_single(
            checks=[{"foo": "bar"}],
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            model_output={
                "response": {
                    "content": "content",
                    "role": "role",
                }
            },
        )
        assert_matches_type(APIResponse[List[CheckAPIResource]], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_single_with_all_params(self, async_client: AsyncHubClient) -> None:
        evaluation = await async_client.evaluations.run_single(
            checks=[{"foo": "bar"}],
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            model_output={
                "response": {
                    "content": "content",
                    "role": "role",
                },
                "error": {
                    "message": "message",
                    "details": {"foo": "bar"},
                },
                "metadata": {"foo": "bar"},
            },
            model_description="model_description",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[List[CheckAPIResource]], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_single(self, async_client: AsyncHubClient) -> None:
        response = await async_client.evaluations.with_raw_response.run_single(
            checks=[{"foo": "bar"}],
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            model_output={
                "response": {
                    "content": "content",
                    "role": "role",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(APIResponse[List[CheckAPIResource]], evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_single(self, async_client: AsyncHubClient) -> None:
        async with async_client.evaluations.with_streaming_response.run_single(
            checks=[{"foo": "bar"}],
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            model_output={
                "response": {
                    "content": "content",
                    "role": "role",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(APIResponse[List[CheckAPIResource]], evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True
