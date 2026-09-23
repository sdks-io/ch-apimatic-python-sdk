from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_prometheus_discovery400_error1 import V1OrganizationsPrometheusDiscovery400Error1
from ..models.v1_organizations_prometheus_discovery500_error1 import V1OrganizationsPrometheusDiscovery500Error1

OrganizationPrometheusDiscoveryGetErrorBody: TypeAlias = (
    V1OrganizationsPrometheusDiscovery400Error1 | V1OrganizationsPrometheusDiscovery500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _OrganizationPrometheusDiscoveryGetError:
    def map(self, response: HttpResponse) -> OrganizationPrometheusDiscoveryGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsPrometheusDiscovery400Error1](response)
            case 500:
                return decode_json[V1OrganizationsPrometheusDiscovery500Error1](response)
            case _:
                return RawError(response)


organization_prometheus_discovery_get_error_mapper: Final[
    ErrorMapper[OrganizationPrometheusDiscoveryGetErrorBody]
] = _OrganizationPrometheusDiscoveryGetError()
