from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_roles400_error1 import V1OrganizationsRoles400Error1
from ..models.v1_organizations_roles500_error1 import V1OrganizationsRoles500Error1

OrganizationRoleGetErrorBody: TypeAlias = V1OrganizationsRoles400Error1 | V1OrganizationsRoles500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _OrganizationRoleGetError:
    def map(self, response: HttpResponse) -> OrganizationRoleGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsRoles400Error1](response)
            case 500:
                return decode_json[V1OrganizationsRoles500Error1](response)
            case _:
                return RawError(response)


organization_role_get_error_mapper: Final[ErrorMapper[OrganizationRoleGetErrorBody]] = _OrganizationRoleGetError()
