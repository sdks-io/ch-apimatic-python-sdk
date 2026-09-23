from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickpipes_context400_error1 import (
    V1OrganizationsServicesClickpipesContext400Error1,
)
from ..models.v1_organizations_services_clickpipes_context500_error1 import (
    V1OrganizationsServicesClickpipesContext500Error1,
)

ClickPipesServiceContextGetErrorBody: TypeAlias = (
    V1OrganizationsServicesClickpipesContext400Error1 | V1OrganizationsServicesClickpipesContext500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickPipesServiceContextGetError:
    def map(self, response: HttpResponse) -> ClickPipesServiceContextGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickpipesContext400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickpipesContext500Error1](response)
            case _:
                return RawError(response)


click_pipes_service_context_get_error_mapper: Final[
    ErrorMapper[ClickPipesServiceContextGetErrorBody]
] = _ClickPipesServiceContextGetError()
