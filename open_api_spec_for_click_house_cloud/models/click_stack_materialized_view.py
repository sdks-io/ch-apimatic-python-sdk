from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .click_stack_aggregated_column import ClickStackAggregatedColumn, ClickStackAggregatedColumnDict


class ClickStackMaterializedView(SdkBaseModel):
    database_name: str = Field(alias="databaseName")
    """Database name for the materialized view"""

    table_name: str = Field(alias="tableName")
    """Table name for the materialized view"""

    dimension_columns: str = Field(alias="dimensionColumns")
    """Columns which are not pre-aggregated in the materialized view and can be used for filtering and grouping."""

    min_granularity: str = Field(alias="minGranularity")
    """The granularity of the timestamp column: a positive integer followed by a unit (s, m, h, d). Common values: 1s,
    15s, 30s, 1m, 5m, 15m, 30m, 1h, 2h, 6h, 12h, 1d, 2d, 7d, 30d."""

    min_date: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="minDate")
    """(Optional) The earliest date and time for which the materialized view contains data. If not provided, then
    HyperDX will assume that the materialized view contains data for all dates for which the source table contains
    data."""

    timestamp_column: str = Field(alias="timestampColumn")
    """Timestamp column name"""

    aggregated_columns: list[ClickStackAggregatedColumn] = Field(alias="aggregatedColumns")
    """Columns which are pre-aggregated by the materialized view"""


class ClickStackMaterializedViewDict(TypedDict):
    database_name: str
    table_name: str
    dimension_columns: str
    min_granularity: str
    min_date: NotRequired[RFC3339DateTime | None]
    timestamp_column: str
    aggregated_columns: list[ClickStackAggregatedColumnDict]
