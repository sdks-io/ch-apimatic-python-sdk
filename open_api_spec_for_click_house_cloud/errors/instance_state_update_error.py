from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_state400_error1 import V1OrganizationsServicesState400Error1
from ..models.v1_organizations_services_state500_error1 import V1OrganizationsServicesState500Error1

InstanceStateUpdateErrorBody: TypeAlias = (
    V1OrganizationsServicesState400Error1 | V1OrganizationsServicesState500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _InstanceStateUpdateError:
    def map(self, response: HttpResponse) -> InstanceStateUpdateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesState400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesState500Error1](response)
            case _:
                return RawError(response)


instance_state_update_error_mapper: Final[ErrorMapper[InstanceStateUpdateErrorBody]] = _InstanceStateUpdateError()
