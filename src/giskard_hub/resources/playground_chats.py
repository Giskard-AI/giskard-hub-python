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
from ._included import embed_included_list, embed_included_single
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.common import APIResponse, APIResponseWithIncluded
from ..types.playground_chat import PlaygroundChat

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
    ) -> List[PlaygroundChat]:
        """List playground chats for a project with optional pagination.

        Parameters
        ----------
        project_id : str
            Project ID to list playground chats for.
        include : list[Literal["agent"]] | None | Omit
            Related resources to embed in the response (e.g. ``["agent"]``).
        limit : int | None | Omit
            Maximum number of playground chats to return.
        offset : int | None | Omit
            Number of results to skip for pagination.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        list[PlaygroundChat]
            List of playground chats for the project.
        """
        response = self._get(
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
            cast_to=APIResponseWithIncluded[List[PlaygroundChat], APIResponse[Agent]],
        )

        if include is not omit and include:
            response = embed_included_list(response, id_getter=lambda playground_chat: playground_chat.id)

        return self._unwrap(response)

    def retrieve(
        self,
        chat_id: str,
        *,
        include: Optional[List[Literal["agent"]]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlaygroundChat:
        """Retrieve a specific playground chat by its ID.

        Parameters
        ----------
        chat_id : str
            ID of the playground chat to retrieve.
        include : list[Literal["agent"]] | None | Omit
            Related resources to embed in the response.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        PlaygroundChat
            The requested playground chat.

        Raises
        ------
        ValueError
            If ``chat_id`` is empty.
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")

        response = self._get(
            f"/v2/playground-chats/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include": include}, PlaygroundChatRetrieveParams),
            ),
            cast_to=APIResponseWithIncluded[PlaygroundChat, APIResponse[Agent]],
        )

        if include is not omit and include:
            response = embed_included_single(response, id_getter=lambda playground_chat: playground_chat.id)

        return self._unwrap(response)

    def delete(
        self,
        chat_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a single playground chat by its ID.

        Parameters
        ----------
        chat_id : str
            ID of the playground chat to delete.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Raises
        ------
        ValueError
            If ``chat_id`` is empty.
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
    ) -> None:
        """Delete multiple playground chats at once.

        Parameters
        ----------
        chat_ids : SequenceNotStr[str]
            IDs of the playground chats to delete.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.
        """
        response = self._delete(
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

        return self._unwrap(response)


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
    ) -> List[PlaygroundChat]:
        """List playground chats for a project with optional pagination.

        Parameters
        ----------
        project_id : str
            Project ID to list playground chats for.
        include : list[Literal["agent"]] | None | Omit
            Related resources to embed in the response (e.g. ``["agent"]``).
        limit : int | None | Omit
            Maximum number of playground chats to return.
        offset : int | None | Omit
            Number of results to skip for pagination.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        list[PlaygroundChat]
            List of playground chats for the project.
        """
        response = await self._get(
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
            cast_to=APIResponseWithIncluded[List[PlaygroundChat], APIResponse[Agent]],
        )

        if include is not omit and include:
            response = embed_included_list(response, id_getter=lambda playground_chat: playground_chat.id)

        return self._unwrap(response)

    async def retrieve(
        self,
        chat_id: str,
        *,
        include: Optional[List[Literal["agent"]]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlaygroundChat:
        """Retrieve a specific playground chat by its ID.

        Parameters
        ----------
        chat_id : str
            ID of the playground chat to retrieve.
        include : list[Literal["agent"]] | None | Omit
            Related resources to embed in the response.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        PlaygroundChat
            The requested playground chat.

        Raises
        ------
        ValueError
            If ``chat_id`` is empty.
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")

        response = await self._get(
            f"/v2/playground-chats/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"include": include}, PlaygroundChatRetrieveParams),
            ),
            cast_to=APIResponseWithIncluded[PlaygroundChat, APIResponse[Agent]],
        )

        if include is not omit and include:
            response = embed_included_single(response, id_getter=lambda playground_chat: playground_chat.id)

        return self._unwrap(response)

    async def delete(
        self,
        chat_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a single playground chat by its ID.

        Parameters
        ----------
        chat_id : str
            ID of the playground chat to delete.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.

        Raises
        ------
        ValueError
            If ``chat_id`` is empty.
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
    ) -> None:
        """Delete multiple playground chats at once.

        Parameters
        ----------
        chat_ids : SequenceNotStr[str]
            IDs of the playground chats to delete.

        Other Parameters
        ----------------
        extra_headers : Headers | None
            Send extra headers.
        extra_query : Query | None
            Add additional query parameters to the request.
        extra_body : Body | None
            Add additional JSON properties to the request.
        timeout : float | httpx.Timeout | None | NotGiven
            Override the client-level default timeout for this request, in seconds.
        """
        response = await self._delete(
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

        return self._unwrap(response)


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
