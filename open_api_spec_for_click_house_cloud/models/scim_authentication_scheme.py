from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ScimAuthenticationScheme(SdkBaseModel):
    type_: str = Field(alias="type")
    """The authentication scheme type (e.g., "httpbasic", "oauthbearertoken")."""

    name: str
    """The common authentication scheme name."""

    description: str
    """A description of the authentication scheme."""

    spec_uri: Optional[str] = Field(default=UNSET, alias="specUri")
    """An HTTP-addressable URL pointing to the scheme specification."""

    primary: Optional[bool] = UNSET
    """A Boolean value indicating the primary authentication scheme."""


class ScimAuthenticationSchemeDict(TypedDict):
    type_: str
    name: str
    description: str
    spec_uri: NotRequired[str]
    primary: NotRequired[bool]
