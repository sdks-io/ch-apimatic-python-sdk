from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MskIamUser(SdkBaseModel):
    access_key_id: Optional[str] = Field(default=UNSET, alias="accessKeyId")
    """IAM access key ID."""

    secret_key: Optional[str] = Field(default=UNSET, alias="secretKey")
    """IAM secret key."""


class MskIamUserDict(TypedDict):
    access_key_id: NotRequired[str]
    secret_key: NotRequired[str]
