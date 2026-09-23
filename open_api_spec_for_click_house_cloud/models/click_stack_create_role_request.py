from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_stack_caslpermission import ClickStackCaslpermission, ClickStackCaslpermissionDict


class ClickStackCreateRoleRequest(SdkBaseModel):
    name: str
    """Role name. Must be unique within the team and not collide with a predefined role."""

    description: Optional[str] = UNSET
    """Human-readable role description."""

    permissions: list[ClickStackCaslpermission]
    """The CASL permissions to grant to the role."""


class ClickStackCreateRoleRequestDict(TypedDict):
    name: str
    description: NotRequired[str]
    permissions: list[ClickStackCaslpermissionDict]
