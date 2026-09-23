from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .scim_group_member import ScimGroupMember, ScimGroupMemberDict
from .scim_group_meta import ScimGroupMeta, ScimGroupMetaDict


class ScimGroupPutRequest(SdkBaseModel):
    schemas: list[str]
    """SCIM schema URIs. Must include "urn:ietf:params:scim:schemas:core:2.0:Group"."""

    external_id: Optional[str] = Field(default=UNSET, alias="externalId")
    """Identifier for the resource as defined by the provisioning client."""

    display_name: str = Field(alias="displayName")
    """Human-readable name for the Group. Maps to Role name."""

    members: Optional[list[ScimGroupMember]] = UNSET
    """Members of the Group."""

    id: Optional[str] = UNSET
    """Server-assigned resource ID echoed back by the IdP. Ignored on write."""

    meta: Optional[ScimGroupMeta] = UNSET


class ScimGroupPutRequestDict(TypedDict):
    schemas: list[str]
    external_id: NotRequired[str]
    display_name: str
    members: NotRequired[list[ScimGroupMemberDict]]
    id: NotRequired[str]
    meta: NotRequired[ScimGroupMetaDict]
