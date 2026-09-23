from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_stack_number_format import ClickStackNumberFormat, ClickStackNumberFormatDict
from .enums.agg_fn import AggFnOrStr
from .enums.display_type import DisplayTypeOrStr
from .enums.metric_data_type import MetricDataTypeOrStr
from .enums.where_language import WhereLanguageOrStr


class ClickStackTimeChartSeries(SdkBaseModel):
    type_: Literal["time"] = Field(default="time", alias="type")
    """Series type discriminator. Must be "time" for time-series charts."""

    source_id: str = Field(alias="sourceId")
    """ID of the data source to query"""

    agg_fn: AggFnOrStr = Field(alias="aggFn")
    """Aggregation function to apply to the field or metric value"""

    level: Optional[float] = UNSET
    """Percentile level for quantile aggregations (e.g., 0.95 for p95)"""

    field: Optional[str] = UNSET
    """Column or expression to aggregate (required for most aggregation functions except count)"""

    alias: Optional[str] = UNSET
    """Display name for the series in the chart"""

    where: str
    """Filter query for the data (syntax depends on whereLanguage)"""

    where_language: WhereLanguageOrStr = Field(alias="whereLanguage")
    """Query language for the where clause"""

    group_by: list[str] = Field(alias="groupBy")
    """Fields to group results by (creates separate series for each group)"""

    number_format: Optional[ClickStackNumberFormat] = Field(default=UNSET, alias="numberFormat")
    metric_data_type: Optional[MetricDataTypeOrStr] = Field(default=UNSET, alias="metricDataType")
    """Metric data type, only for metrics data sources."""

    metric_name: Optional[str] = Field(default=UNSET, alias="metricName")
    """Metric name for metrics data sources"""

    display_type: Optional[DisplayTypeOrStr] = Field(default=UNSET, alias="displayType")
    """Visual representation type for the time series"""


class ClickStackTimeChartSeriesDict(TypedDict):
    type_: Literal["time"]
    source_id: str
    agg_fn: AggFnOrStr
    level: NotRequired[float]
    field: NotRequired[str]
    alias: NotRequired[str]
    where: str
    where_language: WhereLanguageOrStr
    group_by: list[str]
    number_format: NotRequired[ClickStackNumberFormatDict]
    metric_data_type: NotRequired[MetricDataTypeOrStr]
    metric_name: NotRequired[str]
    display_type: NotRequired[DisplayTypeOrStr]
