from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_upgrade_window400_error1 import V1OrganizationsServicesUpgradeWindow400Error1
from ..models.v1_organizations_services_upgrade_window500_error1 import V1OrganizationsServicesUpgradeWindow500Error1

UpgradeWindowUpdateErrorBody: TypeAlias = (
    V1OrganizationsServicesUpgradeWindow400Error1 | V1OrganizationsServicesUpgradeWindow500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _UpgradeWindowUpdateError:
    def map(self, response: HttpResponse) -> UpgradeWindowUpdateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesUpgradeWindow400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesUpgradeWindow500Error1](response)
            case _:
                return RawError(response)


upgrade_window_update_error_mapper: Final[ErrorMapper[UpgradeWindowUpdateErrorBody]] = _UpgradeWindowUpdateError()
