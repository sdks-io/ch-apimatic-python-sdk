from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ScimUserName(SdkBaseModel):
    formatted: Optional[str] = UNSET
    """The full name, including all middle names, titles, and suffixes."""

    family_name: Optional[str] = Field(default=UNSET, alias="familyName")
    """The family name of the User."""

    given_name: Optional[str] = Field(default=UNSET, alias="givenName")
    """The given name of the User."""

    middle_name: Optional[str] = Field(default=UNSET, alias="middleName")
    """The middle name(s) of the User."""

    honorific_prefix: Optional[str] = Field(default=UNSET, alias="honorificPrefix")
    """The honorific prefix(es) of the User, or title in some cultures."""

    honorific_suffix: Optional[str] = Field(default=UNSET, alias="honorificSuffix")
    """The honorific suffix(es) of the User."""


class ScimUserNameDict(TypedDict):
    formatted: NotRequired[str]
    family_name: NotRequired[str]
    given_name: NotRequired[str]
    middle_name: NotRequired[str]
    honorific_prefix: NotRequired[str]
    honorific_suffix: NotRequired[str]
