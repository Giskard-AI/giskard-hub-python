from __future__ import annotations

from typing import List

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.scan import ScanProbe, ScanProbeAttempt
from ..._base_client import make_request_options
from ...types.common import APIResponse

__all__ = ["ProbesResource", "AsyncProbesResource"]


class ProbesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProbesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return ProbesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProbesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return ProbesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        probe_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScanProbe:
        """
        Retrieve Scan Probe

        Args:
          probe_id: Scan Probe Result ID to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not probe_id:
            raise ValueError(f"Expected a non-empty value for `probe_id` but received {probe_id!r}")
        response = self._get(
            f"/v2/scan-probes/{probe_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[ScanProbe],
        )

        return self._unwrap(response)

    def list_attempts(
        self,
        probe_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[ScanProbeAttempt]:
        """
        List Scan Probe Attempts

        Args:
          probe_id: Scan Probe Result ID to list attempts

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not probe_id:
            raise ValueError(f"Expected a non-empty value for `probe_id` but received {probe_id!r}")
        response = self._get(
            f"/v2/scan-probes/{probe_id}/attempts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[ScanProbeAttempt]],
        )

        return self._unwrap(response)


class AsyncProbesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProbesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProbesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProbesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncProbesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        probe_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScanProbe:
        """
        Retrieve Scan Probe

        Args:
          probe_id: Scan Probe Result ID to list attempts

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not probe_id:
            raise ValueError(f"Expected a non-empty value for `probe_id` but received {probe_id!r}")
        response = await self._get(
            f"/v2/scan-probes/{probe_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[ScanProbe],
        )

        return self._unwrap(response)

    async def list_attempts(
        self,
        probe_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[ScanProbeAttempt]:
        """
        List Scan Probe Attempts

        Args:
          probe_id: Scan Probe Result ID to list attempts

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not probe_id:
            raise ValueError(f"Expected a non-empty value for `probe_id` but received {probe_id!r}")
        response = await self._get(
            f"/v2/scan-probes/{probe_id}/attempts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[ScanProbeAttempt]],
        )

        return self._unwrap(response)


class ProbesResourceWithRawResponse:
    def __init__(self, probes: ProbesResource) -> None:
        self._probes = probes

        self.retrieve = to_raw_response_wrapper(
            probes.retrieve,
        )
        self.list_attempts = to_raw_response_wrapper(
            probes.list_attempts,
        )


class AsyncProbesResourceWithRawResponse:
    def __init__(self, probes: AsyncProbesResource) -> None:
        self._probes = probes

        self.retrieve = async_to_raw_response_wrapper(
            probes.retrieve,
        )
        self.list_attempts = async_to_raw_response_wrapper(
            probes.list_attempts,
        )


class ProbesResourceWithStreamingResponse:
    def __init__(self, probes: ProbesResource) -> None:
        self._probes = probes

        self.retrieve = to_streamed_response_wrapper(
            probes.retrieve,
        )
        self.list_attempts = to_streamed_response_wrapper(
            probes.list_attempts,
        )


class AsyncProbesResourceWithStreamingResponse:
    def __init__(self, probes: AsyncProbesResource) -> None:
        self._probes = probes

        self.retrieve = async_to_streamed_response_wrapper(
            probes.retrieve,
        )
        self.list_attempts = async_to_streamed_response_wrapper(
            probes.list_attempts,
        )
