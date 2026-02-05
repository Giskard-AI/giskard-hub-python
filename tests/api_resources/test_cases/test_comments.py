# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from giskard_hub import HubClient, AsyncHubClient
from tests.utils import assert_matches_type
from giskard_hub.types import APIResponse, TestCaseComment

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubClient) -> None:
        comment = client.test_cases.comments.delete(
            comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[None], comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubClient) -> None:
        response = client.test_cases.comments.with_raw_response.delete(
            comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        comment = response.parse()
        assert_matches_type(APIResponse[None], comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubClient) -> None:
        with client.test_cases.comments.with_streaming_response.delete(
            comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            comment = response.parse()
            assert_matches_type(APIResponse[None], comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `test_case_id` but received ''",
        ):
            client.test_cases.comments.with_raw_response.delete(
                comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                test_case_id="",
            )

        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `comment_id` but received ''",
        ):
            client.test_cases.comments.with_raw_response.delete(
                comment_id="",
                test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: HubClient) -> None:
        comment = client.test_cases.comments.add(
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        )
        assert_matches_type(APIResponse[TestCaseComment], comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: HubClient) -> None:
        response = client.test_cases.comments.with_raw_response.add(
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        comment = response.parse()
        assert_matches_type(APIResponse[TestCaseComment], comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: HubClient) -> None:
        with client.test_cases.comments.with_streaming_response.add(
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            comment = response.parse()
            assert_matches_type(APIResponse[TestCaseComment], comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `test_case_id` but received ''",
        ):
            client.test_cases.comments.with_raw_response.add(
                test_case_id="",
                comment="comment",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_edit(self, client: HubClient) -> None:
        comment = client.test_cases.comments.edit(
            comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        )
        assert_matches_type(APIResponse[TestCaseComment], comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_edit(self, client: HubClient) -> None:
        response = client.test_cases.comments.with_raw_response.edit(
            comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        comment = response.parse()
        assert_matches_type(APIResponse[TestCaseComment], comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_edit(self, client: HubClient) -> None:
        with client.test_cases.comments.with_streaming_response.edit(
            comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            comment = response.parse()
            assert_matches_type(APIResponse[TestCaseComment], comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_edit(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `test_case_id` but received ''",
        ):
            client.test_cases.comments.with_raw_response.edit(
                comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                test_case_id="",
                comment="comment",
            )

        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `comment_id` but received ''",
        ):
            client.test_cases.comments.with_raw_response.edit(
                comment_id="",
                test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                comment="comment",
            )


class TestAsyncComments:
    parametrize = pytest.mark.parametrize(
        "async_client",
        [False, True, {"http_client": "aiohttp"}],
        indirect=True,
        ids=["loose", "strict", "aiohttp"],
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubClient) -> None:
        comment = await async_client.test_cases.comments.delete(
            comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[None], comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubClient) -> None:
        response = await async_client.test_cases.comments.with_raw_response.delete(
            comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(APIResponse[None], comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubClient) -> None:
        async with async_client.test_cases.comments.with_streaming_response.delete(
            comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(APIResponse[None], comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `test_case_id` but received ''",
        ):
            await async_client.test_cases.comments.with_raw_response.delete(
                comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                test_case_id="",
            )

        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `comment_id` but received ''",
        ):
            await async_client.test_cases.comments.with_raw_response.delete(
                comment_id="",
                test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncHubClient) -> None:
        comment = await async_client.test_cases.comments.add(
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        )
        assert_matches_type(APIResponse[TestCaseComment], comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncHubClient) -> None:
        response = await async_client.test_cases.comments.with_raw_response.add(
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(APIResponse[TestCaseComment], comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncHubClient) -> None:
        async with async_client.test_cases.comments.with_streaming_response.add(
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(APIResponse[TestCaseComment], comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `test_case_id` but received ''",
        ):
            await async_client.test_cases.comments.with_raw_response.add(
                test_case_id="",
                comment="comment",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_edit(self, async_client: AsyncHubClient) -> None:
        comment = await async_client.test_cases.comments.edit(
            comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        )
        assert_matches_type(APIResponse[TestCaseComment], comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncHubClient) -> None:
        response = await async_client.test_cases.comments.with_raw_response.edit(
            comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(APIResponse[TestCaseComment], comment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncHubClient) -> None:
        async with async_client.test_cases.comments.with_streaming_response.edit(
            comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(APIResponse[TestCaseComment], comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `test_case_id` but received ''",
        ):
            await async_client.test_cases.comments.with_raw_response.edit(
                comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                test_case_id="",
                comment="comment",
            )

        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `comment_id` but received ''",
        ):
            await async_client.test_cases.comments.with_raw_response.edit(
                comment_id="",
                test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                comment="comment",
            )
