from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ScimEnterpriseManager(SdkBaseModel):
    value: Optional[str] = UNSET
    """The id of the SCIM resource representing the user's manager."""

    display_name: Optional[str] = Field(default=UNSET, alias="displayName")
    """The displayName of the user's manager."""


class ScimEnterpriseManagerDict(TypedDict):
    value: NotRequired[str]
    display_name: NotRequired[str]
