from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.bucket_provider1 import BucketProvider1OrStr


class GcpBackupBucket(SdkBaseModel):
    id: Optional[UUID] = UNSET
    """Unique backup bucket ID"""

    bucket_provider: Optional[BucketProvider1OrStr] = Field(default=UNSET, alias="bucketProvider")
    """Bucket provider"""

    bucket_path: Optional[str] = Field(default=UNSET, alias="bucketPath")
    """Bucket path"""

    access_key_id: Optional[str] = Field(default=UNSET, alias="accessKeyId")
    """Access Key ID (HMAC key)"""


class GcpBackupBucketDict(TypedDict):
    id: NotRequired[UUID]
    bucket_provider: NotRequired[BucketProvider1OrStr]
    bucket_path: NotRequired[str]
    access_key_id: NotRequired[str]
