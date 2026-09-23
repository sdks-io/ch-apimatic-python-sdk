from __future__ import annotations

from pydantic import EmailStr, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.role8 import Role8OrStr


class InvitationPostRequest(SdkBaseModel):
    email: Optional[EmailStr] = UNSET
    """Email of the invited user. Only a user with this email can join using the invitation. The email is stored in a
    lowercase form."""

    role: Optional[Role8OrStr] = UNSET
    """DEPRECATED. Use ``assignedRoleIds`` instead. Role to assign to the invited user in the organization."""

    assigned_role_ids: Optional[list[str]] = Field(default=UNSET, alias="assignedRoleIds")
    """List of role IDs to assign to the invited user when they accept the invitation"""


class InvitationPostRequestDict(TypedDict):
    email: NotRequired[EmailStr]
    role: NotRequired[Role8OrStr]
    assigned_role_ids: NotRequired[list[str]]
