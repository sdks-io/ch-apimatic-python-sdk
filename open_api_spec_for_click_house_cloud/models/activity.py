from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.actor_type import ActorTypeOrStr
from .enums.key_update_type import KeyUpdateTypeOrStr
from .enums.type12 import Type12OrStr


class Activity(SdkBaseModel):
    id: Optional[str] = UNSET
    """Unique activity ID."""

    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    """Timestamp of the activity. ISO-8601."""

    type_: Optional[Type12OrStr] = Field(default=UNSET, alias="type")
    """Type of the activity."""

    actor_type: Optional[ActorTypeOrStr] = Field(default=UNSET, alias="actorType")
    """Type of the actor: 'user', 'support', 'system', 'api'."""

    actor_id: Optional[str] = Field(default=UNSET, alias="actorId")
    """Unique actor ID."""

    actor_details: Optional[str] = Field(default=UNSET, alias="actorDetails")
    """Additional information about the actor."""

    actor_ip_address: Optional[str] = Field(default=UNSET, alias="actorIpAddress")
    """IP address of the actor. Defined for 'user' and 'api' actor types."""

    organization_id: Optional[str] = Field(default=UNSET, alias="organizationId")
    """Scope of the activity: organization ID this activity is related to."""

    service_id: Optional[str] = Field(default=UNSET, alias="serviceId")
    """Scope of the activity: service ID this activity is related to."""

    user_agent: Optional[str] = Field(default=UNSET, alias="userAgent")
    """User agent of the actor"""

    target_key_id: Optional[str] = Field(default=UNSET, alias="targetKeyId")
    """For 'openapi_key_update' activities: the ID of the API key that was updated."""

    key_update_type: Optional[KeyUpdateTypeOrStr] = Field(default=UNSET, alias="keyUpdateType")
    """For 'openapi_key_update' activities: the type of update that was performed."""

    target_role_ids: Optional[list[str]] = Field(default=UNSET, alias="targetRoleIds")
    """For role and actor-role activities: IDs of the affected roles."""

    target_role_names: Optional[list[str]] = Field(default=UNSET, alias="targetRoleNames")
    """For role and actor-role activities: names of the affected roles, when recorded."""

    target_actor_ids: Optional[list[str]] = Field(default=UNSET, alias="targetActorIds")
    """For 'organization_member_update_roles' and 'organization_member_remove_roles' activities: IDs of the affected
    actors (e.g. 'user/<id>')."""

    target_resource_ids: Optional[list[str]] = Field(default=UNSET, alias="targetResourceIds")
    """For 'role_resources_delete' activities: IDs of the deleted resources the roles referenced."""


class ActivityDict(TypedDict):
    id: NotRequired[str]
    created_at: NotRequired[RFC3339DateTime]
    type_: NotRequired[Type12OrStr]
    actor_type: NotRequired[ActorTypeOrStr]
    actor_id: NotRequired[str]
    actor_details: NotRequired[str]
    actor_ip_address: NotRequired[str]
    organization_id: NotRequired[str]
    service_id: NotRequired[str]
    user_agent: NotRequired[str]
    target_key_id: NotRequired[str]
    key_update_type: NotRequired[KeyUpdateTypeOrStr]
    target_role_ids: NotRequired[list[str]]
    target_role_names: NotRequired[list[str]]
    target_actor_ids: NotRequired[list[str]]
    target_resource_ids: NotRequired[list[str]]
