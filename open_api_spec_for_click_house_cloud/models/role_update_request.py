from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .rbacpolicy_create_request import RbacpolicyCreateRequest, RbacpolicyCreateRequestDict


class RoleUpdateRequest(SdkBaseModel):
    name: Optional[str] = UNSET
    """New name for the role"""

    actors: Optional[list[str]] = UNSET
    """New list of actor resource IDs (replaces existing actors)"""

    policies: Optional[list[RbacpolicyCreateRequest]] = UNSET
    """New list of policies (replaces existing policies)"""


class RoleUpdateRequestDict(TypedDict):
    name: NotRequired[str]
    actors: NotRequired[list[str]]
    policies: NotRequired[list[RbacpolicyCreateRequestDict]]
