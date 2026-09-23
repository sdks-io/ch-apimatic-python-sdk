from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ServiceClickhouseSettingWarning(SdkBaseModel):
    name: Optional[str] = UNSET
    """Name of the setting the warning applies to."""

    message: Optional[str] = UNSET
    """Warning message."""


class ServiceClickhouseSettingWarningDict(TypedDict):
    name: NotRequired[str]
    message: NotRequired[str]
