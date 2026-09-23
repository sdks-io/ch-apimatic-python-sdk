from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_clickstack_dashboards400_error1 import (
    V1OrganizationsServicesClickstackDashboards400Error1,
)
from ..models.v1_organizations_services_clickstack_dashboards500_error1 import (
    V1OrganizationsServicesClickstackDashboards500Error1,
)

ClickStackListDashboardsErrorBody: TypeAlias = (
    V1OrganizationsServicesClickstackDashboards400Error1
    | V1OrganizationsServicesClickstackDashboards500Error1
    | RawError
)


@dataclass(frozen=True, slots=True)
class _ClickStackListDashboardsError:
    def map(self, response: HttpResponse) -> ClickStackListDashboardsErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesClickstackDashboards400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesClickstackDashboards500Error1](response)
            case _:
                return RawError(response)


click_stack_list_dashboards_error_mapper: Final[
    ErrorMapper[ClickStackListDashboardsErrorBody]
] = _ClickStackListDashboardsError()
