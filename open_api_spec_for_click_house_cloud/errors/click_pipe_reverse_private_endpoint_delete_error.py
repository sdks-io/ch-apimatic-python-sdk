from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id400_error1 import (
    V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400Error1,
)
from ..models.v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id500_error1 import (
    V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500Error1,
)

ClickPipeReversePrivateEndpointDeleteErrorBody: TypeAlias = (
    V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400Error1
    | V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickPipeReversePrivateEndpointDeleteError:
    def map(self, response: HttpResponse) -> ClickPipeReversePrivateEndpointDeleteErrorBody:
        match response.status_code:
            case 400:
                return decode_json[
                    V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400Error1
                ](response)
            case 500:
                return decode_json[
                    V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500Error1
                ](response)
            case _:
                return RawError(response)


click_pipe_reverse_private_endpoint_delete_error_mapper: Final[
    ErrorMapper[ClickPipeReversePrivateEndpointDeleteErrorBody]
] = _ClickPipeReversePrivateEndpointDeleteError()
