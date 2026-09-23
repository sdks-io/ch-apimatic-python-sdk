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

ClickStackListAlertsErrorBody: TypeAlias = (
    V1OrganizationsServicesClickstackAlerts400Error1 | V1OrganizationsServicesClickstackAlerts500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickStackListAlertsError:
    def map(self, response: HttpResponse) -> ClickStackListAlertsErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickstackAlerts400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickstackAlerts500Error1](response)
            case _:
                return RawError(response)


click_stack_list_alerts_error_mapper: Final[ErrorMapper[ClickStackListAlertsErrorBody]] = _ClickStackListAlertsError()
