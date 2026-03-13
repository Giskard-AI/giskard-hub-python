from __future__ import annotations

from typing import List, Tuple, Literal, Optional, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .._included import embed_included_list, embed_included_single, embed_included_paginated
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.agent import AgentOutputParam
from ..._base_client import make_request_options
from ...types.common import APIResponse, APIPaginatedMetadata, APIPaginatedResponse, APIResponseWithIncluded
from ...types.test_case import TestCase
from ...types.evaluation import (
    ResultListParams,
    ResultFiltersParam,
    ResultOrderByParam,
    ResultSearchParams,
    ResultUpdateParams,
    TestCaseEvaluation,
    FailureCategoryParam,
    ResultRetrieveParams,
    ResultUpdateVisibilityParams,
    ResultSubmitLocalOutputParams,
)

__all__ = ["ResultsResource", "AsyncResultsResource"]


class ResultsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return ResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return ResultsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        result_id: str,
        *,
        evaluation_id: str,
        include: Optional[List[Literal["test_case"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseEvaluation:
        """
        Retrieve Evaluation Result

        Args:
          result_id: The ID of the result to retrieve

          evaluation_id: The ID of the evaluation to retrieve the result for

          include: Related resources to include in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")

        if not result_id:
            raise ValueError(f"Expected a non-empty value for `result_id` but received {result_id!r}")

        response = self._get(
            f"/v2/evaluations/{evaluation_id}/results/{result_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include": include}, ResultRetrieveParams),
            ),
            cast_to=APIResponseWithIncluded[TestCaseEvaluation, APIResponse[TestCase]],
        )

        if include is not omit and include:
            response = embed_included_single(response, id_getter=lambda result: result.id)

        return response.data

    def update(
        self,
        result_id: str,
        *,
        evaluation_id: str,
        failure_category: Optional[FailureCategoryParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseEvaluation:
        """
        Update Evaluation Result

        Args:
          result_id: The ID of the result to update

          evaluation_id: The ID of the evaluation to update the result for

          failure_category: The failure category to update the result for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")
        if not result_id:
            raise ValueError(f"Expected a non-empty value for `result_id` but received {result_id!r}")
        response = self._patch(
            f"/v2/evaluations/{evaluation_id}/results/{result_id}",
            body=maybe_transform({"failure_category": failure_category}, ResultUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[TestCaseEvaluation],
        )

        return response.data

    def list(
        self,
        evaluation_id: str,
        *,
        include: Optional[List[Literal["test_case"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[TestCaseEvaluation]:
        """
        List Evaluation Results

        Args:
          evaluation_id: The ID of the evaluation to list the results for

          include: Related resources to include in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")

        response = self._get(
            f"/v2/evaluations/{evaluation_id}/results",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include": include}, ResultListParams),
            ),
            cast_to=APIResponseWithIncluded[List[TestCaseEvaluation], APIResponse[TestCase]],
        )

        if include is not omit and include:
            response = embed_included_list(response, id_getter=lambda result: result.id)

        return response.data

    def rerun_test_case(
        self,
        result_id: str,
        *,
        evaluation_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseEvaluation:
        """
        Rerun Test Case Evaluation

        Args:
          result_id: The ID of the result to rerun the test case for

          evaluation_id: The ID of the evaluation to rerun the test case for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")
        if not result_id:
            raise ValueError(f"Expected a non-empty value for `result_id` but received {result_id!r}")
        response = self._post(
            f"/v2/evaluations/{evaluation_id}/results/{result_id}/rerun-test-case",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[TestCaseEvaluation],
        )

        return response.data

    def submit_local_output(
        self,
        result_id: str,
        *,
        evaluation_id: str,
        error: Optional[str] | Omit = omit,
        output: Optional[AgentOutputParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseEvaluation:
        """
        Submit Local Evaluation Result Output

        Args:
          result_id: The ID of the result to submit the local output for

          evaluation_id: The ID of the evaluation to submit the local output for

          error: The error to submit the local output for

          output: The output to submit the local output for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")
        if not result_id:
            raise ValueError(f"Expected a non-empty value for `result_id` but received {result_id!r}")
        response = self._post(
            f"/v2/evaluations/{evaluation_id}/results/{result_id}/submit-local-output",
            body=maybe_transform(
                {
                    "error": error,
                    "output": output,
                },
                ResultSubmitLocalOutputParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[TestCaseEvaluation],
        )

        return response.data

    @overload
    def search(
        self,
        evaluation_id: str,
        *,
        search: Optional[str] | Omit = omit,
        order_by: Optional[List[ResultOrderByParam]] | Omit = omit,
        filters: Optional[ResultFiltersParam] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        include: Optional[List[Literal["test_case"]]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: Literal[False] = False,
    ) -> List[TestCaseEvaluation]: ...

    @overload
    def search(
        self,
        evaluation_id: str,
        *,
        search: Optional[str] | Omit = omit,
        order_by: Optional[List[ResultOrderByParam]] | Omit = omit,
        filters: Optional[ResultFiltersParam] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        include: Optional[List[Literal["test_case"]]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: Literal[True],
    ) -> Tuple[List[TestCaseEvaluation], APIPaginatedMetadata]: ...

    def search(
        self,
        evaluation_id: str,
        *,
        search: Optional[str] | Omit = omit,
        order_by: Optional[List[ResultOrderByParam]] | Omit = omit,
        filters: Optional[ResultFiltersParam] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        include: Optional[List[Literal["test_case"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: bool = False,
    ) -> List[TestCaseEvaluation] | Tuple[List[TestCaseEvaluation], APIPaginatedMetadata]:
        """
        Search Evaluation Results By Filters

        Args:
          evaluation_id: The ID of the evaluation to search the results for

          search: Search query for evaluation results

          order_by: Order by criteria for evaluation results

          filters: Filter criteria for evaluation results

          limit: Maximum number of results to return

          offset: Number of results to skip

          include: Related resources to include in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")

        response = self._post(
            f"/v2/evaluations/{evaluation_id}/results/search",
            body=maybe_transform({"filters": filters, "order_by": order_by, "search": search}, ResultSearchParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "include": include,
                    },
                    ResultSearchParams,
                ),
            ),
            cast_to=APIPaginatedResponse[TestCaseEvaluation, APIResponse[TestCase]],
        )

        if include is not omit and include:
            response = embed_included_paginated(response, id_getter=lambda result: result.id)

        if include_metadata:
            return response.data, response.metadata

        return response.data

    def update_visibility(
        self,
        result_id: str,
        *,
        evaluation_id: str,
        hidden: bool,
        set_test_case_draft: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseEvaluation:
        """
        Update Evaluation Result Visibility

        Args:
          result_id: The ID of the result to update the visibility for

          evaluation_id: The ID of the evaluation to update the visibility for

          hidden: Whether the result should be hidden

          set_test_case_draft: Whether the test case should be set to draft

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")
        if not result_id:
            raise ValueError(f"Expected a non-empty value for `result_id` but received {result_id!r}")
        response = self._patch(
            f"/v2/evaluations/{evaluation_id}/results/{result_id}/visibility",
            body=maybe_transform(
                {"hidden": hidden, "set_test_case_draft": set_test_case_draft},
                ResultUpdateVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[TestCaseEvaluation],
        )

        return response.data


class AsyncResultsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncResultsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        result_id: str,
        *,
        evaluation_id: str,
        include: Optional[List[Literal["test_case"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseEvaluation:
        """
        Retrieve Evaluation Result

        Args:
          result_id: The ID of the result to retrieve

          evaluation_id: The ID of the evaluation to retrieve the result for

          include: Related resources to include in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")

        if not result_id:
            raise ValueError(f"Expected a non-empty value for `result_id` but received {result_id!r}")

        response = await self._get(
            f"/v2/evaluations/{evaluation_id}/results/{result_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"include": include}, ResultRetrieveParams),
            ),
            cast_to=APIResponseWithIncluded[TestCaseEvaluation, APIResponse[TestCase]],
        )

        if include is not omit and include:
            response = embed_included_single(response, id_getter=lambda result: result.id)

        return response.data

    async def update(
        self,
        result_id: str,
        *,
        evaluation_id: str,
        failure_category: Optional[FailureCategoryParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseEvaluation:
        """
        Update Evaluation Result

        Args:
          result_id: The ID of the result to update

          evaluation_id: The ID of the evaluation to update the result for

          failure_category: The failure category to update the result for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")
        if not result_id:
            raise ValueError(f"Expected a non-empty value for `result_id` but received {result_id!r}")
        response = await self._patch(
            f"/v2/evaluations/{evaluation_id}/results/{result_id}",
            body=await async_maybe_transform({"failure_category": failure_category}, ResultUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[TestCaseEvaluation],
        )

        return response.data

    async def list(
        self,
        evaluation_id: str,
        *,
        include: Optional[List[Literal["test_case"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[TestCaseEvaluation]:
        """
        List Evaluation Results

        Args:
          evaluation_id: The ID of the evaluation to list the results for

          include: Related resources to include in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")

        response = await self._get(
            f"/v2/evaluations/{evaluation_id}/results",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"include": include}, ResultListParams),
            ),
            cast_to=APIResponseWithIncluded[List[TestCaseEvaluation], APIResponse[TestCase]],
        )

        if include is not omit and include:
            response = embed_included_list(response, id_getter=lambda result: result.id)

        return response.data

    async def rerun_test_case(
        self,
        result_id: str,
        *,
        evaluation_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseEvaluation:
        """
        Rerun Test Case Evaluation

        Args:
          result_id: The ID of the result to rerun the test case for

          evaluation_id: The ID of the evaluation to rerun the test case for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")
        if not result_id:
            raise ValueError(f"Expected a non-empty value for `result_id` but received {result_id!r}")
        response = await self._post(
            f"/v2/evaluations/{evaluation_id}/results/{result_id}/rerun-test-case",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[TestCaseEvaluation],
        )

        return response.data

    async def submit_local_output(
        self,
        result_id: str,
        *,
        evaluation_id: str,
        error: Optional[str] | Omit = omit,
        output: Optional[AgentOutputParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseEvaluation:
        """
        Submit Local Evaluation Result Output

        Args:
          result_id: The ID of the result to submit the local output for

          evaluation_id: The ID of the evaluation to submit the local output for

          error: The error to submit the local output for

          output: The output to submit the local output for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")
        if not result_id:
            raise ValueError(f"Expected a non-empty value for `result_id` but received {result_id!r}")
        response = await self._post(
            f"/v2/evaluations/{evaluation_id}/results/{result_id}/submit-local-output",
            body=await async_maybe_transform(
                {
                    "error": error,
                    "output": output,
                },
                ResultSubmitLocalOutputParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[TestCaseEvaluation],
        )

        return response.data

    @overload
    async def search(
        self,
        evaluation_id: str,
        *,
        search: Optional[str] | Omit = omit,
        order_by: Optional[List[ResultOrderByParam]] | Omit = omit,
        filters: Optional[ResultFiltersParam] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        include: Optional[List[Literal["test_case"]]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: Literal[False] = False,
    ) -> List[TestCaseEvaluation]: ...

    @overload
    async def search(
        self,
        evaluation_id: str,
        *,
        search: Optional[str] | Omit = omit,
        order_by: Optional[List[ResultOrderByParam]] | Omit = omit,
        filters: Optional[ResultFiltersParam] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        include: Optional[List[Literal["test_case"]]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: Literal[True],
    ) -> Tuple[List[TestCaseEvaluation], APIPaginatedMetadata]: ...

    async def search(
        self,
        evaluation_id: str,
        *,
        search: Optional[str] | Omit = omit,
        order_by: Optional[List[ResultOrderByParam]] | Omit = omit,
        filters: Optional[ResultFiltersParam] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        include: Optional[List[Literal["test_case"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: bool = False,
    ) -> List[TestCaseEvaluation] | Tuple[List[TestCaseEvaluation], APIPaginatedMetadata]:
        """
        Search Evaluation Results By Filters

        Args:
          evaluation_id: The ID of the evaluation to search the results for

          search: Search query for evaluation results

          order_by: Order by criteria for evaluation results

          filters: Filter criteria for evaluation results

          limit: Maximum number of results to return

          offset: Number of results to skip

          include: Related resources to include in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")

        response = await self._post(
            f"/v2/evaluations/{evaluation_id}/results/search",
            body=await async_maybe_transform(
                {"filters": filters, "order_by": order_by, "search": search}, ResultSearchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "include": include,
                    },
                    ResultSearchParams,
                ),
            ),
            cast_to=APIPaginatedResponse[TestCaseEvaluation, APIResponse[TestCase]],
        )

        if include is not omit and include:
            response = embed_included_paginated(response, id_getter=lambda result: result.id)

        if include_metadata:
            return response.data, response.metadata

        return response.data

    async def update_visibility(
        self,
        result_id: str,
        *,
        evaluation_id: str,
        hidden: bool,
        set_test_case_draft: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseEvaluation:
        """
        Update Evaluation Result Visibility

        Args:
          result_id: The ID of the result to update the visibility for

          evaluation_id: The ID of the evaluation to update the visibility for

          hidden: Whether the result should be hidden

          set_test_case_draft: Whether the test case should be set to draft

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")
        if not result_id:
            raise ValueError(f"Expected a non-empty value for `result_id` but received {result_id!r}")
        response = await self._patch(
            f"/v2/evaluations/{evaluation_id}/results/{result_id}/visibility",
            body=await async_maybe_transform(
                {"hidden": hidden, "set_test_case_draft": set_test_case_draft},
                ResultUpdateVisibilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[TestCaseEvaluation],
        )

        return response.data


class ResultsResourceWithRawResponse:
    def __init__(self, results: ResultsResource) -> None:
        self._results = results

        self.retrieve = to_raw_response_wrapper(
            results.retrieve,
        )
        self.update = to_raw_response_wrapper(
            results.update,
        )
        self.list = to_raw_response_wrapper(
            results.list,
        )
        self.rerun_test_case = to_raw_response_wrapper(
            results.rerun_test_case,
        )
        self.submit_local_output = to_raw_response_wrapper(
            results.submit_local_output,
        )
        self.search = to_raw_response_wrapper(
            results.search,
        )
        self.update_visibility = to_raw_response_wrapper(
            results.update_visibility,
        )


class AsyncResultsResourceWithRawResponse:
    def __init__(self, results: AsyncResultsResource) -> None:
        self._results = results

        self.retrieve = async_to_raw_response_wrapper(
            results.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            results.update,
        )
        self.list = async_to_raw_response_wrapper(
            results.list,
        )
        self.rerun_test_case = async_to_raw_response_wrapper(
            results.rerun_test_case,
        )
        self.submit_local_output = async_to_raw_response_wrapper(
            results.submit_local_output,
        )
        self.search = async_to_raw_response_wrapper(
            results.search,
        )
        self.update_visibility = async_to_raw_response_wrapper(
            results.update_visibility,
        )


class ResultsResourceWithStreamingResponse:
    def __init__(self, results: ResultsResource) -> None:
        self._results = results

        self.retrieve = to_streamed_response_wrapper(
            results.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            results.update,
        )
        self.list = to_streamed_response_wrapper(
            results.list,
        )
        self.rerun_test_case = to_streamed_response_wrapper(
            results.rerun_test_case,
        )
        self.submit_local_output = to_streamed_response_wrapper(
            results.submit_local_output,
        )
        self.search = to_streamed_response_wrapper(
            results.search,
        )
        self.update_visibility = to_streamed_response_wrapper(
            results.update_visibility,
        )


class AsyncResultsResourceWithStreamingResponse:
    def __init__(self, results: AsyncResultsResource) -> None:
        self._results = results

        self.retrieve = async_to_streamed_response_wrapper(
            results.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            results.update,
        )
        self.list = async_to_streamed_response_wrapper(
            results.list,
        )
        self.rerun_test_case = async_to_streamed_response_wrapper(
            results.rerun_test_case,
        )
        self.submit_local_output = async_to_streamed_response_wrapper(
            results.submit_local_output,
        )
        self.search = async_to_streamed_response_wrapper(
            results.search,
        )
        self.update_visibility = async_to_streamed_response_wrapper(
            results.update_visibility,
        )
