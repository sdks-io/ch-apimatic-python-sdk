from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickhouse_settings400_error1 import (
    V1OrganizationsServicesClickhouseSettings400Error1,
)
from ..models.v1_organizations_services_clickhouse_settings500_error1 import (
    V1OrganizationsServicesClickhouseSettings500Error1,
)

ServiceClickhouseSettingsListGetErrorBody: TypeAlias = (
    V1OrganizationsServicesClickhouseSettings400Error1 | V1OrganizationsServicesClickhouseSettings500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _ServiceClickhouseSettingsListGetError:
    def map(self, response: HttpResponse) -> ServiceClickhouseSettingsListGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickhouseSettings400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickhouseSettings500Error1](response)
            case _:
                return RawError(response)


service_clickhouse_settings_list_get_error_mapper: Final[
    ErrorMapper[ServiceClickhouseSettingsListGetErrorBody]
] = _ServiceClickhouseSettingsListGetError()
