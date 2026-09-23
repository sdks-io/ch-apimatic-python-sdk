from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.allow_deny import AllowDenyOrStr
from .rbacpolicy_tags import RbacpolicyTags, RbacpolicyTagsDict


class RbacpolicyCreateRequest(SdkBaseModel):
    allow_deny: AllowDenyOrStr = Field(alias="allowDeny")
    """Whether this policy allows or denies access"""

    permissions: list[str]
    """List of permissions to grant or deny (e.g., ["control-plane:organization:view"])"""

    resources: list[str]
    """List of resource IDs this policy applies to (e.g., ["instance/uuid", "instance/*"])"""

    tags: Optional[RbacpolicyTags] = UNSET


class RbacpolicyCreateRequestDict(TypedDict):
    allow_deny: AllowDenyOrStr
    permissions: list[str]
    resources: list[str]
    tags: NotRequired[RbacpolicyTagsDict]
