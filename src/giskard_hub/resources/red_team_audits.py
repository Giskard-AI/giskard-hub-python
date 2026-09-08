from __future__ import annotations

from typing import List, Mapping, Optional, cast

import httpx

from ..types import (
    RedTeamAudit,
    RedTeamAuditLogs,
    RedTeamAuditContent,
    RedTeamAuditScanType,
    RedTeamAuditDownloadType,
)
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._analytics import capture_event, make_distinct_id
from .._base_client import make_request_options
from ..types.common import APIResponse
from ..types.red_team_audit import (
    RedTeamAuditListParams,
    RedTeamAuditLogsParams,
    RedTeamAuditCreateParams,
    RedTeamAuditImportParams,
    RedTeamAuditDownloadParams,
)

__all__ = ["RedTeamAuditsResource", "AsyncRedTeamAuditsResource"]


class RedTeamAuditsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RedTeamAuditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return RedTeamAuditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RedTeamAuditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return RedTeamAuditsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: str,
        target_agent_id: str,
        input_evaluation_ids: SequenceNotStr[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        scan_types: Optional[List[RedTeamAuditScanType]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAudit:
        """Create a red team audit.

        Parameters
        ----------
        project_id : str
            Project ID to attach the audit to.
        target_agent_id : str
            ID of the agent to audit.
        input_evaluation_ids : list of str, optional
            Evaluation IDs to use as audit inputs.
        name : str or None, optional
            Optional display name for the audit.
        scan_types : list of RedTeamAuditScanType or None, optional
            Scan types to run as part of the audit.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        RedTeamAudit
            The newly created red team audit.
        """
        response = self._post(
            "/v2/red-team-audits",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "target_agent_id": target_agent_id,
                    "input_evaluation_ids": input_evaluation_ids,
                    "name": name,
                    "scan_types": scan_types,
                },
                RedTeamAuditCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[RedTeamAudit],
        )

        result = self._unwrap(response)
        capture_event(
            make_distinct_id(self._client.api_key),
            "red_team_audit_created",
            {"audit_id": result.id},
        )
        return result

    def retrieve(
        self,
        audit_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAudit:
        """Retrieve a red team audit by its ID.

        Parameters
        ----------
        audit_id : str
            ID of the red team audit to retrieve.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        RedTeamAudit
            The requested red team audit.

        Raises
        ------
        ValueError
            If `audit_id` is empty.
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        response = self._get(
            f"/v2/red-team-audits/{audit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[RedTeamAudit],
        )

        return self._unwrap(response)

    def list(
        self,
        *,
        project_id: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[RedTeamAudit]:
        """List red team audits, optionally filtered by project.

        Parameters
        ----------
        project_id : str or None, optional
            Project ID to list audits for.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        list of RedTeamAudit
            The red team audits matching the filter.
        """
        response = self._get(
            "/v2/red-team-audits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, RedTeamAuditListParams),
            ),
            cast_to=APIResponse[List[RedTeamAudit]],
        )

        return self._unwrap(response)

    def delete(
        self,
        audit_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a red team audit by its ID.

        Parameters
        ----------
        audit_id : str
            ID of the red team audit to delete.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If `audit_id` is empty.
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        response = self._delete(
            f"/v2/red-team-audits/{audit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    def import_(
        self,
        *,
        project_id: str,
        target_agent_id: str,
        content: FileTypes,
        name: Optional[str] | Omit = omit,
        report: FileTypes | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAudit:
        """Import a red team audit from an archive.

        Parameters
        ----------
        project_id : str
            Project ID to attach the imported audit to.
        target_agent_id : str
            ID of the agent the imported audit targets.
        content : FileTypes
            Audit archive to import.
        name : str or None, optional
            Optional display name for the imported audit.
        report : FileTypes, optional
            Optional PDF report to attach to the imported audit.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        RedTeamAudit
            The imported red team audit.
        """
        body = deepcopy_minimal(
            {
                "project_id": project_id,
                "target_agent_id": target_agent_id,
                "content": content,
                "name": name,
                "report": report,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["content"], ["report"]])
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        response = self._post(
            "/v2/red-team-audits/import",
            body=maybe_transform(body, RedTeamAuditImportParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[RedTeamAudit],
        )

        return self._unwrap(response)

    def content(
        self,
        audit_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAuditContent:
        """Retrieve the structured content of a red team audit.

        Parameters
        ----------
        audit_id : str
            ID of the red team audit.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        RedTeamAuditContent
            Structured findings, remediations, and overall assessment.

        Raises
        ------
        ValueError
            If `audit_id` is empty.
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        response = self._get(
            f"/v2/red-team-audits/{audit_id}/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[RedTeamAuditContent],
        )

        return self._unwrap(response)

    def logs(
        self,
        audit_id: str,
        *,
        after: int | Omit = omit,
        limit: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAuditLogs:
        """Retrieve log chunks produced by a red team audit.

        Parameters
        ----------
        audit_id : str
            ID of the red team audit.
        after : int, optional
            Return chunks after this cursor.
        limit : int, optional
            Maximum number of log chunks to return.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        RedTeamAuditLogs
            Log chunks and the next cursor.

        Raises
        ------
        ValueError
            If `audit_id` is empty.
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        response = self._get(
            f"/v2/red-team-audits/{audit_id}/logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"after": after, "limit": limit}, RedTeamAuditLogsParams),
            ),
            cast_to=APIResponse[RedTeamAuditLogs],
        )

        return self._unwrap(response)

    def download(
        self,
        audit_id: str,
        *,
        type: RedTeamAuditDownloadType | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> bytes:
        """Download a red team audit artifact.

        Parameters
        ----------
        audit_id : str
            ID of the red team audit.
        type : {'report', 'logs', 'run-archive'}, optional
            Artifact to download. Defaults to ``report``.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        bytes
            The downloaded artifact bytes.

        Raises
        ------
        ValueError
            If `audit_id` is empty.
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            f"/v2/red-team-audits/{audit_id}/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, RedTeamAuditDownloadParams),
            ),
            cast_to=bytes,
        )


class AsyncRedTeamAuditsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRedTeamAuditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRedTeamAuditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRedTeamAuditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncRedTeamAuditsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: str,
        target_agent_id: str,
        input_evaluation_ids: SequenceNotStr[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        scan_types: Optional[List[RedTeamAuditScanType]] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAudit:
        """Create a red team audit.

        Parameters
        ----------
        project_id : str
            Project ID to attach the audit to.
        target_agent_id : str
            ID of the agent to audit.
        input_evaluation_ids : list of str, optional
            Evaluation IDs to use as audit inputs.
        name : str or None, optional
            Optional display name for the audit.
        scan_types : list of RedTeamAuditScanType or None, optional
            Scan types to run as part of the audit.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        RedTeamAudit
            The newly created red team audit.
        """
        response = await self._post(
            "/v2/red-team-audits",
            body=await async_maybe_transform(
                {
                    "project_id": project_id,
                    "target_agent_id": target_agent_id,
                    "input_evaluation_ids": input_evaluation_ids,
                    "name": name,
                    "scan_types": scan_types,
                },
                RedTeamAuditCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[RedTeamAudit],
        )

        result = self._unwrap(response)
        capture_event(
            make_distinct_id(self._client.api_key),
            "red_team_audit_created",
            {"audit_id": result.id},
        )
        return result

    async def retrieve(
        self,
        audit_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAudit:
        """Retrieve a red team audit by its ID.

        Parameters
        ----------
        audit_id : str
            ID of the red team audit to retrieve.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        RedTeamAudit
            The requested red team audit.

        Raises
        ------
        ValueError
            If `audit_id` is empty.
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        response = await self._get(
            f"/v2/red-team-audits/{audit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[RedTeamAudit],
        )

        return self._unwrap(response)

    async def list(
        self,
        *,
        project_id: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> List[RedTeamAudit]:
        """List red team audits, optionally filtered by project.

        Parameters
        ----------
        project_id : str or None, optional
            Project ID to list audits for.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        list of RedTeamAudit
            The red team audits matching the filter.
        """
        response = await self._get(
            "/v2/red-team-audits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project_id": project_id}, RedTeamAuditListParams),
            ),
            cast_to=APIResponse[List[RedTeamAudit]],
        )

        return self._unwrap(response)

    async def delete(
        self,
        audit_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a red team audit by its ID.

        Parameters
        ----------
        audit_id : str
            ID of the red team audit to delete.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If `audit_id` is empty.
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        response = await self._delete(
            f"/v2/red-team-audits/{audit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    async def import_(
        self,
        *,
        project_id: str,
        target_agent_id: str,
        content: FileTypes,
        name: Optional[str] | Omit = omit,
        report: FileTypes | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAudit:
        """Import a red team audit from an archive.

        Parameters
        ----------
        project_id : str
            Project ID to attach the imported audit to.
        target_agent_id : str
            ID of the agent the imported audit targets.
        content : FileTypes
            Audit archive to import.
        name : str or None, optional
            Optional display name for the imported audit.
        report : FileTypes, optional
            Optional PDF report to attach to the imported audit.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        RedTeamAudit
            The imported red team audit.
        """
        body = deepcopy_minimal(
            {
                "project_id": project_id,
                "target_agent_id": target_agent_id,
                "content": content,
                "name": name,
                "report": report,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["content"], ["report"]])
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        response = await self._post(
            "/v2/red-team-audits/import",
            body=await async_maybe_transform(body, RedTeamAuditImportParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[RedTeamAudit],
        )

        return self._unwrap(response)

    async def content(
        self,
        audit_id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAuditContent:
        """Retrieve the structured content of a red team audit.

        Parameters
        ----------
        audit_id : str
            ID of the red team audit.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        RedTeamAuditContent
            Structured findings, remediations, and overall assessment.

        Raises
        ------
        ValueError
            If `audit_id` is empty.
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        response = await self._get(
            f"/v2/red-team-audits/{audit_id}/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[RedTeamAuditContent],
        )

        return self._unwrap(response)

    async def logs(
        self,
        audit_id: str,
        *,
        after: int | Omit = omit,
        limit: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RedTeamAuditLogs:
        """Retrieve log chunks produced by a red team audit.

        Parameters
        ----------
        audit_id : str
            ID of the red team audit.
        after : int, optional
            Return chunks after this cursor.
        limit : int, optional
            Maximum number of log chunks to return.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        RedTeamAuditLogs
            Log chunks and the next cursor.

        Raises
        ------
        ValueError
            If `audit_id` is empty.
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        response = await self._get(
            f"/v2/red-team-audits/{audit_id}/logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"after": after, "limit": limit}, RedTeamAuditLogsParams),
            ),
            cast_to=APIResponse[RedTeamAuditLogs],
        )

        return self._unwrap(response)

    async def download(
        self,
        audit_id: str,
        *,
        type: RedTeamAuditDownloadType | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> bytes:
        """Download a red team audit artifact.

        Parameters
        ----------
        audit_id : str
            ID of the red team audit.
        type : {'report', 'logs', 'run-archive'}, optional
            Artifact to download. Defaults to ``report``.

        Other Parameters
        ----------------
        extra_headers : Headers or None
            Send extra headers.
        extra_query : Query or None
            Add additional query parameters to the request.
        extra_body : Body or None
            Add additional JSON properties to the request.
        timeout : float, httpx.Timeout, or None
            Override the client-level default timeout for this request, in seconds.

        Returns
        -------
        bytes
            The downloaded artifact bytes.

        Raises
        ------
        ValueError
            If `audit_id` is empty.
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            f"/v2/red-team-audits/{audit_id}/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"type": type}, RedTeamAuditDownloadParams),
            ),
            cast_to=bytes,
        )


class RedTeamAuditsResourceWithRawResponse:
    def __init__(self, red_team_audits: RedTeamAuditsResource) -> None:
        self._red_team_audits = red_team_audits

        self.create = to_raw_response_wrapper(
            red_team_audits.create,
        )
        self.retrieve = to_raw_response_wrapper(
            red_team_audits.retrieve,
        )
        self.list = to_raw_response_wrapper(
            red_team_audits.list,
        )
        self.delete = to_raw_response_wrapper(
            red_team_audits.delete,
        )
        self.import_ = to_raw_response_wrapper(
            red_team_audits.import_,
        )
        self.content = to_raw_response_wrapper(
            red_team_audits.content,
        )
        self.logs = to_raw_response_wrapper(
            red_team_audits.logs,
        )
        self.download = to_custom_raw_response_wrapper(
            red_team_audits.download,
            BinaryAPIResponse,
        )


class AsyncRedTeamAuditsResourceWithRawResponse:
    def __init__(self, red_team_audits: AsyncRedTeamAuditsResource) -> None:
        self._red_team_audits = red_team_audits

        self.create = async_to_raw_response_wrapper(
            red_team_audits.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            red_team_audits.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            red_team_audits.list,
        )
        self.delete = async_to_raw_response_wrapper(
            red_team_audits.delete,
        )
        self.import_ = async_to_raw_response_wrapper(
            red_team_audits.import_,
        )
        self.content = async_to_raw_response_wrapper(
            red_team_audits.content,
        )
        self.logs = async_to_raw_response_wrapper(
            red_team_audits.logs,
        )
        self.download = async_to_custom_raw_response_wrapper(
            red_team_audits.download,
            AsyncBinaryAPIResponse,
        )


class RedTeamAuditsResourceWithStreamingResponse:
    def __init__(self, red_team_audits: RedTeamAuditsResource) -> None:
        self._red_team_audits = red_team_audits

        self.create = to_streamed_response_wrapper(
            red_team_audits.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            red_team_audits.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            red_team_audits.list,
        )
        self.delete = to_streamed_response_wrapper(
            red_team_audits.delete,
        )
        self.import_ = to_streamed_response_wrapper(
            red_team_audits.import_,
        )
        self.content = to_streamed_response_wrapper(
            red_team_audits.content,
        )
        self.logs = to_streamed_response_wrapper(
            red_team_audits.logs,
        )
        self.download = to_custom_streamed_response_wrapper(
            red_team_audits.download,
            StreamedBinaryAPIResponse,
        )


class AsyncRedTeamAuditsResourceWithStreamingResponse:
    def __init__(self, red_team_audits: AsyncRedTeamAuditsResource) -> None:
        self._red_team_audits = red_team_audits

        self.create = async_to_streamed_response_wrapper(
            red_team_audits.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            red_team_audits.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            red_team_audits.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            red_team_audits.delete,
        )
        self.import_ = async_to_streamed_response_wrapper(
            red_team_audits.import_,
        )
        self.content = async_to_streamed_response_wrapper(
            red_team_audits.content,
        )
        self.logs = async_to_streamed_response_wrapper(
            red_team_audits.logs,
        )
        self.download = async_to_custom_streamed_response_wrapper(
            red_team_audits.download,
            AsyncStreamedBinaryAPIResponse,
        )
