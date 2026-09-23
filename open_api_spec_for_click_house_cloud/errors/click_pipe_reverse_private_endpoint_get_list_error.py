from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickpipes_reverse_private_endpoints400_error1 import (
    V1OrganizationsServicesClickpipesReversePrivateEndpoints400Error1,
)
from ..models.v1_organizations_services_clickpipes_reverse_private_endpoints500_error1 import (
    V1OrganizationsServicesClickpipesReversePrivateEndpoints500Error1,
)

ClickPipeReversePrivateEndpointGetListErrorBody: TypeAlias = (
    V1OrganizationsServicesClickpipesReversePrivateEndpoints400Error1
    | V1OrganizationsServicesClickpipesReversePrivateEndpoints500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickPipeReversePrivateEndpointGetListError:
    def map(self, response: HttpResponse) -> ClickPipeReversePrivateEndpointGetListErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickpipesReversePrivateEndpoints400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickpipesReversePrivateEndpoints500Error1](response)
            case _:
                return RawError(response)


click_pipe_reverse_private_endpoint_get_list_error_mapper: Final[
    ErrorMapper[ClickPipeReversePrivateEndpointGetListErrorBody]
] = _ClickPipeReversePrivateEndpointGetListError()
