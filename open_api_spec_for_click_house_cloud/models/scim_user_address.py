from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ScimUserAddress(SdkBaseModel):
    formatted: Optional[str] = UNSET
    """The full mailing address, formatted for display or use with a mailing label."""

    street_address: Optional[str] = Field(default=UNSET, alias="streetAddress")
    """The full street address component."""

    locality: Optional[str] = UNSET
    """The city or locality component."""

    region: Optional[str] = UNSET
    """The state or region component."""

    postal_code: Optional[str] = Field(default=UNSET, alias="postalCode")
    """The zip code or postal code component."""

    country: Optional[str] = UNSET
    """The country name component."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Type of address (e.g., "work", "home", "other")."""

    primary: Optional[bool] = UNSET
    """A Boolean value indicating the preferred mailing address."""


class ScimUserAddressDict(TypedDict):
    formatted: NotRequired[str]
    street_address: NotRequired[str]
    locality: NotRequired[str]
    region: NotRequired[str]
    postal_code: NotRequired[str]
    country: NotRequired[str]
    type_: NotRequired[str]
    primary: NotRequired[bool]
