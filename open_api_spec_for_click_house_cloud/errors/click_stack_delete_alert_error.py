from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickstack_alerts_click_stack_alert_id400_error1 import (
    V1OrganizationsServicesClickstackAlertsClickStackAlertId400Error1,
)
from ..models.v1_organizations_services_clickstack_alerts_click_stack_alert_id500_error1 import (
    V1OrganizationsServicesClickstackAlertsClickStackAlertId500Error1,
)

ClickStackDeleteAlertErrorBody: TypeAlias = (
    V1OrganizationsServicesClickstackAlertsClickStackAlertId400Error1
    | V1OrganizationsServicesClickstackAlertsClickStackAlertId500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickStackDeleteAlertError:
    def map(self, response: HttpResponse) -> ClickStackDeleteAlertErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickstackAlertsClickStackAlertId400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickstackAlertsClickStackAlertId500Error1](response)
            case _:
                return RawError(response)


click_stack_delete_alert_error_mapper: Final[
    ErrorMapper[ClickStackDeleteAlertErrorBody]
] = _ClickStackDeleteAlertError()
