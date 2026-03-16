from __future__ import annotations

import json
from typing import Any, List, Tuple, Literal, Mapping, Optional, cast, overload

import httpx

from ..types import (
    APIPaginatedResponse,
    KnowledgeBaseDocumentRow,
    KnowledgeBaseDocumentFiltersParam,
    KnowledgeBaseDocumentOrderByParam,
    KnowledgeBaseSearchDocumentsParams,
)
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.common import APIResponse, TaskProgressParam, APIPaginatedMetadata
from ..types.knowledge_base import (
    KnowledgeBase,
    KnowledgeBaseListParams,
    KnowledgeBaseCreateParams,
    KnowledgeBaseUpdateParams,
    KnowledgeBaseDocumentDetail,
    KnowledgeBaseBulkDeleteParams,
)

__all__ = ["KnowledgeBasesResource", "AsyncKnowledgeBasesResource"]


class KnowledgeBasesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KnowledgeBasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return KnowledgeBasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KnowledgeBasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return KnowledgeBasesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        project_id: str,
        file: FileTypes | list[dict[str, Any]],
        description: Optional[str] | Omit = omit,
        document_column: str | Omit = omit,
        topic_column: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBase:
        """Create a new knowledge base by uploading a file of documents.

        Parameters
        ----------
        name : str
            Name of the knowledge base.
        project_id : str
            Project ID to create the knowledge base in.
        file : FileTypes | list[dict[str, Any]]
            File to upload for the knowledge base.
        description : Optional[str] | Omit
            Description of the knowledge base.
        document_column : str | Omit
            Column name for the document column.
        topic_column : str | Omit
            Column name for the topic column.

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
        KnowledgeBase
            The created knowledge base.
        """
        if isinstance(file, list):
            file = ("kb_documents.json", json.dumps(file).encode("utf-8"))

        body = deepcopy_minimal(
            {
                "project_id": project_id,
                "name": name,
                "description": description,
                "document_column": document_column,
                "topic_column": topic_column,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        response = self._post(
            "/v2/knowledge-bases",
            body=maybe_transform(body, KnowledgeBaseCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[KnowledgeBase],
        )

        return self._unwrap(response)

    def retrieve(
        self,
        knowledge_base_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBase:
        """Retrieve a knowledge base by its ID, including its topics.

        Parameters
        ----------
        knowledge_base_id : str
            ID of the knowledge base to retrieve.

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
        KnowledgeBase
            The retrieved knowledge base.

        Raises
        ------
        ValueError
            If ``knowledge_base_id`` is empty.
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        response = self._get(
            f"/v2/knowledge-bases/{knowledge_base_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[KnowledgeBase],
        )

        return self._unwrap(response)

    def update(
        self,
        knowledge_base_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[TaskProgressParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBase:
        """Update an existing knowledge base's metadata.

        Parameters
        ----------
        knowledge_base_id : str
            ID of the knowledge base to update.
        description : Optional[str] | Omit
            Description of the knowledge base.
        name : Optional[str] | Omit
            Name of the knowledge base.
        project_id : Optional[str] | Omit
            Project ID to update the knowledge base in.
        status : Optional[TaskProgressParam] | Omit
            Task progress status.

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
        KnowledgeBase
            The updated knowledge base.

        Raises
        ------
        ValueError
            If ``knowledge_base_id`` is empty.
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        response = self._patch(
            f"/v2/knowledge-bases/{knowledge_base_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "project_id": project_id,
                    "status": status,
                },
                KnowledgeBaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[KnowledgeBase],
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
    ) -> List[KnowledgeBase]:
        """List all knowledge bases, optionally filtered by project.

        Parameters
        ----------
        project_id : Optional[str] | Omit
            Project ID to list knowledge bases for.

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
        List[KnowledgeBase]
            A list of knowledge bases.
        """
        response = self._get(
            "/v2/knowledge-bases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, KnowledgeBaseListParams),
            ),
            cast_to=APIResponse[List[KnowledgeBase]],
        )

        return self._unwrap(response)

    def delete(
        self,
        knowledge_base_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a knowledge base by its ID.

        Parameters
        ----------
        knowledge_base_id : str
            ID of the knowledge base to delete.

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
            If ``knowledge_base_id`` is empty.
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        response = self._delete(
            f"/v2/knowledge-bases/{knowledge_base_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    def bulk_delete(
        self,
        *,
        knowledge_base_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete multiple knowledge bases at once.

        Parameters
        ----------
        knowledge_base_ids : SequenceNotStr[str]
            IDs of the knowledge bases to delete.

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
            "/v2/knowledge-bases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"knowledge_base_ids": knowledge_base_ids},
                    KnowledgeBaseBulkDeleteParams,
                ),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    @overload
    def search_documents(
        self,
        knowledge_base_id: str,
        *,
        query: Optional[str] | Omit = omit,
        order_by: Optional[List[KnowledgeBaseDocumentOrderByParam]] | Omit = omit,
        filters: Optional[KnowledgeBaseDocumentFiltersParam] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: bool = False,
    ) -> List[KnowledgeBaseDocumentRow]: ...

    @overload
    def search_documents(
        self,
        knowledge_base_id: str,
        *,
        query: Optional[str] | Omit = omit,
        order_by: Optional[List[KnowledgeBaseDocumentOrderByParam]] | Omit = omit,
        filters: Optional[KnowledgeBaseDocumentFiltersParam] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: Literal[True],
    ) -> Tuple[List[KnowledgeBaseDocumentRow], APIPaginatedMetadata]: ...

    def search_documents(
        self,
        knowledge_base_id: str,
        *,
        query: Optional[str] | Omit = omit,
        order_by: Optional[List[KnowledgeBaseDocumentOrderByParam]] | Omit = omit,
        filters: Optional[KnowledgeBaseDocumentFiltersParam] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: bool = False,
    ) -> List[KnowledgeBaseDocumentRow] | Tuple[List[KnowledgeBaseDocumentRow], APIPaginatedMetadata]:
        """Search documents within a knowledge base using filters, sorting, and pagination.

        Parameters
        ----------
        knowledge_base_id : str
            ID of the knowledge base.
        query : Optional[str] | Omit
            Search query for knowledge base documents.
        order_by : Optional[List[KnowledgeBaseDocumentOrderByParam]] | Omit
            Order by criteria for knowledge base documents.
        filters : Optional[KnowledgeBaseDocumentFiltersParam] | Omit
            Search filters.
        limit : int | Omit
            Maximum number of results to return.
        offset : int | Omit
            Number of results to skip.

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
        List[KnowledgeBaseDocumentRow] | Tuple[List[KnowledgeBaseDocumentRow], APIPaginatedMetadata]
            A list of document rows, or a tuple of document rows and pagination metadata.

        Raises
        ------
        ValueError
            If ``knowledge_base_id`` is empty.
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        response = self._post(
            f"/v2/knowledge-bases/{knowledge_base_id}/documents/search",
            body=maybe_transform(
                {"filters": filters, "order_by": order_by, "search": query},
                KnowledgeBaseSearchDocumentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit, "offset": offset},
                    KnowledgeBaseSearchDocumentsParams,
                ),
            ),
            cast_to=APIPaginatedResponse[KnowledgeBaseDocumentRow, None],
        )

        return self._unwrap_paginated(response, include_metadata)

    def retrieve_document(
        self,
        knowledge_base_id: str,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBaseDocumentDetail:
        """Retrieve detailed information about a specific document in a knowledge base.

        Parameters
        ----------
        knowledge_base_id : str
            ID of the knowledge base.
        document_id : str
            ID of the document.

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
        KnowledgeBaseDocumentDetail
            The detailed document information.

        Raises
        ------
        ValueError
            If ``knowledge_base_id`` or ``document_id`` is empty.
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        response = self._get(
            f"/v2/knowledge-bases/{knowledge_base_id}/documents/{document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[KnowledgeBaseDocumentDetail],
        )

        return self._unwrap(response)


class AsyncKnowledgeBasesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKnowledgeBasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKnowledgeBasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKnowledgeBasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Giskard-AI/giskard-hub-python#with_streaming_response
        """
        return AsyncKnowledgeBasesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        project_id: str,
        file: FileTypes | list[dict[str, Any]],
        description: Optional[str] | Omit = omit,
        document_column: str | Omit = omit,
        topic_column: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBase:
        """Create a new knowledge base by uploading a file of documents.

        Parameters
        ----------
        name : str
            Name of the knowledge base.
        project_id : str
            Project ID to create the knowledge base in.
        file : FileTypes | list[dict[str, Any]]
            File to upload for the knowledge base.
        description : Optional[str] | Omit
            Description of the knowledge base.
        document_column : str | Omit
            Column name for the document column.
        topic_column : str | Omit
            Column name for the topic column.

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
        KnowledgeBase
            The created knowledge base.
        """
        if isinstance(file, list):
            file = ("kb_documents.json", json.dumps(file).encode("utf-8"))

        body = deepcopy_minimal(
            {
                "project_id": project_id,
                "name": name,
                "description": description,
                "document_column": document_column,
                "topic_column": topic_column,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        response = await self._post(
            "/v2/knowledge-bases",
            body=await async_maybe_transform(body, KnowledgeBaseCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[KnowledgeBase],
        )

        return self._unwrap(response)

    async def retrieve(
        self,
        knowledge_base_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBase:
        """Retrieve a knowledge base by its ID, including its topics.

        Parameters
        ----------
        knowledge_base_id : str
            ID of the knowledge base to retrieve.

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
        KnowledgeBase
            The retrieved knowledge base.

        Raises
        ------
        ValueError
            If ``knowledge_base_id`` is empty.
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        response = await self._get(
            f"/v2/knowledge-bases/{knowledge_base_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[KnowledgeBase],
        )

        return self._unwrap(response)

    async def update(
        self,
        knowledge_base_id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[TaskProgressParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBase:
        """Update an existing knowledge base's metadata.

        Parameters
        ----------
        knowledge_base_id : str
            ID of the knowledge base to update.
        description : Optional[str] | Omit
            Description of the knowledge base.
        name : Optional[str] | Omit
            Name of the knowledge base.
        project_id : Optional[str] | Omit
            Project ID to update the knowledge base in.
        status : Optional[TaskProgressParam] | Omit
            Task progress status.

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
        KnowledgeBase
            The updated knowledge base.

        Raises
        ------
        ValueError
            If ``knowledge_base_id`` is empty.
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        response = await self._patch(
            f"/v2/knowledge-bases/{knowledge_base_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "project_id": project_id,
                    "status": status,
                },
                KnowledgeBaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[KnowledgeBase],
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
    ) -> List[KnowledgeBase]:
        """List all knowledge bases, optionally filtered by project.

        Parameters
        ----------
        project_id : Optional[str] | Omit
            Project ID to list knowledge bases for.

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
        List[KnowledgeBase]
            A list of knowledge bases.
        """
        response = await self._get(
            "/v2/knowledge-bases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project_id": project_id}, KnowledgeBaseListParams),
            ),
            cast_to=APIResponse[List[KnowledgeBase]],
        )

        return self._unwrap(response)

    async def delete(
        self,
        knowledge_base_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a knowledge base by its ID.

        Parameters
        ----------
        knowledge_base_id : str
            ID of the knowledge base to delete.

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
            If ``knowledge_base_id`` is empty.
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        response = await self._delete(
            f"/v2/knowledge-bases/{knowledge_base_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    async def bulk_delete(
        self,
        *,
        knowledge_base_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete multiple knowledge bases at once.

        Parameters
        ----------
        knowledge_base_ids : SequenceNotStr[str]
            IDs of the knowledge bases to delete.

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
            "/v2/knowledge-bases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"knowledge_base_ids": knowledge_base_ids},
                    KnowledgeBaseBulkDeleteParams,
                ),
            ),
            cast_to=APIResponse[None],
        )

        return self._unwrap(response)

    @overload
    async def search_documents(
        self,
        knowledge_base_id: str,
        *,
        query: Optional[str] | Omit = omit,
        order_by: Optional[List[KnowledgeBaseDocumentOrderByParam]] | Omit = omit,
        filters: Optional[KnowledgeBaseDocumentFiltersParam] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: bool = False,
    ) -> List[KnowledgeBaseDocumentRow]: ...

    @overload
    async def search_documents(
        self,
        knowledge_base_id: str,
        *,
        query: Optional[str] | Omit = omit,
        order_by: Optional[List[KnowledgeBaseDocumentOrderByParam]] | Omit = omit,
        filters: Optional[KnowledgeBaseDocumentFiltersParam] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: Literal[True],
    ) -> Tuple[List[KnowledgeBaseDocumentRow], APIPaginatedMetadata]: ...

    async def search_documents(
        self,
        knowledge_base_id: str,
        *,
        query: Optional[str] | Omit = omit,
        order_by: Optional[List[KnowledgeBaseDocumentOrderByParam]] | Omit = omit,
        filters: Optional[KnowledgeBaseDocumentFiltersParam] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        include_metadata: bool = False,
    ) -> List[KnowledgeBaseDocumentRow] | Tuple[List[KnowledgeBaseDocumentRow], APIPaginatedMetadata]:
        """Search documents within a knowledge base using filters, sorting, and pagination.

        Parameters
        ----------
        knowledge_base_id : str
            ID of the knowledge base.
        query : Optional[str] | Omit
            Search query for knowledge base documents.
        order_by : Optional[List[KnowledgeBaseDocumentOrderByParam]] | Omit
            Order by criteria for knowledge base documents.
        filters : Optional[KnowledgeBaseDocumentFiltersParam] | Omit
            Search filters.
        limit : int | Omit
            Maximum number of results to return.
        offset : int | Omit
            Number of results to skip.

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
        List[KnowledgeBaseDocumentRow] | Tuple[List[KnowledgeBaseDocumentRow], APIPaginatedMetadata]
            A list of document rows, or a tuple of document rows and pagination metadata.

        Raises
        ------
        ValueError
            If ``knowledge_base_id`` is empty.
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        response = await self._post(
            f"/v2/knowledge-bases/{knowledge_base_id}/documents/search",
            body=await async_maybe_transform(
                {"filters": filters, "order_by": order_by, "search": query},
                KnowledgeBaseSearchDocumentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "offset": offset},
                    KnowledgeBaseSearchDocumentsParams,
                ),
            ),
            cast_to=APIPaginatedResponse[KnowledgeBaseDocumentRow, None],
        )

        return self._unwrap_paginated(response, include_metadata)

    async def retrieve_document(
        self,
        knowledge_base_id: str,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowledgeBaseDocumentDetail:
        """Retrieve detailed information about a specific document in a knowledge base.

        Parameters
        ----------
        knowledge_base_id : str
            ID of the knowledge base.
        document_id : str
            ID of the document.

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
        KnowledgeBaseDocumentDetail
            The detailed document information.

        Raises
        ------
        ValueError
            If ``knowledge_base_id`` or ``document_id`` is empty.
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        response = await self._get(
            f"/v2/knowledge-bases/{knowledge_base_id}/documents/{document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[KnowledgeBaseDocumentDetail],
        )

        return self._unwrap(response)


class KnowledgeBasesResourceWithRawResponse:
    def __init__(self, knowledge_bases: KnowledgeBasesResource) -> None:
        self._knowledge_bases = knowledge_bases

        self.create = to_raw_response_wrapper(
            knowledge_bases.create,
        )
        self.retrieve = to_raw_response_wrapper(
            knowledge_bases.retrieve,
        )
        self.update = to_raw_response_wrapper(
            knowledge_bases.update,
        )
        self.list = to_raw_response_wrapper(
            knowledge_bases.list,
        )
        self.delete = to_raw_response_wrapper(
            knowledge_bases.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            knowledge_bases.bulk_delete,
        )
        self.search_documents = to_raw_response_wrapper(
            knowledge_bases.search_documents,
        )
        self.retrieve_document = to_raw_response_wrapper(
            knowledge_bases.retrieve_document,
        )


class AsyncKnowledgeBasesResourceWithRawResponse:
    def __init__(self, knowledge_bases: AsyncKnowledgeBasesResource) -> None:
        self._knowledge_bases = knowledge_bases

        self.create = async_to_raw_response_wrapper(
            knowledge_bases.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            knowledge_bases.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            knowledge_bases.update,
        )
        self.list = async_to_raw_response_wrapper(
            knowledge_bases.list,
        )
        self.delete = async_to_raw_response_wrapper(
            knowledge_bases.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            knowledge_bases.bulk_delete,
        )
        self.search_documents = async_to_raw_response_wrapper(
            knowledge_bases.search_documents,
        )
        self.retrieve_document = async_to_raw_response_wrapper(
            knowledge_bases.retrieve_document,
        )


class KnowledgeBasesResourceWithStreamingResponse:
    def __init__(self, knowledge_bases: KnowledgeBasesResource) -> None:
        self._knowledge_bases = knowledge_bases

        self.create = to_streamed_response_wrapper(
            knowledge_bases.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            knowledge_bases.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            knowledge_bases.update,
        )
        self.list = to_streamed_response_wrapper(
            knowledge_bases.list,
        )
        self.delete = to_streamed_response_wrapper(
            knowledge_bases.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            knowledge_bases.bulk_delete,
        )
        self.search_documents = to_streamed_response_wrapper(
            knowledge_bases.search_documents,
        )
        self.retrieve_document = to_streamed_response_wrapper(
            knowledge_bases.retrieve_document,
        )


class AsyncKnowledgeBasesResourceWithStreamingResponse:
    def __init__(self, knowledge_bases: AsyncKnowledgeBasesResource) -> None:
        self._knowledge_bases = knowledge_bases

        self.create = async_to_streamed_response_wrapper(
            knowledge_bases.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            knowledge_bases.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            knowledge_bases.update,
        )
        self.list = async_to_streamed_response_wrapper(
            knowledge_bases.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            knowledge_bases.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            knowledge_bases.bulk_delete,
        )
        self.search_documents = async_to_streamed_response_wrapper(
            knowledge_bases.search_documents,
        )
        self.retrieve_document = async_to_streamed_response_wrapper(
            knowledge_bases.retrieve_document,
        )
