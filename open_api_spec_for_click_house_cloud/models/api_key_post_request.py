from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, RFC3339DateTime, SdkBaseModel
from .api_key_hash_data import ApiKeyHashData, ApiKeyHashDataDict
from .enums.role3 import Role3OrStr
from .enums.state6 import State6OrStr
from .ip_access_list_entry import IpAccessListEntry, IpAccessListEntryDict


class ApiKeyPostRequest(SdkBaseModel):
    name: Optional[str] = UNSET
    """Name of the key."""

    expire_at: OptionalNullable[RFC3339DateTime] = Field(default=UNSET, alias="expireAt")
    """Timestamp the key expires. If not present, ``null`` or is empty the key never expires. ISO-8601."""

    state: Optional[State6OrStr] = UNSET
    """Initial state of the key: 'enabled', 'disabled'. If not provided the new key will be 'enabled'."""

    hash_data: Optional[ApiKeyHashData] = Field(default=UNSET, alias="hashData")
    roles: Optional[list[Role3OrStr]] = UNSET
    """DEPRECATED. Use ``assignedRoleIds`` instead. List of roles assigned to the key. Contains at least 1 element."""

    assigned_role_ids: Optional[list[UUID]] = Field(default=UNSET, alias="assignedRoleIds")
    """Array of role UUIDs to assign to the API key"""

    ip_access_list: Optional[list[IpAccessListEntry]] = Field(default=UNSET, alias="ipAccessList")
    """List of IP addresses allowed to access the API using this key"""


class ApiKeyPostRequestDict(TypedDict):
    name: NotRequired[str]
    expire_at: NotRequired[RFC3339DateTime | None]
    state: NotRequired[State6OrStr]
    hash_data: NotRequired[ApiKeyHashDataDict]
    roles: NotRequired[list[Role3OrStr]]
    assigned_role_ids: NotRequired[list[UUID]]
    ip_access_list: NotRequired[list[IpAccessListEntryDict]]
