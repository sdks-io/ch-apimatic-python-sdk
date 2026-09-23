from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickpipes400_error1 import V1OrganizationsServicesClickpipes400Error1
from ..models.v1_organizations_services_clickpipes500_error1 import V1OrganizationsServicesClickpipes500Error1

ClickPipeCreateErrorBody: TypeAlias = (
    V1OrganizationsServicesClickpipes400Error1 | V1OrganizationsServicesClickpipes500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickPipeCreateError:
    def map(self, response: HttpResponse) -> ClickPipeCreateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickpipes400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickpipes500Error1](response)
            case _:
                return RawError(response)


click_pipe_create_error_mapper: Final[ErrorMapper[ClickPipeCreateErrorBody]] = _ClickPipeCreateError()
