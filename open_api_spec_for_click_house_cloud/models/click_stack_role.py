from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .click_stack_caslpermission import ClickStackCaslpermission, ClickStackCaslpermissionDict


class ClickStackRole(SdkBaseModel):
    id: str
    """Role ID."""

    name: str
    """Role name."""

    description: Optional[str] = UNSET
    """Human-readable role description."""

    permissions: list[ClickStackCaslpermission]
    """The CASL permissions granted by this role."""

    is_predefined: bool = Field(alias="isPredefined")
    """Whether this is an immutable predefined/system role."""

    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    """Creation timestamp."""

    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")
    """Last update timestamp."""


class ClickStackRoleDict(TypedDict):
    id: str
    name: str
    description: NotRequired[str]
    permissions: list[ClickStackCaslpermissionDict]
    is_predefined: bool
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
