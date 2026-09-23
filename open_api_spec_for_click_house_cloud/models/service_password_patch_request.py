from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ServicePasswordPatchRequest(SdkBaseModel):
    new_password_hash: Optional[str] = Field(default=UNSET, alias="newPasswordHash")
    """Optional password hash. Used to avoid password transmission over network. If not provided a new password is
    generated and is provided in the response. Otherwise this hash is used. Algorithm: echo -n "yourpassword" |
    sha256sum | tr -d '-' | xxd -r -p | base64"""

    new_double_sha1_hash: Optional[str] = Field(default=UNSET, alias="newDoubleSha1Hash")
    """Optional double SHA1 password hash for MySQL protocol. If newPasswordHash is not provided this key will be
    ignored and the generated password will be used. Algorithm: echo -n "yourpassword" | sha1sum | tr -d '-' | xxd -r -p
    | sha1sum | tr -d '-'"""


class ServicePasswordPatchRequestDict(TypedDict):
    new_password_hash: NotRequired[str]
    new_double_sha1_hash: NotRequired[str]
