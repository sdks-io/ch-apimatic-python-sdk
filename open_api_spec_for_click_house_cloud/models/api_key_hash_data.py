from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ApiKeyHashData(SdkBaseModel):
    key_id_hash: Optional[str] = Field(default=UNSET, alias="keyIdHash")
    """Hash of the key ID."""

    key_id_suffix: Optional[str] = Field(default=UNSET, alias="keyIdSuffix")
    """Last 4 digits of the key ID. Algorithm: echo -n "yourpassword" | sha256sum | tr -d '-' | xxd -r -p | base64"""

    key_secret_hash: Optional[str] = Field(default=UNSET, alias="keySecretHash")
    """Hash of the key secret. Algorithm: echo -n "yourpassword" | sha256sum | tr -d '-' | xxd -r -p | base64"""


class ApiKeyHashDataDict(TypedDict):
    key_id_hash: NotRequired[str]
    key_id_suffix: NotRequired[str]
    key_secret_hash: NotRequired[str]
