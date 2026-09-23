from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ScimUserPhoneNumber(SdkBaseModel):
    value: Optional[str] = UNSET
    """Phone number value."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Type of phone number (e.g., "work", "home", "mobile")."""

    primary: Optional[bool] = UNSET
    """A Boolean value indicating the preferred phone number."""


class ScimUserPhoneNumberDict(TypedDict):
    value: NotRequired[str]
    type_: NotRequired[str]
    primary: NotRequired[bool]
