from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_postgres_restored_service400_error1 import (
    V1OrganizationsPostgresRestoredService400Error1,
)
from ..models.v1_organizations_postgres_restored_service500_error1 import (
    V1OrganizationsPostgresRestoredService500Error1,
)

PostgresInstanceRestoreErrorBody: TypeAlias = (
    V1OrganizationsPostgresRestoredService400Error1 | V1OrganizationsPostgresRestoredService500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _PostgresInstanceRestoreError:
    def map(self, response: HttpResponse) -> PostgresInstanceRestoreErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsPostgresRestoredService400Error1](response)
            case 500:
                return decode_json[V1OrganizationsPostgresRestoredService500Error1](response)
            case _:
                return RawError(response)


postgres_instance_restore_error_mapper: Final[
    ErrorMapper[PostgresInstanceRestoreErrorBody]
] = _PostgresInstanceRestoreError()
