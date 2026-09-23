from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickpipes_click_pipe_id_state400_error1 import (
    V1OrganizationsServicesClickpipesClickPipeIdState400Error1,
)
from ..models.v1_organizations_services_clickpipes_click_pipe_id_state500_error1 import (
    V1OrganizationsServicesClickpipesClickPipeIdState500Error1,
)

ClickPipeStateUpdateErrorBody: TypeAlias = (
    V1OrganizationsServicesClickpipesClickPipeIdState400Error1
    | V1OrganizationsServicesClickpipesClickPipeIdState500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickPipeStateUpdateError:
    def map(self, response: HttpResponse) -> ClickPipeStateUpdateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickpipesClickPipeIdState400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickpipesClickPipeIdState500Error1](response)
            case _:
                return RawError(response)


click_pipe_state_update_error_mapper: Final[ErrorMapper[ClickPipeStateUpdateErrorBody]] = _ClickPipeStateUpdateError()
