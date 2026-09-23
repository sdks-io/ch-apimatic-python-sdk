from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickpipes_click_pipe_id_settings400_error1 import (
    V1OrganizationsServicesClickpipesClickPipeIdSettings400Error1,
)
from ..models.v1_organizations_services_clickpipes_click_pipe_id_settings500_error1 import (
    V1OrganizationsServicesClickpipesClickPipeIdSettings500Error1,
)

ClickPipeSettingsGetErrorBody: TypeAlias = (
    V1OrganizationsServicesClickpipesClickPipeIdSettings400Error1
    | V1OrganizationsServicesClickpipesClickPipeIdSettings500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickPipeSettingsGetError:
    def map(self, response: HttpResponse) -> ClickPipeSettingsGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickpipesClickPipeIdSettings400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickpipesClickPipeIdSettings500Error1](response)
            case _:
                return RawError(response)


click_pipe_settings_get_error_mapper: Final[ErrorMapper[ClickPipeSettingsGetErrorBody]] = _ClickPipeSettingsGetError()
