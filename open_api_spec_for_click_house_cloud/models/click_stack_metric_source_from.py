from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ClickStackMetricSourceFrom(SdkBaseModel):
    database_name: str = Field(alias="databaseName")
    """ClickHouse database name"""

    table_name: OptionalNullable[str] = Field(default=UNSET, alias="tableName")
    """ClickHouse table name"""


class ClickStackMetricSourceFromDict(TypedDict):
    database_name: str
    table_name: NotRequired[str | None]
