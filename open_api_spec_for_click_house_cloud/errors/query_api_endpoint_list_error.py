from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_query_api_endpoints400_error1 import (
    V1OrganizationsServicesQueryApiEndpoints400Error1,
)
from ..models.v1_organizations_services_query_api_endpoints403_error1 import (
    V1OrganizationsServicesQueryApiEndpoints403Error1,
)
from ..models.v1_organizations_services_query_api_endpoints404_error1 import (
    V1OrganizationsServicesQueryApiEndpoints404Error1,
)
from ..models.v1_organizations_services_query_api_endpoints500_error1 import (
    V1OrganizationsServicesQueryApiEndpoints500Error1,
)

QueryApiEndpointListErrorBody: TypeAlias = (
    V1OrganizationsServicesQueryApiEndpoints400Error1
    | V1OrganizationsServicesQueryApiEndpoints403Error1
    | V1OrganizationsServicesQueryApiEndpoints404Error1
    | V1OrganizationsServicesQueryApiEndpoints500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _QueryApiEndpointListError:
    def map(self, response: HttpResponse) -> QueryApiEndpointListErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesQueryApiEndpoints400Error1](response)
            case 403:
                return decode_json[V1OrganizationsServicesQueryApiEndpoints403Error1](response)
            case 404:
                return decode_json[V1OrganizationsServicesQueryApiEndpoints404Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesQueryApiEndpoints500Error1](response)
            case _:
                return RawError(response)


query_api_endpoint_list_error_mapper: Final[ErrorMapper[QueryApiEndpointListErrorBody]] = _QueryApiEndpointListError()
