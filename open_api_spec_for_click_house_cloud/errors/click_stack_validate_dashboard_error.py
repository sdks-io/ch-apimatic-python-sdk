from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickstack_dashboards_validate400_error1 import (
    V1OrganizationsServicesClickstackDashboardsValidate400Error1,
)
from ..models.v1_organizations_services_clickstack_dashboards_validate500_error1 import (
    V1OrganizationsServicesClickstackDashboardsValidate500Error1,
)

ClickStackValidateDashboardErrorBody: TypeAlias = (
    V1OrganizationsServicesClickstackDashboardsValidate400Error1
    | V1OrganizationsServicesClickstackDashboardsValidate500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickStackValidateDashboardError:
    def map(self, response: HttpResponse) -> ClickStackValidateDashboardErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickstackDashboardsValidate400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickstackDashboardsValidate500Error1](response)
            case _:
                return RawError(response)


click_stack_validate_dashboard_error_mapper: Final[
    ErrorMapper[ClickStackValidateDashboardErrorBody]
] = _ClickStackValidateDashboardError()
