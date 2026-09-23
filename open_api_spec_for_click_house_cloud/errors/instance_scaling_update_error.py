from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_scaling400_error1 import V1OrganizationsServicesScaling400Error1
from ..models.v1_organizations_services_scaling500_error1 import V1OrganizationsServicesScaling500Error1

InstanceScalingUpdateErrorBody: TypeAlias = (
    V1OrganizationsServicesScaling400Error1 | V1OrganizationsServicesScaling500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _InstanceScalingUpdateError:
    def map(self, response: HttpResponse) -> InstanceScalingUpdateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesScaling400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesScaling500Error1](response)
            case _:
                return RawError(response)


instance_scaling_update_error_mapper: Final[ErrorMapper[InstanceScalingUpdateErrorBody]] = _InstanceScalingUpdateError()
