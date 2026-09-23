from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .click_stack_filter_settings_column import ClickStackFilterSettingsColumn, ClickStackFilterSettingsColumnDict


class ClickStackSourceFilterSettings(SdkBaseModel):
    database_name: str = Field(alias="databaseName")
    """ClickHouse database name"""

    table_name: str = Field(alias="tableName")
    """ClickHouse table name"""

    columns: list[ClickStackFilterSettingsColumn]
    """Columns to expose as filters (max 10)"""


class ClickStackSourceFilterSettingsDict(TypedDict):
    database_name: str
    table_name: str
    columns: list[ClickStackFilterSettingsColumnDict]
