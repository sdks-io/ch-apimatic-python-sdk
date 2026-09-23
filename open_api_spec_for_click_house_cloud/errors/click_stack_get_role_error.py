from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickstack_roles_click_stack_role_id400_error1 import (
    V1OrganizationsServicesClickstackRolesClickStackRoleId400Error1,
)
from ..models.v1_organizations_services_clickstack_roles_click_stack_role_id500_error1 import (
    V1OrganizationsServicesClickstackRolesClickStackRoleId500Error1,
)

ClickStackGetRoleErrorBody: TypeAlias = (
    V1OrganizationsServicesClickstackRolesClickStackRoleId400Error1
    | V1OrganizationsServicesClickstackRolesClickStackRoleId500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickStackGetRoleError:
    def map(self, response: HttpResponse) -> ClickStackGetRoleErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickstackRolesClickStackRoleId400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickstackRolesClickStackRoleId500Error1](response)
            case _:
                return RawError(response)


click_stack_get_role_error_mapper: Final[ErrorMapper[ClickStackGetRoleErrorBody]] = _ClickStackGetRoleError()
