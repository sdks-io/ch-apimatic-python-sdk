from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_prometheus400_error1 import V1OrganizationsServicesPrometheus400Error1
from ..models.v1_organizations_services_prometheus500_error1 import V1OrganizationsServicesPrometheus500Error1

InstancePrometheusGetErrorBody: TypeAlias = (
    V1OrganizationsServicesPrometheus400Error1 | V1OrganizationsServicesPrometheus500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _InstancePrometheusGetError:
    def map(self, response: HttpResponse) -> InstancePrometheusGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesPrometheus400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesPrometheus500Error1](response)
            case _:
                return RawError(response)


instance_prometheus_get_error_mapper: Final[ErrorMapper[InstancePrometheusGetErrorBody]] = _InstancePrometheusGetError()
