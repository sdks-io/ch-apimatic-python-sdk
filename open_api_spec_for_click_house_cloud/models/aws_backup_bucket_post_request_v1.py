from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.bucket_provider import BucketProviderOrStr


class AwsBackupBucketPostRequestV1(SdkBaseModel):
    bucket_provider: Optional[BucketProviderOrStr] = Field(default=UNSET, alias="bucketProvider")
    """Bucket provider"""

    bucket_path: Optional[str] = Field(default=UNSET, alias="bucketPath")
    """Bucket path"""

    iam_role_arn: Optional[str] = Field(default=UNSET, alias="iamRoleArn")
    """AWS Role ARN"""

    iam_role_session_name: Optional[str] = Field(default=UNSET, alias="iamRoleSessionName")
    """AWS Role session name"""


class AwsBackupBucketPostRequestV1Dict(TypedDict):
    bucket_provider: NotRequired[BucketProviderOrStr]
    bucket_path: NotRequired[str]
    iam_role_arn: NotRequired[str]
    iam_role_session_name: NotRequired[str]
