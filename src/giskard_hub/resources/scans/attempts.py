from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.scans import Severity, ReviewStatus, attempt_update_params
from ..._base_client import make_request_options
from ...types.scans.attempt_update_response import AttemptUpdateResponse

__all__ = ["AttemptsResource", "AsyncAttemptsResource"]


class AttemptsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AttemptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AttemptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttemptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AttemptsResourceWithStreamingResponse(self)

    def update(
        self,
        probe_attempt_id: str,
        *,
        review_status: Optional[ReviewStatus] | Omit = omit,
        severity: Optional[Severity] | Omit = omit,
        successful: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttemptUpdateResponse:
        """
        Update Scan Probe Attempt

        Args:
          probe_attempt_id: Scan Probe Attempt ID to update

          review_status: Review status of the attempt

          severity: Severity of the attempt

          successful: Whether the attempt was successful

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not probe_attempt_id:
            raise ValueError(f"Expected a non-empty value for `probe_attempt_id` but received {probe_attempt_id!r}")
        return self._patch(
            f"/v2/scan-attempts/{probe_attempt_id}",
            body=maybe_transform(
                {
                    "review_status": review_status,
                    "severity": severity,
                    "successful": successful,
                },
                attempt_update_params.AttemptUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttemptUpdateResponse,
        )


class AsyncAttemptsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAttemptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAttemptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttemptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncAttemptsResourceWithStreamingResponse(self)

    async def update(
        self,
        probe_attempt_id: str,
        *,
        review_status: Optional[ReviewStatus] | Omit = omit,
        severity: Optional[Severity] | Omit = omit,
        successful: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AttemptUpdateResponse:
        """
        Update Scan Probe Attempt

        Args:
          probe_attempt_id: Scan Probe Attempt ID to update

          review_status: Review status of the attempt

          severity: Severity of the attempt

          successful: Whether the attempt was successful

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not probe_attempt_id:
            raise ValueError(f"Expected a non-empty value for `probe_attempt_id` but received {probe_attempt_id!r}")
        return await self._patch(
            f"/v2/scan-attempts/{probe_attempt_id}",
            body=await async_maybe_transform(
                {
                    "review_status": review_status,
                    "severity": severity,
                    "successful": successful,
                },
                attempt_update_params.AttemptUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttemptUpdateResponse,
        )


class AttemptsResourceWithRawResponse:
    def __init__(self, attempts: AttemptsResource) -> None:
        self._attempts = attempts

        self.update = to_raw_response_wrapper(
            attempts.update,
        )


class AsyncAttemptsResourceWithRawResponse:
    def __init__(self, attempts: AsyncAttemptsResource) -> None:
        self._attempts = attempts

        self.update = async_to_raw_response_wrapper(
            attempts.update,
        )


class AttemptsResourceWithStreamingResponse:
    def __init__(self, attempts: AttemptsResource) -> None:
        self._attempts = attempts

        self.update = to_streamed_response_wrapper(
            attempts.update,
        )


class AsyncAttemptsResourceWithStreamingResponse:
    def __init__(self, attempts: AsyncAttemptsResource) -> None:
        self._attempts = attempts

        self.update = async_to_streamed_response_wrapper(
            attempts.update,
        )
