from __future__ import annotations

from typing import TypeAlias

from ..aws_backup_bucket_properties import AwsBackupBucketProperties, AwsBackupBucketPropertiesDict
from ..azure_backup_bucket_properties import AzureBackupBucketProperties, AzureBackupBucketPropertiesDict
from ..gcp_backup_bucket_properties import GcpBackupBucketProperties, GcpBackupBucketPropertiesDict

BackupBucketProperties: TypeAlias = AwsBackupBucketProperties | GcpBackupBucketProperties | AzureBackupBucketProperties

BackupBucketPropertiesDict: TypeAlias = (
    AwsBackupBucketPropertiesDict | GcpBackupBucketPropertiesDict | AzureBackupBucketPropertiesDict
)
