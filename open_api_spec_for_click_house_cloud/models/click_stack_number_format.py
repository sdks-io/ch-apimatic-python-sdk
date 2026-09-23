from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.numeric_unit import NumericUnitOrStr
from .enums.output import OutputOrStr


class ClickStackNumberFormat(SdkBaseModel):
    output: Optional[OutputOrStr] = UNSET
    """Output format applied to the number."""

    mantissa: Optional[int] = UNSET
    """Number of decimal places."""

    thousand_separated: Optional[bool] = Field(default=UNSET, alias="thousandSeparated")
    """Whether to use thousand separators."""

    average: Optional[bool] = UNSET
    """Whether to show as average."""

    decimal_bytes: Optional[bool] = Field(default=UNSET, alias="decimalBytes")
    """Use decimal bytes (1000) vs binary bytes (1024)."""

    factor: Optional[float] = UNSET
    """Multiplication factor."""

    currency_symbol: Optional[str] = Field(default=UNSET, alias="currencySymbol")
    """Currency symbol for currency format."""

    numeric_unit: Optional[NumericUnitOrStr] = Field(default=UNSET, alias="numericUnit")
    """Numeric unit for data, data rate, or throughput formats."""

    unit: Optional[str] = UNSET
    """Custom unit label."""


class ClickStackNumberFormatDict(TypedDict):
    output: NotRequired[OutputOrStr]
    mantissa: NotRequired[int]
    thousand_separated: NotRequired[bool]
    average: NotRequired[bool]
    decimal_bytes: NotRequired[bool]
    factor: NotRequired[float]
    currency_symbol: NotRequired[str]
    numeric_unit: NotRequired[NumericUnitOrStr]
    unit: NotRequired[str]
