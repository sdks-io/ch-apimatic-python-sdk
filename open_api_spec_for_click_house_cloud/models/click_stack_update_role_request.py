from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .click_stack_caslpermission import ClickStackCaslpermission, ClickStackCaslpermissionDict


class ClickStackUpdateRoleRequest(SdkBaseModel):
    name: Optional[str] = UNSET
    """New role name. Omit to leave the name unchanged."""

    description: Optional[str] = UNSET
    """New role description."""

    permissions: list[ClickStackCaslpermission]
    """The replacement set of CASL permissions for the role."""


class ClickStackUpdateRoleRequestDict(TypedDict):
    name: NotRequired[str]
    description: NotRequired[str]
    permissions: list[ClickStackCaslpermissionDict]
