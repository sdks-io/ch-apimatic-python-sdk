from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_backups400_error1 import V1OrganizationsServicesBackups400Error1
from ..models.v1_organizations_services_backups500_error1 import V1OrganizationsServicesBackups500Error1

BackupGetListErrorBody: TypeAlias = (
    V1OrganizationsServicesBackups400Error1 | V1OrganizationsServicesBackups500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _BackupGetListError:
    def map(self, response: HttpResponse) -> BackupGetListErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesBackups400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesBackups500Error1](response)
            case _:
                return RawError(response)


backup_get_list_error_mapper: Final[ErrorMapper[BackupGetListErrorBody]] = _BackupGetListError()
