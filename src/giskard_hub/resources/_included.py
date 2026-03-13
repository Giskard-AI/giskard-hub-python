from __future__ import annotations

from typing import Any, Dict, List, TypeVar, Callable, cast

from ..types.common import APIResponse, APIPaginatedResponse, APIResponseWithIncluded

T = TypeVar("T")


def _apply_included_to_item(item: object, included_for_item: Dict[str, Any]) -> None:
    """
    Replace reference fields on `item` with fully included resources.

    For each entry under `included_for_item`, if the key matches an attribute on
    `item`, that attribute is replaced with the underlying data:

    - If the value is an `APIResponse`, we use its `.data`
    - If it's a list of `APIResponse` objects, we map to a list of their `.data`
    - Otherwise, we assign the value as-is
    """

    for field_name, related in included_for_item.items():
        if not hasattr(item, field_name):
            continue

        if isinstance(related, APIResponse):
            typed_related = cast(APIResponse[Any], related)
            setattr(item, field_name, typed_related.data)
        elif isinstance(related, list):
            # Handle lists of APIResponse objects, falling back to the raw
            # element if it isn't an APIResponse instance.
            values: List[Any] = []
            related_list = cast(List[object], related)
            for element in related_list:
                if isinstance(element, APIResponse):
                    typed_element = cast(APIResponse[Any], element)
                    values.append(typed_element.data)
                else:
                    values.append(element)
            setattr(item, field_name, values)
        else:
            setattr(item, field_name, related)


def embed_included_single(
    response: APIResponseWithIncluded[T, Any],
    *,
    id_getter: Callable[[T], str],
) -> APIResponseWithIncluded[T, Any]:
    """
    Embed included resources into a single primary object.

    This mutates and returns the same `response` instance.
    """

    if not response.included:
        return response

    item_id = id_getter(response.data)
    included_for_item = response.included.get(item_id)
    if not included_for_item:
        return response

    _apply_included_to_item(response.data, included_for_item)
    return response


def embed_included_list(
    response: APIResponseWithIncluded[List[T], Any],
    *,
    id_getter: Callable[[T], str],
) -> APIResponseWithIncluded[List[T], Any]:
    """
    Embed included resources into each primary object in a list.

    This mutates and returns the same `response` instance.
    """

    if not response.included:
        return response

    for item in response.data:
        item_id = id_getter(item)
        included_for_item = response.included.get(item_id)
        if not included_for_item:
            continue

        _apply_included_to_item(item, included_for_item)

    return response


def embed_included_paginated(
    response: APIPaginatedResponse[T, Any],
    *,
    id_getter: Callable[[T], str],
) -> APIPaginatedResponse[T, Any]:
    """
    Embed included resources into each primary object in a paginated response.

    This mutates and returns the same `response` instance.
    """

    if not response.included:
        return response

    for item in response.data:
        item_id = id_getter(item)
        included_for_item = response.included.get(item_id)
        if not included_for_item:
            continue

        _apply_included_to_item(item, included_for_item)

    return response
