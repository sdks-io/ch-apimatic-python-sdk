from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.service_clickhouse_setting_value import ServiceClickhouseSettingValue, ServiceClickhouseSettingValueDict


class ServiceClickhouseSetting(SdkBaseModel):
    name: Optional[str] = UNSET
    """Name of the setting."""

    value: Optional[ServiceClickhouseSettingValue] = UNSET
    """Setting value in its native JSON type. Use the settings schema endpoint for per-setting constraints."""


class ServiceClickhouseSettingDict(TypedDict):
    name: NotRequired[str]
    value: NotRequired[ServiceClickhouseSettingValueDict]
