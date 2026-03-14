# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, List, Tuple, cast

import pytest

from giskard_hub import HubClient, AsyncHubClient
from tests.utils import assert_matches_type
from giskard_hub.types import APIPaginatedMetadata
from giskard_hub.types.evaluation import TestCaseEvaluation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResults:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: HubClient) -> None:
        result = client.evaluations.results.retrieve(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: HubClient) -> None:
        result = client.evaluations.results.retrieve(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include=["test_case"],
        )
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: HubClient) -> None:
        response = client.evaluations.results.with_raw_response.retrieve(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        result = response.parse()
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: HubClient) -> None:
        with client.evaluations.results.with_streaming_response.retrieve(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            result = response.parse()
            assert_matches_type(TestCaseEvaluation, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            client.evaluations.results.with_raw_response.retrieve(
                result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                evaluation_id="",
            )

        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `result_id` but received ''",
        ):
            client.evaluations.results.with_raw_response.retrieve(
                result_id="",
                evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubClient) -> None:
        result = client.evaluations.results.update(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubClient) -> None:
        result = client.evaluations.results.update(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            failure_category={
                "description": "description",
                "identifier": "identifier",
                "title": "title",
            },
        )
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubClient) -> None:
        response = client.evaluations.results.with_raw_response.update(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        result = response.parse()
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubClient) -> None:
        with client.evaluations.results.with_streaming_response.update(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            result = response.parse()
            assert_matches_type(TestCaseEvaluation, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            client.evaluations.results.with_raw_response.update(
                result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                evaluation_id="",
            )

        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `result_id` but received ''",
        ):
            client.evaluations.results.with_raw_response.update(
                result_id="",
                evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubClient) -> None:
        result = client.evaluations.results.list(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(List[TestCaseEvaluation], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubClient) -> None:
        result = client.evaluations.results.list(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include=["test_case"],
        )
        assert_matches_type(List[TestCaseEvaluation], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubClient) -> None:
        response = client.evaluations.results.with_raw_response.list(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        result = response.parse()
        assert_matches_type(List[TestCaseEvaluation], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubClient) -> None:
        with client.evaluations.results.with_streaming_response.list(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            result = response.parse()
            assert_matches_type(List[TestCaseEvaluation], result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            client.evaluations.results.with_raw_response.list(
                evaluation_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_rerun_test_case(self, client: HubClient) -> None:
        result = client.evaluations.results.rerun_test_case(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_rerun_test_case(self, client: HubClient) -> None:
        response = client.evaluations.results.with_raw_response.rerun_test_case(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        result = response.parse()
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_rerun_test_case(self, client: HubClient) -> None:
        with client.evaluations.results.with_streaming_response.rerun_test_case(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            result = response.parse()
            assert_matches_type(TestCaseEvaluation, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_rerun_test_case(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            client.evaluations.results.with_raw_response.rerun_test_case(
                result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                evaluation_id="",
            )

        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `result_id` but received ''",
        ):
            client.evaluations.results.with_raw_response.rerun_test_case(
                result_id="",
                evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_local_output(self, client: HubClient) -> None:
        result = client.evaluations.results.submit_local_output(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_local_output_with_all_params(self, client: HubClient) -> None:
        result = client.evaluations.results.submit_local_output(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            error="error",
            agent_output={
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
        )
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit_local_output(self, client: HubClient) -> None:
        response = client.evaluations.results.with_raw_response.submit_local_output(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        result = response.parse()
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit_local_output(self, client: HubClient) -> None:
        with client.evaluations.results.with_streaming_response.submit_local_output(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            result = response.parse()
            assert_matches_type(TestCaseEvaluation, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_submit_local_output(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            client.evaluations.results.with_raw_response.submit_local_output(
                result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                evaluation_id="",
            )

        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `result_id` but received ''",
        ):
            client.evaluations.results.with_raw_response.submit_local_output(
                result_id="",
                evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: HubClient) -> None:
        result = client.evaluations.results.search(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(List[TestCaseEvaluation], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: HubClient) -> None:
        result = client.evaluations.results.search(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            search="query",
            filters={},
            limit=20,
            offset=0,
            include=["test_case"],
        )
        assert_matches_type(List[TestCaseEvaluation], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_metadata(self, client: HubClient) -> None:
        result = client.evaluations.results.search(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_metadata=True,
        )
        assert_matches_type(Tuple[List[TestCaseEvaluation], APIPaginatedMetadata], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: HubClient) -> None:
        response = client.evaluations.results.with_raw_response.search(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        result = response.parse()
        assert_matches_type(List[TestCaseEvaluation], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: HubClient) -> None:
        with client.evaluations.results.with_streaming_response.search(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            result = response.parse()
            assert_matches_type(List[TestCaseEvaluation], result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_search(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            client.evaluations.results.with_raw_response.search(
                evaluation_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_visibility(self, client: HubClient) -> None:
        result = client.evaluations.results.update_visibility(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            hidden=False,
        )
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_visibility(self, client: HubClient) -> None:
        response = client.evaluations.results.with_raw_response.update_visibility(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            hidden=False,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        result = response.parse()
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_visibility(self, client: HubClient) -> None:
        with client.evaluations.results.with_streaming_response.update_visibility(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            hidden=False,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            result = response.parse()
            assert_matches_type(TestCaseEvaluation, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_visibility(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            client.evaluations.results.with_raw_response.update_visibility(
                result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                evaluation_id="",
                hidden=False,
            )

        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `result_id` but received ''",
        ):
            client.evaluations.results.with_raw_response.update_visibility(
                result_id="",
                evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                hidden=False,
            )


class TestAsyncResults:
    parametrize = pytest.mark.parametrize(
        "async_client",
        [False, True, {"http_client": "aiohttp"}],
        indirect=True,
        ids=["loose", "strict", "aiohttp"],
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHubClient) -> None:
        result = await async_client.evaluations.results.retrieve(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncHubClient) -> None:
        result = await async_client.evaluations.results.retrieve(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include=["test_case"],
        )
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHubClient) -> None:
        response = await async_client.evaluations.results.with_raw_response.retrieve(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        result = await response.parse()
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHubClient) -> None:
        async with async_client.evaluations.results.with_streaming_response.retrieve(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            result = await response.parse()
            assert_matches_type(TestCaseEvaluation, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            await async_client.evaluations.results.with_raw_response.retrieve(
                result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                evaluation_id="",
            )

        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `result_id` but received ''",
        ):
            await async_client.evaluations.results.with_raw_response.retrieve(
                result_id="",
                evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubClient) -> None:
        result = await async_client.evaluations.results.update(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubClient) -> None:
        result = await async_client.evaluations.results.update(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            failure_category={
                "description": "description",
                "identifier": "identifier",
                "title": "title",
            },
        )
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubClient) -> None:
        response = await async_client.evaluations.results.with_raw_response.update(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        result = await response.parse()
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubClient) -> None:
        async with async_client.evaluations.results.with_streaming_response.update(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            result = await response.parse()
            assert_matches_type(TestCaseEvaluation, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            await async_client.evaluations.results.with_raw_response.update(
                result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                evaluation_id="",
            )

        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `result_id` but received ''",
        ):
            await async_client.evaluations.results.with_raw_response.update(
                result_id="",
                evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubClient) -> None:
        result = await async_client.evaluations.results.list(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(List[TestCaseEvaluation], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubClient) -> None:
        result = await async_client.evaluations.results.list(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include=["test_case"],
        )
        assert_matches_type(List[TestCaseEvaluation], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubClient) -> None:
        response = await async_client.evaluations.results.with_raw_response.list(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        result = await response.parse()
        assert_matches_type(List[TestCaseEvaluation], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubClient) -> None:
        async with async_client.evaluations.results.with_streaming_response.list(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            result = await response.parse()
            assert_matches_type(List[TestCaseEvaluation], result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            await async_client.evaluations.results.with_raw_response.list(
                evaluation_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_rerun_test_case(self, async_client: AsyncHubClient) -> None:
        result = await async_client.evaluations.results.rerun_test_case(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_rerun_test_case(self, async_client: AsyncHubClient) -> None:
        response = await async_client.evaluations.results.with_raw_response.rerun_test_case(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        result = await response.parse()
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_rerun_test_case(self, async_client: AsyncHubClient) -> None:
        async with async_client.evaluations.results.with_streaming_response.rerun_test_case(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            result = await response.parse()
            assert_matches_type(TestCaseEvaluation, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_rerun_test_case(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            await async_client.evaluations.results.with_raw_response.rerun_test_case(
                result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                evaluation_id="",
            )

        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `result_id` but received ''",
        ):
            await async_client.evaluations.results.with_raw_response.rerun_test_case(
                result_id="",
                evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_local_output(self, async_client: AsyncHubClient) -> None:
        result = await async_client.evaluations.results.submit_local_output(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_local_output_with_all_params(self, async_client: AsyncHubClient) -> None:
        result = await async_client.evaluations.results.submit_local_output(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            error="error",
            agent_output={
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
        )
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit_local_output(self, async_client: AsyncHubClient) -> None:
        response = await async_client.evaluations.results.with_raw_response.submit_local_output(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        result = await response.parse()
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit_local_output(self, async_client: AsyncHubClient) -> None:
        async with async_client.evaluations.results.with_streaming_response.submit_local_output(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            result = await response.parse()
            assert_matches_type(TestCaseEvaluation, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_submit_local_output(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            await async_client.evaluations.results.with_raw_response.submit_local_output(
                result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                evaluation_id="",
            )

        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `result_id` but received ''",
        ):
            await async_client.evaluations.results.with_raw_response.submit_local_output(
                result_id="",
                evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHubClient) -> None:
        result = await async_client.evaluations.results.search(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(List[TestCaseEvaluation], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHubClient) -> None:
        result = await async_client.evaluations.results.search(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            search="query",
            filters={},
            limit=20,
            offset=0,
            include=["test_case"],
        )
        assert_matches_type(List[TestCaseEvaluation], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_metadata(self, async_client: AsyncHubClient) -> None:
        result = await async_client.evaluations.results.search(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_metadata=True,
        )
        assert_matches_type(Tuple[List[TestCaseEvaluation], APIPaginatedMetadata], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHubClient) -> None:
        response = await async_client.evaluations.results.with_raw_response.search(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        result = await response.parse()
        assert_matches_type(List[TestCaseEvaluation], result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHubClient) -> None:
        async with async_client.evaluations.results.with_streaming_response.search(
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            result = await response.parse()
            assert_matches_type(List[TestCaseEvaluation], result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_search(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            await async_client.evaluations.results.with_raw_response.search(
                evaluation_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_visibility(self, async_client: AsyncHubClient) -> None:
        result = await async_client.evaluations.results.update_visibility(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            hidden=False,
        )
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_visibility(self, async_client: AsyncHubClient) -> None:
        response = await async_client.evaluations.results.with_raw_response.update_visibility(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            hidden=False,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        result = await response.parse()
        assert_matches_type(TestCaseEvaluation, result, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_visibility(self, async_client: AsyncHubClient) -> None:
        async with async_client.evaluations.results.with_streaming_response.update_visibility(
            result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            hidden=False,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            result = await response.parse()
            assert_matches_type(TestCaseEvaluation, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_visibility(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `evaluation_id` but received ''",
        ):
            await async_client.evaluations.results.with_raw_response.update_visibility(
                result_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                evaluation_id="",
                hidden=False,
            )

        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `result_id` but received ''",
        ):
            await async_client.evaluations.results.with_raw_response.update_visibility(
                result_id="",
                evaluation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                hidden=False,
            )
