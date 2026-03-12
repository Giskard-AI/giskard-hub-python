from __future__ import annotations

from typing import List, Literal, Optional

import httpx

from ..types import (
    Agent,
    PlaygroundChatListParams,
    PlaygroundChatRetrieveParams,
    PlaygroundChatBulkDeleteParams,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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

    def list(
        self,
        *,
        project_id: str,
        include: Optional[List[Literal["agent"]]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseWithIncluded[List[PlaygroundChatAPIResource], APIResponse[Agent]]:
        """
        List Playground Chats

        Args:
          project_id: Project ID to list playground chats for

          include: Related resources to include in the response

          limit: Maximum number of playground chats to return

          offset: Offset for pagination of playground chats

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
            cast_to=APIResponseWithIncluded[List[PlaygroundChatAPIResource], APIResponse[Agent]],
        )

    def retrieve(
        self,
        chat_id: str,
        *,
        include: Optional[List[Literal["agent"]]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseWithIncluded[PlaygroundChatAPIResource, APIResponse[Agent]]:
        """
        Get Playground Chat

        Args:
          chat_id: Playground chat ID to retrieve

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
            cast_to=APIResponseWithIncluded[PlaygroundChatAPIResource, APIResponse[Agent]],
        )

    def delete(
        self,
        chat_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[None]:
        """
        Delete Playground Chat

        Args:
          chat_id: Playground chat ID to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self.bulk_delete(
            chat_ids=[chat_id],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    def bulk_delete(
        self,
        *,
        chat_ids: SequenceNotStr[str],
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[None]:
        """
        Delete Playground Chats

        Args:
          chat_ids: List of playground chat IDs to delete

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
                query=maybe_transform({"chat_ids": chat_ids}, PlaygroundChatBulkDeleteParams),
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

    async def list(
        self,
        *,
        project_id: str,
        include: Optional[List[Literal["agent"]]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseWithIncluded[List[PlaygroundChatAPIResource], APIResponse[Agent]]:
        """
        List Playground Chats

        Args:
          project_id: Project ID to list playground chats for

          include: Related resources to include in the response

          limit: Maximum number of playground chats to return

          offset: Offset for pagination of playground chats

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
            cast_to=APIResponseWithIncluded[List[PlaygroundChatAPIResource], APIResponse[Agent]],
        )

    async def retrieve(
        self,
        chat_id: str,
        *,
        include: Optional[List[Literal["agent"]]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseWithIncluded[PlaygroundChatAPIResource, APIResponse[Agent]]:
        """
        Get Playground Chat

        Args:
          chat_id: Playground chat ID to retrieve

          include: Related resources to include in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
            cast_to=APIResponseWithIncluded[PlaygroundChatAPIResource, APIResponse[Agent]],
        )

    async def delete(
        self,
        chat_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[None]:
        """
        Delete Playground Chat

        Args:
          chat_id: Playground chat ID to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self.bulk_delete(
            chat_ids=[chat_id],
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    async def bulk_delete(
        self,
        *,
        chat_ids: SequenceNotStr[str],
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[None]:
        """
        Delete Playground Chats

        Args:
          chat_ids: List of playground chat IDs to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v2/playground-chats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"chat_ids": chat_ids}, PlaygroundChatBulkDeleteParams),
            ),
            cast_to=APIResponse[None],
        )


class PlaygroundChatsResourceWithRawResponse:
    def __init__(self, playground_chats: PlaygroundChatsResource) -> None:
        self._playground_chats = playground_chats

        self.list = to_raw_response_wrapper(
            playground_chats.list,
        )
        self.retrieve = to_raw_response_wrapper(
            playground_chats.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            playground_chats.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            playground_chats.bulk_delete,
        )


class AsyncPlaygroundChatsResourceWithRawResponse:
    def __init__(self, playground_chats: AsyncPlaygroundChatsResource) -> None:
        self._playground_chats = playground_chats

        self.list = async_to_raw_response_wrapper(
            playground_chats.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            playground_chats.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            playground_chats.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            playground_chats.bulk_delete,
        )


class PlaygroundChatsResourceWithStreamingResponse:
    def __init__(self, playground_chats: PlaygroundChatsResource) -> None:
        self._playground_chats = playground_chats

        self.list = to_streamed_response_wrapper(
            playground_chats.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            playground_chats.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            playground_chats.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            playground_chats.bulk_delete,
        )


class AsyncPlaygroundChatsResourceWithStreamingResponse:
    def __init__(self, playground_chats: AsyncPlaygroundChatsResource) -> None:
        self._playground_chats = playground_chats

        self.list = async_to_streamed_response_wrapper(
            playground_chats.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            playground_chats.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            playground_chats.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            playground_chats.bulk_delete,
        )
