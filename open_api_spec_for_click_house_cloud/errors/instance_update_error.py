from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services400_error1 import V1OrganizationsServices400Error1
from ..models.v1_organizations_services500_error1 import V1OrganizationsServices500Error1

InstanceUpdateErrorBody: TypeAlias = V1OrganizationsServices400Error1 | V1OrganizationsServices500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _InstanceUpdateError:
    def map(self, response: HttpResponse) -> InstanceUpdateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServices400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServices500Error1](response)
            case _:
                return RawError(response)


instance_update_error_mapper: Final[ErrorMapper[InstanceUpdateErrorBody]] = _InstanceUpdateError()
