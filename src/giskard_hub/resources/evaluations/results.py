from __future__ import annotations

from typing import List, Tuple, Literal, Optional, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .._included import embed_included_single, embed_included_paginated
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
        """Retrieve a specific evaluation result by its ID.

        Parameters
        ----------
        result_id : str
            The ID of the result to retrieve.
        evaluation_id : str
            The ID of the evaluation to retrieve the result for.
        include : Optional[List[Literal["test_case"]]], optional
            Related resources to include in response.

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
        TestCaseEvaluation
            The retrieved evaluation result.
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

        return self._unwrap(response)

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
        """Update the failure category of an evaluation result.

        Parameters
        ----------
        result_id : str
            The ID of the result to update.
        evaluation_id : str
            The ID of the evaluation to update the result for.
        failure_category : Optional[FailureCategoryParam], optional
            The failure category to update the result for.

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
        TestCaseEvaluation
            The updated evaluation result.

        Raises
        ------
        ValueError
            If ``evaluation_id`` or ``result_id`` is empty.
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

        return self._unwrap(response)

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
        """Rerun a single test case evaluation to get fresh results.

        Parameters
        ----------
        result_id : str
            The ID of the result to rerun the test case for.
        evaluation_id : str
            The ID of the evaluation to rerun the test case for.

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
        TestCaseEvaluation
            The rerun evaluation result.

        Raises
        ------
        ValueError
            If ``evaluation_id`` or ``result_id`` is empty.
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

        return self._unwrap(response)

    def submit_local_output(
        self,
        result_id: str,
        *,
        evaluation_id: str,
        error: Optional[str] | Omit = omit,
        agent_output: Optional[AgentOutputParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseEvaluation:
        """Submit a locally-generated agent output for evaluation and scoring.

        Parameters
        ----------
        result_id : str
            The ID of the result to submit the local output for.
        evaluation_id : str
            The ID of the evaluation to submit the local output for.
        error : Optional[str], optional
            The error to submit the local output for.
        agent_output : Optional[AgentOutputParam], optional
            The output to submit the local output for.

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
        TestCaseEvaluation
            The evaluation result with the submitted output.

        Raises
        ------
        ValueError
            If ``evaluation_id`` or ``result_id`` is empty.
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
                    "output": agent_output,
                },
                ResultSubmitLocalOutputParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[TestCaseEvaluation],
        )

        return self._unwrap(response)

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
        """List all results for a given evaluation.

        Fetches every page via :meth:`search` (same as an unfiltered search).

        Parameters
        ----------
        evaluation_id : str
            The ID of the evaluation to list the results for.
        include : Optional[List[Literal["test_case"]]], optional
            Related resources to include in response.

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
        List[TestCaseEvaluation]
            A list of evaluation results.

        Raises
        ------
        ValueError
            If ``evaluation_id`` is empty.
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")

        page_limit = 100
        all_items: List[TestCaseEvaluation] = []
        offset = 0
        while True:
            page, meta = self.search(
                evaluation_id,
                limit=page_limit,
                offset=offset,
                include=include,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                include_metadata=True,
            )
            all_items.extend(page)
            next_offset = meta.offset + meta.count
            if next_offset >= meta.total or not page:
                break
            offset = next_offset
        return all_items

    @overload
    def search(
        self,
        evaluation_id: str,
        *,
        query: Optional[str] | Omit = omit,
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
        query: Optional[str] | Omit = omit,
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
        query: Optional[str] | Omit = omit,
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
        """Search evaluation results using filters, sorting, and pagination.

        Parameters
        ----------
        evaluation_id : str
            The ID of the evaluation to search the results for.
        query : Optional[str], optional
            Search query for evaluation results.
        order_by : Optional[List[ResultOrderByParam]], optional
            Order by criteria for evaluation results.
        filters : Optional[ResultFiltersParam], optional
            Filter criteria for evaluation results.
        limit : Optional[int], optional
            Maximum number of results to return.
        offset : Optional[int], optional
            Number of results to skip.
        include : Optional[List[Literal["test_case"]]], optional
            Related resources to include in response.

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
        List[TestCaseEvaluation] | Tuple[List[TestCaseEvaluation], APIPaginatedMetadata]
            The search results, optionally with pagination metadata.

        Raises
        ------
        ValueError
            If ``evaluation_id`` is empty.
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")

        response = self._post(
            f"/v2/evaluations/{evaluation_id}/results/search",
            body=maybe_transform({"filters": filters, "order_by": order_by, "search": query}, ResultSearchParams),
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

        return self._unwrap_paginated(response, include_metadata)

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
        """Update the visibility of an evaluation result, optionally setting the linked test case to draft.

        Parameters
        ----------
        result_id : str
            The ID of the result to update the visibility for.
        evaluation_id : str
            The ID of the evaluation to update the visibility for.
        hidden : bool
            Whether the result should be hidden.
        set_test_case_draft : Optional[bool], optional
            Whether the test case should be set to draft.

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
        TestCaseEvaluation
            The updated evaluation result.

        Raises
        ------
        ValueError
            If ``evaluation_id`` or ``result_id`` is empty.
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

        return self._unwrap(response)


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
        """Retrieve a specific evaluation result by its ID.

        Parameters
        ----------
        result_id : str
            The ID of the result to retrieve.
        evaluation_id : str
            The ID of the evaluation to retrieve the result for.
        include : Optional[List[Literal["test_case"]]], optional
            Related resources to include in response.

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
        TestCaseEvaluation
            The retrieved evaluation result.
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

        return self._unwrap(response)

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
        """Update the failure category of an evaluation result.

        Parameters
        ----------
        result_id : str
            The ID of the result to update.
        evaluation_id : str
            The ID of the evaluation to update the result for.
        failure_category : Optional[FailureCategoryParam], optional
            The failure category to update the result for.

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
        TestCaseEvaluation
            The updated evaluation result.

        Raises
        ------
        ValueError
            If ``evaluation_id`` or ``result_id`` is empty.
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

        return self._unwrap(response)

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
        """Rerun a single test case evaluation to get fresh results.

        Parameters
        ----------
        result_id : str
            The ID of the result to rerun the test case for.
        evaluation_id : str
            The ID of the evaluation to rerun the test case for.

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
        TestCaseEvaluation
            The rerun evaluation result.

        Raises
        ------
        ValueError
            If ``evaluation_id`` or ``result_id`` is empty.
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

        return self._unwrap(response)

    async def submit_local_output(
        self,
        result_id: str,
        *,
        evaluation_id: str,
        error: Optional[str] | Omit = omit,
        agent_output: Optional[AgentOutputParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseEvaluation:
        """Submit a locally-generated agent output for evaluation and scoring.

        Parameters
        ----------
        result_id : str
            The ID of the result to submit the local output for.
        evaluation_id : str
            The ID of the evaluation to submit the local output for.
        error : Optional[str], optional
            The error to submit the local output for.
        agent_output : Optional[AgentOutputParam], optional
            The output to submit the local output for.

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
        TestCaseEvaluation
            The evaluation result with the submitted output.

        Raises
        ------
        ValueError
            If ``evaluation_id`` or ``result_id`` is empty.
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
                    "output": agent_output,
                },
                ResultSubmitLocalOutputParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[TestCaseEvaluation],
        )

        return self._unwrap(response)

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
        """List all results for a given evaluation.

        Fetches every page via :meth:`search` (same as an unfiltered search).

        Parameters
        ----------
        evaluation_id : str
            The ID of the evaluation to list the results for.
        include : Optional[List[Literal["test_case"]]], optional
            Related resources to include in response.

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
        List[TestCaseEvaluation]
            A list of evaluation results.

        Raises
        ------
        ValueError
            If ``evaluation_id`` is empty.
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")

        page_limit = 100
        all_items: List[TestCaseEvaluation] = []
        offset = 0
        while True:
            page, meta = await self.search(
                evaluation_id,
                limit=page_limit,
                offset=offset,
                include=include,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                include_metadata=True,
            )
            all_items.extend(page)
            next_offset = meta.offset + meta.count
            if next_offset >= meta.total or not page:
                break
            offset = next_offset
        return all_items

    @overload
    async def search(
        self,
        evaluation_id: str,
        *,
        query: Optional[str] | Omit = omit,
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
        query: Optional[str] | Omit = omit,
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
        query: Optional[str] | Omit = omit,
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
        """Search evaluation results using filters, sorting, and pagination.

        Parameters
        ----------
        evaluation_id : str
            The ID of the evaluation to search the results for.
        query : Optional[str], optional
            Search query for evaluation results.
        order_by : Optional[List[ResultOrderByParam]], optional
            Order by criteria for evaluation results.
        filters : Optional[ResultFiltersParam], optional
            Filter criteria for evaluation results.
        limit : Optional[int], optional
            Maximum number of results to return.
        offset : Optional[int], optional
            Number of results to skip.
        include : Optional[List[Literal["test_case"]]], optional
            Related resources to include in response.

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
        List[TestCaseEvaluation] | Tuple[List[TestCaseEvaluation], APIPaginatedMetadata]
            The search results, optionally with pagination metadata.

        Raises
        ------
        ValueError
            If ``evaluation_id`` is empty.
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")

        response = await self._post(
            f"/v2/evaluations/{evaluation_id}/results/search",
            body=await async_maybe_transform(
                {"filters": filters, "order_by": order_by, "search": query}, ResultSearchParams
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

        return self._unwrap_paginated(response, include_metadata)

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
        """Update the visibility of an evaluation result, optionally setting the linked test case to draft.

        Parameters
        ----------
        result_id : str
            The ID of the result to update the visibility for.
        evaluation_id : str
            The ID of the evaluation to update the visibility for.
        hidden : bool
            Whether the result should be hidden.
        set_test_case_draft : Optional[bool], optional
            Whether the test case should be set to draft.

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
        TestCaseEvaluation
            The updated evaluation result.

        Raises
        ------
        ValueError
            If ``evaluation_id`` or ``result_id`` is empty.
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

        return self._unwrap(response)


class ResultsResourceWithRawResponse:
    def __init__(self, results: ResultsResource) -> None:
        self._results = results

        self.retrieve = to_raw_response_wrapper(
            results.retrieve,
        )
        self.update = to_raw_response_wrapper(
            results.update,
        )
        self.rerun_test_case = to_raw_response_wrapper(
            results.rerun_test_case,
        )
        self.submit_local_output = to_raw_response_wrapper(
            results.submit_local_output,
        )
        self.list = to_raw_response_wrapper(
            results.list,
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
        self.rerun_test_case = async_to_raw_response_wrapper(
            results.rerun_test_case,
        )
        self.submit_local_output = async_to_raw_response_wrapper(
            results.submit_local_output,
        )
        self.list = async_to_raw_response_wrapper(
            results.list,
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
        self.rerun_test_case = to_streamed_response_wrapper(
            results.rerun_test_case,
        )
        self.submit_local_output = to_streamed_response_wrapper(
            results.submit_local_output,
        )
        self.list = to_streamed_response_wrapper(
            results.list,
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
        self.rerun_test_case = async_to_streamed_response_wrapper(
            results.rerun_test_case,
        )
        self.submit_local_output = async_to_streamed_response_wrapper(
            results.submit_local_output,
        )
        self.list = async_to_streamed_response_wrapper(
            results.list,
        )
        self.search = async_to_streamed_response_wrapper(
            results.search,
        )
        self.update_visibility = async_to_streamed_response_wrapper(
            results.update_visibility,
        )
