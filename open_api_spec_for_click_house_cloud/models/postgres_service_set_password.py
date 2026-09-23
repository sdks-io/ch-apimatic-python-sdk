from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PostgresServiceSetPassword(SdkBaseModel):
    password: Optional[str] = UNSET
    """Optional password. If not provided a new password is generated and provided in the response. Must contain:

    * At least one lowercase letter
    * At least one uppercase letter
    * At least one digit"""


class PostgresServiceSetPasswordDict(TypedDict):
    password: NotRequired[str]
