from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_members400_error1 import V1OrganizationsMembers400Error1
from ..models.v1_organizations_members500_error1 import V1OrganizationsMembers500Error1

MemberGetErrorBody: TypeAlias = V1OrganizationsMembers400Error1 | V1OrganizationsMembers500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _MemberGetError:
    def map(self, response: HttpResponse) -> MemberGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsMembers400Error1](response)
            case 500:
                return decode_json[V1OrganizationsMembers500Error1](response)
            case _:
                return RawError(response)


member_get_error_mapper: Final[ErrorMapper[MemberGetErrorBody]] = _MemberGetError()
