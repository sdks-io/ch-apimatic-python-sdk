from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ClickStackAggregatedColumn(SdkBaseModel):
    source_column: OptionalNullable[str] = Field(default=UNSET, alias="sourceColumn")
    """Source column name"""

    agg_fn: str = Field(alias="aggFn")
    """Aggregation function (e.g., count, sum, avg)"""

    mv_column: str = Field(alias="mvColumn")
    """Materialized view column name"""


class ClickStackAggregatedColumnDict(TypedDict):
    source_column: NotRequired[str | None]
    agg_fn: str
    mv_column: str
