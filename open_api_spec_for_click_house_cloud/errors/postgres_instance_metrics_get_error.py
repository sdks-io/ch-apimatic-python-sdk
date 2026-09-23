from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_postgres_metrics400_error1 import V1OrganizationsPostgresMetrics400Error1
from ..models.v1_organizations_postgres_metrics500_error1 import V1OrganizationsPostgresMetrics500Error1

PostgresInstanceMetricsGetErrorBody: TypeAlias = (
    V1OrganizationsPostgresMetrics400Error1 | V1OrganizationsPostgresMetrics500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _PostgresInstanceMetricsGetError:
    def map(self, response: HttpResponse) -> PostgresInstanceMetricsGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsPostgresMetrics400Error1](response)
            case 500:
                return decode_json[V1OrganizationsPostgresMetrics500Error1](response)
            case _:
                return RawError(response)


postgres_instance_metrics_get_error_mapper: Final[
    ErrorMapper[PostgresInstanceMetricsGetErrorBody]
] = _PostgresInstanceMetricsGetError()
