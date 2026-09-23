from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class InstancePrivateEndpointsPatch(SdkBaseModel):
    add: Optional[list[str]] = UNSET
    """Elements to add. Executed after "remove" part is processed."""

    remove: Optional[list[str]] = UNSET
    """Elements to remove. Executed before "add" part is processed."""


class InstancePrivateEndpointsPatchDict(TypedDict):
    add: NotRequired[list[str]]
    remove: NotRequired[list[str]]
