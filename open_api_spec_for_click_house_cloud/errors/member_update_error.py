from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_members400_error1 import V1OrganizationsMembers400Error1
from ..models.v1_organizations_members500_error1 import V1OrganizationsMembers500Error1

MemberUpdateErrorBody: TypeAlias = V1OrganizationsMembers400Error1 | V1OrganizationsMembers500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _MemberUpdateError:
    def map(self, response: HttpResponse) -> MemberUpdateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsMembers400Error1](response)
            case 500:
                return decode_json[V1OrganizationsMembers500Error1](response)
            case _:
                return RawError(response)


member_update_error_mapper: Final[ErrorMapper[MemberUpdateErrorBody]] = _MemberUpdateError()
