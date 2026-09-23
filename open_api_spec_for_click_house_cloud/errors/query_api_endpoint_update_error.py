from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_query_api_endpoints_endpoint_id400_error31 import (
    V1OrganizationsServicesQueryApiEndpointsEndpointId400Error31,
)
from ..models.v1_organizations_services_query_api_endpoints_endpoint_id403_error1 import (
    V1OrganizationsServicesQueryApiEndpointsEndpointId403Error1,
)
from ..models.v1_organizations_services_query_api_endpoints_endpoint_id404_error1 import (
    V1OrganizationsServicesQueryApiEndpointsEndpointId404Error1,
)
from ..models.v1_organizations_services_query_api_endpoints_endpoint_id409_error1 import (
    V1OrganizationsServicesQueryApiEndpointsEndpointId409Error1,
)
from ..models.v1_organizations_services_query_api_endpoints_endpoint_id500_error1 import (
    V1OrganizationsServicesQueryApiEndpointsEndpointId500Error1,
)

QueryApiEndpointUpdateErrorBody: TypeAlias = (
    V1OrganizationsServicesQueryApiEndpointsEndpointId400Error31
    | V1OrganizationsServicesQueryApiEndpointsEndpointId403Error1
    | V1OrganizationsServicesQueryApiEndpointsEndpointId404Error1
    | V1OrganizationsServicesQueryApiEndpointsEndpointId409Error1
    | V1OrganizationsServicesQueryApiEndpointsEndpointId500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _QueryApiEndpointUpdateError:
    def map(self, response: HttpResponse) -> QueryApiEndpointUpdateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesQueryApiEndpointsEndpointId400Error31](response)
            case 403:
                return decode_json[V1OrganizationsServicesQueryApiEndpointsEndpointId403Error1](response)
            case 404:
                return decode_json[V1OrganizationsServicesQueryApiEndpointsEndpointId404Error1](response)
            case 409:
                return decode_json[V1OrganizationsServicesQueryApiEndpointsEndpointId409Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesQueryApiEndpointsEndpointId500Error1](response)
            case _:
                return RawError(response)


query_api_endpoint_update_error_mapper: Final[
    ErrorMapper[QueryApiEndpointUpdateErrorBody]
] = _QueryApiEndpointUpdateError()
