from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.op import OpOrStr


class ScimPatchOperation(SdkBaseModel):
    op: OpOrStr
    """The operation to perform."""

    path: Optional[str] = UNSET
    """Target attribute path (e.g. "active", "userName")."""

    value: Optional[str] = UNSET
    """New value for the attribute."""


class ScimPatchOperationDict(TypedDict):
    op: OpOrStr
    path: NotRequired[str]
    value: NotRequired[str]
