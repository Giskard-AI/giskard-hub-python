from __future__ import annotations

from typing import List, Union, Literal, Optional
from datetime import datetime

import httpx

from ..types import (
    Agent,
    Dataset,
    Evaluation,
    APIResponse,
    FrequencyOption,
    ScheduledEvaluation,
    APIResponseWithIncluded,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from ._included import embed_included_list, embed_included_single
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.scheduled_evaluation import (
    LastExecutionStatusParam,
    ScheduledEvaluationListParams,
    ScheduledEvaluationCreateParams,
    ScheduledEvaluationUpdateParams,
    ScheduledEvaluationRetrieveParams,
    ScheduledEvaluationBulkDeleteParams,
    ScheduledEvaluationListEvaluationsParams,
)

__all__ = ["ScheduledEvaluationsResource", "AsyncScheduledEvaluationsResource"]


class ScheduledEvaluationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScheduledEvaluationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return ScheduledEvaluationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScheduledEvaluationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return ScheduledEvaluationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: str,
        name: str,
        agent_id: str,
        dataset_id: str,
        tags: SequenceNotStr[str] | Omit = omit,
        run_count: int | Omit = omit,
        frequency: FrequencyOption,
        time: str,
        day_of_month: Optional[int] | Omit = omit,
        day_of_week: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledEvaluation:
        """Create a new scheduled evaluation for recurring agent testing.

        Parameters
        ----------
        project_id : str
            Project ID to use for the scheduled evaluation.
        name : str
            Name of the scheduled evaluation.
        agent_id : str
            Agent ID to use for the scheduled evaluation.
        dataset_id : str
            Dataset ID to use for the scheduled evaluation.
        tags : SequenceNotStr[str] | Omit
            List of tags to apply to the scheduled evaluation.
        run_count : int | Omit
            The number of times to run each test case. This is useful to get a more
            accurate result when the chatbot's generation is not deterministic. Testing
            stops at the first failure. If all runs pass, the test case is considered
            successful.
        frequency : FrequencyOption
            Frequency of the scheduled evaluation.
        time : str
            Time of the scheduled evaluation.
        day_of_month : int | None | Omit
            Day of the month to run the scheduled evaluation.
        day_of_week : int | None | Omit
            Day of the week to run the scheduled evaluation.

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
        ScheduledEvaluation
            The newly created scheduled evaluation.
        """
        response = self._post(
            "/v2/scheduled-evaluations",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "dataset_id": dataset_id,
                    "frequency": frequency,
                    "name": name,
                    "project_id": project_id,
                    "time": time,
                    "day_of_month": day_of_month,
                    "day_of_week": day_of_week,
                    "run_count": run_count,
                    "tags": tags,
                },
                ScheduledEvaluationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[ScheduledEvaluation],
        )

        return self._unwrap(response)

    def retrieve(
        self,
        scheduled_evaluation_id: str,
        include: Optional[List[Literal["evaluations"]]] | Omit = omit,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledEvaluation:
        """Retrieve a scheduled evaluation by its ID.

        Parameters
        ----------
        scheduled_evaluation_id : str
            ID of the scheduled evaluation to retrieve.
        include : list[Literal["evaluations"]] | None | Omit
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
        ScheduledEvaluation
            The requested scheduled evaluation.

        Raises
        ------
        ValueError
            If ``scheduled_evaluation_id`` is empty.
        """
        if not scheduled_evaluation_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_evaluation_id` but received {scheduled_evaluation_id!r}"
            )
        response = self._get(
            f"/v2/scheduled-evaluations/{scheduled_evaluation_id}",
            options=make_request_options(
                query=maybe_transform({"include": include}, ScheduledEvaluationRetrieveParams),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponseWithIncluded[ScheduledEvaluation, List[APIResponse[Evaluation]]],
        )

        if include is not omit and include:
            response = embed_included_single(response, id_getter=lambda scheduled: scheduled.id)

        return self._unwrap(response)

    def update(
        self,
        scheduled_evaluation_id: str,
        *,
        name: Optional[str] | Omit = omit,
        run_count: Optional[int] | Omit = omit,
        frequency: Optional[FrequencyOption] | Omit = omit,
        time: Optional[str] | Omit = omit,
        day_of_week: Optional[int] | Omit = omit,
        day_of_month: Optional[int] | Omit = omit,
        last_execution_at: Union[str, datetime, None] | Omit = omit,
        last_execution_status: Optional[LastExecutionStatusParam] | Omit = omit,
        paused: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledEvaluation:
        """Update an existing scheduled evaluation's configuration.

        Parameters
        ----------
        scheduled_evaluation_id : str
            ID of the scheduled evaluation to update.
        name : str | None | Omit
            Name of the scheduled evaluation.
        run_count : int | None | Omit
            The number of times to run each test case. This is useful to get a more
            accurate result when the chatbot's generation is not deterministic. Testing
            stops at the first failure. If all runs pass, the test case is considered
            successful.
        frequency : FrequencyOption | None | Omit
            Frequency of the scheduled evaluation.
        time : str | None | Omit
            Time of the scheduled evaluation.
        day_of_week : int | None | Omit
            Day of the week to run the scheduled evaluation.
        day_of_month : int | None | Omit
            Day of the month to run the scheduled evaluation.
        last_execution_at : str | datetime | None | Omit
            The date and time of the last execution of the scheduled evaluation.
        last_execution_status : LastExecutionStatusParam | None | Omit
            The status of the last execution of the scheduled evaluation.
        paused : bool | None | Omit
            Whether the scheduled evaluation is paused.

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
        ScheduledEvaluation
            The updated scheduled evaluation.

        Raises
        ------
        ValueError
            If ``scheduled_evaluation_id`` is empty.
        """
        if not scheduled_evaluation_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_evaluation_id` but received {scheduled_evaluation_id!r}"
            )
        response = self._patch(
            f"/v2/scheduled-evaluations/{scheduled_evaluation_id}",
            body=maybe_transform(
                {
                    "day_of_month": day_of_month,
                    "day_of_week": day_of_week,
                    "frequency": frequency,
                    "last_execution_at": last_execution_at,
                    "last_execution_status": last_execution_status,
                    "name": name,
                    "paused": paused,
                    "run_count": run_count,
                    "time": time,
                },
                ScheduledEvaluationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[ScheduledEvaluation],
        )

        return self._unwrap(response)

    def list(
        self,
        *,
        project_id: str,
        include: Optional[List[Literal["evaluations"]]] | Omit = omit,
        last_days: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[ScheduledEvaluation]:
        """List all scheduled evaluations for a project.

        Parameters
        ----------
        project_id : str
            Project ID to use for the scheduled evaluation.
        include : list[Literal["evaluations"]] | None | Omit
            Related resources to include in response.
        last_days : int | None | Omit
            Number of days to include in the response.

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
        list[ScheduledEvaluation]
            A list of scheduled evaluations for the project.
        """
        response = self._get(
            "/v2/scheduled-evaluations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"project_id": project_id, "include": include, "last_days": last_days},
                    ScheduledEvaluationListParams,
                ),
            ),
            cast_to=APIResponseWithIncluded[List[ScheduledEvaluation], List[APIResponse[Evaluation]]],
        )

        if include is not omit and include:
            response = embed_included_list(response, id_getter=lambda scheduled: scheduled.id)

        return self._unwrap(response)

    def delete(
        self,
        scheduled_evaluation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a scheduled evaluation by its ID.

        Parameters
        ----------
        scheduled_evaluation_id : str
            ID of the scheduled evaluation to delete.

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
        None

        Raises
        ------
        ValueError
            If ``scheduled_evaluation_id`` is empty.
        """
        if not scheduled_evaluation_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_evaluation_id` but received {scheduled_evaluation_id!r}"
            )
        response = self._delete(
            f"/v2/scheduled-evaluations/{scheduled_evaluation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    def bulk_delete(
        self,
        *,
        scheduled_evaluation_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete multiple scheduled evaluations at once.

        Parameters
        ----------
        scheduled_evaluation_ids : SequenceNotStr[str]
            IDs of the scheduled evaluations to delete.

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
        None
        """
        response = self._delete(
            "/v2/scheduled-evaluations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"scheduled_evaluation_ids": scheduled_evaluation_ids},
                    ScheduledEvaluationBulkDeleteParams,
                ),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    def list_evaluations(
        self,
        scheduled_evaluation_id: str,
        include: Optional[List[Literal["agent", "dataset"]]] | Omit = omit,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[Evaluation]:
        """List all evaluation runs triggered by a specific scheduled evaluation.

        Parameters
        ----------
        scheduled_evaluation_id : str
            ID of the scheduled evaluation to list evaluations for.
        include : list[Literal["agent", "dataset"]] | None | Omit
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
        list[Evaluation]
            A list of evaluations triggered by the scheduled evaluation.

        Raises
        ------
        ValueError
            If ``scheduled_evaluation_id`` is empty.
        """
        if not scheduled_evaluation_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_evaluation_id` but received {scheduled_evaluation_id!r}"
            )

        response = self._get(
            f"/v2/scheduled-evaluations/{scheduled_evaluation_id}/evaluations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include": include},
                    ScheduledEvaluationListEvaluationsParams,
                ),
            ),
            cast_to=APIResponseWithIncluded[List[Evaluation], APIResponse[Agent | Dataset]],
        )

        if include is not omit and include:
            response = embed_included_list(response, id_getter=lambda evaluation: evaluation.id)

        return self._unwrap(response)


class AsyncScheduledEvaluationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScheduledEvaluationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScheduledEvaluationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScheduledEvaluationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncScheduledEvaluationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: str,
        name: str,
        agent_id: str,
        dataset_id: str,
        tags: SequenceNotStr[str] | Omit = omit,
        run_count: int | Omit = omit,
        frequency: FrequencyOption,
        time: str,
        day_of_month: Optional[int] | Omit = omit,
        day_of_week: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledEvaluation:
        """Create a new scheduled evaluation for recurring agent testing.

        Parameters
        ----------
        project_id : str
            Project ID to use for the scheduled evaluation.
        name : str
            Name of the scheduled evaluation.
        agent_id : str
            Agent ID to use for the scheduled evaluation.
        dataset_id : str
            Dataset ID to use for the scheduled evaluation.
        tags : SequenceNotStr[str] | Omit
            List of tags to apply to the scheduled evaluation.
        run_count : int | Omit
            The number of times to run each test case. This is useful to get a more
            accurate result when the chatbot's generation is not deterministic. Testing
            stops at the first failure. If all runs pass, the test case is considered
            successful.
        frequency : FrequencyOption
            Frequency of the scheduled evaluation.
        time : str
            Time of the scheduled evaluation.
        day_of_month : int | None | Omit
            Day of the month to run the scheduled evaluation.
        day_of_week : int | None | Omit
            Day of the week to run the scheduled evaluation.

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
        ScheduledEvaluation
            The newly created scheduled evaluation.
        """
        response = await self._post(
            "/v2/scheduled-evaluations",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "dataset_id": dataset_id,
                    "frequency": frequency,
                    "name": name,
                    "project_id": project_id,
                    "time": time,
                    "day_of_month": day_of_month,
                    "day_of_week": day_of_week,
                    "run_count": run_count,
                    "tags": tags,
                },
                ScheduledEvaluationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[ScheduledEvaluation],
        )

        return self._unwrap(response)

    async def retrieve(
        self,
        scheduled_evaluation_id: str,
        include: Optional[List[Literal["evaluations"]]] | Omit = omit,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledEvaluation:
        """Retrieve a scheduled evaluation by its ID.

        Parameters
        ----------
        scheduled_evaluation_id : str
            ID of the scheduled evaluation to retrieve.
        include : list[Literal["evaluations"]] | None | Omit
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
        ScheduledEvaluation
            The requested scheduled evaluation.

        Raises
        ------
        ValueError
            If ``scheduled_evaluation_id`` is empty.
        """
        if not scheduled_evaluation_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_evaluation_id` but received {scheduled_evaluation_id!r}"
            )
        response = await self._get(
            f"/v2/scheduled-evaluations/{scheduled_evaluation_id}",
            options=make_request_options(
                query=maybe_transform({"include": include}, ScheduledEvaluationRetrieveParams),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponseWithIncluded[ScheduledEvaluation, List[APIResponse[Evaluation]]],
        )

        if include is not omit and include:
            response = embed_included_single(response, id_getter=lambda scheduled: scheduled.id)

        return self._unwrap(response)

    async def update(
        self,
        scheduled_evaluation_id: str,
        *,
        name: Optional[str] | Omit = omit,
        run_count: Optional[int] | Omit = omit,
        frequency: Optional[FrequencyOption] | Omit = omit,
        time: Optional[str] | Omit = omit,
        day_of_week: Optional[int] | Omit = omit,
        day_of_month: Optional[int] | Omit = omit,
        last_execution_at: Union[str, datetime, None] | Omit = omit,
        last_execution_status: Optional[LastExecutionStatusParam] | Omit = omit,
        paused: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledEvaluation:
        """Update an existing scheduled evaluation's configuration.

        Parameters
        ----------
        scheduled_evaluation_id : str
            ID of the scheduled evaluation to update.
        name : str | None | Omit
            Name of the scheduled evaluation.
        run_count : int | None | Omit
            The number of times to run each test case. This is useful to get a more
            accurate result when the chatbot's generation is not deterministic. Testing
            stops at the first failure. If all runs pass, the test case is considered
            successful.
        frequency : FrequencyOption | None | Omit
            Frequency of the scheduled evaluation.
        time : str | None | Omit
            Time of the scheduled evaluation.
        day_of_week : int | None | Omit
            Day of the week to run the scheduled evaluation.
        day_of_month : int | None | Omit
            Day of the month to run the scheduled evaluation.
        last_execution_at : str | datetime | None | Omit
            The date and time of the last execution of the scheduled evaluation.
        last_execution_status : LastExecutionStatusParam | None | Omit
            The status of the last execution of the scheduled evaluation.
        paused : bool | None | Omit
            Whether the scheduled evaluation is paused.

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
        ScheduledEvaluation
            The updated scheduled evaluation.

        Raises
        ------
        ValueError
            If ``scheduled_evaluation_id`` is empty.
        """
        if not scheduled_evaluation_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_evaluation_id` but received {scheduled_evaluation_id!r}"
            )
        response = await self._patch(
            f"/v2/scheduled-evaluations/{scheduled_evaluation_id}",
            body=await async_maybe_transform(
                {
                    "day_of_month": day_of_month,
                    "day_of_week": day_of_week,
                    "frequency": frequency,
                    "last_execution_at": last_execution_at,
                    "last_execution_status": last_execution_status,
                    "name": name,
                    "paused": paused,
                    "run_count": run_count,
                    "time": time,
                },
                ScheduledEvaluationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[ScheduledEvaluation],
        )

        return self._unwrap(response)

    async def list(
        self,
        *,
        project_id: str,
        include: Optional[List[Literal["evaluations"]]] | Omit = omit,
        last_days: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[ScheduledEvaluation]:
        """List all scheduled evaluations for a project.

        Parameters
        ----------
        project_id : str
            Project ID to use for the scheduled evaluation.
        include : list[Literal["evaluations"]] | None | Omit
            Related resources to include in response.
        last_days : int | None | Omit
            Number of days to include in the response.

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
        list[ScheduledEvaluation]
            A list of scheduled evaluations for the project.
        """
        response = await self._get(
            "/v2/scheduled-evaluations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id, "include": include, "last_days": last_days},
                    ScheduledEvaluationListParams,
                ),
            ),
            cast_to=APIResponseWithIncluded[List[ScheduledEvaluation], List[APIResponse[Evaluation]]],
        )

        if include is not omit and include:
            response = embed_included_list(response, id_getter=lambda scheduled: scheduled.id)

        return self._unwrap(response)

    async def delete(
        self,
        scheduled_evaluation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a scheduled evaluation by its ID.

        Parameters
        ----------
        scheduled_evaluation_id : str
            ID of the scheduled evaluation to delete.

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
        None

        Raises
        ------
        ValueError
            If ``scheduled_evaluation_id`` is empty.
        """
        if not scheduled_evaluation_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_evaluation_id` but received {scheduled_evaluation_id!r}"
            )
        response = await self._delete(
            f"/v2/scheduled-evaluations/{scheduled_evaluation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    async def bulk_delete(
        self,
        *,
        scheduled_evaluation_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete multiple scheduled evaluations at once.

        Parameters
        ----------
        scheduled_evaluation_ids : SequenceNotStr[str]
            IDs of the scheduled evaluations to delete.

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
        None
        """
        response = await self._delete(
            "/v2/scheduled-evaluations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"scheduled_evaluation_ids": scheduled_evaluation_ids},
                    ScheduledEvaluationBulkDeleteParams,
                ),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    async def list_evaluations(
        self,
        scheduled_evaluation_id: str,
        include: Optional[List[Literal["agent", "dataset"]]] | Omit = omit,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[Evaluation]:
        """List all evaluation runs triggered by a specific scheduled evaluation.

        Parameters
        ----------
        scheduled_evaluation_id : str
            ID of the scheduled evaluation to list evaluations for.
        include : list[Literal["agent", "dataset"]] | None | Omit
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
        list[Evaluation]
            A list of evaluations triggered by the scheduled evaluation.

        Raises
        ------
        ValueError
            If ``scheduled_evaluation_id`` is empty.
        """
        if not scheduled_evaluation_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_evaluation_id` but received {scheduled_evaluation_id!r}"
            )

        response = await self._get(
            f"/v2/scheduled-evaluations/{scheduled_evaluation_id}/evaluations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include": include},
                    ScheduledEvaluationListEvaluationsParams,
                ),
            ),
            cast_to=APIResponseWithIncluded[List[Evaluation], APIResponse[Agent | Dataset]],
        )

        if include is not omit and include:
            response = embed_included_list(response, id_getter=lambda evaluation: evaluation.id)

        return self._unwrap(response)


class ScheduledEvaluationsResourceWithRawResponse:
    def __init__(self, scheduled_evaluations: ScheduledEvaluationsResource) -> None:
        self._scheduled_evaluations = scheduled_evaluations

        self.create = to_raw_response_wrapper(
            scheduled_evaluations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            scheduled_evaluations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            scheduled_evaluations.update,
        )
        self.list = to_raw_response_wrapper(
            scheduled_evaluations.list,
        )
        self.delete = to_raw_response_wrapper(
            scheduled_evaluations.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            scheduled_evaluations.bulk_delete,
        )
        self.list_evaluations = to_raw_response_wrapper(
            scheduled_evaluations.list_evaluations,
        )


class AsyncScheduledEvaluationsResourceWithRawResponse:
    def __init__(self, scheduled_evaluations: AsyncScheduledEvaluationsResource) -> None:
        self._scheduled_evaluations = scheduled_evaluations

        self.create = async_to_raw_response_wrapper(
            scheduled_evaluations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            scheduled_evaluations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            scheduled_evaluations.update,
        )
        self.list = async_to_raw_response_wrapper(
            scheduled_evaluations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            scheduled_evaluations.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            scheduled_evaluations.bulk_delete,
        )
        self.list_evaluations = async_to_raw_response_wrapper(
            scheduled_evaluations.list_evaluations,
        )


class ScheduledEvaluationsResourceWithStreamingResponse:
    def __init__(self, scheduled_evaluations: ScheduledEvaluationsResource) -> None:
        self._scheduled_evaluations = scheduled_evaluations

        self.create = to_streamed_response_wrapper(
            scheduled_evaluations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            scheduled_evaluations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            scheduled_evaluations.update,
        )
        self.list = to_streamed_response_wrapper(
            scheduled_evaluations.list,
        )
        self.delete = to_streamed_response_wrapper(
            scheduled_evaluations.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            scheduled_evaluations.bulk_delete,
        )
        self.list_evaluations = to_streamed_response_wrapper(
            scheduled_evaluations.list_evaluations,
        )


class AsyncScheduledEvaluationsResourceWithStreamingResponse:
    def __init__(self, scheduled_evaluations: AsyncScheduledEvaluationsResource) -> None:
        self._scheduled_evaluations = scheduled_evaluations

        self.create = async_to_streamed_response_wrapper(
            scheduled_evaluations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            scheduled_evaluations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            scheduled_evaluations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            scheduled_evaluations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            scheduled_evaluations.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            scheduled_evaluations.bulk_delete,
        )
        self.list_evaluations = async_to_streamed_response_wrapper(
            scheduled_evaluations.list_evaluations,
        )
