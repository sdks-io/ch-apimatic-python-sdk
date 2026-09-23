from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_postgres400_error1 import V1OrganizationsPostgres400Error1
from ..models.v1_organizations_postgres500_error1 import V1OrganizationsPostgres500Error1

PostgresServiceCreateErrorBody: TypeAlias = (
    V1OrganizationsPostgres400Error1 | V1OrganizationsPostgres500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _PostgresServiceCreateError:
    def map(self, response: HttpResponse) -> PostgresServiceCreateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsPostgres400Error1](response)
            case 500:
                return decode_json[V1OrganizationsPostgres500Error1](response)
            case _:
                return RawError(response)


postgres_service_create_error_mapper: Final[ErrorMapper[PostgresServiceCreateErrorBody]] = _PostgresServiceCreateError()
