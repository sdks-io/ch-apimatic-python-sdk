from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_postgres_config400_error1 import V1OrganizationsPostgresConfig400Error1
from ..models.v1_organizations_postgres_config500_error1 import V1OrganizationsPostgresConfig500Error1

PostgresInstanceConfigPatchErrorBody: TypeAlias = (
    V1OrganizationsPostgresConfig400Error1 | V1OrganizationsPostgresConfig500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _PostgresInstanceConfigPatchError:
    def map(self, response: HttpResponse) -> PostgresInstanceConfigPatchErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsPostgresConfig400Error1](response)
            case 500:
                return decode_json[V1OrganizationsPostgresConfig500Error1](response)
            case _:
                return RawError(response)


postgres_instance_config_patch_error_mapper: Final[
    ErrorMapper[PostgresInstanceConfigPatchErrorBody]
] = _PostgresInstanceConfigPatchError()
