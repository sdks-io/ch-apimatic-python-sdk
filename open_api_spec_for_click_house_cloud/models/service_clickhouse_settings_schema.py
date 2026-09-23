from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .service_clickhouse_setting_schema_entry import (
    ServiceClickhouseSettingSchemaEntry,
    ServiceClickhouseSettingSchemaEntryDict,
)


class ServiceClickhouseSettingsSchema(SdkBaseModel):
    settings: Optional[list[ServiceClickhouseSettingSchemaEntry]] = UNSET
    """List of all configurable ClickHouse settings with their types, descriptions, and constraints."""


class ServiceClickhouseSettingsSchemaDict(TypedDict):
    settings: NotRequired[list[ServiceClickhouseSettingSchemaEntryDict]]
