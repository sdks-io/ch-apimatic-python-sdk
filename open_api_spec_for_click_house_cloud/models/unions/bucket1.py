from __future__ import annotations

from typing import TypeAlias

from ..aws_backup_bucket_properties import AwsBackupBucketProperties, AwsBackupBucketPropertiesDict
from ..azure_backup_bucket_properties import AzureBackupBucketProperties, AzureBackupBucketPropertiesDict
from ..gcp_backup_bucket_properties import GcpBackupBucketProperties, GcpBackupBucketPropertiesDict

Bucket1: TypeAlias = AwsBackupBucketProperties | GcpBackupBucketProperties | AzureBackupBucketProperties
"""Backup bucket where the snapshot is stored."""

Bucket1Dict: TypeAlias = AwsBackupBucketPropertiesDict | GcpBackupBucketPropertiesDict | AzureBackupBucketPropertiesDict
