from __future__ import annotations

from typing import Any, Dict, List, Mapping, Optional, cast

import httpx

from ..types import (
    knowledge_base_list_params,
    knowledge_base_create_params,
    knowledge_base_update_params,
    knowledge_base_bulk_delete_params,
    knowledge_base_search_documents_params,
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
from ..types.common import APIResponse
from ..types.knowledge_base import KnowledgeBase
from ..types.api_response_none import APIResponseNone
from ..types.task_progress_param import TaskProgressParam
from ..types.knowledge_base_document_detail_api_resource import KnowledgeBaseDocumentDetailAPIResource
from ..types.paginated_api_response_knowledge_base_document_row_api_resource import (
    PaginatedAPIResponseKnowledgeBaseDocumentRowAPIResource,
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
        file: FileTypes,
        description: Optional[str] | Omit = omit,
        document_column: str | Omit = omit,
        topic_column: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[KnowledgeBase]:
        """
        Create Knowledge Base

        Args:
          name: Name of the knowledge base

          project_id: Project ID to create the knowledge base in

          file: File to upload for the knowledge base

          description: Description of the knowledge base

          document_column: Column name for the document column

          topic_column: Column name for the topic column

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        return self._post(
            "/v2/knowledge-bases",
            body=maybe_transform(body, knowledge_base_create_params.KnowledgeBaseCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[KnowledgeBase],
        )

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
    ) -> APIResponse[KnowledgeBase]:
        """
        Retrieve Knowledge Base

        Args:
          knowledge_base_id: ID of the knowledge base to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return self._get(
            f"/v2/knowledge-bases/{knowledge_base_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[KnowledgeBase],
        )

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
    ) -> APIResponse[KnowledgeBase]:
        """
        Update Knowledge Base

        Args:
          knowledge_base_id: ID of the knowledge base to update

          description: Description of the knowledge base

          name: Name of the knowledge base

          project_id: Project ID to update the knowledge base in

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return self._patch(
            f"/v2/knowledge-bases/{knowledge_base_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "project_id": project_id,
                    "status": status,
                },
                knowledge_base_update_params.KnowledgeBaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[KnowledgeBase],
        )

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
    ) -> APIResponse[List[KnowledgeBase]]:
        """
        List Knowledge Bases

        Args:
          project_id: Project ID to list knowledge bases for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/knowledge-bases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, knowledge_base_list_params.KnowledgeBaseListParams),
            ),
            cast_to=APIResponse[List[KnowledgeBase]],
        )

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
    ) -> APIResponseNone:
        """
        Delete Knowledge Base

        Args:
          knowledge_base_id: ID of the knowledge base to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return self._delete(
            f"/v2/knowledge-bases/{knowledge_base_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseNone,
        )

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
    ) -> APIResponseNone:
        """
        Bulk Delete Knowledge Bases

        Args:
          knowledge_base_ids: IDs of the knowledge bases to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v2/knowledge-bases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"knowledge_base_ids": knowledge_base_ids},
                    knowledge_base_bulk_delete_params.KnowledgeBaseBulkDeleteParams,
                ),
            ),
            cast_to=APIResponseNone,
        )

    def search_documents(
        self,
        knowledge_base_id: str,
        *,
        search: Optional[str] | Omit = omit,
        order_by: SequenceNotStr[Dict[str, Any]] | Omit = omit,
        filters: Dict[str, Dict[str, Any]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedAPIResponseKnowledgeBaseDocumentRowAPIResource:
        """
        Search Knowledge Base Documents By Filters

        Args:
          knowledge_base_id: ID of the knowledge base

          search: Search query for knowledge base documents

          order_by: Order by criteria for knowledge base documents

          filters: Search filters

          limit: Maximum number of results to return

          offset: Number of results to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return self._post(
            f"/v2/knowledge-bases/{knowledge_base_id}/documents/search",
            body=maybe_transform(
                {"filters": filters, "order_by": order_by, "search": search},
                knowledge_base_search_documents_params.KnowledgeBaseSearchDocumentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit, "offset": offset},
                    knowledge_base_search_documents_params.KnowledgeBaseSearchDocumentsParams,
                ),
            ),
            cast_to=PaginatedAPIResponseKnowledgeBaseDocumentRowAPIResource,
        )

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
    ) -> APIResponse[KnowledgeBaseDocumentDetailAPIResource]:
        """
        Retrieve Knowledge Base Document

        Args:
          knowledge_base_id: ID of the knowledge base

          document_id: ID of the document

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._get(
            f"/v2/knowledge-bases/{knowledge_base_id}/documents/{document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[KnowledgeBaseDocumentDetailAPIResource],
        )


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
        file: FileTypes,
        description: Optional[str] | Omit = omit,
        document_column: str | Omit = omit,
        topic_column: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponse[KnowledgeBase]:
        """
        Create Knowledge Base

        Args:
          name: Name of the knowledge base

          project_id: Project ID to create the knowledge base in

          file: File to upload for the knowledge base

          description: Description of the knowledge base

          document_column: Column name for the document column

          topic_column: Column name for the topic column

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        return await self._post(
            "/v2/knowledge-bases",
            body=await async_maybe_transform(body, knowledge_base_create_params.KnowledgeBaseCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[KnowledgeBase],
        )

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
    ) -> APIResponse[KnowledgeBase]:
        """
        Retrieve Knowledge Base

        Args:
          knowledge_base_id: ID of the knowledge base to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return await self._get(
            f"/v2/knowledge-bases/{knowledge_base_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[KnowledgeBase],
        )

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
    ) -> APIResponse[KnowledgeBase]:
        """
        Update Knowledge Base

        Args:
          knowledge_base_id: ID of the knowledge base to update

          description: Description of the knowledge base

          name: Name of the knowledge base

          project_id: Project ID to update the knowledge base in

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return await self._patch(
            f"/v2/knowledge-bases/{knowledge_base_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "project_id": project_id,
                    "status": status,
                },
                knowledge_base_update_params.KnowledgeBaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[KnowledgeBase],
        )

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
    ) -> APIResponse[List[KnowledgeBase]]:
        """
        List Knowledge Bases

        Args:
          project_id: Project ID to list knowledge bases for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/knowledge-bases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id}, knowledge_base_list_params.KnowledgeBaseListParams
                ),
            ),
            cast_to=APIResponse[List[KnowledgeBase]],
        )

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
    ) -> APIResponseNone:
        """
        Delete Knowledge Base

        Args:
          knowledge_base_id: ID of the knowledge base to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return await self._delete(
            f"/v2/knowledge-bases/{knowledge_base_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseNone,
        )

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
    ) -> APIResponseNone:
        """
        Bulk Delete Knowledge Bases

        Args:
          knowledge_base_ids: IDs of the knowledge bases to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v2/knowledge-bases",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"knowledge_base_ids": knowledge_base_ids},
                    knowledge_base_bulk_delete_params.KnowledgeBaseBulkDeleteParams,
                ),
            ),
            cast_to=APIResponseNone,
        )

    async def search_documents(
        self,
        knowledge_base_id: str,
        *,
        search: Optional[str] | Omit = omit,
        order_by: SequenceNotStr[Dict[str, Any]] | Omit = omit,
        filters: Dict[str, Dict[str, Any]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedAPIResponseKnowledgeBaseDocumentRowAPIResource:
        """
        Search Knowledge Base Documents By Filters

        Args:
          knowledge_base_id: ID of the knowledge base

          search: Search query for knowledge base documents

          order_by: Order by criteria for knowledge base documents

          filters: Search filters

          limit: Maximum number of results to return

          offset: Number of results to skip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return await self._post(
            f"/v2/knowledge-bases/{knowledge_base_id}/documents/search",
            body=await async_maybe_transform(
                {"filters": filters, "order_by": order_by, "search": search},
                knowledge_base_search_documents_params.KnowledgeBaseSearchDocumentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "offset": offset},
                    knowledge_base_search_documents_params.KnowledgeBaseSearchDocumentsParams,
                ),
            ),
            cast_to=PaginatedAPIResponseKnowledgeBaseDocumentRowAPIResource,
        )

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
    ) -> APIResponse[KnowledgeBaseDocumentDetailAPIResource]:
        """
        Retrieve Knowledge Base Document

        Args:
          knowledge_base_id: ID of the knowledge base

          document_id: ID of the document

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._get(
            f"/v2/knowledge-bases/{knowledge_base_id}/documents/{document_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponse[KnowledgeBaseDocumentDetailAPIResource],
        )


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
