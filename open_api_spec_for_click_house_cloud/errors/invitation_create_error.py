from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_invitations400_error1 import V1OrganizationsInvitations400Error1
from ..models.v1_organizations_invitations500_error1 import V1OrganizationsInvitations500Error1

InvitationCreateErrorBody: TypeAlias = (
    V1OrganizationsInvitations400Error1 | V1OrganizationsInvitations500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _InvitationCreateError:
    def map(self, response: HttpResponse) -> InvitationCreateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsInvitations400Error1](response)
            case 500:
                return decode_json[V1OrganizationsInvitations500Error1](response)
            case _:
                return RawError(response)


invitation_create_error_mapper: Final[ErrorMapper[InvitationCreateErrorBody]] = _InvitationCreateError()
