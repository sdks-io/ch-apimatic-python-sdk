from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_backup_configuration400_error1 import (
    V1OrganizationsServicesBackupConfiguration400Error1,
)
from ..models.v1_organizations_services_backup_configuration500_error1 import (
    V1OrganizationsServicesBackupConfiguration500Error1,
)

BackupConfigurationUpdateErrorBody: TypeAlias = (
    V1OrganizationsServicesBackupConfiguration400Error1 | V1OrganizationsServicesBackupConfiguration500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _BackupConfigurationUpdateError:
    def map(self, response: HttpResponse) -> BackupConfigurationUpdateErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesBackupConfiguration400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesBackupConfiguration500Error1](response)
            case _:
                return RawError(response)


backup_configuration_update_error_mapper: Final[
    ErrorMapper[BackupConfigurationUpdateErrorBody]
] = _BackupConfigurationUpdateError()
