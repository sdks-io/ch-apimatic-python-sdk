from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ScimUserGroup(SdkBaseModel):
    value: Optional[str] = UNSET
    """The identifier of the group."""

    display: Optional[str] = UNSET
    """A human-readable name for the group."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """A label indicating the attribute's function (e.g., "direct" or "indirect")."""


class ScimUserGroupDict(TypedDict):
    value: NotRequired[str]
    display: NotRequired[str]
    type_: NotRequired[str]
