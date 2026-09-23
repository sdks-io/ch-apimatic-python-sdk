from __future__ import annotations

from pydantic import EmailStr, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ScimUserEmail(SdkBaseModel):
    value: EmailStr
    """Email address value."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Type of email (e.g., "work", "home")."""

    primary: Optional[bool] = UNSET
    """A Boolean value indicating the primary email address."""


class ScimUserEmailDict(TypedDict):
    value: EmailStr
    type_: NotRequired[str]
    primary: NotRequired[bool]
