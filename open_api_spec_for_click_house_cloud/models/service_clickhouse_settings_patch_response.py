from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .service_clickhouse_setting_warning import ServiceClickhouseSettingWarning, ServiceClickhouseSettingWarningDict
from .unions.service_clickhouse_setting_value import ServiceClickhouseSettingValue, ServiceClickhouseSettingValueDict


class ServiceClickhouseSettingsPatchResponse(SdkBaseModel):
    settings: Optional[dict[str, ServiceClickhouseSettingValue]] = UNSET
    """Nonempty object mapping configurable setting names to their values. Use DELETE to reset a setting."""

    warnings: Optional[list[ServiceClickhouseSettingWarning]] = UNSET
    """Warnings for settings that may have disruptive effects."""


class ServiceClickhouseSettingsPatchResponseDict(TypedDict):
    settings: NotRequired[dict[str, ServiceClickhouseSettingValueDict]]
    warnings: NotRequired[list[ServiceClickhouseSettingWarningDict]]
