from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_postgres_prometheus400_error1 import V1OrganizationsPostgresPrometheus400Error1
from ..models.v1_organizations_postgres_prometheus500_error1 import V1OrganizationsPostgresPrometheus500Error1

PostgresOrgPrometheusGetErrorBody: TypeAlias = (
    V1OrganizationsPostgresPrometheus400Error1 | V1OrganizationsPostgresPrometheus500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _PostgresOrgPrometheusGetError:
    def map(self, response: HttpResponse) -> PostgresOrgPrometheusGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsPostgresPrometheus400Error1](response)
            case 500:
                return decode_json[V1OrganizationsPostgresPrometheus500Error1](response)
            case _:
                return RawError(response)


postgres_org_prometheus_get_error_mapper: Final[
    ErrorMapper[PostgresOrgPrometheusGetErrorBody]
] = _PostgresOrgPrometheusGetError()
