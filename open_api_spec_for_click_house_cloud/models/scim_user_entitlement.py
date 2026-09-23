from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ScimUserEntitlement(SdkBaseModel):
    value: Optional[str] = UNSET
    """The value of an entitlement."""

    display: Optional[str] = UNSET
    """A human-readable name for the entitlement."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """A label indicating the attribute's function."""

    primary: Optional[bool] = UNSET
    """A Boolean value indicating the primary entitlement."""


class ScimUserEntitlementDict(TypedDict):
    value: NotRequired[str]
    display: NotRequired[str]
    type_: NotRequired[str]
    primary: NotRequired[bool]
