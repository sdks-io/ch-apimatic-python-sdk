from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.bucket_provider1 import BucketProvider1OrStr


class GcpBackupBucketPostRequestV1(SdkBaseModel):
    bucket_provider: Optional[BucketProvider1OrStr] = Field(default=UNSET, alias="bucketProvider")
    """Bucket provider"""

    bucket_path: Optional[str] = Field(default=UNSET, alias="bucketPath")
    """Bucket path"""

    access_key_id: Optional[str] = Field(default=UNSET, alias="accessKeyId")
    """Access Key ID (HMAC key)"""

    secret_access_key: Optional[str] = Field(default=UNSET, alias="secretAccessKey")
    """Secret Access Key (HMAC secret key)"""


class GcpBackupBucketPostRequestV1Dict(TypedDict):
    bucket_provider: NotRequired[BucketProvider1OrStr]
    bucket_path: NotRequired[str]
    access_key_id: NotRequired[str]
    secret_access_key: NotRequired[str]
