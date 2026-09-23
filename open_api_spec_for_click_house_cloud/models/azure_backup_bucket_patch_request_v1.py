from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.bucket_provider2 import BucketProvider2OrStr


class AzureBackupBucketPatchRequestV1(SdkBaseModel):
    bucket_provider: Optional[BucketProvider2OrStr] = Field(default=UNSET, alias="bucketProvider")
    """Bucket provider"""

    container_name: Optional[str] = Field(default=UNSET, alias="containerName")
    """Container Name"""

    connection_string: Optional[str] = Field(default=UNSET, alias="connectionString")
    """Connection String"""


class AzureBackupBucketPatchRequestV1Dict(TypedDict):
    bucket_provider: NotRequired[BucketProvider2OrStr]
    container_name: NotRequired[str]
    connection_string: NotRequired[str]
