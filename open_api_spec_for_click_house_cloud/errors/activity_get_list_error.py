from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_activities400_error1 import V1OrganizationsActivities400Error1
from ..models.v1_organizations_activities500_error1 import V1OrganizationsActivities500Error1

ActivityGetListErrorBody: TypeAlias = V1OrganizationsActivities400Error1 | V1OrganizationsActivities500Error1 | RawError


@dataclass(frozen=True, slots=True)
class _ActivityGetListError:
    def map(self, response: HttpResponse) -> ActivityGetListErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsActivities400Error1](response)
            case 500:
                return decode_json[V1OrganizationsActivities500Error1](response)
            case _:
                return RawError(response)


activity_get_list_error_mapper: Final[ErrorMapper[ActivityGetListErrorBody]] = _ActivityGetListError()
