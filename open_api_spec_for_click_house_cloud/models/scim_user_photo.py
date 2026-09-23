from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ScimUserPhoto(SdkBaseModel):
    value: Optional[str] = UNSET
    """URL of a photo of the User."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Type of photo (e.g., "photo", "thumbnail")."""

    primary: Optional[bool] = UNSET
    """A Boolean value indicating the preferred photo."""


class ScimUserPhotoDict(TypedDict):
    value: NotRequired[str]
    type_: NotRequired[str]
    primary: NotRequired[bool]
