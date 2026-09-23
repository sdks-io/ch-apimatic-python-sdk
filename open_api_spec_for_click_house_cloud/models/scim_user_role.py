from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ScimUserRole(SdkBaseModel):
    value: Optional[str] = UNSET
    """The value of a role; a string or label representing a collection of entitlements. No canonical types."""

    display: Optional[str] = UNSET
    """A human-readable name, primarily used for display purposes."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """A label indicating the attribute's function."""

    primary: Optional[bool] = UNSET
    """A Boolean value indicating the primary or preferred role."""


class ScimUserRoleDict(TypedDict):
    value: NotRequired[str]
    display: NotRequired[str]
    type_: NotRequired[str]
    primary: NotRequired[bool]
