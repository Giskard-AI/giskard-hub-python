from __future__ import annotations

from typing import List, Iterable, Optional

import httpx

from ..types import check_list_params, check_create_params, check_update_params, check_bulk_delete_params
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
from ..types.common import APIResponse
from ..types.api_response_none import APIResponseNone
from ..types.check_api_resource import CheckAPIResource

__all__ = ["ChecksResource", "AsyncChecksResource"]


class ChecksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return ChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return ChecksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        assertions: Iterable[check_create_params.Assertion],
        identifier: str,
        name: str,
        project_id: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[CheckAPIResource]:
        """
        Create Check

        Args:
          assertions: Assertions of the check

          identifier: Identifier of the check

          name: Name of the check to create

          project_id: Project ID to create the check in

          description: Description of the check to create

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/checks",
            body=maybe_transform(
                {
                    "assertions": assertions,
                    "description": description,
                    "identifier": identifier,
                    "name": name,
                    "project_id": project_id,
                },
                check_create_params.CheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[CheckAPIResource],
        )

    def retrieve(
        self,
        check_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[CheckAPIResource]:
        """
        Retrieve Check

        Args:
          check_id: ID of the check to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not check_id:
            raise ValueError(f"Expected a non-empty value for `check_id` but received {check_id!r}")
        return self._get(
            f"/v2/checks/{check_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[CheckAPIResource],
        )

    def update(
        self,
        check_id: str,
        *,
        assertions: Optional[Iterable[check_update_params.Assertion]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        identifier: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[CheckAPIResource]:
        """
        Update Check

        Args:
          check_id: ID of the check to update

          assertions: Assertions of the check

          description: Description of the check

          identifier: Identifier of the check

          name: Name of the check

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not check_id:
            raise ValueError(f"Expected a non-empty value for `check_id` but received {check_id!r}")
        return self._patch(
            f"/v2/checks/{check_id}",
            body=maybe_transform(
                {
                    "assertions": assertions,
                    "description": description,
                    "identifier": identifier,
                    "name": name,
                },
                check_update_params.CheckUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[CheckAPIResource],
        )

    def list(
        self,
        *,
        project_id: str,
        filter_builtin: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[List[CheckAPIResource]]:
        """
        List Checks

        Args:
          project_id: Project ID to list checks for

          filter_builtin: Whether to filter builtin checks

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/checks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "project_id": project_id,
                        "filter_builtin": filter_builtin,
                    },
                    check_list_params.CheckListParams,
                ),
            ),
            cast_to=APIResponse[List[CheckAPIResource]],
        )

    def delete(
        self,
        check_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseNone:
        """
        Delete Check

        Args:
          check_id: ID of the check to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not check_id:
            raise ValueError(f"Expected a non-empty value for `check_id` but received {check_id!r}")
        return self._delete(
            f"/v2/checks/{check_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseNone,
        )

    def bulk_delete(
        self,
        *,
        check_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseNone:
        """
        Bulk Delete Checks

        Args:
          check_ids: IDs of the checks to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v2/checks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"check_ids": check_ids}, check_bulk_delete_params.CheckBulkDeleteParams),
            ),
            cast_to=APIResponseNone,
        )


class AsyncChecksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncChecksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        assertions: Iterable[check_create_params.Assertion],
        identifier: str,
        name: str,
        project_id: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[CheckAPIResource]:
        """
        Create Check

        Args:
          assertions: Assertions of the check

          identifier: Identifier of the check

          name: Name of the check to create

          project_id: Project ID to create the check in

          description: Description of the check to create

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/checks",
            body=await async_maybe_transform(
                {
                    "assertions": assertions,
                    "description": description,
                    "identifier": identifier,
                    "name": name,
                    "project_id": project_id,
                },
                check_create_params.CheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[CheckAPIResource],
        )

    async def retrieve(
        self,
        check_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[CheckAPIResource]:
        """
        Retrieve Check

        Args:
          check_id: ID of the check to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not check_id:
            raise ValueError(f"Expected a non-empty value for `check_id` but received {check_id!r}")
        return await self._get(
            f"/v2/checks/{check_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[CheckAPIResource],
        )

    async def update(
        self,
        check_id: str,
        *,
        assertions: Optional[Iterable[check_update_params.Assertion]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        identifier: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[CheckAPIResource]:
        """
        Update Check

        Args:
          check_id: ID of the check to update

          assertions: Assertions of the check

          description: Description of the check

          identifier: Identifier of the check

          name: Name of the check

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not check_id:
            raise ValueError(f"Expected a non-empty value for `check_id` but received {check_id!r}")
        return await self._patch(
            f"/v2/checks/{check_id}",
            body=await async_maybe_transform(
                {
                    "assertions": assertions,
                    "description": description,
                    "identifier": identifier,
                    "name": name,
                },
                check_update_params.CheckUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[CheckAPIResource],
        )

    async def list(
        self,
        *,
        project_id: str,
        filter_builtin: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[List[CheckAPIResource]]:
        """
        List Checks

        Args:
          project_id: Project ID to list checks for

          filter_builtin: Whether to filter builtin checks

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/checks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "project_id": project_id,
                        "filter_builtin": filter_builtin,
                    },
                    check_list_params.CheckListParams,
                ),
            ),
            cast_to=APIResponse[List[CheckAPIResource]],
        )

    async def delete(
        self,
        check_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseNone:
        """
        Delete Check

        Args:
          check_id: ID of the check to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not check_id:
            raise ValueError(f"Expected a non-empty value for `check_id` but received {check_id!r}")
        return await self._delete(
            f"/v2/checks/{check_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseNone,
        )

    async def bulk_delete(
        self,
        *,
        check_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseNone:
        """
        Bulk Delete Checks

        Args:
          check_ids: IDs of the checks to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v2/checks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"check_ids": check_ids}, check_bulk_delete_params.CheckBulkDeleteParams
                ),
            ),
            cast_to=APIResponseNone,
        )


class ChecksResourceWithRawResponse:
    def __init__(self, checks: ChecksResource) -> None:
        self._checks = checks

        self.create = to_raw_response_wrapper(
            checks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            checks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            checks.update,
        )
        self.list = to_raw_response_wrapper(
            checks.list,
        )
        self.delete = to_raw_response_wrapper(
            checks.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            checks.bulk_delete,
        )


class AsyncChecksResourceWithRawResponse:
    def __init__(self, checks: AsyncChecksResource) -> None:
        self._checks = checks

        self.create = async_to_raw_response_wrapper(
            checks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            checks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            checks.update,
        )
        self.list = async_to_raw_response_wrapper(
            checks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            checks.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            checks.bulk_delete,
        )


class ChecksResourceWithStreamingResponse:
    def __init__(self, checks: ChecksResource) -> None:
        self._checks = checks

        self.create = to_streamed_response_wrapper(
            checks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            checks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            checks.update,
        )
        self.list = to_streamed_response_wrapper(
            checks.list,
        )
        self.delete = to_streamed_response_wrapper(
            checks.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            checks.bulk_delete,
        )


class AsyncChecksResourceWithStreamingResponse:
    def __init__(self, checks: AsyncChecksResource) -> None:
        self._checks = checks

        self.create = async_to_streamed_response_wrapper(
            checks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            checks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            checks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            checks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            checks.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            checks.bulk_delete,
        )
