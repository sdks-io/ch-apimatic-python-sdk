from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickpipes_click_pipe_id_scaling400_error1 import (
    V1OrganizationsServicesClickpipesClickPipeIdScaling400Error1,
)
from ..models.v1_organizations_services_clickpipes_click_pipe_id_scaling500_error1 import (
    V1OrganizationsServicesClickpipesClickPipeIdScaling500Error1,
)

ClickPipeScalingUpdateErrorBody: TypeAlias = (
    V1OrganizationsServicesClickpipesClickPipeIdScaling400Error1
    | V1OrganizationsServicesClickpipesClickPipeIdScaling500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickPipeScalingUpdateError:
    def map(self, response: HttpResponse) -> ClickPipeScalingUpdateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickpipesClickPipeIdScaling400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickpipesClickPipeIdScaling500Error1](response)
            case _:
                return RawError(response)


click_pipe_scaling_update_error_mapper: Final[
    ErrorMapper[ClickPipeScalingUpdateErrorBody]
] = _ClickPipeScalingUpdateError()
