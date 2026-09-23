from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_service_profiles400_error1 import V1OrganizationsServiceProfiles400Error1
from ..models.v1_organizations_service_profiles500_error1 import V1OrganizationsServiceProfiles500Error1

ServiceProfilesListErrorBody: TypeAlias = (
    V1OrganizationsServiceProfiles400Error1 | V1OrganizationsServiceProfiles500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _ServiceProfilesListError:
    def map(self, response: HttpResponse) -> ServiceProfilesListErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServiceProfiles400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServiceProfiles500Error1](response)
            case _:
                return RawError(response)


service_profiles_list_error_mapper: Final[ErrorMapper[ServiceProfilesListErrorBody]] = _ServiceProfilesListError()
