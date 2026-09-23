from __future__ import annotations

from typing import TypeAlias

from ..aws_backup_bucket import AwsBackupBucket, AwsBackupBucketDict
from ..azure_backup_bucket import AzureBackupBucket, AzureBackupBucketDict
from ..gcp_backup_bucket import GcpBackupBucket, GcpBackupBucketDict

BackupBucket: TypeAlias = AwsBackupBucket | GcpBackupBucket | AzureBackupBucket

BackupBucketDict: TypeAlias = AwsBackupBucketDict | GcpBackupBucketDict | AzureBackupBucketDict
