from __future__ import annotations

from typing import Any, Dict, List, TypeVar, Callable

from ..types.common import APIResponse, APIResponseWithIncluded

T = TypeVar("T")
URelated = TypeVar("URelated")


def _apply_included_to_item(item: T, included_for_item: Dict[str, Any]) -> None:
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
            setattr(item, field_name, related.data)
        elif isinstance(related, list):
            # Handle lists of APIResponse objects, falling back to the raw
            # element if it isn't an APIResponse instance.
            values: List[Any] = []
            for element in related:
                if isinstance(element, APIResponse):
                    values.append(element.data)
                else:
                    values.append(element)
            setattr(item, field_name, values)
        else:
            setattr(item, field_name, related)


def embed_included_single(
    response: APIResponseWithIncluded[T, APIResponse[URelated]],
    *,
    id_getter: Callable[[T], str],
) -> APIResponseWithIncluded[T, APIResponse[URelated]]:
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
    response: APIResponseWithIncluded[List[T], APIResponse[URelated]],
    *,
    id_getter: Callable[[T], str],
) -> APIResponseWithIncluded[List[T], APIResponse[URelated]]:
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
