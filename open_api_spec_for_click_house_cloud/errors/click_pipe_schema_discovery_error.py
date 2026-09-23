from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickpipes_schema_discovery400_error1 import (
    V1OrganizationsServicesClickpipesSchemaDiscovery400Error1,
)
from ..models.v1_organizations_services_clickpipes_schema_discovery500_error1 import (
    V1OrganizationsServicesClickpipesSchemaDiscovery500Error1,
)

ClickPipeSchemaDiscoveryErrorBody: TypeAlias = (
    V1OrganizationsServicesClickpipesSchemaDiscovery400Error1
    | V1OrganizationsServicesClickpipesSchemaDiscovery500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickPipeSchemaDiscoveryError:
    def map(self, response: HttpResponse) -> ClickPipeSchemaDiscoveryErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickpipesSchemaDiscovery400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickpipesSchemaDiscovery500Error1](response)
            case _:
                return RawError(response)


click_pipe_schema_discovery_error_mapper: Final[
    ErrorMapper[ClickPipeSchemaDiscoveryErrorBody]
] = _ClickPipeSchemaDiscoveryError()
