from __future__ import annotations

from typing import List, Union, Optional, Literal
from datetime import datetime

import httpx

from ..types import (
    FrequencyOption,
    scheduled_evaluation_list_params,
    scheduled_evaluation_create_params,
    scheduled_evaluation_update_params,
    scheduled_evaluation_bulk_delete_params,
    scheduled_evaluation_list_latest_runs_params,
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
from ..types.frequency_option import FrequencyOption
from ..types.api_response_none import APIResponseNone
from ..types.api_response_scheduled_evaluation import APIResponseScheduledEvaluation
from ..types.scheduled_evaluation_list_response import ScheduledEvaluationListResponse
from ..types.scheduled_evaluation_list_evaluations_response import ScheduledEvaluationListEvaluationsResponse
from ..types.scheduled_evaluation_list_latest_runs_response import ScheduledEvaluationListLatestRunsResponse

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
        agent_id: str,
        dataset_id: str,
        frequency: FrequencyOption,
        name: str,
        project_id: str,
        time: str,
        day_of_month: Optional[int] | Omit = omit,
        day_of_week: Optional[int] | Omit = omit,
        run_count: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseScheduledEvaluation:
        """
        Create Scheduled Evaluation

        Args:
          run_count: The number of times to run each test case. This is useful to get a more accurate
              result when the chatbot's generation is not deterministic. Testing stops at the
              first failure. If all runs pass, the test case is considered successful.

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
            cast_to=APIResponseScheduledEvaluation,
        )

    def retrieve(
        self,
        scheduled_evaluation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseScheduledEvaluation:
        """
        Retrieve Scheduled Evaluation

        Args:
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseScheduledEvaluation,
        )

    def update(
        self,
        scheduled_evaluation_id: str,
        *,
        day_of_month: Optional[int] | Omit = omit,
        day_of_week: Optional[int] | Omit = omit,
        frequency: Optional[FrequencyOption] | Omit = omit,
        last_execution_at: Union[str, datetime, None] | Omit = omit,
        last_execution_status: Optional[scheduled_evaluation_update_params.LastExecutionStatus] | Omit = omit,
        name: Optional[str] | Omit = omit,
        paused: Optional[bool] | Omit = omit,
        run_count: Optional[int] | Omit = omit,
        time: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseScheduledEvaluation:
        """
        Update Scheduled Evaluation

        Args:
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
            cast_to=APIResponseScheduledEvaluation,
        )

    def list(
        self,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledEvaluationListResponse:
        """
        List Scheduled Evaluations

        Args:
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
                    {"project_id": project_id}, scheduled_evaluation_list_params.ScheduledEvaluationListParams
                ),
            ),
            cast_to=ScheduledEvaluationListResponse,
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
    ) -> APIResponseNone:
        """
        Delete Scheduled Evaluation

        Args:
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
            cast_to=APIResponseNone,
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
    ) -> APIResponseNone:
        """
        Bulk Delete Scheduled Evaluations

        Args:
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
            cast_to=APIResponseNone,
        )

    def list_evaluations(
        self,
        scheduled_evaluation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledEvaluationListEvaluationsResponse:
        """
        List Scheduled Evaluation Evaluations

        Args:
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledEvaluationListEvaluationsResponse,
        )

    def list_latest_runs(
        self,
        *,
        project_id: str,
        include: Optional[List[Literal["scheduled_evaluation", "latest_runs"]]] | Omit = omit,
        last_days: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledEvaluationListLatestRunsResponse:
        """
        List all evaluation runs triggered by a schedule for a project, grouped by
        scheduled evaluation.

        Optional `last_days` filters by creation date.

        Args:
          last_days: If provided, only include evaluation runs created in the last N days.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/scheduled-evaluation-runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "project_id": project_id,
                        "include": include,
                        "last_days": last_days,
                    },
                    scheduled_evaluation_list_latest_runs_params.ScheduledEvaluationListLatestRunsParams,
                ),
            ),
            cast_to=ScheduledEvaluationListLatestRunsResponse,
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
        agent_id: str,
        dataset_id: str,
        frequency: FrequencyOption,
        name: str,
        project_id: str,
        time: str,
        day_of_month: Optional[int] | Omit = omit,
        day_of_week: Optional[int] | Omit = omit,
        run_count: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseScheduledEvaluation:
        """
        Create Scheduled Evaluation

        Args:
          run_count: The number of times to run each test case. This is useful to get a more accurate
              result when the chatbot's generation is not deterministic. Testing stops at the
              first failure. If all runs pass, the test case is considered successful.

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
            cast_to=APIResponseScheduledEvaluation,
        )

    async def retrieve(
        self,
        scheduled_evaluation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseScheduledEvaluation:
        """
        Retrieve Scheduled Evaluation

        Args:
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseScheduledEvaluation,
        )

    async def update(
        self,
        scheduled_evaluation_id: str,
        *,
        day_of_month: Optional[int] | Omit = omit,
        day_of_week: Optional[int] | Omit = omit,
        frequency: Optional[FrequencyOption] | Omit = omit,
        last_execution_at: Union[str, datetime, None] | Omit = omit,
        last_execution_status: Optional[scheduled_evaluation_update_params.LastExecutionStatus] | Omit = omit,
        name: Optional[str] | Omit = omit,
        paused: Optional[bool] | Omit = omit,
        run_count: Optional[int] | Omit = omit,
        time: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseScheduledEvaluation:
        """
        Update Scheduled Evaluation

        Args:
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
            cast_to=APIResponseScheduledEvaluation,
        )

    async def list(
        self,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledEvaluationListResponse:
        """
        List Scheduled Evaluations

        Args:
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
                    {"project_id": project_id}, scheduled_evaluation_list_params.ScheduledEvaluationListParams
                ),
            ),
            cast_to=ScheduledEvaluationListResponse,
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
    ) -> APIResponseNone:
        """
        Delete Scheduled Evaluation

        Args:
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
            cast_to=APIResponseNone,
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
    ) -> APIResponseNone:
        """
        Bulk Delete Scheduled Evaluations

        Args:
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
            cast_to=APIResponseNone,
        )

    async def list_evaluations(
        self,
        scheduled_evaluation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledEvaluationListEvaluationsResponse:
        """
        List Scheduled Evaluation Evaluations

        Args:
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledEvaluationListEvaluationsResponse,
        )

    async def list_latest_runs(
        self,
        *,
        project_id: str,
        include: Optional[List[Literal["scheduled_evaluation", "latest_runs"]]] | Omit = omit,
        last_days: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduledEvaluationListLatestRunsResponse:
        """
        List all evaluation runs triggered by a schedule for a project, grouped by
        scheduled evaluation.

        Optional `last_days` filters by creation date.

        Args:
          last_days: If provided, only include evaluation runs created in the last N days.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/scheduled-evaluation-runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "project_id": project_id,
                        "include": include,
                        "last_days": last_days,
                    },
                    scheduled_evaluation_list_latest_runs_params.ScheduledEvaluationListLatestRunsParams,
                ),
            ),
            cast_to=ScheduledEvaluationListLatestRunsResponse,
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
        self.list_latest_runs = to_raw_response_wrapper(
            scheduled_evaluations.list_latest_runs,
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
        self.list_latest_runs = async_to_raw_response_wrapper(
            scheduled_evaluations.list_latest_runs,
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
        self.list_latest_runs = to_streamed_response_wrapper(
            scheduled_evaluations.list_latest_runs,
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
        self.list_latest_runs = async_to_streamed_response_wrapper(
            scheduled_evaluations.list_latest_runs,
        )
