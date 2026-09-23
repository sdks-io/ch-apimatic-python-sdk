from __future__ import annotations

from typing import TypeAlias

from ..aws_backup_bucket_post_request_v1 import AwsBackupBucketPostRequestV1, AwsBackupBucketPostRequestV1Dict
from ..azure_backup_bucket_post_request_v1 import AzureBackupBucketPostRequestV1, AzureBackupBucketPostRequestV1Dict
from ..gcp_backup_bucket_post_request_v1 import GcpBackupBucketPostRequestV1, GcpBackupBucketPostRequestV1Dict

BackupBucketPostRequest: TypeAlias = (
    AwsBackupBucketPostRequestV1 | GcpBackupBucketPostRequestV1 | AzureBackupBucketPostRequestV1
)

BackupBucketPostRequestDict: TypeAlias = (
    AwsBackupBucketPostRequestV1Dict | GcpBackupBucketPostRequestV1Dict | AzureBackupBucketPostRequestV1Dict
)
