from __future__ import annotations

from typing import TypeAlias

from ..aws_backup_bucket_patch_request_v1 import AwsBackupBucketPatchRequestV1, AwsBackupBucketPatchRequestV1Dict
from ..azure_backup_bucket_patch_request_v1 import AzureBackupBucketPatchRequestV1, AzureBackupBucketPatchRequestV1Dict
from ..gcp_backup_bucket_patch_request_v1 import GcpBackupBucketPatchRequestV1, GcpBackupBucketPatchRequestV1Dict

BackupBucketPatchRequest: TypeAlias = (
    AwsBackupBucketPatchRequestV1 | GcpBackupBucketPatchRequestV1 | AzureBackupBucketPatchRequestV1
)

BackupBucketPatchRequestDict: TypeAlias = (
    AwsBackupBucketPatchRequestV1Dict | GcpBackupBucketPatchRequestV1Dict | AzureBackupBucketPatchRequestV1Dict
)
