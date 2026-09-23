from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .service_clickhouse_setting import ServiceClickhouseSetting, ServiceClickhouseSettingDict


class ServiceClickhouseSettingsList(SdkBaseModel):
    settings: Optional[list[ServiceClickhouseSetting]] = UNSET
    """List of ClickHouse settings with their current values."""


class ServiceClickhouseSettingsListDict(TypedDict):
    settings: NotRequired[list[ServiceClickhouseSettingDict]]
