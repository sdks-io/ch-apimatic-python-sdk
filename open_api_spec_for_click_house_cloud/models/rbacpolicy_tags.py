from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.role_v2 import RoleV2OrStr


class RbacpolicyTags(SdkBaseModel):
    grants: Optional[list[str]] = UNSET
    """Optional list of database grants (e.g., database names)"""

    role_v2: Optional[RoleV2OrStr] = Field(default=UNSET, alias="roleV2")
    """Optional SQL console role type"""


class RbacpolicyTagsDict(TypedDict):
    grants: NotRequired[list[str]]
    role_v2: NotRequired[RoleV2OrStr]
