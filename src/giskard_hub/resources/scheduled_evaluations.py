from __future__ import annotations

from typing import List, Union, Literal, Optional
from datetime import datetime

import httpx

from ..types import (
    Agent,
    Dataset,
    APIResponse,
    FrequencyOption,
    ScheduledEvaluation,
    EvaluationAPIResource,
    APIResponseWithIncluded,
    scheduled_evaluation_list_params,
    scheduled_evaluation_create_params,
    scheduled_evaluation_update_params,
    scheduled_evaluation_retrieve_params,
    scheduled_evaluation_bulk_delete_params,
    scheduled_evaluation_list_evaluations_params,
)
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
    ) -> APIResponse[ScheduledEvaluation]:
        """
        Create Scheduled Evaluation

        Args:
          project_id: Project ID to use for the scheduled evaluation

          name: Name of the scheduled evaluation

          agent_id: Agent ID to use for the scheduled evaluation

          dataset_id: Dataset ID to use for the scheduled evaluation

          tags: List of tags to apply to the scheduled evaluation

          run_count: The number of times to run each test case. This is useful to get a more accurate
              result when the chatbot's generation is not deterministic. Testing stops at the
              first failure. If all runs pass, the test case is considered successful.

          frequency: Frequency of the scheduled evaluation

          time: Time of the scheduled evaluation

          day_of_month: Day of the month to run the scheduled evaluation

          day_of_week: Day of the week to run the scheduled evaluation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
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
                scheduled_evaluation_create_params.ScheduledEvaluationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[ScheduledEvaluation],
        )

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
    ) -> APIResponseWithIncluded[ScheduledEvaluation, List[APIResponse[EvaluationAPIResource]]]:
        """
        Retrieve Scheduled Evaluation

        Args:
          scheduled_evaluation_id: ID of the scheduled evaluation to retrieve

          include: Related resources to include in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scheduled_evaluation_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_evaluation_id` but received {scheduled_evaluation_id!r}"
            )
        return self._get(
            f"/v2/scheduled-evaluations/{scheduled_evaluation_id}",
            options=make_request_options(
                query=maybe_transform(
                    {"include": include}, scheduled_evaluation_retrieve_params.ScheduledEvaluationRetrieveParams
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponseWithIncluded[ScheduledEvaluation, List[APIResponse[EvaluationAPIResource]]],
        )

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
        last_execution_status: Optional[scheduled_evaluation_update_params.LastExecutionStatus] | Omit = omit,
        paused: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[ScheduledEvaluation]:
        """
        Update Scheduled Evaluation

        Args:
          scheduled_evaluation_id: ID of the scheduled evaluation to update

          name: Name of the scheduled evaluation

          run_count: The number of times to run each test case. This is useful to get a more accurate
              result when the chatbot's generation is not deterministic. Testing stops at the
              first failure. If all runs pass, the test case is considered successful.

          frequency: Frequency of the scheduled evaluation

          time: Time of the scheduled evaluation

          day_of_month: Day of the month to run the scheduled evaluation

          day_of_week: Day of the week to run the scheduled evaluation

          last_execution_at: The date and time of the last execution of the scheduled evaluation

          last_execution_status: The status of the last execution of the scheduled evaluation

          paused: Whether the scheduled evaluation is paused

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scheduled_evaluation_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_evaluation_id` but received {scheduled_evaluation_id!r}"
            )
        return self._patch(
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
                scheduled_evaluation_update_params.ScheduledEvaluationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[ScheduledEvaluation],
        )

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
    ) -> APIResponseWithIncluded[List[ScheduledEvaluation], List[APIResponse[EvaluationAPIResource]]]:
        """
        List Scheduled Evaluations

        Args:
          project_id: Project ID to use for the scheduled evaluation

          include: Related resources to include in response

          last_days: Number of days to include in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/scheduled-evaluations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"project_id": project_id, "include": include, "last_days": last_days},
                    scheduled_evaluation_list_params.ScheduledEvaluationListParams,
                ),
            ),
            cast_to=APIResponseWithIncluded[List[ScheduledEvaluation], List[APIResponse[EvaluationAPIResource]]],
        )

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
    ) -> APIResponse[None]:
        """
        Delete Scheduled Evaluation

        Args:
          scheduled_evaluation_id: ID of the scheduled evaluation to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scheduled_evaluation_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_evaluation_id` but received {scheduled_evaluation_id!r}"
            )
        return self._delete(
            f"/v2/scheduled-evaluations/{scheduled_evaluation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

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
    ) -> APIResponse[None]:
        """
        Bulk Delete Scheduled Evaluations

        Args:
          scheduled_evaluation_ids: IDs of the scheduled evaluations to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v2/scheduled-evaluations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"scheduled_evaluation_ids": scheduled_evaluation_ids},
                    scheduled_evaluation_bulk_delete_params.ScheduledEvaluationBulkDeleteParams,
                ),
            ),
            cast_to=APIResponse[None],
        )

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
    ) -> APIResponseWithIncluded[List[EvaluationAPIResource], APIResponse[Agent | Dataset]]:
        """
        List Scheduled Evaluation Evaluations

        Args:
          scheduled_evaluation_id: ID of the scheduled evaluation to list evaluations for

          include: Related resources to include in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scheduled_evaluation_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_evaluation_id` but received {scheduled_evaluation_id!r}"
            )
        return self._get(
            f"/v2/scheduled-evaluations/{scheduled_evaluation_id}/evaluations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include": include},
                    scheduled_evaluation_list_evaluations_params.ScheduledEvaluationListEvaluationsParams,
                ),
            ),
            cast_to=APIResponseWithIncluded[List[EvaluationAPIResource], APIResponse[Agent | Dataset]],
        )


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
    ) -> APIResponse[ScheduledEvaluation]:
        """
        Create Scheduled Evaluation

        Args:
          project_id: Project ID to use for the scheduled evaluation

          name: Name of the scheduled evaluation

          agent_id: Agent ID to use for the scheduled evaluation

          dataset_id: Dataset ID to use for the scheduled evaluation

          tags: List of tags to apply to the scheduled evaluation

          run_count: The number of times to run each test case. This is useful to get a more accurate
              result when the chatbot's generation is not deterministic. Testing stops at the
              first failure. If all runs pass, the test case is considered successful.

          frequency: Frequency of the scheduled evaluation

          time: Time of the scheduled evaluation

          day_of_month: Day of the month to run the scheduled evaluation

          day_of_week: Day of the week to run the scheduled evaluation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
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
                scheduled_evaluation_create_params.ScheduledEvaluationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[ScheduledEvaluation],
        )

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
    ) -> APIResponseWithIncluded[ScheduledEvaluation, List[APIResponse[EvaluationAPIResource]]]:
        """
        Retrieve Scheduled Evaluation

        Args:
          scheduled_evaluation_id: ID of the scheduled evaluation to retrieve

          include: Related resources to include in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scheduled_evaluation_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_evaluation_id` but received {scheduled_evaluation_id!r}"
            )
        return await self._get(
            f"/v2/scheduled-evaluations/{scheduled_evaluation_id}",
            options=make_request_options(
                query=maybe_transform(
                    {"include": include}, scheduled_evaluation_retrieve_params.ScheduledEvaluationRetrieveParams
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=APIResponseWithIncluded[ScheduledEvaluation, List[APIResponse[EvaluationAPIResource]]],
        )

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
        last_execution_status: Optional[scheduled_evaluation_update_params.LastExecutionStatus] | Omit = omit,
        paused: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[ScheduledEvaluation]:
        """
        Update Scheduled Evaluation

        Args:
          scheduled_evaluation_id: ID of the scheduled evaluation to update

          name: Name of the scheduled evaluation

          run_count: The number of times to run each test case. This is useful to get a more accurate
              result when the chatbot's generation is not deterministic. Testing stops at the
              first failure. If all runs pass, the test case is considered successful.

          frequency: Frequency of the scheduled evaluation

          time: Time of the scheduled evaluation

          day_of_month: Day of the month to run the scheduled evaluation

          day_of_week: Day of the week to run the scheduled evaluation

          last_execution_at: The date and time of the last execution of the scheduled evaluation

          last_execution_status: The status of the last execution of the scheduled evaluation

          paused: Whether the scheduled evaluation is paused

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scheduled_evaluation_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_evaluation_id` but received {scheduled_evaluation_id!r}"
            )
        return await self._patch(
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
                scheduled_evaluation_update_params.ScheduledEvaluationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[ScheduledEvaluation],
        )

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
    ) -> APIResponseWithIncluded[List[ScheduledEvaluation], List[APIResponse[EvaluationAPIResource]]]:
        """
        List Scheduled Evaluations

        Args:
          project_id: Project ID to use for the scheduled evaluation

          include: Related resources to include in response

          last_days: Number of days to include in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/scheduled-evaluations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id, "include": include, "last_days": last_days},
                    scheduled_evaluation_list_params.ScheduledEvaluationListParams,
                ),
            ),
            cast_to=APIResponseWithIncluded[List[ScheduledEvaluation], List[APIResponse[EvaluationAPIResource]]],
        )

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
    ) -> APIResponse[None]:
        """
        Delete Scheduled Evaluation

        Args:
          scheduled_evaluation_id: ID of the scheduled evaluation to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scheduled_evaluation_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_evaluation_id` but received {scheduled_evaluation_id!r}"
            )
        return await self._delete(
            f"/v2/scheduled-evaluations/{scheduled_evaluation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

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
    ) -> APIResponse[None]:
        """
        Bulk Delete Scheduled Evaluations

        Args:
          scheduled_evaluation_ids: IDs of the scheduled evaluations to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v2/scheduled-evaluations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"scheduled_evaluation_ids": scheduled_evaluation_ids},
                    scheduled_evaluation_bulk_delete_params.ScheduledEvaluationBulkDeleteParams,
                ),
            ),
            cast_to=APIResponse[None],
        )

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
    ) -> APIResponseWithIncluded[List[EvaluationAPIResource], APIResponse[Agent | Dataset]]:
        """
        List Scheduled Evaluation Evaluations

        Args:
          scheduled_evaluation_id: ID of the scheduled evaluation to list evaluations for

          include: Related resources to include in response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not scheduled_evaluation_id:
            raise ValueError(
                f"Expected a non-empty value for `scheduled_evaluation_id` but received {scheduled_evaluation_id!r}"
            )
        return await self._get(
            f"/v2/scheduled-evaluations/{scheduled_evaluation_id}/evaluations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include": include},
                    scheduled_evaluation_list_evaluations_params.ScheduledEvaluationListEvaluationsParams,
                ),
            ),
            cast_to=APIResponseWithIncluded[List[EvaluationAPIResource], APIResponse[Agent | Dataset]],
        )


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
