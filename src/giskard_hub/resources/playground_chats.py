from __future__ import annotations

from typing import List, Literal, Optional

import httpx

from ..types import (
    CreatePlaygroundChat,
    PlaygroundChatListParams,
    PlaygroundChatUpdateData,
    PlaygroundChatRetrieveParams,
)
from .._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.common import APIResponse, APIResponseWithIncluded
from ..types.playground_chat_api_resource import PlaygroundChatAPIResource

__all__ = ["PlaygroundChatsResource", "AsyncPlaygroundChatsResource"]


class PlaygroundChatsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlaygroundChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return PlaygroundChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlaygroundChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return PlaygroundChatsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: str,
        name: str,
        agent_id: Optional[str] | NotGiven = not_given,
        description: Optional[str] | NotGiven = not_given,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[PlaygroundChatAPIResource]:
        """
        Create Playground Chat

        Args:
          project_id: Project ID to create the chat in

          name: Name of the chat

          agent_id: Agent ID to associate with the chat

          description: Description of the chat

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/playground-chats",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "name": name,
                    "agent_id": agent_id,
                    "description": description,
                },
                CreatePlaygroundChat,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[PlaygroundChatAPIResource],
        )

    def list(
        self,
        *,
        project_id: str,
        include: Optional[List[Literal["agent"]]] | NotGiven = not_given,
        limit: Optional[int] | NotGiven = not_given,
        offset: Optional[int] | NotGiven = not_given,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseWithIncluded[List[PlaygroundChatAPIResource], object]:
        """
        List Playground Chats

        Args:
          project_id: Project ID to list chats for

          include: Related resources to include in the response

          limit: Maximum number of chats to return

          offset: Offset for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/playground-chats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "project_id": project_id,
                        "include": include,
                        "limit": limit,
                        "offset": offset,
                    },
                    PlaygroundChatListParams,
                ),
            ),
            cast_to=APIResponseWithIncluded[List[PlaygroundChatAPIResource], object],
        )

    def retrieve(
        self,
        chat_id: str,
        *,
        include: Optional[List[Literal["agent"]]] | NotGiven = not_given,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseWithIncluded[PlaygroundChatAPIResource, object]:
        """
        Get Playground Chat

        Args:
          chat_id: Chat ID to retrieve

          include: Related resources to include in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get(
            f"/v2/playground-chats/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include": include}, PlaygroundChatRetrieveParams),
            ),
            cast_to=APIResponseWithIncluded[PlaygroundChatAPIResource, object],
        )

    def update(
        self,
        chat_id: str,
        *,
        name: Optional[str] | NotGiven = not_given,
        agent_id: Optional[str] | NotGiven = not_given,
        description: Optional[str] | NotGiven = not_given,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[PlaygroundChatAPIResource]:
        """
        Update Playground Chat

        Args:
          chat_id: Chat ID to update

          name: Name of the chat

          agent_id: Agent ID to associate with the chat

          description: Description of the chat

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._patch(
            f"/v2/playground-chats/{chat_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "agent_id": agent_id,
                    "description": description,
                },
                PlaygroundChatUpdateData,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[PlaygroundChatAPIResource],
        )

    def delete_many(
        self,
        *,
        chat_ids: Optional[SequenceNotStr[str]] | NotGiven = not_given,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[None]:
        """
        Delete Playground Chats

        Args:
          chat_ids: List of chat IDs to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v2/playground-chats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query={"chat_ids": chat_ids} if chat_ids is not not_given else {},
            ),
            cast_to=APIResponse[None],
        )


class AsyncPlaygroundChatsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlaygroundChatsResourceWithRawResponse:
        return AsyncPlaygroundChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlaygroundChatsResourceWithStreamingResponse:
        return AsyncPlaygroundChatsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: str,
        name: str,
        agent_id: Optional[str] | NotGiven = not_given,
        description: Optional[str] | NotGiven = not_given,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[PlaygroundChatAPIResource]:
        """Create Playground Chat"""
        return await self._post(
            "/v2/playground-chats",
            body=await async_maybe_transform(
                {
                    "project_id": project_id,
                    "name": name,
                    "agent_id": agent_id,
                    "description": description,
                },
                CreatePlaygroundChat,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[PlaygroundChatAPIResource],
        )

    async def list(
        self,
        *,
        project_id: str,
        include: Optional[List[Literal["agent"]]] | NotGiven = not_given,
        limit: Optional[int] | NotGiven = not_given,
        offset: Optional[int] | NotGiven = not_given,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseWithIncluded[List[PlaygroundChatAPIResource], object]:
        """List Playground Chats"""
        return await self._get(
            "/v2/playground-chats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "project_id": project_id,
                        "include": include,
                        "limit": limit,
                        "offset": offset,
                    },
                    PlaygroundChatListParams,
                ),
            ),
            cast_to=APIResponseWithIncluded[List[PlaygroundChatAPIResource], object],
        )

    async def retrieve(
        self,
        chat_id: str,
        *,
        include: Optional[List[Literal["agent"]]] | NotGiven = not_given,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseWithIncluded[PlaygroundChatAPIResource, object]:
        """Get Playground Chat"""
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._get(
            f"/v2/playground-chats/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"include": include}, PlaygroundChatRetrieveParams),
            ),
            cast_to=APIResponseWithIncluded[PlaygroundChatAPIResource, object],
        )

    async def update(
        self,
        chat_id: str,
        *,
        name: Optional[str] | NotGiven = not_given,
        agent_id: Optional[str] | NotGiven = not_given,
        description: Optional[str] | NotGiven = not_given,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[PlaygroundChatAPIResource]:
        """Update Playground Chat"""
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._patch(
            f"/v2/playground-chats/{chat_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "agent_id": agent_id,
                    "description": description,
                },
                PlaygroundChatUpdateData,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[PlaygroundChatAPIResource],
        )

    async def delete_many(
        self,
        *,
        chat_ids: Optional[SequenceNotStr[str]] | NotGiven = not_given,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[None]:
        """Delete Playground Chats"""
        return await self._delete(
            "/v2/playground-chats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query={"chat_ids": chat_ids} if chat_ids is not not_given else {},
            ),
            cast_to=APIResponse[None],
        )


class PlaygroundChatsResourceWithRawResponse:
    def __init__(self, playground_chats: PlaygroundChatsResource) -> None:
        self._playground_chats = playground_chats

        self.create = to_raw_response_wrapper(
            playground_chats.create,
        )
        self.list = to_raw_response_wrapper(
            playground_chats.list,
        )
        self.retrieve = to_raw_response_wrapper(
            playground_chats.retrieve,
        )
        self.update = to_raw_response_wrapper(
            playground_chats.update,
        )
        self.delete_many = to_raw_response_wrapper(
            playground_chats.delete_many,
        )


class AsyncPlaygroundChatsResourceWithRawResponse:
    def __init__(self, playground_chats: AsyncPlaygroundChatsResource) -> None:
        self._playground_chats = playground_chats

        self.create = async_to_raw_response_wrapper(
            playground_chats.create,
        )
        self.list = async_to_raw_response_wrapper(
            playground_chats.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            playground_chats.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            playground_chats.update,
        )
        self.delete_many = async_to_raw_response_wrapper(
            playground_chats.delete_many,
        )


class PlaygroundChatsResourceWithStreamingResponse:
    def __init__(self, playground_chats: PlaygroundChatsResource) -> None:
        self._playground_chats = playground_chats

        self.create = to_streamed_response_wrapper(
            playground_chats.create,
        )
        self.list = to_streamed_response_wrapper(
            playground_chats.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            playground_chats.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            playground_chats.update,
        )
        self.delete_many = to_streamed_response_wrapper(
            playground_chats.delete_many,
        )


class AsyncPlaygroundChatsResourceWithStreamingResponse:
    def __init__(self, playground_chats: AsyncPlaygroundChatsResource) -> None:
        self._playground_chats = playground_chats

        self.create = async_to_streamed_response_wrapper(
            playground_chats.create,
        )
        self.list = async_to_streamed_response_wrapper(
            playground_chats.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            playground_chats.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            playground_chats.update,
        )
        self.delete_many = async_to_streamed_response_wrapper(
            playground_chats.delete_many,
        )
