from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_postgres_password400_error1 import V1OrganizationsPostgresPassword400Error1
from ..models.v1_organizations_postgres_password500_error1 import V1OrganizationsPostgresPassword500Error1

PostgresServiceSetPasswordErrorBody: TypeAlias = (
    V1OrganizationsPostgresPassword400Error1 | V1OrganizationsPostgresPassword500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _PostgresServiceSetPasswordError:
    def map(self, response: HttpResponse) -> PostgresServiceSetPasswordErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsPostgresPassword400Error1](response)
            case 500:
                return decode_json[V1OrganizationsPostgresPassword500Error1](response)
            case _:
                return RawError(response)


postgres_service_set_password_error_mapper: Final[
    ErrorMapper[PostgresServiceSetPasswordErrorBody]
] = _PostgresServiceSetPasswordError()
