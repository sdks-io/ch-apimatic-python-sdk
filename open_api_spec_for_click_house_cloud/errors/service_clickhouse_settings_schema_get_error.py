from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickhouse_settings_schema400_error1 import (
    V1OrganizationsServicesClickhouseSettingsSchema400Error1,
)
from ..models.v1_organizations_services_clickhouse_settings_schema500_error1 import (
    V1OrganizationsServicesClickhouseSettingsSchema500Error1,
)

ServiceClickhouseSettingsSchemaGetErrorBody: TypeAlias = (
    V1OrganizationsServicesClickhouseSettingsSchema400Error1
    | V1OrganizationsServicesClickhouseSettingsSchema500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ServiceClickhouseSettingsSchemaGetError:
    def map(self, response: HttpResponse) -> ServiceClickhouseSettingsSchemaGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickhouseSettingsSchema400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickhouseSettingsSchema500Error1](response)
            case _:
                return RawError(response)


service_clickhouse_settings_schema_get_error_mapper: Final[
    ErrorMapper[ServiceClickhouseSettingsSchemaGetErrorBody]
] = _ServiceClickhouseSettingsSchemaGetError()
