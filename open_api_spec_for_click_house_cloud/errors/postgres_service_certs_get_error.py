from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_postgres_ca_certificates400_error1 import V1OrganizationsPostgresCaCertificates400Error1
from ..models.v1_organizations_postgres_ca_certificates500_error1 import V1OrganizationsPostgresCaCertificates500Error1

PostgresServiceCertsGetErrorBody: TypeAlias = (
    V1OrganizationsPostgresCaCertificates400Error1 | V1OrganizationsPostgresCaCertificates500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _PostgresServiceCertsGetError:
    def map(self, response: HttpResponse) -> PostgresServiceCertsGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsPostgresCaCertificates400Error1](response)
            case 500:
                return decode_json[V1OrganizationsPostgresCaCertificates500Error1](response)
            case _:
                return RawError(response)


postgres_service_certs_get_error_mapper: Final[
    ErrorMapper[PostgresServiceCertsGetErrorBody]
] = _PostgresServiceCertsGetError()
