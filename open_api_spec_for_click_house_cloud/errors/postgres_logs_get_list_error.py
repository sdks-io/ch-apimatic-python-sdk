from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_postgres_logs400_error1 import V1OrganizationsPostgresLogs400Error1
from ..models.v1_organizations_postgres_logs500_error1 import V1OrganizationsPostgresLogs500Error1

PostgresLogsGetListErrorBody: TypeAlias = (
    V1OrganizationsPostgresLogs400Error1 | V1OrganizationsPostgresLogs500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _PostgresLogsGetListError:
    def map(self, response: HttpResponse) -> PostgresLogsGetListErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsPostgresLogs400Error1](response)
            case 500:
                return decode_json[V1OrganizationsPostgresLogs500Error1](response)
            case _:
                return RawError(response)


postgres_logs_get_list_error_mapper: Final[ErrorMapper[PostgresLogsGetListErrorBody]] = _PostgresLogsGetListError()
