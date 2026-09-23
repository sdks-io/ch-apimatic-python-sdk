from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_stack_heatmap_select_item import ClickStackHeatmapSelectItem, ClickStackHeatmapSelectItemDict
from .click_stack_number_format import ClickStackNumberFormat, ClickStackNumberFormatDict
from .enums.where_language4 import WhereLanguage4OrStr


class ClickStackHeatmapChartConfig(SdkBaseModel):
    display_type: Literal["heatmap"] = Field(default="heatmap", alias="displayType")
    """Display type discriminator. Must be "heatmap" for heatmap tiles."""

    source_id: str = Field(alias="sourceId")
    """ID of the data source to query."""

    select: list[ClickStackHeatmapSelectItem]
    """Exactly one heatmap select item."""

    where: Optional[str] = UNSET
    """Row-level filter (syntax depends on whereLanguage)."""

    where_language: Optional[WhereLanguage4OrStr] = Field(default=UNSET, alias="whereLanguage")
    """Query language for the where clause."""

    number_format: Optional[ClickStackNumberFormat] = Field(default=UNSET, alias="numberFormat")


class ClickStackHeatmapChartConfigDict(TypedDict):
    display_type: Literal["heatmap"]
    source_id: str
    select: list[ClickStackHeatmapSelectItemDict]
    where: NotRequired[str]
    where_language: NotRequired[WhereLanguage4OrStr]
    number_format: NotRequired[ClickStackNumberFormatDict]
