from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.bucket_provider2 import BucketProvider2OrStr


class AzureBackupBucketProperties(SdkBaseModel):
    bucket_provider: Optional[BucketProvider2OrStr] = Field(default=UNSET, alias="bucketProvider")
    """Bucket provider"""

    container_name: Optional[str] = Field(default=UNSET, alias="containerName")
    """Container Name"""


class AzureBackupBucketPropertiesDict(TypedDict):
    bucket_provider: NotRequired[BucketProvider2OrStr]
    container_name: NotRequired[str]
