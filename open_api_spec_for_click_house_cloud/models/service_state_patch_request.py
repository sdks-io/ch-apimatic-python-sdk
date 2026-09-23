from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.command1 import Command1OrStr


class ServiceStatePatchRequest(SdkBaseModel):
    command: Optional[Command1OrStr] = UNSET
    """Command to change the state: 'start', 'stop', 'awake'."""


class ServiceStatePatchRequestDict(TypedDict):
    command: NotRequired[Command1OrStr]
