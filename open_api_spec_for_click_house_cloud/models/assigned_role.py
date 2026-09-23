from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.role_type import RoleTypeOrStr


class AssignedRole(SdkBaseModel):
    role_id: Optional[UUID] = Field(default=UNSET, alias="roleId")
    """Unique identifier of the role"""

    role_name: Optional[str] = Field(default=UNSET, alias="roleName")
    """Human-readable name of the role"""

    role_type: Optional[RoleTypeOrStr] = Field(default=UNSET, alias="roleType")
    """Type of role: system (predefined) or custom (organization-defined)"""


class AssignedRoleDict(TypedDict):
    role_id: NotRequired[UUID]
    role_name: NotRequired[str]
    role_type: NotRequired[RoleTypeOrStr]
