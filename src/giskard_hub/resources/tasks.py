from __future__ import annotations

from typing import List, Optional

import httpx

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
from ..types.task import (
    Task,
    TaskStatus,
    TaskPriority,
    TaskListParams,
    TaskCreateParams,
    TaskUpdateParams,
    TaskBulkDeleteParams,
)
from .._base_client import make_request_options
from ..types.common import APIResponse

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: str,
        priority: Optional[TaskPriority] | Omit = omit,
        status: TaskStatus | Omit = omit,
        description: str,
        assignee_ids: SequenceNotStr[str] | Omit = omit,
        evaluation_result_id: Optional[str] | Omit = omit,
        dataset_test_case_id: Optional[str] | Omit = omit,
        probe_attempt_id: Optional[str] | Omit = omit,
        disable_test: bool | Omit = omit,
        hide_result: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """
        Create a new task in the specified project.

        Parameters
        ----------
        project_id : str
            Project ID to create the task in.
        priority : Optional[TaskPriority] | Omit
            Priority of the task.
        status : TaskStatus | Omit
            Status of the task.
        description : str
            Description of the task to create.
        assignee_ids : SequenceNotStr[str] | Omit
            IDs of the users to assign the task to.
        evaluation_result_id : Optional[str] | Omit
            ID of the evaluation result to assign the task to.
        dataset_test_case_id : Optional[str] | Omit
            ID of the dataset test case to assign the task to.
        probe_attempt_id : Optional[str] | Omit
            ID of the probe attempt to assign the task to.
        disable_test : bool | Omit
            Whether to disable the test.
        hide_result : bool | Omit
            Whether to hide the result.

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
        Task
            The newly created task.
        """
        response = self._post(
            "/v2/tasks",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "priority": priority,
                    "status": status,
                    "description": description,
                    "assignee_ids": assignee_ids,
                    "evaluation_result_id": evaluation_result_id,
                    "dataset_test_case_id": dataset_test_case_id,
                    "probe_attempt_id": probe_attempt_id,
                    "disable_test": disable_test,
                    "hide_result": hide_result,
                },
                TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Task],
        )

        return self._unwrap(response)

    def retrieve(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """
        Retrieve a task by its ID.

        Parameters
        ----------
        task_id : str
            ID of the task to retrieve.

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
        Task
            The requested task.

        Raises
        ------
        ValueError
            If ``task_id`` is empty.
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        response = self._get(
            f"/v2/tasks/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Task],
        )

        return self._unwrap(response)

    def update(
        self,
        task_id: str,
        *,
        status: Optional[TaskStatus] | Omit = omit,
        description: Optional[str] | Omit = omit,
        priority: Optional[TaskPriority] | Omit = omit,
        assignee_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        set_test_case_status: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """
        Update an existing task's metadata and assignees.

        Parameters
        ----------
        task_id : str
            ID of the task to update.
        status : Optional[TaskStatus] | Omit
            Status of the task.
        description : Optional[str] | Omit
            Description of the task.
        priority : Optional[TaskPriority] | Omit
            Priority of the task.
        assignee_ids : Optional[SequenceNotStr[str]] | Omit
            IDs of the users to assign the task to.
        set_test_case_status : Optional[str] | Omit
            Status of the test case to set.

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
        Task
            The updated task.

        Raises
        ------
        ValueError
            If ``task_id`` is empty.
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        response = self._patch(
            f"/v2/tasks/{task_id}",
            body=maybe_transform(
                {
                    "status": status,
                    "description": description,
                    "priority": priority,
                    "assignee_ids": assignee_ids,
                    "set_test_case_status": set_test_case_status,
                },
                TaskUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Task],
        )

        return self._unwrap(response)

    def list(
        self,
        *,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[Task]:
        """
        List all tasks for a project, ordered by creation date descending.

        Parameters
        ----------
        project_id : Optional[str] | Omit
            Project ID to list tasks for.

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
        List[Task]
            A list of tasks for the specified project.
        """
        response = self._get(
            "/v2/tasks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "project_id": project_id,
                    },
                    TaskListParams,
                ),
            ),
            cast_to=APIResponse[List[Task]],
        )

        return self._unwrap(response)

    def delete(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a task by its ID.

        Parameters
        ----------
        task_id : str
            ID of the task to delete.

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
            If ``task_id`` is empty.
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        response = self._delete(
            f"/v2/tasks/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    def bulk_delete(
        self,
        *,
        task_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete multiple tasks at once.

        Parameters
        ----------
        task_ids : SequenceNotStr[str]
            IDs of the tasks to delete.

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
            "/v2/tasks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"task_ids": task_ids}, TaskBulkDeleteParams),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)


class AsyncTasksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: str,
        priority: Optional[TaskPriority] | Omit = omit,
        status: TaskStatus | Omit = omit,
        description: str,
        assignee_ids: SequenceNotStr[str] | Omit = omit,
        evaluation_result_id: Optional[str] | Omit = omit,
        dataset_test_case_id: Optional[str] | Omit = omit,
        probe_attempt_id: Optional[str] | Omit = omit,
        disable_test: bool | Omit = omit,
        hide_result: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """
        Create a new task in the specified project.

        Parameters
        ----------
        project_id : str
            Project ID to create the task in.
        priority : Optional[TaskPriority] | Omit
            Priority of the task.
        status : TaskStatus | Omit
            Status of the task.
        description : str
            Description of the task to create.
        assignee_ids : SequenceNotStr[str] | Omit
            IDs of the users to assign the task to.
        evaluation_result_id : Optional[str] | Omit
            ID of the evaluation result to assign the task to.
        dataset_test_case_id : Optional[str] | Omit
            ID of the dataset test case to assign the task to.
        probe_attempt_id : Optional[str] | Omit
            ID of the probe attempt to assign the task to.
        disable_test : bool | Omit
            Whether to disable the test.
        hide_result : bool | Omit
            Whether to hide the result.

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
        Task
            The newly created task.
        """
        response = await self._post(
            "/v2/tasks",
            body=await async_maybe_transform(
                {
                    "project_id": project_id,
                    "priority": priority,
                    "status": status,
                    "description": description,
                    "assignee_ids": assignee_ids,
                    "evaluation_result_id": evaluation_result_id,
                    "dataset_test_case_id": dataset_test_case_id,
                    "probe_attempt_id": probe_attempt_id,
                    "disable_test": disable_test,
                    "hide_result": hide_result,
                },
                TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Task],
        )

        return self._unwrap(response)

    async def retrieve(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """
        Retrieve a task by its ID.

        Parameters
        ----------
        task_id : str
            ID of the task to retrieve.

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
        Task
            The requested task.

        Raises
        ------
        ValueError
            If ``task_id`` is empty.
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        response = await self._get(
            f"/v2/tasks/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Task],
        )

        return self._unwrap(response)

    async def update(
        self,
        task_id: str,
        *,
        status: Optional[TaskStatus] | Omit = omit,
        description: Optional[str] | Omit = omit,
        priority: Optional[TaskPriority] | Omit = omit,
        assignee_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        set_test_case_status: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Task:
        """
        Update an existing task's metadata and assignees.

        Parameters
        ----------
        task_id : str
            ID of the task to update.
        status : Optional[TaskStatus] | Omit
            Status of the task.
        description : Optional[str] | Omit
            Description of the task.
        priority : Optional[TaskPriority] | Omit
            Priority of the task.
        assignee_ids : Optional[SequenceNotStr[str]] | Omit
            IDs of the users to assign the task to.
        set_test_case_status : Optional[str] | Omit
            Status of the test case to set.

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
        Task
            The updated task.

        Raises
        ------
        ValueError
            If ``task_id`` is empty.
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        response = await self._patch(
            f"/v2/tasks/{task_id}",
            body=await async_maybe_transform(
                {
                    "status": status,
                    "description": description,
                    "priority": priority,
                    "assignee_ids": assignee_ids,
                    "set_test_case_status": set_test_case_status,
                },
                TaskUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[Task],
        )

        return self._unwrap(response)

    async def list(
        self,
        *,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[Task]:
        """
        List all tasks for a project, ordered by creation date descending.

        Parameters
        ----------
        project_id : Optional[str] | Omit
            Project ID to list tasks for.

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
        List[Task]
            A list of tasks for the specified project.
        """
        response = await self._get(
            "/v2/tasks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "project_id": project_id,
                    },
                    TaskListParams,
                ),
            ),
            cast_to=APIResponse[List[Task]],
        )

        return self._unwrap(response)

    async def delete(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a task by its ID.

        Parameters
        ----------
        task_id : str
            ID of the task to delete.

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
            If ``task_id`` is empty.
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        response = await self._delete(
            f"/v2/tasks/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    async def bulk_delete(
        self,
        *,
        task_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete multiple tasks at once.

        Parameters
        ----------
        task_ids : SequenceNotStr[str]
            IDs of the tasks to delete.

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
            "/v2/tasks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"task_ids": task_ids}, TaskBulkDeleteParams),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            tasks.update,
        )
        self.list = to_raw_response_wrapper(
            tasks.list,
        )
        self.delete = to_raw_response_wrapper(
            tasks.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            tasks.bulk_delete,
        )


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            tasks.update,
        )
        self.list = async_to_raw_response_wrapper(
            tasks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tasks.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            tasks.bulk_delete,
        )


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            tasks.update,
        )
        self.list = to_streamed_response_wrapper(
            tasks.list,
        )
        self.delete = to_streamed_response_wrapper(
            tasks.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            tasks.bulk_delete,
        )


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            tasks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tasks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tasks.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            tasks.bulk_delete,
        )
