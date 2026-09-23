from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ScimUserIm(SdkBaseModel):
    value: Optional[str] = UNSET
    """Instant messaging address."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Type of IM address (e.g., "aim", "gtalk", "icq", "xmpp", "msn", "skype", "qq")."""

    primary: Optional[bool] = UNSET
    """A Boolean value indicating the preferred IM address."""


class ScimUserImDict(TypedDict):
    value: NotRequired[str]
    type_: NotRequired[str]
    primary: NotRequired[bool]
