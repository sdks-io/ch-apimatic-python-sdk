from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_password400_error1 import V1OrganizationsServicesPassword400Error1
from ..models.v1_organizations_services_password500_error1 import V1OrganizationsServicesPassword500Error1

InstancePasswordUpdateErrorBody: TypeAlias = (
    V1OrganizationsServicesPassword400Error1 | V1OrganizationsServicesPassword500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _InstancePasswordUpdateError:
    def map(self, response: HttpResponse) -> InstancePasswordUpdateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesPassword400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesPassword500Error1](response)
            case _:
                return RawError(response)


instance_password_update_error_mapper: Final[
    ErrorMapper[InstancePasswordUpdateErrorBody]
] = _InstancePasswordUpdateError()
