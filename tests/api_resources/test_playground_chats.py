from __future__ import annotations

import os
from typing import Any, List, cast

import pytest

from giskard_hub import HubClient, AsyncHubClient
from tests.utils import assert_matches_type
from giskard_hub.types import (
    Agent,
    APIResponse,
    APIResponseWithIncluded,
    PlaygroundChatAPIResource,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlaygroundChats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubClient) -> None:
        playground_chat = client.playground_chats.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            APIResponseWithIncluded[List[PlaygroundChatAPIResource], APIResponse[Agent]],
            playground_chat,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubClient) -> None:
        playground_chat = client.playground_chats.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include=["agent"],
            limit=10,
            offset=0,
        )
        assert_matches_type(
            APIResponseWithIncluded[List[PlaygroundChatAPIResource], APIResponse[Agent]],
            playground_chat,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubClient) -> None:
        response = client.playground_chats.with_raw_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        playground_chat = response.parse()
        assert_matches_type(
            APIResponseWithIncluded[List[PlaygroundChatAPIResource], APIResponse[Agent]],
            playground_chat,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubClient) -> None:
        with client.playground_chats.with_streaming_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            playground_chat = response.parse()
            assert_matches_type(
                APIResponseWithIncluded[List[PlaygroundChatAPIResource], APIResponse[Agent]],
                playground_chat,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: HubClient) -> None:
        playground_chat = client.playground_chats.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            APIResponseWithIncluded[PlaygroundChatAPIResource, APIResponse[Agent]], playground_chat, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: HubClient) -> None:
        playground_chat = client.playground_chats.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include=["agent"],
        )
        assert_matches_type(
            APIResponseWithIncluded[PlaygroundChatAPIResource, APIResponse[Agent]], playground_chat, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: HubClient) -> None:
        response = client.playground_chats.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        playground_chat = response.parse()
        assert_matches_type(
            APIResponseWithIncluded[PlaygroundChatAPIResource, APIResponse[Agent]], playground_chat, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: HubClient) -> None:
        with client.playground_chats.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            playground_chat = response.parse()
            assert_matches_type(
                APIResponseWithIncluded[PlaygroundChatAPIResource, APIResponse[Agent]],
                playground_chat,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `chat_id` but received ''",
        ):
            client.playground_chats.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubClient) -> None:
        playground_chat = client.playground_chats.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[None], playground_chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubClient) -> None:
        response = client.playground_chats.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        playground_chat = response.parse()
        assert_matches_type(APIResponse[None], playground_chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubClient) -> None:
        with client.playground_chats.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            playground_chat = response.parse()
            assert_matches_type(APIResponse[None], playground_chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `chat_id` but received ''",
        ):
            client.playground_chats.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bulk_delete(self, client: HubClient) -> None:
        playground_chat = client.playground_chats.bulk_delete(
            chat_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(APIResponse[None], playground_chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_bulk_delete(self, client: HubClient) -> None:
        response = client.playground_chats.with_raw_response.bulk_delete(
            chat_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        playground_chat = response.parse()
        assert_matches_type(APIResponse[None], playground_chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_bulk_delete(self, client: HubClient) -> None:
        with client.playground_chats.with_streaming_response.bulk_delete(
            chat_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            playground_chat = response.parse()
            assert_matches_type(APIResponse[None], playground_chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPlaygroundChats:
    parametrize = pytest.mark.parametrize(
        "async_client",
        [False, True, {"http_client": "aiohttp"}],
        indirect=True,
        ids=["loose", "strict", "aiohttp"],
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubClient) -> None:
        playground_chat = await async_client.playground_chats.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            APIResponseWithIncluded[List[PlaygroundChatAPIResource], APIResponse[Agent]],
            playground_chat,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubClient) -> None:
        playground_chat = await async_client.playground_chats.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include=["agent"],
            limit=10,
            offset=0,
        )
        assert_matches_type(
            APIResponseWithIncluded[List[PlaygroundChatAPIResource], APIResponse[Agent]],
            playground_chat,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubClient) -> None:
        response = await async_client.playground_chats.with_raw_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        playground_chat = await response.parse()
        assert_matches_type(
            APIResponseWithIncluded[List[PlaygroundChatAPIResource], APIResponse[Agent]],
            playground_chat,
            path=["response"],
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubClient) -> None:
        async with async_client.playground_chats.with_streaming_response.list(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            playground_chat = await response.parse()
            assert_matches_type(
                APIResponseWithIncluded[List[PlaygroundChatAPIResource], APIResponse[Agent]],
                playground_chat,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHubClient) -> None:
        playground_chat = await async_client.playground_chats.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            APIResponseWithIncluded[PlaygroundChatAPIResource, APIResponse[Agent]], playground_chat, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncHubClient) -> None:
        playground_chat = await async_client.playground_chats.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include=["agent"],
        )
        assert_matches_type(
            APIResponseWithIncluded[PlaygroundChatAPIResource, APIResponse[Agent]], playground_chat, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHubClient) -> None:
        response = await async_client.playground_chats.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        playground_chat = await response.parse()
        assert_matches_type(
            APIResponseWithIncluded[PlaygroundChatAPIResource, APIResponse[Agent]], playground_chat, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHubClient) -> None:
        async with async_client.playground_chats.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            playground_chat = await response.parse()
            assert_matches_type(
                APIResponseWithIncluded[PlaygroundChatAPIResource, APIResponse[Agent]],
                playground_chat,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `chat_id` but received ''",
        ):
            await async_client.playground_chats.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubClient) -> None:
        playground_chat = await async_client.playground_chats.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponse[None], playground_chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubClient) -> None:
        response = await async_client.playground_chats.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        playground_chat = await response.parse()
        assert_matches_type(APIResponse[None], playground_chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubClient) -> None:
        async with async_client.playground_chats.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            playground_chat = await response.parse()
            assert_matches_type(APIResponse[None], playground_chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubClient) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `chat_id` but received ''",
        ):
            await async_client.playground_chats.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncHubClient) -> None:
        playground_chat = await async_client.playground_chats.bulk_delete(
            chat_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(APIResponse[None], playground_chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncHubClient) -> None:
        response = await async_client.playground_chats.with_raw_response.bulk_delete(
            chat_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Giskard-Lang") == "python"
        playground_chat = await response.parse()
        assert_matches_type(APIResponse[None], playground_chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncHubClient) -> None:
        async with async_client.playground_chats.with_streaming_response.bulk_delete(
            chat_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Giskard-Lang") == "python"

            playground_chat = await response.parse()
            assert_matches_type(APIResponse[None], playground_chat, path=["response"])

        assert cast(Any, response.is_closed) is True
