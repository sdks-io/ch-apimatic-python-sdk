from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.command import CommandOrStr


class PostgresServiceSetState(SdkBaseModel):
    command: Optional[CommandOrStr] = UNSET
    """Postgres status, which initiates a process."""


class PostgresServiceSetStateDict(TypedDict):
    command: NotRequired[CommandOrStr]
