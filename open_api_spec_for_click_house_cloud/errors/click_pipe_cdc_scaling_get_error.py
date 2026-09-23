from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickpipes_cdc_scaling400_error1 import (
    V1OrganizationsServicesClickpipesCdcScaling400Error1,
)
from ..models.v1_organizations_services_clickpipes_cdc_scaling500_error1 import (
    V1OrganizationsServicesClickpipesCdcScaling500Error1,
)

ClickPipeCdcScalingGetErrorBody: TypeAlias = (
    V1OrganizationsServicesClickpipesCdcScaling400Error1
    | V1OrganizationsServicesClickpipesCdcScaling500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickPipeCdcScalingGetError:
    def map(self, response: HttpResponse) -> ClickPipeCdcScalingGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickpipesCdcScaling400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickpipesCdcScaling500Error1](response)
            case _:
                return RawError(response)


click_pipe_cdc_scaling_get_error_mapper: Final[
    ErrorMapper[ClickPipeCdcScalingGetErrorBody]
] = _ClickPipeCdcScalingGetError()
