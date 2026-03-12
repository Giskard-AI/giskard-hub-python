# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, List, cast

import pytest

from giskard_hub import HubClient, AsyncHubClient
from tests.utils import assert_matches_type
from giskard_hub.types import (
    Agent,
    Dataset,
    Evaluation,
    APIResponse,
    ScheduledEvaluation,
    APIResponseWithIncluded,
)
from giskard_hub._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScheduledEvaluations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubClient) -> None:
        scheduled_evaluation = client.scheduled_evaluations.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            frequency="daily",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time="20:20",
        )
        assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubClient) -> None:
        scheduled_evaluation = client.scheduled_evaluations.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            frequency="daily",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time="20:20",
            day_of_month=1,
            day_of_week=1,
            run_count=1,
            tags=["string"],
        )
        assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubClient) -> None:
        response = client.scheduled_evaluations.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            frequency="daily",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time="20:20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        scheduled_evaluation = response.parse()
        assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubClient) -> None:
        with client.scheduled_evaluations.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            frequency="daily",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time="20:20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            scheduled_evaluation = response.parse()
            assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: HubClient) -> None:
        scheduled_evaluation = client.scheduled_evaluations.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: HubClient) -> None:
        response = client.scheduled_evaluations.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        scheduled_evaluation = response.parse()
        assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: HubClient) -> None:
        with client.scheduled_evaluations.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            scheduled_evaluation = response.parse()
            assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `scheduled_evaluation_id` but received ''",
        ):
            client.scheduled_evaluations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubClient) -> None:
        scheduled_evaluation = client.scheduled_evaluations.update(
            scheduled_evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubClient) -> None:
        scheduled_evaluation = client.scheduled_evaluations.update(
            scheduled_evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            day_of_month=1,
            day_of_week=1,
            frequency="daily",
            last_execution_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_execution_status={
                "evaluation_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "status": "success",
            },
            name="name",
            paused=True,
            run_count=1,
            time="20:20",
        )
        assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubClient) -> None:
        response = client.scheduled_evaluations.with_raw_response.update(
            scheduled_evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        scheduled_evaluation = response.parse()
        assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubClient) -> None:
        with client.scheduled_evaluations.with_streaming_response.update(
            scheduled_evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            scheduled_evaluation = response.parse()
            assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `scheduled_evaluation_id` but received ''",
        ):
            client.scheduled_evaluations.with_raw_response.update(
                scheduled_evaluation_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubClient) -> None:
        scheduled_evaluation = client.scheduled_evaluations.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            APIResponseWithIncluded[List[ScheduledEvaluation], List[APIResponse[Evaluation]]],
            scheduled_evaluation,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubClient) -> None:
        response = client.scheduled_evaluations.with_raw_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        scheduled_evaluation = response.parse()
        assert_matches_type(
            APIResponseWithIncluded[List[ScheduledEvaluation], List[APIResponse[Evaluation]]],
            scheduled_evaluation,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubClient) -> None:
        with client.scheduled_evaluations.with_streaming_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            scheduled_evaluation = response.parse()
            assert_matches_type(
                APIResponseWithIncluded[List[ScheduledEvaluation], List[APIResponse[Evaluation]]],
                scheduled_evaluation,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubClient) -> None:
        scheduled_evaluation = client.scheduled_evaluations.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[None], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubClient) -> None:
        response = client.scheduled_evaluations.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        scheduled_evaluation = response.parse()
        assert_matches_type(APIResponse[None], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubClient) -> None:
        with client.scheduled_evaluations.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            scheduled_evaluation = response.parse()
            assert_matches_type(APIResponse[None], scheduled_evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `scheduled_evaluation_id` but received ''",
        ):
            client.scheduled_evaluations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bulk_delete(self, client: HubClient) -> None:
        scheduled_evaluation = client.scheduled_evaluations.bulk_delete(
            scheduled_evaluation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(APIResponse[None], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_bulk_delete(self, client: HubClient) -> None:
        response = client.scheduled_evaluations.with_raw_response.bulk_delete(
            scheduled_evaluation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        scheduled_evaluation = response.parse()
        assert_matches_type(APIResponse[None], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_bulk_delete(self, client: HubClient) -> None:
        with client.scheduled_evaluations.with_streaming_response.bulk_delete(
            scheduled_evaluation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            scheduled_evaluation = response.parse()
            assert_matches_type(APIResponse[None], scheduled_evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_evaluations(self, client: HubClient) -> None:
        scheduled_evaluation = client.scheduled_evaluations.list_evaluations(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            APIResponseWithIncluded[List[Evaluation], APIResponse[Agent | Dataset]],
            scheduled_evaluation,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_evaluations(self, client: HubClient) -> None:
        response = client.scheduled_evaluations.with_raw_response.list_evaluations(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        scheduled_evaluation = response.parse()
        assert_matches_type(
            APIResponseWithIncluded[List[Evaluation], APIResponse[Agent | Dataset]],
            scheduled_evaluation,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_evaluations(self, client: HubClient) -> None:
        with client.scheduled_evaluations.with_streaming_response.list_evaluations(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            scheduled_evaluation = response.parse()
            assert_matches_type(
                APIResponseWithIncluded[List[Evaluation], APIResponse[Agent | Dataset]],
                scheduled_evaluation,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_evaluations(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `scheduled_evaluation_id` but received ''",
        ):
            client.scheduled_evaluations.with_raw_response.list_evaluations(
                "",
            )


class TestAsyncScheduledEvaluations:
    parametrize = pytest.mark.parametrize(
        "async_client",
        [False, True, {"http_client": "aiohttp"}],
        indirect=True,
        ids=["loose", "strict", "aiohttp"],
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubClient) -> None:
        scheduled_evaluation = await async_client.scheduled_evaluations.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            frequency="daily",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time="20:20",
        )
        assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubClient) -> None:
        scheduled_evaluation = await async_client.scheduled_evaluations.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            frequency="daily",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time="20:20",
            day_of_month=1,
            day_of_week=1,
            run_count=1,
            tags=["string"],
        )
        assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubClient) -> None:
        response = await async_client.scheduled_evaluations.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            frequency="daily",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time="20:20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        scheduled_evaluation = await response.parse()
        assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubClient) -> None:
        async with async_client.scheduled_evaluations.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            frequency="daily",
            name="name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            time="20:20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            scheduled_evaluation = await response.parse()
            assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHubClient) -> None:
        scheduled_evaluation = await async_client.scheduled_evaluations.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHubClient) -> None:
        response = await async_client.scheduled_evaluations.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        scheduled_evaluation = await response.parse()
        assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHubClient) -> None:
        async with async_client.scheduled_evaluations.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            scheduled_evaluation = await response.parse()
            assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `scheduled_evaluation_id` but received ''",
        ):
            await async_client.scheduled_evaluations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubClient) -> None:
        scheduled_evaluation = await async_client.scheduled_evaluations.update(
            scheduled_evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubClient) -> None:
        scheduled_evaluation = await async_client.scheduled_evaluations.update(
            scheduled_evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            day_of_month=1,
            day_of_week=1,
            frequency="daily",
            last_execution_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_execution_status={
                "evaluation_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "status": "success",
            },
            name="name",
            paused=True,
            run_count=1,
            time="20:20",
        )
        assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubClient) -> None:
        response = await async_client.scheduled_evaluations.with_raw_response.update(
            scheduled_evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        scheduled_evaluation = await response.parse()
        assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubClient) -> None:
        async with async_client.scheduled_evaluations.with_streaming_response.update(
            scheduled_evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            scheduled_evaluation = await response.parse()
            assert_matches_type(APIResponse[ScheduledEvaluation], scheduled_evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `scheduled_evaluation_id` but received ''",
        ):
            await async_client.scheduled_evaluations.with_raw_response.update(
                scheduled_evaluation_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubClient) -> None:
        scheduled_evaluation = await async_client.scheduled_evaluations.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            APIResponseWithIncluded[List[ScheduledEvaluation], List[APIResponse[Evaluation]]],
            scheduled_evaluation,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubClient) -> None:
        response = await async_client.scheduled_evaluations.with_raw_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        scheduled_evaluation = await response.parse()
        assert_matches_type(
            APIResponseWithIncluded[List[ScheduledEvaluation], List[APIResponse[Evaluation]]],
            scheduled_evaluation,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubClient) -> None:
        async with async_client.scheduled_evaluations.with_streaming_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            scheduled_evaluation = await response.parse()
            assert_matches_type(
                APIResponseWithIncluded[List[ScheduledEvaluation], List[APIResponse[Evaluation]]],
                scheduled_evaluation,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubClient) -> None:
        scheduled_evaluation = await async_client.scheduled_evaluations.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[None], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubClient) -> None:
        response = await async_client.scheduled_evaluations.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        scheduled_evaluation = await response.parse()
        assert_matches_type(APIResponse[None], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubClient) -> None:
        async with async_client.scheduled_evaluations.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            scheduled_evaluation = await response.parse()
            assert_matches_type(APIResponse[None], scheduled_evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `scheduled_evaluation_id` but received ''",
        ):
            await async_client.scheduled_evaluations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncHubClient) -> None:
        scheduled_evaluation = await async_client.scheduled_evaluations.bulk_delete(
            scheduled_evaluation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(APIResponse[None], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncHubClient) -> None:
        response = await async_client.scheduled_evaluations.with_raw_response.bulk_delete(
            scheduled_evaluation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        scheduled_evaluation = await response.parse()
        assert_matches_type(APIResponse[None], scheduled_evaluation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncHubClient) -> None:
        async with async_client.scheduled_evaluations.with_streaming_response.bulk_delete(
            scheduled_evaluation_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            scheduled_evaluation = await response.parse()
            assert_matches_type(APIResponse[None], scheduled_evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_evaluations(self, async_client: AsyncHubClient) -> None:
        scheduled_evaluation = await async_client.scheduled_evaluations.list_evaluations(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            APIResponseWithIncluded[List[Evaluation], APIResponse[Agent | Dataset]],
            scheduled_evaluation,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_evaluations(self, async_client: AsyncHubClient) -> None:
        response = await async_client.scheduled_evaluations.with_raw_response.list_evaluations(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        scheduled_evaluation = await response.parse()
        assert_matches_type(
            APIResponseWithIncluded[List[Evaluation], APIResponse[Agent | Dataset]],
            scheduled_evaluation,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_evaluations(self, async_client: AsyncHubClient) -> None:
        async with async_client.scheduled_evaluations.with_streaming_response.list_evaluations(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            scheduled_evaluation = await response.parse()
            assert_matches_type(
                APIResponseWithIncluded[List[Evaluation], APIResponse[Agent | Dataset]],
                scheduled_evaluation,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_evaluations(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `scheduled_evaluation_id` but received ''",
        ):
            await async_client.scheduled_evaluations.with_raw_response.list_evaluations(
                "",
            )
