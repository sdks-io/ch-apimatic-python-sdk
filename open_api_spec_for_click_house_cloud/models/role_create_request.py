from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .rbacpolicy_create_request import RbacpolicyCreateRequest, RbacpolicyCreateRequestDict


class RoleCreateRequest(SdkBaseModel):
    name: str
    """Name of the role"""

    actors: list[str]
    """List of actor resource IDs to assign to this role (e.g., ["user/uuid", "apiKey/uuid"])"""

    policies: list[RbacpolicyCreateRequest]
    """List of policies to create for this role"""


class RoleCreateRequestDict(TypedDict):
    name: str
    actors: list[str]
    policies: list[RbacpolicyCreateRequestDict]
