from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickstack_roles400_error1 import (
    V1OrganizationsServicesClickstackRoles400Error1,
)
from ..models.v1_organizations_services_clickstack_roles500_error1 import (
    V1OrganizationsServicesClickstackRoles500Error1,
)

ClickStackCreateRoleErrorBody: TypeAlias = (
    V1OrganizationsServicesClickstackRoles400Error1 | V1OrganizationsServicesClickstackRoles500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickStackCreateRoleError:
    def map(self, response: HttpResponse) -> ClickStackCreateRoleErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickstackRoles400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickstackRoles500Error1](response)
            case _:
                return RawError(response)


click_stack_create_role_error_mapper: Final[ErrorMapper[ClickStackCreateRoleErrorBody]] = _ClickStackCreateRoleError()
