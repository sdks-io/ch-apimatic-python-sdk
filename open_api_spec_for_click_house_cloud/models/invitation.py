from __future__ import annotations

from uuid import UUID

from pydantic import EmailStr, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .assigned_role import AssignedRole, AssignedRoleDict
from .enums.role2 import Role2OrStr


class Invitation(SdkBaseModel):
    role: Optional[Role2OrStr] = UNSET
    """DEPRECATED. Use ``assignedRoles`` instead. Role of the invited user in the organization. For organizations that
    have migrated to custom roles, this field is frozen at the pre-migration value and does not reflect the role
    assignment that will be applied."""

    id: Optional[UUID] = UNSET
    """Unique invitation ID."""

    email: Optional[EmailStr] = UNSET
    """Email of the invited user. Only a user with this email can join using the invitation. The email is stored in a
    lowercase form."""

    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    """Invitation creation timestamp. ISO-8601."""

    expire_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="expireAt")
    """Timestamp the invitation expires. ISO-8601."""

    assigned_roles: Optional[list[AssignedRole]] = Field(default=UNSET, alias="assignedRoles")
    """Custom roles and System roles that will be assigned to the user when they accept the invitation"""


class InvitationDict(TypedDict):
    role: NotRequired[Role2OrStr]
    id: NotRequired[UUID]
    email: NotRequired[EmailStr]
    created_at: NotRequired[RFC3339DateTime]
    expire_at: NotRequired[RFC3339DateTime]
    assigned_roles: NotRequired[list[AssignedRoleDict]]
