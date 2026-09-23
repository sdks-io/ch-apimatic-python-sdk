from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_stack_number_format import ClickStackNumberFormat, ClickStackNumberFormatDict
from .click_stack_select_item import ClickStackSelectItem, ClickStackSelectItemDict


class ClickStackPieBuilderChartConfig(SdkBaseModel):
    display_type: Literal["pie"] = Field(default="pie", alias="displayType")
    """Display type discriminator. Must be "pie" for pie charts."""

    source_id: str = Field(alias="sourceId")
    """ID of the data source to query."""

    select: list[ClickStackSelectItem]
    """Exactly one aggregated value used to size each pie slice."""

    group_by: Optional[str] = Field(default=UNSET, alias="groupBy")
    """Field expression to group results by (one slice per group value)."""

    order_by: Optional[str] = Field(default=UNSET, alias="orderBy")
    """Optional custom SQL ORDER BY expression (raw SQL). Overrides the default value-descending ordering and, when
    combined with "limit", controls which slices are kept."""

    number_format: Optional[ClickStackNumberFormat] = Field(default=UNSET, alias="numberFormat")
    limit: Optional[int] = UNSET
    """Maximum number of slices (SQL LIMIT). Without a custom "orderBy" the query keeps the groups with the largest
    aggregated values; with an "orderBy" it keeps the first slices in that order. Omit or set 0 to fetch all groups."""


class ClickStackPieBuilderChartConfigDict(TypedDict):
    display_type: Literal["pie"]
    source_id: str
    select: list[ClickStackSelectItemDict]
    group_by: NotRequired[str]
    order_by: NotRequired[str]
    number_format: NotRequired[ClickStackNumberFormatDict]
    limit: NotRequired[int]
