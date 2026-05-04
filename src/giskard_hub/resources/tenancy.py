from __future__ import annotations

from typing import Any, Dict

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.tenancy import (
    HealthStatus,
    FindTenantRequest,
    FindTenantResponse,
)

__all__ = ["TenancyResource", "AsyncTenancyResource"]


class TenancyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TenancyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return TenancyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TenancyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return TenancyResourceWithStreamingResponse(self)

    def discovery(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dict[str, Any]:
        """Discovery endpoint used to configure auth per host.

        Returns public OIDC discovery inputs for the tenant.

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
        dict[str, Any]
            OIDC discovery configuration.
        """
        return self._get(
            "/v2/tenancy/discovery",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=dict,
        )

    def health(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HealthStatus:
        """Tenant-scoped health endpoint.

        Checks tenant DB connectivity and tenant Keycloak realm reachability.

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
        HealthStatus
            Health status information including version and service statuses.
        """
        return self._get(
            "/v2/tenancy/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthStatus,
        )

    def find_tenant(
        self,
        *,
        email: str,
        turnstile_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindTenantResponse:
        """Find which tenant(s) an email belongs to.

        Cross-tenant email lookup for the tenant finder portal.

        Parameters
        ----------
        email : str
            Email address to search for.
        turnstile_token : str
            Cloudflare Turnstile token for verification.

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
        FindTenantResponse
            List of tenants associated with the email address.
        """
        return self._post(
            "/v2/tenancy/find-tenant",
            body=maybe_transform(
                {
                    "email": email,
                    "turnstile_token": turnstile_token,
                },
                FindTenantRequest,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FindTenantResponse,
        )


class AsyncTenancyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTenancyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTenancyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTenancyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncTenancyResourceWithStreamingResponse(self)

    async def discovery(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dict[str, Any]:
        """Discovery endpoint used to configure auth per host.

        Returns public OIDC discovery inputs for the tenant.

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
        dict[str, Any]
            OIDC discovery configuration.
        """
        return await self._get(
            "/v2/tenancy/discovery",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=dict,
        )

    async def health(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HealthStatus:
        """Tenant-scoped health endpoint.

        Checks tenant DB connectivity and tenant Keycloak realm reachability.

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
        HealthStatus
            Health status information including version and service statuses.
        """
        return await self._get(
            "/v2/tenancy/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HealthStatus,
        )

    async def find_tenant(
        self,
        *,
        email: str,
        turnstile_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindTenantResponse:
        """Find which tenant(s) an email belongs to.

        Cross-tenant email lookup for the tenant finder portal.

        Parameters
        ----------
        email : str
            Email address to search for.
        turnstile_token : str
            Cloudflare Turnstile token for verification.

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
        FindTenantResponse
            List of tenants associated with the email address.
        """
        return await self._post(
            "/v2/tenancy/find-tenant",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "turnstile_token": turnstile_token,
                },
                FindTenantRequest,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FindTenantResponse,
        )


class TenancyResourceWithRawResponse:
    def __init__(self, tenancy: TenancyResource) -> None:
        self._tenancy = tenancy

        self.discovery = to_raw_response_wrapper(
            tenancy.discovery,
        )
        self.health = to_raw_response_wrapper(
            tenancy.health,
        )
        self.find_tenant = to_raw_response_wrapper(
            tenancy.find_tenant,
        )


class AsyncTenancyResourceWithRawResponse:
    def __init__(self, tenancy: AsyncTenancyResource) -> None:
        self._tenancy = tenancy

        self.discovery = async_to_raw_response_wrapper(
            tenancy.discovery,
        )
        self.health = async_to_raw_response_wrapper(
            tenancy.health,
        )
        self.find_tenant = async_to_raw_response_wrapper(
            tenancy.find_tenant,
        )


class TenancyResourceWithStreamingResponse:
    def __init__(self, tenancy: TenancyResource) -> None:
        self._tenancy = tenancy

        self.discovery = to_streamed_response_wrapper(
            tenancy.discovery,
        )
        self.health = to_streamed_response_wrapper(
            tenancy.health,
        )
        self.find_tenant = to_streamed_response_wrapper(
            tenancy.find_tenant,
        )


class AsyncTenancyResourceWithStreamingResponse:
    def __init__(self, tenancy: AsyncTenancyResource) -> None:
        self._tenancy = tenancy

        self.discovery = async_to_streamed_response_wrapper(
            tenancy.discovery,
        )
        self.health = async_to_streamed_response_wrapper(
            tenancy.health,
        )
        self.find_tenant = async_to_streamed_response_wrapper(
            tenancy.find_tenant,
        )
