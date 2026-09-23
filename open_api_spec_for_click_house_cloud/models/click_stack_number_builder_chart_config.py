from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_stack_background_chart import ClickStackBackgroundChart, ClickStackBackgroundChartDict
from .click_stack_formula import ClickStackFormula, ClickStackFormulaDict
from .click_stack_number_format import ClickStackNumberFormat, ClickStackNumberFormatDict
from .click_stack_select_item import ClickStackSelectItem, ClickStackSelectItemDict
from .enums.color4 import Color4OrStr
from .unions.click_stack_number_tile_color_condition import (
    ClickStackNumberTileColorCondition,
    ClickStackNumberTileColorConditionDict,
)


class ClickStackNumberBuilderChartConfig(SdkBaseModel):
    display_type: Literal["number"] = Field(default="number", alias="displayType")
    """Display type discriminator. Must be "number" for single big-number charts."""

    source_id: str = Field(alias="sourceId")
    """ID of the data source to query."""

    select: list[ClickStackSelectItem]
    """Exactly one aggregated value to display as a single number — unless "formulas" is set, in which case the select
    items are the formula's operands and the (single) formula value is displayed instead."""

    formulas: Optional[list[ClickStackFormula]] = UNSET
    """A single derived value computed from the select items via letter-ref arithmetic ("A" = select[0], "B" =
    select[1], ...). Metric, log, and trace sources only. Number tiles display the formula value and always hide the
    operand series."""

    number_format: Optional[ClickStackNumberFormat] = Field(default=UNSET, alias="numberFormat")
    color: Optional[Color4OrStr] = UNSET
    """Optional static color applied to the displayed number."""

    color_rules: Optional[list[ClickStackNumberTileColorCondition]] = Field(default=UNSET, alias="colorRules")
    """Ordered conditional color rules evaluated against the displayed value (last match wins). Falls back to color,
    then the default text color when no rule matches."""

    background_chart: Optional[ClickStackBackgroundChart] = Field(default=UNSET, alias="backgroundChart")


class ClickStackNumberBuilderChartConfigDict(TypedDict):
    display_type: Literal["number"]
    source_id: str
    select: list[ClickStackSelectItemDict]
    formulas: NotRequired[list[ClickStackFormulaDict]]
    number_format: NotRequired[ClickStackNumberFormatDict]
    color: NotRequired[Color4OrStr]
    color_rules: NotRequired[list[ClickStackNumberTileColorConditionDict]]
    background_chart: NotRequired[ClickStackBackgroundChartDict]
