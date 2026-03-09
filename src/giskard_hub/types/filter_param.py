from typing import Any, List, Union, Literal, Optional, TypeAlias
from typing_extensions import TypedDict

__all__ = [
    "ListFilterValueParam",
    "DateRangeFilterValueParam",
    "FilterValueParam",
]


class ListFilterValueParam(TypedDict, total=False):
    selected_options: List[Any]
    """Values to match against."""

    is_empty: bool
    """Match rows where the column is empty."""

    match_mode: Literal["include", "exclude"]
    """Whether to include or exclude rows matching `selected_options`. Defaults to ``"include"``."""

    match_logic: Literal["any", "all"]
    """Whether any or all of `selected_options` must match. Defaults to ``"any"``."""


class DateRangeFilterValueParam(TypedDict, total=False):
    from_: Optional[str]
    """Start of the date range (ISO 8601). Serialised as ``"from"`` on the wire."""

    to_: Optional[str]
    """End of the date range (ISO 8601). Serialised as ``"to"`` on the wire."""


# A filter might be either a ListFilterValueParam or a DateRangeFilterValueParam
FilterValueParam: TypeAlias = Union[ListFilterValueParam, DateRangeFilterValueParam]
