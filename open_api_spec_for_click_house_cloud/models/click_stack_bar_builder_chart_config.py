from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_stack_formula import ClickStackFormula, ClickStackFormulaDict
from .click_stack_number_format import ClickStackNumberFormat, ClickStackNumberFormatDict
from .click_stack_select_item import ClickStackSelectItem, ClickStackSelectItemDict


class ClickStackBarBuilderChartConfig(SdkBaseModel):
    display_type: Literal["stacked_bar"] = Field(default="stacked_bar", alias="displayType")
    """Display type discriminator. Must be "stacked_bar" for stacked-bar charts."""

    source_id: str = Field(alias="sourceId")
    """ID of the data source to query."""

    select: list[ClickStackSelectItem]
    """One or more aggregated values to plot. When asRatio is true, exactly two select items are required."""

    group_by: Optional[str] = Field(default=UNSET, alias="groupBy")
    """Field expression to group results by (creates separate bars segments per group value)."""

    as_ratio: Optional[bool] = Field(default=UNSET, alias="asRatio")
    """Plot select[0] / select[1] as a ratio. Requires exactly two select items."""

    align_date_range_to_granularity: Optional[bool] = Field(default=UNSET, alias="alignDateRangeToGranularity")
    """Align the date range boundaries to the query granularity interval."""

    fill_nulls: Optional[bool] = Field(default=UNSET, alias="fillNulls")
    """Fill missing time buckets with zero instead of leaving gaps."""

    number_format: Optional[ClickStackNumberFormat] = Field(default=UNSET, alias="numberFormat")
    series_limit: Optional[int] = Field(default=UNSET, alias="seriesLimit")
    """Maximum number of series rendered (top-N by value). Omit to use the default render cap, set 0 for unlimited, or a
    positive N to keep the top N series."""

    formulas: Optional[list[ClickStackFormula]] = UNSET
    """Derived series computed from the select items via letter-ref arithmetic ("A" = select[0], "B" = select[1], ...).
    Metric, log, and trace sources only. Cannot be combined with asRatio."""

    show_operand_series: Optional[bool] = Field(default=UNSET, alias="showOperandSeries")
    """Only meaningful with formulas. When false, only the formula series are returned; the raw operand series are
    hidden."""


class ClickStackBarBuilderChartConfigDict(TypedDict):
    display_type: Literal["stacked_bar"]
    source_id: str
    select: list[ClickStackSelectItemDict]
    group_by: NotRequired[str]
    as_ratio: NotRequired[bool]
    align_date_range_to_granularity: NotRequired[bool]
    fill_nulls: NotRequired[bool]
    number_format: NotRequired[ClickStackNumberFormatDict]
    series_limit: NotRequired[int]
    formulas: NotRequired[list[ClickStackFormulaDict]]
    show_operand_series: NotRequired[bool]
