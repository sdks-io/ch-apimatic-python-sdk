from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_stack_formula import ClickStackFormula, ClickStackFormulaDict
from .click_stack_number_format import ClickStackNumberFormat, ClickStackNumberFormatDict
from .click_stack_select_item import ClickStackSelectItem, ClickStackSelectItemDict
from .unions.click_stack_on_click import ClickStackOnClick, ClickStackOnClickDict


class ClickStackTableBuilderChartConfig(SdkBaseModel):
    display_type: Literal["table"] = Field(default="table", alias="displayType")
    """Display type discriminator. Must be "table" for table charts."""

    source_id: str = Field(alias="sourceId")
    """ID of the data source to query."""

    select: list[ClickStackSelectItem]
    """One or more aggregated values to display as table columns. When asRatio is true, exactly two select items are
    required."""

    group_by: Optional[str] = Field(default=UNSET, alias="groupBy")
    """Field expression to group results by (one row per group value)."""

    having: Optional[str] = UNSET
    """Post-aggregation SQL HAVING condition."""

    order_by: Optional[str] = Field(default=UNSET, alias="orderBy")
    """SQL ORDER BY expression for sorting table rows."""

    as_ratio: Optional[bool] = Field(default=UNSET, alias="asRatio")
    """Display select[0] / select[1] as a ratio. Requires exactly two select items."""

    number_format: Optional[ClickStackNumberFormat] = Field(default=UNSET, alias="numberFormat")
    group_by_columns_on_left: Optional[bool] = Field(default=UNSET, alias="groupByColumnsOnLeft")
    """When true, render Group By columns to the left of series columns in the table. Defaults to false (Group By
    columns on the right)."""

    on_click: Optional[ClickStackOnClick] = Field(default=UNSET, alias="onClick")
    formulas: Optional[list[ClickStackFormula]] = UNSET
    """Derived columns computed from the select items via letter-ref arithmetic ("A" = select[0], "B" = select[1], ...).
    Metric, log, and trace sources only. Cannot be combined with asRatio."""

    show_operand_series: Optional[bool] = Field(default=UNSET, alias="showOperandSeries")
    """Only meaningful with formulas. When false, only the formula columns are returned; the raw operand columns are
    hidden."""


class ClickStackTableBuilderChartConfigDict(TypedDict):
    display_type: Literal["table"]
    source_id: str
    select: list[ClickStackSelectItemDict]
    group_by: NotRequired[str]
    having: NotRequired[str]
    order_by: NotRequired[str]
    as_ratio: NotRequired[bool]
    number_format: NotRequired[ClickStackNumberFormatDict]
    group_by_columns_on_left: NotRequired[bool]
    on_click: NotRequired[ClickStackOnClickDict]
    formulas: NotRequired[list[ClickStackFormulaDict]]
    show_operand_series: NotRequired[bool]
