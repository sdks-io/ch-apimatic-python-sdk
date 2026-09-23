from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ClickStackSourceFrom(SdkBaseModel):
    database_name: str = Field(alias="databaseName")
    """ClickHouse database name"""

    table_name: str = Field(alias="tableName")
    """ClickHouse table name"""


class ClickStackSourceFromDict(TypedDict):
    database_name: str
    table_name: str
