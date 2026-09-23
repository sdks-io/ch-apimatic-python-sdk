from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.service_clickhouse_setting_value import ServiceClickhouseSettingValue, ServiceClickhouseSettingValueDict


class ServiceClickhouseSettingsPatchRequest(SdkBaseModel):
    settings: dict[str, ServiceClickhouseSettingValue]
    """Nonempty object mapping configurable setting names to their values. Use DELETE to reset a setting."""


class ServiceClickhouseSettingsPatchRequestDict(TypedDict):
    settings: dict[str, ServiceClickhouseSettingValueDict]
