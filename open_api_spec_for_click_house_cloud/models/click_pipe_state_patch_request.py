from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.command2 import Command2OrStr


class ClickPipeStatePatchRequest(SdkBaseModel):
    command: Optional[Command2OrStr] = UNSET
    """Command to change the state: 'start', 'stop', 'resync'."""


class ClickPipeStatePatchRequestDict(TypedDict):
    command: NotRequired[Command2OrStr]
