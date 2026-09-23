from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id400_error1 import (
    V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400Error1,
)
from ..models.v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id500_error1 import (
    V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500Error1,
)

ClickStackGetDashboardErrorBody: TypeAlias = (
    V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400Error1
    | V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickStackGetDashboardError:
    def map(self, response: HttpResponse) -> ClickStackGetDashboardErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500Error1](response)
            case _:
                return RawError(response)


click_stack_get_dashboard_error_mapper: Final[
    ErrorMapper[ClickStackGetDashboardErrorBody]
] = _ClickStackGetDashboardError()
