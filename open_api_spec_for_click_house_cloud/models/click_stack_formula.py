from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_stack_number_format import ClickStackNumberFormat, ClickStackNumberFormatDict


class ClickStackFormula(SdkBaseModel):
    expression: str
    """Arithmetic expression over the select items by position, e.g. "A / (A + B) * 100" for a success-rate
    percentage."""

    alias: Optional[str] = UNSET
    """Display label for the formula series in chart legends and column headers. Falls back to the raw expression text
    when unset."""

    number_format: Optional[ClickStackNumberFormat] = Field(default=UNSET, alias="numberFormat")


class ClickStackFormulaDict(TypedDict):
    expression: str
    alias: NotRequired[str]
    number_format: NotRequired[ClickStackNumberFormatDict]
