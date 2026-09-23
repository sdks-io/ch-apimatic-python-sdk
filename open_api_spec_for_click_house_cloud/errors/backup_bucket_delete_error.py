from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.v1_organizations_services_backup_bucket400_error1 import V1OrganizationsServicesBackupBucket400Error1
from ..models.v1_organizations_services_backup_bucket500_error1 import V1OrganizationsServicesBackupBucket500Error1

BackupBucketDeleteErrorBody: TypeAlias = (
    V1OrganizationsServicesBackupBucket400Error1 | V1OrganizationsServicesBackupBucket500Error1 | RawError
)


@dataclass(frozen=True, slots=True)
class _BackupBucketDeleteError:
    def map(self, response: HttpResponse) -> BackupBucketDeleteErrorBody:
        match response.status_code:
            case 400:
                return decode_json[V1OrganizationsServicesBackupBucket400Error1](response)
            case 500:
                return decode_json[V1OrganizationsServicesBackupBucket500Error1](response)
            case _:
                return RawError(response)


backup_bucket_delete_error_mapper: Final[ErrorMapper[BackupBucketDeleteErrorBody]] = _BackupBucketDeleteError()
