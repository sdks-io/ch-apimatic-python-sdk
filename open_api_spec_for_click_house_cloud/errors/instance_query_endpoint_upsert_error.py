from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_service_query_endpoint400_error1 import (
    V1OrganizationsServicesServiceQueryEndpoint400Error1,
)
from ..models.v1_organizations_services_service_query_endpoint500_error1 import (
    V1OrganizationsServicesServiceQueryEndpoint500Error1,
)

InstanceQueryEndpointUpsertErrorBody: TypeAlias = (
    V1OrganizationsServicesServiceQueryEndpoint400Error1
    | V1OrganizationsServicesServiceQueryEndpoint500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _InstanceQueryEndpointUpsertError:
    def map(self, response: HttpResponse) -> InstanceQueryEndpointUpsertErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesServiceQueryEndpoint400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesServiceQueryEndpoint500Error1](response)
            case _:
                return RawError(response)


instance_query_endpoint_upsert_error_mapper: Final[
    ErrorMapper[InstanceQueryEndpointUpsertErrorBody]
] = _InstanceQueryEndpointUpsertError()
