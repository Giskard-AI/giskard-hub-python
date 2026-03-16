from __future__ import annotations

import httpx

from ...types import TestCaseComment
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.common import APIResponse
from ...types.test_case import CommentAddParams, CommentEditParams

__all__ = ["CommentsResource", "AsyncCommentsResource"]


class CommentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return CommentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return CommentsResourceWithStreamingResponse(self)

    def delete(
        self,
        comment_id: str,
        *,
        test_case_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Test Case Comment

        Args:
          comment_id: Comment ID to delete

          test_case_id: Test Case ID to delete the comment from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_id:
            raise ValueError(f"Expected a non-empty value for `test_case_id` but received {test_case_id!r}")
        if not comment_id:
            raise ValueError(f"Expected a non-empty value for `comment_id` but received {comment_id!r}")
        response = self._delete(
            f"/v2/test-cases/{test_case_id}/comments/{comment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    def add(
        self,
        test_case_id: str,
        *,
        content: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseComment:
        """
        Add Test Case Comment

        Args:
          test_case_id: Test Case ID to add the comment to

          content: Content of the comment to add

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_id:
            raise ValueError(f"Expected a non-empty value for `test_case_id` but received {test_case_id!r}")
        response = self._post(
            f"/v2/test-cases/{test_case_id}/comments",
            body=maybe_transform({"comment": content}, CommentAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[TestCaseComment],
        )

        return self._unwrap(response)

    def edit(
        self,
        comment_id: str,
        *,
        test_case_id: str,
        content: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseComment:
        """
        Edit Test Case Comment

        Args:
          comment_id: Comment ID to edit

          test_case_id: Test Case ID to edit the comment from

          content: Content of the comment to edit

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_id:
            raise ValueError(f"Expected a non-empty value for `test_case_id` but received {test_case_id!r}")
        if not comment_id:
            raise ValueError(f"Expected a non-empty value for `comment_id` but received {comment_id!r}")
        response = self._patch(
            f"/v2/test-cases/{test_case_id}/comments/{comment_id}",
            body=maybe_transform({"comment": content}, CommentEditParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[TestCaseComment],
        )

        return self._unwrap(response)


class AsyncCommentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncCommentsResourceWithStreamingResponse(self)

    async def delete(
        self,
        comment_id: str,
        *,
        test_case_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Test Case Comment

        Args:
          comment_id: Comment ID to delete

          test_case_id: Test Case ID to delete the comment from

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_id:
            raise ValueError(f"Expected a non-empty value for `test_case_id` but received {test_case_id!r}")
        if not comment_id:
            raise ValueError(f"Expected a non-empty value for `comment_id` but received {comment_id!r}")
        response = await self._delete(
            f"/v2/test-cases/{test_case_id}/comments/{comment_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    async def add(
        self,
        test_case_id: str,
        *,
        content: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseComment:
        """
        Add Test Case Comment

        Args:
          test_case_id: Test Case ID to add the comment to

          content: Content of the comment to add

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_id:
            raise ValueError(f"Expected a non-empty value for `test_case_id` but received {test_case_id!r}")
        response = await self._post(
            f"/v2/test-cases/{test_case_id}/comments",
            body=await async_maybe_transform({"comment": content}, CommentAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[TestCaseComment],
        )

        return self._unwrap(response)

    async def edit(
        self,
        comment_id: str,
        *,
        test_case_id: str,
        content: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseComment:
        """
        Edit Test Case Comment

        Args:
          comment_id: Comment ID to edit

          test_case_id: Test Case ID to edit the comment from

          content: Content of the comment to edit

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_id:
            raise ValueError(f"Expected a non-empty value for `test_case_id` but received {test_case_id!r}")
        if not comment_id:
            raise ValueError(f"Expected a non-empty value for `comment_id` but received {comment_id!r}")
        response = await self._patch(
            f"/v2/test-cases/{test_case_id}/comments/{comment_id}",
            body=await async_maybe_transform({"comment": content}, CommentEditParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[TestCaseComment],
        )

        return self._unwrap(response)


class CommentsResourceWithRawResponse:
    def __init__(self, comments: CommentsResource) -> None:
        self._comments = comments

        self.delete = to_raw_response_wrapper(
            comments.delete,
        )
        self.add = to_raw_response_wrapper(
            comments.add,
        )
        self.edit = to_raw_response_wrapper(
            comments.edit,
        )


class AsyncCommentsResourceWithRawResponse:
    def __init__(self, comments: AsyncCommentsResource) -> None:
        self._comments = comments

        self.delete = async_to_raw_response_wrapper(
            comments.delete,
        )
        self.add = async_to_raw_response_wrapper(
            comments.add,
        )
        self.edit = async_to_raw_response_wrapper(
            comments.edit,
        )


class CommentsResourceWithStreamingResponse:
    def __init__(self, comments: CommentsResource) -> None:
        self._comments = comments

        self.delete = to_streamed_response_wrapper(
            comments.delete,
        )
        self.add = to_streamed_response_wrapper(
            comments.add,
        )
        self.edit = to_streamed_response_wrapper(
            comments.edit,
        )


class AsyncCommentsResourceWithStreamingResponse:
    def __init__(self, comments: AsyncCommentsResource) -> None:
        self._comments = comments

        self.delete = async_to_streamed_response_wrapper(
            comments.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            comments.add,
        )
        self.edit = async_to_streamed_response_wrapper(
            comments.edit,
        )
