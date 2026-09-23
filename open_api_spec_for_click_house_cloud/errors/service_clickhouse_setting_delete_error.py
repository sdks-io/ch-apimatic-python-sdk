from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickhouse_settings_setting_name400_error1 import (
    V1OrganizationsServicesClickhouseSettingsSettingName400Error1,
)
from ..models.v1_organizations_services_clickhouse_settings_setting_name500_error1 import (
    V1OrganizationsServicesClickhouseSettingsSettingName500Error1,
)

ServiceClickhouseSettingDeleteErrorBody: TypeAlias = (
    V1OrganizationsServicesClickhouseSettingsSettingName400Error1
    | V1OrganizationsServicesClickhouseSettingsSettingName500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ServiceClickhouseSettingDeleteError:
    def map(self, response: HttpResponse) -> ServiceClickhouseSettingDeleteErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickhouseSettingsSettingName400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickhouseSettingsSettingName500Error1](response)
            case _:
                return RawError(response)


service_clickhouse_setting_delete_error_mapper: Final[
    ErrorMapper[ServiceClickhouseSettingDeleteErrorBody]
] = _ServiceClickhouseSettingDeleteError()
