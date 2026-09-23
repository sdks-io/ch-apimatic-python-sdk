from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ServiceClickhouseSettingSchemaEntry(SdkBaseModel):
    name: Optional[str] = UNSET
    """Name of the setting."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """Data type of the setting value."""

    description: Optional[str] = UNSET
    """Description of the setting."""

    enum: Optional[list[int]] = UNSET
    """List of allowed values, if the setting is an enum."""

    warning: Optional[str] = UNSET
    """Warning message about potential disruptive effects of changing this setting."""

    deprecation_notice: Optional[str] = Field(default=UNSET, alias="deprecationNotice")
    """Deprecation notice, if applicable."""

    example: Optional[str] = UNSET
    """Example value for the setting."""


class ServiceClickhouseSettingSchemaEntryDict(TypedDict):
    name: NotRequired[str]
    type_: NotRequired[str]
    description: NotRequired[str]
    enum: NotRequired[list[int]]
    warning: NotRequired[str]
    deprecation_notice: NotRequired[str]
    example: NotRequired[str]
