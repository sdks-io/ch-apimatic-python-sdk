from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.allow_deny import AllowDenyOrStr
from .rbacpolicy_tags import RbacpolicyTags, RbacpolicyTagsDict


class Rbacpolicy(SdkBaseModel):
    id: Optional[str] = UNSET
    """Unique policy identifier"""

    role_id: Optional[str] = Field(default=UNSET, alias="roleId")
    """ID of the role this policy belongs to"""

    tenant_id: Optional[str] = Field(default=UNSET, alias="tenantId")
    """Tenant resource ID (e.g., organization/uuid)"""

    allow_deny: Optional[AllowDenyOrStr] = Field(default=UNSET, alias="allowDeny")
    """Whether this policy allows or denies access"""

    permissions: Optional[list[str]] = UNSET
    """List of permissions granted or denied by this policy"""

    resources: Optional[list[str]] = UNSET
    """List of resource IDs this policy applies to (e.g., instance/uuid, instance/*)"""

    tags: Optional[RbacpolicyTags] = UNSET


class RbacpolicyDict(TypedDict):
    id: NotRequired[str]
    role_id: NotRequired[str]
    tenant_id: NotRequired[str]
    allow_deny: NotRequired[AllowDenyOrStr]
    permissions: NotRequired[list[str]]
    resources: NotRequired[list[str]]
    tags: NotRequired[RbacpolicyTagsDict]
