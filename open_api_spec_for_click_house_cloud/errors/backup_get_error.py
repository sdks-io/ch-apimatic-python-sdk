from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_backups_backup_id400_error1 import (
    V1OrganizationsServicesBackupsBackupId400Error1,
)
from ..models.v1_organizations_services_backups_backup_id500_error1 import (
    V1OrganizationsServicesBackupsBackupId500Error1,
)

BackupGetErrorBody: TypeAlias = (
    V1OrganizationsServicesBackupsBackupId400Error1 | V1OrganizationsServicesBackupsBackupId500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _BackupGetError:
    def map(self, response: HttpResponse) -> BackupGetErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesBackupsBackupId400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesBackupsBackupId500Error1](response)
            case _:
                return RawError(response)


backup_get_error_mapper: Final[ErrorMapper[BackupGetErrorBody]] = _BackupGetError()
