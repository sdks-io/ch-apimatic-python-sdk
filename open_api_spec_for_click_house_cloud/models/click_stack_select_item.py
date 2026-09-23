from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_stack_number_format import ClickStackNumberFormat, ClickStackNumberFormatDict
from .enums.agg_fn3 import AggFn3OrStr
from .enums.level import LevelOrInt
from .enums.metric_type import MetricTypeOrStr
from .enums.period_agg_fn import PeriodAggFnOrStr
from .enums.where_language4 import WhereLanguage4OrStr


class ClickStackSelectItem(SdkBaseModel):
    agg_fn: AggFn3OrStr = Field(alias="aggFn")
    """Aggregation function to apply. "count" does not require a valueExpression; "quantile" requires a level field
    indicating the desired percentile (e.g., 0.95)."""

    value_expression: Optional[str] = Field(default=UNSET, alias="valueExpression")
    """Expression for the column or value to aggregate. Must be omitted when aggFn is "count"; required for all other
    aggFn values."""

    alias: Optional[str] = UNSET
    """Display alias for this select item in chart legends."""

    level: Optional[LevelOrInt] = UNSET
    """Percentile level; only valid when aggFn is "quantile"."""

    where: Optional[str] = UNSET
    """SQL or Lucene filter condition applied before aggregation."""

    where_language: Optional[WhereLanguage4OrStr] = Field(default=UNSET, alias="whereLanguage")
    """Query language for the where clause."""

    metric_name: Optional[str] = Field(default=UNSET, alias="metricName")
    """Name of the metric to aggregate; only applicable when the source is a metrics source."""

    metric_type: Optional[MetricTypeOrStr] = Field(default=UNSET, alias="metricType")
    """Metric type; only applicable when the source is a metrics source."""

    period_agg_fn: Optional[PeriodAggFnOrStr] = Field(default=UNSET, alias="periodAggFn")
    """Optional period aggregation function for Gauge metrics (e.g., compute the delta over the period)."""

    number_format: Optional[ClickStackNumberFormat] = Field(default=UNSET, alias="numberFormat")


class ClickStackSelectItemDict(TypedDict):
    agg_fn: AggFn3OrStr
    value_expression: NotRequired[str]
    alias: NotRequired[str]
    level: NotRequired[LevelOrInt]
    where: NotRequired[str]
    where_language: NotRequired[WhereLanguage4OrStr]
    metric_name: NotRequired[str]
    metric_type: NotRequired[MetricTypeOrStr]
    period_agg_fn: NotRequired[PeriodAggFnOrStr]
    number_format: NotRequired[ClickStackNumberFormatDict]
