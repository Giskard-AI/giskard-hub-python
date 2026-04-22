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
from ..._analytics import capture_event, make_distinct_id
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
        """Create and launch a new evaluation of an agent on a dataset.

        Parameters
        ----------
        project_id : str
            The ID of the project to create the evaluation for.
        agent_id : str
            The ID of the agent to create the evaluation for.
        name : str or Omit
            The name of the evaluation.
        dataset_id : str, optional
            The ID of the dataset to draw test cases from. Exactly one of
            ``dataset_id`` or ``old_evaluation_id`` must be provided.
        tags : sequence of str, optional
            Optional tags to restrict the subset to test cases carrying those
            tags. Only used when ``dataset_id`` is provided.
        old_evaluation_id : str, optional
            The ID of a previous evaluation whose test cases should be reused.
            Exactly one of ``old_evaluation_id`` or ``dataset_id`` must be
            provided.
        run_count : int or Omit
            The number of times to run each test case.
        scheduled_evaluation_id : str, optional
            The ID of the scheduled evaluation to associate with.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, None, or NotGiven
            Override the client-level default timeout for this request, in
            seconds.

        Returns
        -------
        Evaluation
            The newly created evaluation.

        Raises
        ------
        ValueError
            If neither or both of ``dataset_id`` and ``old_evaluation_id`` are
            provided.
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

        result = self._unwrap(response)
        capture_event(make_distinct_id(self._client.api_key), "evaluation_created", {"evaluation_id": result.id})
        return result

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
        """Retrieve an evaluation by its ID, with optional related resource inclusion.

        Parameters
        ----------
        evaluation_id : str
            The ID of the evaluation to retrieve.
        include : list of {"agent", "dataset"}, optional
            Related resources to include in response.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, None, or NotGiven
            Override the client-level default timeout for this request, in
            seconds.

        Returns
        -------
        Evaluation
            The requested evaluation.

        Raises
        ------
        ValueError
            If ``evaluation_id`` is empty.
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
        """Update an evaluation's name.

        Parameters
        ----------
        evaluation_id : str
            The ID of the evaluation to update.
        name : str
            The name of the evaluation.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, None, or NotGiven
            Override the client-level default timeout for this request, in
            seconds.

        Returns
        -------
        Evaluation
            The updated evaluation.

        Raises
        ------
        ValueError
            If ``evaluation_id`` is empty.
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
        """List all evaluations for a project, with optional related resource inclusion.

        Parameters
        ----------
        project_id : str
            The ID of the project to list evaluations for.
        include : list of {"agent", "dataset"}, optional
            Related resources to include in response.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, None, or NotGiven
            Override the client-level default timeout for this request, in
            seconds.

        Returns
        -------
        list of Evaluation
            The evaluations belonging to the project.
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
        """Delete an evaluation by its ID.

        Parameters
        ----------
        evaluation_id : str
            The ID of the evaluation to delete.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, None, or NotGiven
            Override the client-level default timeout for this request, in
            seconds.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If ``evaluation_id`` is empty.
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
        """Delete multiple evaluations at once.

        Parameters
        ----------
        evaluation_ids : sequence of str
            The IDs of the evaluations to delete.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, None, or NotGiven
            Override the client-level default timeout for this request, in
            seconds.

        Returns
        -------
        None
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
        """Create a local evaluation for running agent checks without a remote agent.

        Parameters
        ----------
        agent_info : MinimalAgentParam
            Minimal agent information (name and optional description) to use
            for the evaluation.
        name : str, optional
            The name of the evaluation.
        dataset_id : str, optional
            The ID of the dataset to draw test cases from. Exactly one of
            ``dataset_id`` or ``old_evaluation_id`` must be provided.
        tags : sequence of str, optional
            Optional tags to restrict the subset to test cases carrying those
            tags. Only used when ``dataset_id`` is provided.
        old_evaluation_id : str, optional
            The ID of a previous evaluation whose test cases should be reused.
            Exactly one of ``old_evaluation_id`` or ``dataset_id`` must be
            provided.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, None, or NotGiven
            Override the client-level default timeout for this request, in
            seconds.

        Returns
        -------
        Evaluation
            The newly created local evaluation.

        Raises
        ------
        ValueError
            If neither or both of ``dataset_id`` and ``old_evaluation_id`` are
            provided.
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

        result = self._unwrap(response)
        capture_event(
            make_distinct_id(self._client.api_key), "local_evaluation_created", {"evaluation_id": result.id}
        )
        return result

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
        """Rerun all evaluation results that ended in an error state.

        Parameters
        ----------
        evaluation_id : str
            The ID of the evaluation to rerun errored results for.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, None, or NotGiven
            Override the client-level default timeout for this request, in
            seconds.

        Returns
        -------
        Evaluation
            The evaluation after rerunning errored results.

        Raises
        ------
        ValueError
            If ``evaluation_id`` is empty.
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
        """Run a single check against a provided agent output without creating a full evaluation.

        Parameters
        ----------
        checks : iterable of CheckConfigParam
            The checks to run for the evaluation.
        messages : iterable of ChatMessageParam
            The messages to send to the agent.
        agent_output : AgentOutputParam
            The output from the agent.
        agent_description : str or Omit
            The description of the agent.
        project_id : str, optional
            The ID of the project to run the evaluation for.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, None, or NotGiven
            Override the client-level default timeout for this request, in
            seconds.

        Returns
        -------
        list of CheckResult
            The results of the checks.
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
        """Create and launch a new evaluation of an agent on a dataset.

        Parameters
        ----------
        project_id : str
            The ID of the project to create the evaluation for.
        agent_id : str
            The ID of the agent to create the evaluation for.
        name : str or Omit
            The name of the evaluation.
        dataset_id : str, optional
            The ID of the dataset to draw test cases from. Exactly one of
            ``dataset_id`` or ``old_evaluation_id`` must be provided.
        tags : sequence of str, optional
            Optional tags to restrict the subset to test cases carrying those
            tags. Only used when ``dataset_id`` is provided.
        old_evaluation_id : str, optional
            The ID of a previous evaluation whose test cases should be reused.
            Exactly one of ``old_evaluation_id`` or ``dataset_id`` must be
            provided.
        run_count : int or Omit
            The number of times to run each test case.
        scheduled_evaluation_id : str, optional
            The ID of the scheduled evaluation to associate with.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, None, or NotGiven
            Override the client-level default timeout for this request, in
            seconds.

        Returns
        -------
        Evaluation
            The newly created evaluation.

        Raises
        ------
        ValueError
            If neither or both of ``dataset_id`` and ``old_evaluation_id`` are
            provided.
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

        result = self._unwrap(response)
        capture_event(make_distinct_id(self._client.api_key), "evaluation_created", {"evaluation_id": result.id})
        return result

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
        """Retrieve an evaluation by its ID, with optional related resource inclusion.

        Parameters
        ----------
        evaluation_id : str
            The ID of the evaluation to retrieve.
        include : list of {"agent", "dataset"}, optional
            Related resources to include in response.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, None, or NotGiven
            Override the client-level default timeout for this request, in
            seconds.

        Returns
        -------
        Evaluation
            The requested evaluation.

        Raises
        ------
        ValueError
            If ``evaluation_id`` is empty.
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
        """Update an evaluation's name.

        Parameters
        ----------
        evaluation_id : str
            The ID of the evaluation to update.
        name : str
            The name of the evaluation.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, None, or NotGiven
            Override the client-level default timeout for this request, in
            seconds.

        Returns
        -------
        Evaluation
            The updated evaluation.

        Raises
        ------
        ValueError
            If ``evaluation_id`` is empty.
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
        """List all evaluations for a project, with optional related resource inclusion.

        Parameters
        ----------
        project_id : str
            The ID of the project to list evaluations for.
        include : list of {"agent", "dataset"}, optional
            Related resources to include in response.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, None, or NotGiven
            Override the client-level default timeout for this request, in
            seconds.

        Returns
        -------
        list of Evaluation
            The evaluations belonging to the project.
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
        """Delete an evaluation by its ID.

        Parameters
        ----------
        evaluation_id : str
            The ID of the evaluation to delete.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, None, or NotGiven
            Override the client-level default timeout for this request, in
            seconds.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If ``evaluation_id`` is empty.
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
        """Delete multiple evaluations at once.

        Parameters
        ----------
        evaluation_ids : sequence of str
            The IDs of the evaluations to delete.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, None, or NotGiven
            Override the client-level default timeout for this request, in
            seconds.

        Returns
        -------
        None
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
        """Create a local evaluation for running agent checks without a remote agent.

        Parameters
        ----------
        agent_info : MinimalAgentParam
            Minimal agent information (name and optional description) to use
            for the evaluation.
        name : str, optional
            The name of the evaluation.
        dataset_id : str, optional
            The ID of the dataset to draw test cases from. Exactly one of
            ``dataset_id`` or ``old_evaluation_id`` must be provided.
        tags : sequence of str, optional
            Optional tags to restrict the subset to test cases carrying those
            tags. Only used when ``dataset_id`` is provided.
        old_evaluation_id : str, optional
            The ID of a previous evaluation whose test cases should be reused.
            Exactly one of ``old_evaluation_id`` or ``dataset_id`` must be
            provided.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, None, or NotGiven
            Override the client-level default timeout for this request, in
            seconds.

        Returns
        -------
        Evaluation
            The newly created local evaluation.

        Raises
        ------
        ValueError
            If neither or both of ``dataset_id`` and ``old_evaluation_id`` are
            provided.
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

        result = self._unwrap(response)
        capture_event(
            make_distinct_id(self._client.api_key), "local_evaluation_created", {"evaluation_id": result.id}
        )
        return result

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
        """Rerun all evaluation results that ended in an error state.

        Parameters
        ----------
        evaluation_id : str
            The ID of the evaluation to rerun errored results for.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, None, or NotGiven
            Override the client-level default timeout for this request, in
            seconds.

        Returns
        -------
        Evaluation
            The evaluation after rerunning errored results.

        Raises
        ------
        ValueError
            If ``evaluation_id`` is empty.
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
        """Run a single check against a provided agent output without creating a full evaluation.

        Parameters
        ----------
        checks : iterable of CheckConfigParam
            The checks to run for the evaluation.
        messages : iterable of ChatMessageParam
            The messages to send to the agent.
        agent_output : AgentOutputParam
            The output from the agent.
        agent_description : str or Omit
            The description of the agent.
        project_id : str, optional
            The ID of the project to run the evaluation for.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, None, or NotGiven
            Override the client-level default timeout for this request, in
            seconds.

        Returns
        -------
        list of CheckResult
            The results of the checks.
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
