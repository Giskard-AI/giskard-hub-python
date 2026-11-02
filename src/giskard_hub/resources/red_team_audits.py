from __future__ import annotations

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.common import APIResponse
from ..types.credit import CreditEstimate
from ..types.red_team_audit import RedTeamAuditCoverageMode, RedTeamAuditEstimateParams

__all__ = ["RedTeamAuditsResource", "AsyncRedTeamAuditsResource"]


class RedTeamAuditsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RedTeamAuditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return RedTeamAuditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RedTeamAuditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return RedTeamAuditsResourceWithStreamingResponse(self)

    def estimate(
        self,
        *,
        mode: RedTeamAuditCoverageMode | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditEstimate:
        """Estimate the credit cost of a red team audit.

        Parameters
        ----------
        mode : Literal["regular", "light"] | Omit
            Coverage mode to price. Defaults to ``regular`` on the server when omitted.

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
        CreditEstimate
            Estimated credit cost of the audit.
        """
        response = self._post(
            "/v2/red-team-audits/estimate",
            body=maybe_transform(
                {
                    "mode": mode,
                },
                RedTeamAuditEstimateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[CreditEstimate],
        )

        return self._unwrap(response)


class AsyncRedTeamAuditsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRedTeamAuditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRedTeamAuditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRedTeamAuditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncRedTeamAuditsResourceWithStreamingResponse(self)

    async def estimate(
        self,
        *,
        mode: RedTeamAuditCoverageMode | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditEstimate:
        """Estimate the credit cost of a red team audit.

        Parameters
        ----------
        mode : Literal["regular", "light"] | Omit
            Coverage mode to price. Defaults to ``regular`` on the server when omitted.

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
        CreditEstimate
            Estimated credit cost of the audit.
        """
        response = await self._post(
            "/v2/red-team-audits/estimate",
            body=await async_maybe_transform(
                {
                    "mode": mode,
                },
                RedTeamAuditEstimateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[CreditEstimate],
        )

        return self._unwrap(response)


class RedTeamAuditsResourceWithRawResponse:
    def __init__(self, red_team_audits: RedTeamAuditsResource) -> None:
        self._red_team_audits = red_team_audits

        self.estimate = to_raw_response_wrapper(
            red_team_audits.estimate,
        )


class AsyncRedTeamAuditsResourceWithRawResponse:
    def __init__(self, red_team_audits: AsyncRedTeamAuditsResource) -> None:
        self._red_team_audits = red_team_audits

        self.estimate = async_to_raw_response_wrapper(
            red_team_audits.estimate,
        )


class RedTeamAuditsResourceWithStreamingResponse:
    def __init__(self, red_team_audits: RedTeamAuditsResource) -> None:
        self._red_team_audits = red_team_audits

        self.estimate = to_streamed_response_wrapper(
            red_team_audits.estimate,
        )


class AsyncRedTeamAuditsResourceWithStreamingResponse:
    def __init__(self, red_team_audits: AsyncRedTeamAuditsResource) -> None:
        self._red_team_audits = red_team_audits

        self.estimate = async_to_streamed_response_wrapper(
            red_team_audits.estimate,
        )
