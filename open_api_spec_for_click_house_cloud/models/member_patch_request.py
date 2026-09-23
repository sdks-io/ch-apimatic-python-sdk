from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.role7 import Role7OrStr


class MemberPatchRequest(SdkBaseModel):
    role: Optional[Role7OrStr] = UNSET
    """DEPRECATED. Use ``assignedRoleIds`` instead. Role of the member in the organization."""

    assigned_role_ids: Optional[list[str]] = Field(default=UNSET, alias="assignedRoleIds")
    """List of role IDs to assign to the member"""


class MemberPatchRequestDict(TypedDict):
    role: NotRequired[Role7OrStr]
    assigned_role_ids: NotRequired[list[str]]
