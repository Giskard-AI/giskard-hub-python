from __future__ import annotations

from typing import Any, Dict, List, TypeVar, Callable, Iterable, cast

from ..types.common import APIResponse, APIPaginatedResponse, APIResponseWithIncluded

T = TypeVar("T")


def _unwrap(value: Any) -> Any:
    """Return ``value.data`` if it's an APIResponse, otherwise ``value`` as-is."""
    if isinstance(value, APIResponse):
        return cast(APIResponse[Any], value).data
    return value


def _apply_included_to_item(item: object, included_for_item: Dict[str, Any]) -> None:
    """Replace reference fields on *item* with fully-resolved included resources."""
    for field_name, related in included_for_item.items():
        if not hasattr(item, field_name):
            continue

        if isinstance(related, list):
            resolved: Any = [_unwrap(el) for el in cast(List[Any], related)]
        else:
            resolved = _unwrap(related)
        setattr(item, field_name, resolved)


def _embed_into_items(
    items: Iterable[T],
    included: Dict[str, Dict[str, Any]],
    id_getter: Callable[[T], str],
) -> None:
    """Shared loop: embed included resources into each item in *items*."""
    for item in items:
        included_for_item = included.get(id_getter(item))
        if included_for_item:
            _apply_included_to_item(item, included_for_item)


def embed_included_single(
    response: APIResponseWithIncluded[T, Any],
    *,
    id_getter: Callable[[T], str],
) -> APIResponseWithIncluded[T, Any]:
    """Embed included resources into a single primary object (mutates *response*)."""
    if response.included:
        included_for_item = response.included.get(id_getter(response.data))
        if included_for_item:
            _apply_included_to_item(response.data, included_for_item)
    return response


def embed_included_list(
    response: APIResponseWithIncluded[List[T], Any],
    *,
    id_getter: Callable[[T], str],
) -> APIResponseWithIncluded[List[T], Any]:
    """Embed included resources into each primary object in a list (mutates *response*)."""
    if response.included:
        _embed_into_items(response.data, response.included, id_getter)
    return response


def embed_included_paginated(
    response: APIPaginatedResponse[T, Any],
    *,
    id_getter: Callable[[T], str],
) -> APIPaginatedResponse[T, Any]:
    """Embed included resources into each primary object in a paginated response (mutates *response*)."""
    if response.included:
        _embed_into_items(response.data, response.included, id_getter)
    return response
