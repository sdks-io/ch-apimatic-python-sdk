from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.release_channel import ReleaseChannelOrStr
from .instance_private_endpoints_patch import InstancePrivateEndpointsPatch, InstancePrivateEndpointsPatchDict
from .instance_tags_patch import InstanceTagsPatch, InstanceTagsPatchDict
from .ip_access_list_patch import IpAccessListPatch, IpAccessListPatchDict
from .service_endpoint_change import ServiceEndpointChange, ServiceEndpointChangeDict


class ServicePatchRequest(SdkBaseModel):
    name: Optional[str] = UNSET
    """Name of the service. Alphanumerical string with whitespaces up to 50 characters."""

    ip_access_list: Optional[IpAccessListPatch] = Field(default=UNSET, alias="ipAccessList")
    private_endpoint_ids: Optional[InstancePrivateEndpointsPatch] = Field(default=UNSET, alias="privateEndpointIds")
    release_channel: Optional[ReleaseChannelOrStr] = Field(default=UNSET, alias="releaseChannel")
    """Select fast if you want to get new ClickHouse releases as soon as they are available. You'll get new features
    faster, but with a higher risk of bugs. Select slow if you would like to defer releases to give yourself more time
    to test. This feature is only available for production services. default is the regular release channel."""

    endpoints: Optional[list[ServiceEndpointChange]] = UNSET
    """List of service endpoints to change"""

    transparent_data_encryption_key_id: Optional[str] = Field(default=UNSET, alias="transparentDataEncryptionKeyId")
    """The id of the key to rotate"""

    tags: Optional[InstanceTagsPatch] = UNSET
    enable_core_dumps: Optional[bool] = Field(default=UNSET, alias="enableCoreDumps")
    """If true, the underlying infra is enabled for collecting core dumps."""


class ServicePatchRequestDict(TypedDict):
    name: NotRequired[str]
    ip_access_list: NotRequired[IpAccessListPatchDict]
    private_endpoint_ids: NotRequired[InstancePrivateEndpointsPatchDict]
    release_channel: NotRequired[ReleaseChannelOrStr]
    endpoints: NotRequired[list[ServiceEndpointChangeDict]]
    transparent_data_encryption_key_id: NotRequired[str]
    tags: NotRequired[InstanceTagsPatchDict]
    enable_core_dumps: NotRequired[bool]
