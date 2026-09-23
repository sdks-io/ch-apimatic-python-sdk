from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_postgres_read_replica400_error1 import V1OrganizationsPostgresReadReplica400Error1
from ..models.v1_organizations_postgres_read_replica500_error1 import V1OrganizationsPostgresReadReplica500Error1

PostgresInstanceCreateReadReplicaErrorBody: TypeAlias = (
    V1OrganizationsPostgresReadReplica400Error1 | V1OrganizationsPostgresReadReplica500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _PostgresInstanceCreateReadReplicaError:
    def map(self, response: HttpResponse) -> PostgresInstanceCreateReadReplicaErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsPostgresReadReplica400Error1](response)
            case 500:
                return decode_json[V1OrganizationsPostgresReadReplica500Error1](response)
            case _:
                return RawError(response)


postgres_instance_create_read_replica_error_mapper: Final[
    ErrorMapper[PostgresInstanceCreateReadReplicaErrorBody]
] = _PostgresInstanceCreateReadReplicaError()
