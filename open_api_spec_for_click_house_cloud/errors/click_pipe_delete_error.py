from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickpipes_click_pipe_id400_error1 import (
    V1OrganizationsServicesClickpipesClickPipeId400Error1,
)
from ..models.v1_organizations_services_clickpipes_click_pipe_id500_error1 import (
    V1OrganizationsServicesClickpipesClickPipeId500Error1,
)

ClickPipeDeleteErrorBody: TypeAlias = (
    V1OrganizationsServicesClickpipesClickPipeId400Error1
    | V1OrganizationsServicesClickpipesClickPipeId500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickPipeDeleteError:
    def map(self, response: HttpResponse) -> ClickPipeDeleteErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickpipesClickPipeId400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickpipesClickPipeId500Error1](response)
            case _:
                return RawError(response)


click_pipe_delete_error_mapper: Final[ErrorMapper[ClickPipeDeleteErrorBody]] = _ClickPipeDeleteError()
