from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.bucket_provider2 import BucketProvider2OrStr


class AzureBackupBucket(SdkBaseModel):
    id: Optional[UUID] = UNSET
    """Unique backup bucket ID."""

    bucket_provider: Optional[BucketProvider2OrStr] = Field(default=UNSET, alias="bucketProvider")
    """Bucket provider"""

    container_name: Optional[str] = Field(default=UNSET, alias="containerName")
    """Container Name"""


class AzureBackupBucketDict(TypedDict):
    id: NotRequired[UUID]
    bucket_provider: NotRequired[BucketProvider2OrStr]
    container_name: NotRequired[str]
