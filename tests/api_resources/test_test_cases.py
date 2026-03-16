# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, List, cast

import pytest

from giskard_hub import HubClient, AsyncHubClient
from tests.utils import assert_matches_type
from giskard_hub.types import TestCase

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTestCases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubClient) -> None:
        test_case = client.test_cases.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubClient) -> None:
        test_case = client.test_cases.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            checks=[
                {
                    "identifier": "correctness",
                    "params": {
                        "reference": "reference",
                    },
                    "enabled": True,
                }
            ],
            demo_output="content",
            status="active",
            tags=["string"],
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubClient) -> None:
        response = client.test_cases.with_raw_response.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        test_case = response.parse()
        assert_matches_type(TestCase, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubClient) -> None:
        with client.test_cases.with_streaming_response.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            test_case = response.parse()
            assert_matches_type(TestCase, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: HubClient) -> None:
        test_case = client.test_cases.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: HubClient) -> None:
        response = client.test_cases.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        test_case = response.parse()
        assert_matches_type(TestCase, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: HubClient) -> None:
        with client.test_cases.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            test_case = response.parse()
            assert_matches_type(TestCase, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `test_case_id` but received ''",
        ):
            client.test_cases.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubClient) -> None:
        test_case = client.test_cases.update(
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubClient) -> None:
        test_case = client.test_cases.update(
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            checks=[
                {
                    "identifier": "correctness",
                    "params": {
                        "reference": "reference",
                    },
                    "enabled": True,
                }
            ],
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            demo_output="content",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            tags=["string"],
            status="active",
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubClient) -> None:
        response = client.test_cases.with_raw_response.update(
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        test_case = response.parse()
        assert_matches_type(TestCase, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubClient) -> None:
        with client.test_cases.with_streaming_response.update(
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            test_case = response.parse()
            assert_matches_type(TestCase, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `test_case_id` but received ''",
        ):
            client.test_cases.with_raw_response.update(
                test_case_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubClient) -> None:
        test_case = client.test_cases.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(None, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubClient) -> None:
        response = client.test_cases.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        test_case = response.parse()
        assert_matches_type(None, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubClient) -> None:
        with client.test_cases.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            test_case = response.parse()
            assert_matches_type(None, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `test_case_id` but received ''",
        ):
            client.test_cases.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bulk_delete(self, client: HubClient) -> None:
        test_case = client.test_cases.bulk_delete(
            test_case_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(None, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_bulk_delete(self, client: HubClient) -> None:
        response = client.test_cases.with_raw_response.bulk_delete(
            test_case_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        test_case = response.parse()
        assert_matches_type(None, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_bulk_delete(self, client: HubClient) -> None:
        with client.test_cases.with_streaming_response.bulk_delete(
            test_case_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            test_case = response.parse()
            assert_matches_type(None, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bulk_update(self, client: HubClient) -> None:
        test_case = client.test_cases.bulk_update(
            test_case_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(List[TestCase], test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bulk_update_with_all_params(self, client: HubClient) -> None:
        test_case = client.test_cases.bulk_update(
            test_case_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            disabled_checks=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            enabled_checks=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(List[TestCase], test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_bulk_update(self, client: HubClient) -> None:
        response = client.test_cases.with_raw_response.bulk_update(
            test_case_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        test_case = response.parse()
        assert_matches_type(List[TestCase], test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_bulk_update(self, client: HubClient) -> None:
        with client.test_cases.with_streaming_response.bulk_update(
            test_case_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            test_case = response.parse()
            assert_matches_type(List[TestCase], test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bulk_move(self, client: HubClient) -> None:
        test_case = client.test_cases.bulk_move(
            test_case_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            target_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(None, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bulk_move_with_all_params(self, client: HubClient) -> None:
        test_case = client.test_cases.bulk_move(
            test_case_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            target_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            duplicate=True,
        )
        assert_matches_type(None, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_bulk_move(self, client: HubClient) -> None:
        response = client.test_cases.with_raw_response.bulk_move(
            test_case_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            target_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        test_case = response.parse()
        assert_matches_type(None, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_bulk_move(self, client: HubClient) -> None:
        with client.test_cases.with_streaming_response.bulk_move(
            test_case_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            target_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            test_case = response.parse()
            assert_matches_type(None, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTestCases:
    parametrize = pytest.mark.parametrize(
        "async_client",
        [False, True, {"http_client": "aiohttp"}],
        indirect=True,
        ids=["loose", "strict", "aiohttp"],
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubClient) -> None:
        test_case = await async_client.test_cases.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubClient) -> None:
        test_case = await async_client.test_cases.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            checks=[
                {
                    "identifier": "correctness",
                    "params": {
                        "reference": "reference",
                    },
                    "enabled": True,
                }
            ],
            demo_output="content",
            status="active",
            tags=["string"],
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubClient) -> None:
        response = await async_client.test_cases.with_raw_response.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        test_case = await response.parse()
        assert_matches_type(TestCase, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubClient) -> None:
        async with async_client.test_cases.with_streaming_response.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            test_case = await response.parse()
            assert_matches_type(TestCase, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHubClient) -> None:
        test_case = await async_client.test_cases.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHubClient) -> None:
        response = await async_client.test_cases.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        test_case = await response.parse()
        assert_matches_type(TestCase, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHubClient) -> None:
        async with async_client.test_cases.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            test_case = await response.parse()
            assert_matches_type(TestCase, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `test_case_id` but received ''",
        ):
            await async_client.test_cases.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubClient) -> None:
        test_case = await async_client.test_cases.update(
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubClient) -> None:
        test_case = await async_client.test_cases.update(
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            checks=[
                {
                    "identifier": "correctness",
                    "params": {
                        "reference": "reference",
                    },
                    "enabled": True,
                }
            ],
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            demo_output="content",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            tags=["string"],
        )
        assert_matches_type(TestCase, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubClient) -> None:
        response = await async_client.test_cases.with_raw_response.update(
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        test_case = await response.parse()
        assert_matches_type(TestCase, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubClient) -> None:
        async with async_client.test_cases.with_streaming_response.update(
            test_case_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            test_case = await response.parse()
            assert_matches_type(TestCase, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `test_case_id` but received ''",
        ):
            await async_client.test_cases.with_raw_response.update(
                test_case_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubClient) -> None:
        test_case = await async_client.test_cases.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(None, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubClient) -> None:
        response = await async_client.test_cases.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        test_case = await response.parse()
        assert_matches_type(None, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubClient) -> None:
        async with async_client.test_cases.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            test_case = await response.parse()
            assert_matches_type(None, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `test_case_id` but received ''",
        ):
            await async_client.test_cases.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncHubClient) -> None:
        test_case = await async_client.test_cases.bulk_delete(
            test_case_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(None, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncHubClient) -> None:
        response = await async_client.test_cases.with_raw_response.bulk_delete(
            test_case_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        test_case = await response.parse()
        assert_matches_type(None, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncHubClient) -> None:
        async with async_client.test_cases.with_streaming_response.bulk_delete(
            test_case_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            test_case = await response.parse()
            assert_matches_type(None, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bulk_update(self, async_client: AsyncHubClient) -> None:
        test_case = await async_client.test_cases.bulk_update(
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(List[TestCase], test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bulk_update_with_all_params(self, async_client: AsyncHubClient) -> None:
        test_case = await async_client.test_cases.bulk_update(
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            disabled_checks=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            enabled_checks=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(List[TestCase], test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_bulk_update(self, async_client: AsyncHubClient) -> None:
        response = await async_client.test_cases.with_raw_response.bulk_update(
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        test_case = await response.parse()
        assert_matches_type(List[TestCase], test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_update(self, async_client: AsyncHubClient) -> None:
        async with async_client.test_cases.with_streaming_response.bulk_update(
            ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            test_case = await response.parse()
            assert_matches_type(List[TestCase], test_case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bulk_move(self, async_client: AsyncHubClient) -> None:
        test_case = await async_client.test_cases.bulk_move(
            test_case_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            target_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(None, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bulk_move_with_all_params(self, async_client: AsyncHubClient) -> None:
        test_case = await async_client.test_cases.bulk_move(
            test_case_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            target_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            duplicate=True,
        )
        assert_matches_type(None, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_bulk_move(self, async_client: AsyncHubClient) -> None:
        response = await async_client.test_cases.with_raw_response.bulk_move(
            test_case_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            target_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        test_case = await response.parse()
        assert_matches_type(None, test_case, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_move(self, async_client: AsyncHubClient) -> None:
        async with async_client.test_cases.with_streaming_response.bulk_move(
            test_case_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            target_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            test_case = await response.parse()
            assert_matches_type(None, test_case, path=["response"])

        assert cast(Any, response.is_closed) is True
