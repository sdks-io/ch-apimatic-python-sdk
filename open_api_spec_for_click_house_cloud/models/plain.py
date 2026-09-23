from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Plain(SdkBaseModel):
    username: Optional[str] = UNSET
    """Database username."""

    password: Optional[str] = UNSET
    """Database password."""


class PlainDict(TypedDict):
    username: NotRequired[str]
    password: NotRequired[str]
