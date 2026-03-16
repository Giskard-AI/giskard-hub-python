from __future__ import annotations

from typing import List, Literal, Iterable, Optional, cast

import httpx

from ...types import Agent, Dataset
from .results import (
    ResultsResource,
    AsyncResultsResource,
    ResultsResourceWithRawResponse,
    AsyncResultsResourceWithRawResponse,
    ResultsResourceWithStreamingResponse,
    AsyncResultsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .._included import embed_included_list, embed_included_single
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.chat import ChatMessageParam
from ...types.agent import AgentOutputParam, MinimalAgentParam
from ...types.check import CheckResult, CheckConfigParam
from ..._base_client import make_request_options
from ...types.common import APIResponse, APIResponseWithIncluded
from ...types.dataset import DatasetSubsetParam
from ...types.evaluation import (
    Evaluation,
    EvaluationListParams,
    EvaluationCreateParams,
    EvaluationUpdateParams,
    EvaluationRetrieveParams,
    EvaluationRunSingleParams,
    CriterionEvaluationDataset,
    EvaluationBulkDeleteParams,
    EvaluationCreateLocalParams,
)

__all__ = ["EvaluationsResource", "AsyncEvaluationsResource"]


def _validate_dataset_or_old_evaluation(
    dataset_id: Optional[str] | Omit,
    old_evaluation_id: Optional[str] | Omit,
) -> None:
    """
    Ensure that exactly one of `dataset_id` or `old_evaluation_id` is provided.

    Raises
    ------
    ValueError
        If both are provided or both are omitted.
    """
    if (dataset_id is omit and old_evaluation_id is omit) or (dataset_id is not omit and old_evaluation_id is not omit):
        raise ValueError("Exactly one of `dataset_id` or `old_evaluation_id` must be provided")


def _check_params_to_api(checks: Iterable[CheckConfigParam]) -> Iterable[dict[str, object]]:
    return [{"identifier": check["identifier"], **(check.get("params", {}))} for check in checks]


class EvaluationsResource(SyncAPIResource):
    @cached_property
    def results(self) -> ResultsResource:
        return ResultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EvaluationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return EvaluationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: str,
        agent_id: str,
        name: str | Omit = omit,
        dataset_id: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        old_evaluation_id: Optional[str] | Omit = omit,
        run_count: int | Omit = omit,
        scheduled_evaluation_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Evaluation:
        """Create Evaluation

        Args:
          project_id: The ID of the project to create the evaluation for

          agent_id: The ID of the agent to create the evaluation for

          name: The name of the evaluation

          dataset_id: The ID of the dataset to draw test cases from. Exactly one of
              `dataset_id` or `old_evaluation_id` must be provided.

          tags: Optional tags to restrict the subset to test cases carrying those tags.
              Only used when `dataset_id` is provided.

          old_evaluation_id: The ID of a previous evaluation whose test cases should be
              reused. Exactly one of `old_evaluation_id` or `dataset_id` must be provided.

          run_count: The number of times to run each test case

          scheduled_evaluation_id: The ID of the scheduled evaluation to associate with

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """

        _validate_dataset_or_old_evaluation(dataset_id, old_evaluation_id)
        criteria: DatasetSubsetParam | CriterionEvaluationDataset | Omit = omit

        if dataset_id is not omit:
            criteria = DatasetSubsetParam(
                dataset_id=cast(str, dataset_id),
                tags=None if tags is omit else cast(Optional[SequenceNotStr[str]], tags),
            )

        response = self._post(
            "/v2/evaluations",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "project_id": project_id,
                    "criteria": criteria,
                    "name": name,
                    "old_evaluation_id": old_evaluation_id,
                    "run_count": run_count,
                    "scheduled_evaluation_id": scheduled_evaluation_id,
                },
                EvaluationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Evaluation],
        )

        return self._unwrap(response)

    def retrieve(
        self,
        evaluation_id: str,
        *,
        include: Optional[List[Literal["agent", "dataset"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Evaluation:
        """
        Retrieve Evaluation

        Args:
          evaluation_id: The ID of the evaluation to retrieve

          include: Related resources to include in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")

        response = self._get(
            f"/v2/evaluations/{evaluation_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include": include}, EvaluationRetrieveParams),
            ),
            cast_to=APIResponseWithIncluded[Evaluation, APIResponse[Agent | Dataset]],
        )

        if include is not omit and include:
            response = embed_included_single(response, id_getter=lambda evaluation: evaluation.id)

        return self._unwrap(response)

    def update(
        self,
        evaluation_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Evaluation:
        """
        Update Evaluation

        Args:
          evaluation_id: The ID of the evaluation to update

          name: The name of the evaluation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")
        response = self._patch(
            f"/v2/evaluations/{evaluation_id}",
            body=maybe_transform({"name": name}, EvaluationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Evaluation],
        )

        return self._unwrap(response)

    def list(
        self,
        *,
        project_id: str,
        include: Optional[List[Literal["agent", "dataset"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[Evaluation]:
        """
        List Evaluations

        Args:
          project_id: The ID of the project to list evaluations for

          include: Related resources to include in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        response = self._get(
            "/v2/evaluations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "project_id": project_id,
                        "include": include,
                    },
                    EvaluationListParams,
                ),
            ),
            cast_to=APIResponseWithIncluded[List[Evaluation], APIResponse[Agent | Dataset]],
        )

        if include is not omit and include:
            response = embed_included_list(response, id_getter=lambda evaluation: evaluation.id)

        return self._unwrap(response)

    def delete(
        self,
        evaluation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Evaluation

        Args:
          evaluation_id: The ID of the evaluation to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")
        response = self._delete(
            f"/v2/evaluations/{evaluation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    def bulk_delete(
        self,
        *,
        evaluation_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Bulk Delete Evaluations

        Args:
          evaluation_ids: The IDs of the evaluations to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        response = self._delete(
            "/v2/evaluations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"evaluation_ids": evaluation_ids}, EvaluationBulkDeleteParams),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    def create_local(
        self,
        *,
        agent_info: MinimalAgentParam,
        name: Optional[str] | Omit = omit,
        dataset_id: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        old_evaluation_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Evaluation:
        """
        Create Local Evaluation

        Args:
          agent_info: Minimal agent information (name and optional description) to use
              for the evaluation.

          name: The name of the evaluation

          dataset_id: The ID of the dataset to draw test cases from. Exactly one of
              `dataset_id` or `old_evaluation_id` must be provided.

          tags: Optional tags to restrict the subset to test cases carrying those tags.
              Only used when `dataset_id` is provided.

          old_evaluation_id: The ID of a previous evaluation whose test cases should be
              reused. Exactly one of `old_evaluation_id` or `dataset_id` must be provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        _validate_dataset_or_old_evaluation(dataset_id, old_evaluation_id)
        criteria: DatasetSubsetParam | CriterionEvaluationDataset | Omit = omit

        if dataset_id is not omit:
            criteria = DatasetSubsetParam(
                dataset_id=cast(str, dataset_id),
                tags=None if tags is omit else cast(Optional[SequenceNotStr[str]], tags),
            )
        elif old_evaluation_id is not omit:
            criteria = CriterionEvaluationDataset(evaluation_id=cast(str, old_evaluation_id))

        response = self._post(
            "/v2/evaluations/create-local",
            body=maybe_transform(
                {
                    "criteria": [criteria],
                    "model": agent_info,
                    "name": name,
                },
                EvaluationCreateLocalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Evaluation],
        )

        return self._unwrap(response)

    def rerun_errored_results(
        self,
        evaluation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Evaluation:
        """
        Rerun Errored Evaluation Results

        Args:
          evaluation_id: The ID of the evaluation to rerun errored results for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")
        response = self._post(
            f"/v2/evaluations/{evaluation_id}/rerun-errored-results",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Evaluation],
        )

        return self._unwrap(response)

    def run_single(
        self,
        *,
        checks: Iterable[CheckConfigParam],
        messages: Iterable[ChatMessageParam],
        agent_output: AgentOutputParam,
        agent_description: str | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[CheckResult]:
        """
        Run Single Evaluation

        Args:
          checks: The checks to run for the evaluation

          messages: The messages to send to the agent

          agent_output: The output from the agent

          agent_description: The description of the agent

          project_id: The ID of the project to run the evaluation for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        api_checks: Iterable[dict[str, object]] = _check_params_to_api(checks)

        response = self._post(
            "/v2/evaluations/run-single",
            body=maybe_transform(
                {
                    "checks": api_checks,
                    "messages": messages,
                    "model_output": agent_output,
                    "model_description": agent_description,
                    "project_id": project_id,
                },
                EvaluationRunSingleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[CheckResult]],
        )

        return self._unwrap(response)


class AsyncEvaluationsResource(AsyncAPIResource):
    @cached_property
    def results(self) -> AsyncResultsResource:
        return AsyncResultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEvaluationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncEvaluationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: str,
        agent_id: str,
        name: str | Omit = omit,
        dataset_id: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        old_evaluation_id: Optional[str] | Omit = omit,
        run_count: int | Omit = omit,
        scheduled_evaluation_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Evaluation:
        """Create Evaluation

        Args:
          project_id: The ID of the project to create the evaluation for

          agent_id: The ID of the agent to create the evaluation for

          name: The name of the evaluation

          dataset_id: The ID of the dataset to draw test cases from. Exactly one of
              `dataset_id` or `old_evaluation_id` must be provided.

          tags: Optional tags to restrict the subset to test cases carrying those tags.
              Only used when `dataset_id` is provided.

          old_evaluation_id: The ID of a previous evaluation whose test cases should be
              reused. Exactly one of `old_evaluation_id` or `dataset_id` must be provided.

          run_count: The number of times to run each test case

          scheduled_evaluation_id: The ID of the scheduled evaluation to associate with

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """

        _validate_dataset_or_old_evaluation(dataset_id, old_evaluation_id)
        criteria: DatasetSubsetParam | CriterionEvaluationDataset | Omit = omit

        if dataset_id is not omit:
            criteria = DatasetSubsetParam(
                dataset_id=cast(str, dataset_id),
                tags=None if tags is omit else cast(Optional[SequenceNotStr[str]], tags),
            )

        response = await self._post(
            "/v2/evaluations",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "project_id": project_id,
                    "criteria": criteria,
                    "name": name,
                    "old_evaluation_id": old_evaluation_id,
                    "run_count": run_count,
                    "scheduled_evaluation_id": scheduled_evaluation_id,
                },
                EvaluationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Evaluation],
        )

        return self._unwrap(response)

    async def retrieve(
        self,
        evaluation_id: str,
        *,
        include: Optional[List[Literal["agent", "dataset"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Evaluation:
        """
        Retrieve Evaluation

        Args:
          evaluation_id: The ID of the evaluation to retrieve

          include: Related resources to include in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")

        response = await self._get(
            f"/v2/evaluations/{evaluation_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"include": include}, EvaluationRetrieveParams),
            ),
            cast_to=APIResponseWithIncluded[Evaluation, APIResponse[Agent | Dataset]],
        )

        if include is not omit and include:
            response = embed_included_single(response, id_getter=lambda evaluation: evaluation.id)

        return self._unwrap(response)

    async def update(
        self,
        evaluation_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Evaluation:
        """
        Update Evaluation

        Args:
          evaluation_id: The ID of the evaluation to update

          name: The name of the evaluation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")
        response = await self._patch(
            f"/v2/evaluations/{evaluation_id}",
            body=await async_maybe_transform({"name": name}, EvaluationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Evaluation],
        )

        return self._unwrap(response)

    async def list(
        self,
        *,
        project_id: str,
        include: Optional[List[Literal["agent", "dataset"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[Evaluation]:
        """
        List Evaluations

        Args:
          project_id: The ID of the project to list evaluations for

          include: Related resources to include in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        response = await self._get(
            "/v2/evaluations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "project_id": project_id,
                        "include": include,
                    },
                    EvaluationListParams,
                ),
            ),
            cast_to=APIResponseWithIncluded[List[Evaluation], APIResponse[Agent | Dataset]],
        )

        if include is not omit and include:
            response = embed_included_list(response, id_getter=lambda evaluation: evaluation.id)

        return self._unwrap(response)

    async def delete(
        self,
        evaluation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Evaluation

        Args:
          evaluation_id: The ID of the evaluation to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")
        response = await self._delete(
            f"/v2/evaluations/{evaluation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    async def bulk_delete(
        self,
        *,
        evaluation_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Bulk Delete Evaluations

        Args:
          evaluation_ids: The IDs of the evaluations to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        response = await self._delete(
            "/v2/evaluations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"evaluation_ids": evaluation_ids}, EvaluationBulkDeleteParams),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    async def create_local(
        self,
        *,
        agent_info: MinimalAgentParam,
        name: Optional[str] | Omit = omit,
        dataset_id: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        old_evaluation_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Evaluation:
        """
        Create Local Evaluation

        Args:
          agent_info: Minimal agent information (name and optional description) to use
              for the evaluation.

          name: The name of the evaluation

          dataset_id: The ID of the dataset to draw test cases from. Exactly one of
              `dataset_id` or `old_evaluation_id` must be provided.

          tags: Optional tags to restrict the subset to test cases carrying those tags.
              Only used when `dataset_id` is provided.

          old_evaluation_id: The ID of a previous evaluation whose test cases should be
              reused. Exactly one of `old_evaluation_id` or `dataset_id` must be provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        _validate_dataset_or_old_evaluation(dataset_id, old_evaluation_id)
        criteria: DatasetSubsetParam | CriterionEvaluationDataset | Omit = omit

        if dataset_id is not omit:
            criteria = DatasetSubsetParam(
                dataset_id=cast(str, dataset_id),
                tags=None if tags is omit else cast(Optional[SequenceNotStr[str]], tags),
            )
        elif old_evaluation_id is not omit:
            criteria = CriterionEvaluationDataset(evaluation_id=cast(str, old_evaluation_id))

        response = await self._post(
            "/v2/evaluations/create-local",
            body=await async_maybe_transform(
                {
                    "criteria": [criteria],
                    "model": agent_info,
                    "name": name,
                },
                EvaluationCreateLocalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Evaluation],
        )

        return self._unwrap(response)

    async def rerun_errored_results(
        self,
        evaluation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Evaluation:
        """
        Rerun Errored Evaluation Results

        Args:
          evaluation_id: The ID of the evaluation to rerun errored results for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not evaluation_id:
            raise ValueError(f"Expected a non-empty value for `evaluation_id` but received {evaluation_id!r}")
        response = await self._post(
            f"/v2/evaluations/{evaluation_id}/rerun-errored-results",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Evaluation],
        )

        return self._unwrap(response)

    async def run_single(
        self,
        *,
        checks: Iterable[CheckConfigParam],
        messages: Iterable[ChatMessageParam],
        agent_output: AgentOutputParam,
        agent_description: str | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[CheckResult]:
        """
        Run Single Evaluation

        Args:
          checks: The checks to run for the evaluation

          messages: The messages to send to the agent

          agent_output: The output from the agent

          agent_description: The description of the agent

          project_id: The ID of the project to run the evaluation for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        api_checks: Iterable[dict[str, object]] = _check_params_to_api(checks)

        response = await self._post(
            "/v2/evaluations/run-single",
            body=await async_maybe_transform(
                {
                    "checks": api_checks,
                    "messages": messages,
                    "model_output": agent_output,
                    "model_description": agent_description,
                    "project_id": project_id,
                },
                EvaluationRunSingleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[List[CheckResult]],
        )

        return self._unwrap(response)


class EvaluationsResourceWithRawResponse:
    def __init__(self, evaluations: EvaluationsResource) -> None:
        self._evaluations = evaluations

        self.create = to_raw_response_wrapper(
            evaluations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            evaluations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            evaluations.update,
        )
        self.list = to_raw_response_wrapper(
            evaluations.list,
        )
        self.delete = to_raw_response_wrapper(
            evaluations.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            evaluations.bulk_delete,
        )
        self.create_local = to_raw_response_wrapper(
            evaluations.create_local,
        )
        self.rerun_errored_results = to_raw_response_wrapper(
            evaluations.rerun_errored_results,
        )
        self.run_single = to_raw_response_wrapper(
            evaluations.run_single,
        )

    @cached_property
    def results(self) -> ResultsResourceWithRawResponse:
        return ResultsResourceWithRawResponse(self._evaluations.results)


class AsyncEvaluationsResourceWithRawResponse:
    def __init__(self, evaluations: AsyncEvaluationsResource) -> None:
        self._evaluations = evaluations

        self.create = async_to_raw_response_wrapper(
            evaluations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            evaluations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            evaluations.update,
        )
        self.list = async_to_raw_response_wrapper(
            evaluations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            evaluations.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            evaluations.bulk_delete,
        )
        self.create_local = async_to_raw_response_wrapper(
            evaluations.create_local,
        )
        self.rerun_errored_results = async_to_raw_response_wrapper(
            evaluations.rerun_errored_results,
        )
        self.run_single = async_to_raw_response_wrapper(
            evaluations.run_single,
        )

    @cached_property
    def results(self) -> AsyncResultsResourceWithRawResponse:
        return AsyncResultsResourceWithRawResponse(self._evaluations.results)


class EvaluationsResourceWithStreamingResponse:
    def __init__(self, evaluations: EvaluationsResource) -> None:
        self._evaluations = evaluations

        self.create = to_streamed_response_wrapper(
            evaluations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            evaluations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            evaluations.update,
        )
        self.list = to_streamed_response_wrapper(
            evaluations.list,
        )
        self.delete = to_streamed_response_wrapper(
            evaluations.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            evaluations.bulk_delete,
        )
        self.create_local = to_streamed_response_wrapper(
            evaluations.create_local,
        )
        self.rerun_errored_results = to_streamed_response_wrapper(
            evaluations.rerun_errored_results,
        )
        self.run_single = to_streamed_response_wrapper(
            evaluations.run_single,
        )

    @cached_property
    def results(self) -> ResultsResourceWithStreamingResponse:
        return ResultsResourceWithStreamingResponse(self._evaluations.results)


class AsyncEvaluationsResourceWithStreamingResponse:
    def __init__(self, evaluations: AsyncEvaluationsResource) -> None:
        self._evaluations = evaluations

        self.create = async_to_streamed_response_wrapper(
            evaluations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            evaluations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            evaluations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            evaluations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            evaluations.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            evaluations.bulk_delete,
        )
        self.create_local = async_to_streamed_response_wrapper(
            evaluations.create_local,
        )
        self.rerun_errored_results = async_to_streamed_response_wrapper(
            evaluations.rerun_errored_results,
        )
        self.run_single = async_to_streamed_response_wrapper(
            evaluations.run_single,
        )

    @cached_property
    def results(self) -> AsyncResultsResourceWithStreamingResponse:
        return AsyncResultsResourceWithStreamingResponse(self._evaluations.results)
