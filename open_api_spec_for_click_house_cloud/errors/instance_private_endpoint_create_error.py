from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_private_endpoint400_error1 import (
    V1OrganizationsServicesPrivateEndpoint400Error1,
)
from ..models.v1_organizations_services_private_endpoint500_error1 import (
    V1OrganizationsServicesPrivateEndpoint500Error1,
)

InstancePrivateEndpointCreateErrorBody: TypeAlias = (
    V1OrganizationsServicesPrivateEndpoint400Error1 | V1OrganizationsServicesPrivateEndpoint500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _InstancePrivateEndpointCreateError:
    def map(self, response: HttpResponse) -> InstancePrivateEndpointCreateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesPrivateEndpoint400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesPrivateEndpoint500Error1](response)
            case _:
                return RawError(response)


instance_private_endpoint_create_error_mapper: Final[
    ErrorMapper[InstancePrivateEndpointCreateErrorBody]
] = _InstancePrivateEndpointCreateError()
