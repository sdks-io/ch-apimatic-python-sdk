from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickstack_alerts400_error1 import (
    V1OrganizationsServicesClickstackAlerts400Error1,
)
from ..models.v1_organizations_services_clickstack_alerts500_error1 import (
    V1OrganizationsServicesClickstackAlerts500Error1,
)

ClickStackCreateAlertErrorBody: TypeAlias = (
    V1OrganizationsServicesClickstackAlerts400Error1 | V1OrganizationsServicesClickstackAlerts500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickStackCreateAlertError:
    def map(self, response: HttpResponse) -> ClickStackCreateAlertErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickstackAlerts400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickstackAlerts500Error1](response)
            case _:
                return RawError(response)


click_stack_create_alert_error_mapper: Final[
    ErrorMapper[ClickStackCreateAlertErrorBody]
] = _ClickStackCreateAlertError()
