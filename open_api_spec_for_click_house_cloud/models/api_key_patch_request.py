from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .enums.role3 import Role3OrStr
from .enums.state4 import State4OrStr
from .ip_access_list_entry import IpAccessListEntry, IpAccessListEntryDict


class ApiKeyPatchRequest(SdkBaseModel):
    name: Optional[str] = UNSET
    """Name of the key"""

    roles: Optional[list[Role3OrStr]] = UNSET
    """DEPRECATED. Use ``assignedRoleIds`` instead. List of roles assigned to the key."""

    assigned_role_ids: Optional[list[UUID]] = Field(default=UNSET, alias="assignedRoleIds")
    """Array of role UUIDs to assign to the API key"""

    expire_at: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="expireAt")
    """Timestamp the key expires. If ``null`` or is empty the key never expires. ISO-8601."""

    state: Optional[State4OrStr] = UNSET
    """State of the key: 'enabled', 'disabled'."""

    ip_access_list: Optional[list[IpAccessListEntry]] = Field(default=UNSET, alias="ipAccessList")
    """List of IP addresses allowed to access the API using this key"""


class ApiKeyPatchRequestDict(TypedDict):
    name: NotRequired[str]
    roles: NotRequired[list[Role3OrStr]]
    assigned_role_ids: NotRequired[list[UUID]]
    expire_at: NotRequired[RFC3339DateTime | None]
    state: NotRequired[State4OrStr]
    ip_access_list: NotRequired[list[IpAccessListEntryDict]]
