from __future__ import annotations

from pydantic import EmailStr, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .assigned_role import AssignedRole, AssignedRoleDict
from .enums.role1 import Role1OrStr


class Member(SdkBaseModel):
    user_id: Optional[str] = Field(default=UNSET, alias="userId")
    """Unique user ID. If a user is a member in multiple organizations this ID will stay the same."""

    name: Optional[str] = UNSET
    """Name of the member as set a personal user profile."""

    email: Optional[EmailStr] = UNSET
    """Email of the member as set in personal user profile."""

    role: Optional[Role1OrStr] = UNSET
    """DEPRECATED. Use ``assignedRoles`` instead. Role of the member in the organization. For organizations that have
    migrated to custom roles, this field is frozen at the pre-migration value and does not reflect current role
    assignments."""

    joined_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="joinedAt")
    """Timestamp the member joined the organization. ISO-8601."""

    assigned_roles: Optional[list[AssignedRole]] = Field(default=UNSET, alias="assignedRoles")
    """Custom roles and System roles assigned to this member"""


class MemberDict(TypedDict):
    user_id: NotRequired[str]
    name: NotRequired[str]
    email: NotRequired[EmailStr]
    role: NotRequired[Role1OrStr]
    joined_at: NotRequired[RFC3339DateTime]
    assigned_roles: NotRequired[list[AssignedRoleDict]]
