from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_private_endpoint_config400_error1 import (
    V1OrganizationsServicesPrivateEndpointConfig400Error1,
)
from ..models.v1_organizations_services_private_endpoint_config500_error1 import (
    V1OrganizationsServicesPrivateEndpointConfig500Error1,
)

InstancePrivateEndpointConfigGetErrorBody: TypeAlias = (
    V1OrganizationsServicesPrivateEndpointConfig400Error1
    | V1OrganizationsServicesPrivateEndpointConfig500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _InstancePrivateEndpointConfigGetError:
    def map(self, response: HttpResponse) -> InstancePrivateEndpointConfigGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesPrivateEndpointConfig400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesPrivateEndpointConfig500Error1](response)
            case _:
                return RawError(response)


instance_private_endpoint_config_get_error_mapper: Final[
    ErrorMapper[InstancePrivateEndpointConfigGetErrorBody]
] = _InstancePrivateEndpointConfigGetError()
