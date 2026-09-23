from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.type import TypeOrStr
from .rbacpolicy import Rbacpolicy, RbacpolicyDict


class Rbacrole(SdkBaseModel):
    id: Optional[str] = UNSET
    """Unique role identifier"""

    tenant_id: Optional[str] = Field(default=UNSET, alias="tenantId")
    """Tenant resource ID (e.g., organization/uuid)"""

    owner_id: Optional[str] = Field(default=UNSET, alias="ownerId")
    """Owner resource ID (e.g., organization/uuid)"""

    name: Optional[str] = UNSET
    """Name of the role"""

    type_: Optional[TypeOrStr] = Field(default=UNSET, alias="type")
    """Whether this is a system role or a custom role"""

    actors: Optional[list[str]] = UNSET
    """List of actor resource IDs assigned to this role (e.g., user/uuid, apiKey/uuid)"""

    policies: Optional[list[Rbacpolicy]] = UNSET
    """List of policies associated with this role"""

    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    """Timestamp when the role was created. ISO-8601."""

    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")
    """Timestamp when the role was last updated. ISO-8601."""


class RbacroleDict(TypedDict):
    id: NotRequired[str]
    tenant_id: NotRequired[str]
    owner_id: NotRequired[str]
    name: NotRequired[str]
    type_: NotRequired[TypeOrStr]
    actors: NotRequired[list[str]]
    policies: NotRequired[list[RbacpolicyDict]]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
