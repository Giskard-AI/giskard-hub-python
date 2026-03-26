from __future__ import annotations

import os
from typing import Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import (
    audit,
    tasks,
    agents,
    checks,
    helpers,
    datasets,
    projects,
    knowledge_bases,
    playground_chats,
    scheduled_evaluations,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, HubClientError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.scans import scans
from .resources.test_cases import test_cases
from .resources.evaluations import evaluations

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "HubClient",
    "AsyncHubClient",
    "Client",
    "AsyncClient",
]

_API_SUFFIX = "/_api"


def _normalize_base_url(base_url: str, *, auto_add_api_suffix: bool) -> str:
    base_url = base_url.rstrip("/")
    if auto_add_api_suffix and not base_url.endswith(_API_SUFFIX):
        base_url += _API_SUFFIX
    return base_url


class HubClient(SyncAPIClient):
    audit_logs: audit.AuditLogsResource
    agents: agents.AgentsResource
    checks: checks.ChecksResource
    datasets: datasets.DatasetsResource
    evaluations: evaluations.EvaluationsResource
    helpers: "helpers.HelpersResource"
    knowledge_bases: knowledge_bases.KnowledgeBasesResource
    playground_chats: playground_chats.PlaygroundChatsResource
    projects: projects.ProjectsResource
    scans: scans.ScansResource
    scheduled_evaluations: scheduled_evaluations.ScheduledEvaluationsResource
    tasks: tasks.TasksResource
    test_cases: test_cases.TestCasesResource
    with_raw_response: HubClientWithRawResponse
    with_streaming_response: HubClientWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        auto_add_api_suffix: bool = True,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        # When debugging, you can set this to False to ignore validation errors.
        _strict_response_validation: bool = True,
    ) -> None:
        """Construct a new synchronous HubClient client instance.

        This automatically infers the `api_key` argument from the `GISKARD_HUB_API_KEY` environment variable if it is not provided.
        The `base_url` will have `/_api` appended automatically unless it is already present or `auto_add_api_suffix=False`.
        """
        if api_key is None:
            api_key = os.environ.get("GISKARD_HUB_API_KEY")
        if api_key is None:
            raise HubClientError(
                "The api_key client option must be set either by passing api_key to the client or by setting the GISKARD_HUB_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("GISKARD_HUB_BASE_URL")
        if base_url is None:
            raise HubClientError(
                "No base_url provided. Pass base_url to the client or set the GISKARD_HUB_BASE_URL environment variable."
            )
        base_url = _normalize_base_url(str(base_url), auto_add_api_suffix=auto_add_api_suffix)

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.audit_logs = audit.AuditLogsResource(self)
        self.agents = agents.AgentsResource(self)
        self.checks = checks.ChecksResource(self)
        self.datasets = datasets.DatasetsResource(self)
        self.evaluations = evaluations.EvaluationsResource(self)
        self.helpers = helpers.HelpersResource(self)
        self.knowledge_bases = knowledge_bases.KnowledgeBasesResource(self)
        self.playground_chats = playground_chats.PlaygroundChatsResource(self)
        self.projects = projects.ProjectsResource(self)
        self.scans = scans.ScansResource(self)
        self.scheduled_evaluations = scheduled_evaluations.ScheduledEvaluationsResource(self)
        self.tasks = tasks.TasksResource(self)
        self.test_cases = test_cases.TestCasesResource(self)
        self.with_raw_response = HubClientWithRawResponse(self)
        self.with_streaming_response = HubClientWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Giskard-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        auto_add_api_suffix: bool = True,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            auto_add_api_suffix=auto_add_api_suffix if base_url is not None else False,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncHubClient(AsyncAPIClient):
    audit_logs: audit.AsyncAuditLogsResource
    agents: agents.AsyncAgentsResource
    checks: checks.AsyncChecksResource
    datasets: datasets.AsyncDatasetsResource
    evaluations: evaluations.AsyncEvaluationsResource
    helpers: "helpers.AsyncHelpersResource"
    knowledge_bases: knowledge_bases.AsyncKnowledgeBasesResource
    playground_chats: playground_chats.AsyncPlaygroundChatsResource
    projects: projects.AsyncProjectsResource
    scans: scans.AsyncScansResource
    scheduled_evaluations: scheduled_evaluations.AsyncScheduledEvaluationsResource
    tasks: tasks.AsyncTasksResource
    test_cases: test_cases.AsyncTestCasesResource
    with_raw_response: AsyncHubClientWithRawResponse
    with_streaming_response: AsyncHubClientWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        auto_add_api_suffix: bool = True,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        # When debugging, you can set this to False to ignore validation errors.
        _strict_response_validation: bool = True,
    ) -> None:
        """Construct a new async AsyncHubClient client instance.

        This automatically infers the `api_key` argument from the `GISKARD_HUB_API_KEY` environment variable if it is not provided.
        The `base_url` will have `/_api` appended automatically unless it is already present or `auto_add_api_suffix=False`.
        """
        if api_key is None:
            api_key = os.environ.get("GISKARD_HUB_API_KEY")
        if api_key is None:
            raise HubClientError(
                "The api_key client option must be set either by passing api_key to the client or by setting the GISKARD_HUB_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("GISKARD_HUB_BASE_URL")
        if base_url is None:
            raise HubClientError(
                "No base_url provided. Pass base_url to the client or set the GISKARD_HUB_BASE_URL environment variable."
            )
        base_url = _normalize_base_url(str(base_url), auto_add_api_suffix=auto_add_api_suffix)

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.audit_logs = audit.AsyncAuditLogsResource(self)
        self.agents = agents.AsyncAgentsResource(self)
        self.checks = checks.AsyncChecksResource(self)
        self.datasets = datasets.AsyncDatasetsResource(self)
        self.evaluations = evaluations.AsyncEvaluationsResource(self)
        self.helpers = helpers.AsyncHelpersResource(self)
        self.knowledge_bases = knowledge_bases.AsyncKnowledgeBasesResource(self)
        self.playground_chats = playground_chats.AsyncPlaygroundChatsResource(self)
        self.projects = projects.AsyncProjectsResource(self)
        self.scans = scans.AsyncScansResource(self)
        self.scheduled_evaluations = scheduled_evaluations.AsyncScheduledEvaluationsResource(self)
        self.tasks = tasks.AsyncTasksResource(self)
        self.test_cases = test_cases.AsyncTestCasesResource(self)
        self.with_raw_response = AsyncHubClientWithRawResponse(self)
        self.with_streaming_response = AsyncHubClientWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        # Use repeated query params for arrays, e.g. `include=agent&include=dataset`.
        # This is what FastAPI expects for query params typed as `List[...]`.
        return Querystring(array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Giskard-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        auto_add_api_suffix: bool = True,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            auto_add_api_suffix=auto_add_api_suffix if base_url is not None else False,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class HubClientWithRawResponse:
    def __init__(self, client: HubClient) -> None:
        self.audit_logs = audit.AuditLogsResourceWithRawResponse(client.audit_logs)
        self.agents = agents.AgentsResourceWithRawResponse(client.agents)
        self.checks = checks.ChecksResourceWithRawResponse(client.checks)
        self.datasets = datasets.DatasetsResourceWithRawResponse(client.datasets)
        self.evaluations = evaluations.EvaluationsResourceWithRawResponse(client.evaluations)
        self.knowledge_bases = knowledge_bases.KnowledgeBasesResourceWithRawResponse(client.knowledge_bases)
        self.playground_chats = playground_chats.PlaygroundChatsResourceWithRawResponse(client.playground_chats)
        self.projects = projects.ProjectsResourceWithRawResponse(client.projects)
        self.scans = scans.ScansResourceWithRawResponse(client.scans)
        self.scheduled_evaluations = scheduled_evaluations.ScheduledEvaluationsResourceWithRawResponse(
            client.scheduled_evaluations
        )
        self.tasks = tasks.TasksResourceWithRawResponse(client.tasks)
        self.test_cases = test_cases.TestCasesResourceWithRawResponse(client.test_cases)
        self.helpers = helpers.HelpersResource(client)


class AsyncHubClientWithRawResponse:
    def __init__(self, client: AsyncHubClient) -> None:
        self.audit_logs = audit.AsyncAuditLogsResourceWithRawResponse(client.audit_logs)
        self.agents = agents.AsyncAgentsResourceWithRawResponse(client.agents)
        self.checks = checks.AsyncChecksResourceWithRawResponse(client.checks)
        self.datasets = datasets.AsyncDatasetsResourceWithRawResponse(client.datasets)
        self.evaluations = evaluations.AsyncEvaluationsResourceWithRawResponse(client.evaluations)
        self.knowledge_bases = knowledge_bases.AsyncKnowledgeBasesResourceWithRawResponse(client.knowledge_bases)
        self.playground_chats = playground_chats.AsyncPlaygroundChatsResourceWithRawResponse(client.playground_chats)
        self.projects = projects.AsyncProjectsResourceWithRawResponse(client.projects)
        self.scans = scans.AsyncScansResourceWithRawResponse(client.scans)
        self.scheduled_evaluations = scheduled_evaluations.AsyncScheduledEvaluationsResourceWithRawResponse(
            client.scheduled_evaluations
        )
        self.tasks = tasks.AsyncTasksResourceWithRawResponse(client.tasks)
        self.test_cases = test_cases.AsyncTestCasesResourceWithRawResponse(client.test_cases)
        self.helpers = helpers.AsyncHelpersResource(client)


class HubClientWithStreamedResponse:
    def __init__(self, client: HubClient) -> None:
        self.audit_logs = audit.AuditLogsResourceWithStreamingResponse(client.audit_logs)
        self.agents = agents.AgentsResourceWithStreamingResponse(client.agents)
        self.checks = checks.ChecksResourceWithStreamingResponse(client.checks)
        self.datasets = datasets.DatasetsResourceWithStreamingResponse(client.datasets)
        self.evaluations = evaluations.EvaluationsResourceWithStreamingResponse(client.evaluations)
        self.knowledge_bases = knowledge_bases.KnowledgeBasesResourceWithStreamingResponse(client.knowledge_bases)
        self.playground_chats = playground_chats.PlaygroundChatsResourceWithStreamingResponse(client.playground_chats)
        self.projects = projects.ProjectsResourceWithStreamingResponse(client.projects)
        self.scans = scans.ScansResourceWithStreamingResponse(client.scans)
        self.scheduled_evaluations = scheduled_evaluations.ScheduledEvaluationsResourceWithStreamingResponse(
            client.scheduled_evaluations
        )
        self.tasks = tasks.TasksResourceWithStreamingResponse(client.tasks)
        self.test_cases = test_cases.TestCasesResourceWithStreamingResponse(client.test_cases)
        self.helpers = helpers.HelpersResource(client)


class AsyncHubClientWithStreamedResponse:
    def __init__(self, client: AsyncHubClient) -> None:
        self.audit_logs = audit.AsyncAuditLogsResourceWithStreamingResponse(client.audit_logs)
        self.agents = agents.AsyncAgentsResourceWithStreamingResponse(client.agents)
        self.checks = checks.AsyncChecksResourceWithStreamingResponse(client.checks)
        self.datasets = datasets.AsyncDatasetsResourceWithStreamingResponse(client.datasets)
        self.evaluations = evaluations.AsyncEvaluationsResourceWithStreamingResponse(client.evaluations)
        self.knowledge_bases = knowledge_bases.AsyncKnowledgeBasesResourceWithStreamingResponse(client.knowledge_bases)
        self.playground_chats = playground_chats.AsyncPlaygroundChatsResourceWithStreamingResponse(
            client.playground_chats
        )
        self.projects = projects.AsyncProjectsResourceWithStreamingResponse(client.projects)
        self.scans = scans.AsyncScansResourceWithStreamingResponse(client.scans)
        self.scheduled_evaluations = scheduled_evaluations.AsyncScheduledEvaluationsResourceWithStreamingResponse(
            client.scheduled_evaluations
        )
        self.tasks = tasks.AsyncTasksResourceWithStreamingResponse(client.tasks)
        self.test_cases = test_cases.AsyncTestCasesResourceWithStreamingResponse(client.test_cases)
        self.helpers = helpers.AsyncHelpersResource(client)


Client = HubClient

AsyncClient = AsyncHubClient
