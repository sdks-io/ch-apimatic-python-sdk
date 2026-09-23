from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickpipes400_error1 import V1OrganizationsServicesClickpipes400Error1
from ..models.v1_organizations_services_clickpipes500_error1 import V1OrganizationsServicesClickpipes500Error1

ClickPipeGetListErrorBody: TypeAlias = (
    V1OrganizationsServicesClickpipes400Error1 | V1OrganizationsServicesClickpipes500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickPipeGetListError:
    def map(self, response: HttpResponse) -> ClickPipeGetListErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickpipes400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickpipes500Error1](response)
            case _:
                return RawError(response)


click_pipe_get_list_error_mapper: Final[ErrorMapper[ClickPipeGetListErrorBody]] = _ClickPipeGetListError()
