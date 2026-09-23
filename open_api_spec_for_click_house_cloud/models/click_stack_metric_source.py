from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .click_stack_metric_source_from import ClickStackMetricSourceFrom, ClickStackMetricSourceFromDict
from .click_stack_metric_tables import ClickStackMetricTables, ClickStackMetricTablesDict
from .click_stack_query_setting import ClickStackQuerySetting, ClickStackQuerySettingDict


class ClickStackMetricSource(SdkBaseModel):
    id: Optional[str] = UNSET
    """Unique source ID. Server-generated; ignored if sent in create/update requests."""

    name: str
    """Display name for the source."""

    section: Optional[str] = UNSET
    """Optional grouping label used to organize sources in the source selector. Sources that share a section value are
    displayed together."""

    disabled: OptionalNullable[bool] = UNSET
    """When true, the source is hidden from source selectors in the UI. Defaults to false."""

    kind: Literal["metric"] = "metric"
    """Source kind discriminator. Must be "metric" for metric sources."""

    connection: str
    """ID of the ClickHouse connection used by this source."""

    from_: ClickStackMetricSourceFrom = Field(alias="from")
    query_settings: Optional[list[ClickStackQuerySetting]] = Field(default=UNSET, alias="querySettings")
    """Optional ClickHouse query settings applied when querying this source."""

    metric_tables: ClickStackMetricTables = Field(alias="metricTables")
    timestamp_value_expression: str = Field(alias="timestampValueExpression")
    """DateTime column or expression that is part of your table's primary key."""

    resource_attributes_expression: str = Field(alias="resourceAttributesExpression")
    """Column containing resource attributes for metrics"""

    log_source_id: OptionalNullable[str] = Field(default=UNSET, alias="logSourceId")
    """HyperDX Source for logs associated with metrics. Optional"""


class ClickStackMetricSourceDict(TypedDict):
    id: NotRequired[str]
    name: str
    section: NotRequired[str]
    disabled: NotRequired[bool | None]
    kind: Literal["metric"]
    connection: str
    from_: ClickStackMetricSourceFromDict
    query_settings: NotRequired[list[ClickStackQuerySettingDict]]
    metric_tables: ClickStackMetricTablesDict
    timestamp_value_expression: str
    resource_attributes_expression: str
    log_source_id: NotRequired[str | None]
