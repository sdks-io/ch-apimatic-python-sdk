from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_postgres_config400_error1 import V1OrganizationsPostgresConfig400Error1
from ..models.v1_organizations_postgres_config500_error1 import V1OrganizationsPostgresConfig500Error1

PostgresInstanceConfigPostErrorBody: TypeAlias = (
    V1OrganizationsPostgresConfig400Error1 | V1OrganizationsPostgresConfig500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _PostgresInstanceConfigPostError:
    def map(self, response: HttpResponse) -> PostgresInstanceConfigPostErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsPostgresConfig400Error1](response)
            case 500:
                return decode_json[V1OrganizationsPostgresConfig500Error1](response)
            case _:
                return RawError(response)


postgres_instance_config_post_error_mapper: Final[
    ErrorMapper[PostgresInstanceConfigPostErrorBody]
] = _PostgresInstanceConfigPostError()
