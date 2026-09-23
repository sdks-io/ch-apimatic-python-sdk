from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .assigned_role import AssignedRole, AssignedRoleDict
from .enums.role3 import Role3OrStr
from .enums.state4 import State4OrStr
from .ip_access_list_entry import IpAccessListEntry, IpAccessListEntryDict


class ApiKey(SdkBaseModel):
    id: Optional[UUID] = UNSET
    """Unique API key ID."""

    name: Optional[str] = UNSET
    """Name of the key"""

    state: Optional[State4OrStr] = UNSET
    """State of the key: 'enabled', 'disabled'."""

    roles: Optional[list[Role3OrStr]] = UNSET
    """DEPRECATED. Use ``assignedRoles`` instead. List of roles assigned to the key. For organizations that have
    migrated to custom roles, this field is frozen at the pre-migration value and does not reflect current role
    assignments."""

    assigned_roles: Optional[list[AssignedRole]] = Field(default=UNSET, alias="assignedRoles")
    """Custom roles and System roles assigned to this API key"""

    key_suffix: Optional[str] = Field(default=UNSET, alias="keySuffix")
    """Last 4 letters of the key."""

    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    """Timestamp the key was created. ISO-8601."""

    expire_at: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="expireAt")
    """Timestamp the key expires. If not present, ``null`` or is empty the key never expires. ISO-8601."""

    used_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="usedAt")
    """Timestamp the key was used last time, with one-minute precision. If not present the key was never used.
    ISO-8601."""

    ip_access_list: Optional[list[IpAccessListEntry]] = Field(default=UNSET, alias="ipAccessList")
    """List of IP addresses allowed to access the API using this key"""


class ApiKeyDict(TypedDict):
    id: NotRequired[UUID]
    name: NotRequired[str]
    state: NotRequired[State4OrStr]
    roles: NotRequired[list[Role3OrStr]]
    assigned_roles: NotRequired[list[AssignedRoleDict]]
    key_suffix: NotRequired[str]
    created_at: NotRequired[RFC3339DateTime]
    expire_at: NotRequired[RFC3339DateTime | None]
    used_at: NotRequired[RFC3339DateTime]
    ip_access_list: NotRequired[list[IpAccessListEntryDict]]
