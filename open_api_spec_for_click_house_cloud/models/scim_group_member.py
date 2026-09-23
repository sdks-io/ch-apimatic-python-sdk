from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ScimGroupMember(SdkBaseModel):
    value: str
    """The identifier of the member (user ID)."""

    display: Optional[str] = UNSET
    """A human-readable name for the member."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Indicates the type of resource, typically "User"."""


class ScimGroupMemberDict(TypedDict):
    value: str
    display: NotRequired[str]
    type_: NotRequired[str]
