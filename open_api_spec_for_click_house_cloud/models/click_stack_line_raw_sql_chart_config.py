from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_stack_number_format import ClickStackNumberFormat, ClickStackNumberFormatDict


class ClickStackLineRawSqlChartConfig(SdkBaseModel):
    config_type: Literal["sql"] = Field(default="sql", alias="configType")
    """Must be "sql" to use the Raw SQL chart config variant."""

    connection_id: str = Field(alias="connectionId")
    """ID of the ClickHouse connection to execute the query against."""

    sql_template: str = Field(alias="sqlTemplate")
    """SQL query template to execute. Supports HyperDX template variables."""

    source_id: Optional[str] = Field(default=UNSET, alias="sourceId")
    """Optional ID of the data source associated with this Raw SQL chart. Used for applying dashboard filters."""

    number_format: Optional[ClickStackNumberFormat] = Field(default=UNSET, alias="numberFormat")
    display_type: Literal["line"] = Field(default="line", alias="displayType")
    """Display as a line time-series chart."""

    compare_to_previous_period: Optional[bool] = Field(default=UNSET, alias="compareToPreviousPeriod")
    """Overlay the equivalent previous time period for comparison."""

    fill_nulls: Optional[bool] = Field(default=UNSET, alias="fillNulls")
    """Fill missing time buckets with zero instead of leaving gaps."""

    align_date_range_to_granularity: Optional[bool] = Field(default=UNSET, alias="alignDateRangeToGranularity")
    """Expand date range boundaries to the query granularity interval."""

    fit_y_axis_to_data: Optional[bool] = Field(default=UNSET, alias="fitYAxisToData")
    """Set the y-axis lower bound to the minimum of the displayed data instead of zero, making small fluctuations
    between series easier to see."""


class ClickStackLineRawSqlChartConfigDict(TypedDict):
    config_type: Literal["sql"]
    connection_id: str
    sql_template: str
    source_id: NotRequired[str]
    number_format: NotRequired[ClickStackNumberFormatDict]
    display_type: Literal["line"]
    compare_to_previous_period: NotRequired[bool]
    fill_nulls: NotRequired[bool]
    align_date_range_to_granularity: NotRequired[bool]
    fit_y_axis_to_data: NotRequired[bool]
