from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_prometheus400_error1 import V1OrganizationsPrometheus400Error1
from ..models.v1_organizations_prometheus500_error1 import V1OrganizationsPrometheus500Error1

OrganizationPrometheusGetErrorBody: TypeAlias = (
    V1OrganizationsPrometheus400Error1 | V1OrganizationsPrometheus500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _OrganizationPrometheusGetError:
    def map(self, response: HttpResponse) -> OrganizationPrometheusGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsPrometheus400Error1](response)
            case 500:
                return decode_json[V1OrganizationsPrometheus500Error1](response)
            case _:
                return RawError(response)


organization_prometheus_get_error_mapper: Final[
    ErrorMapper[OrganizationPrometheusGetErrorBody]
] = _OrganizationPrometheusGetError()
