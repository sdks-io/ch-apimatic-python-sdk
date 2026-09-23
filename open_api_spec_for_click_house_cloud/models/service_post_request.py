from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.autoscaling_mode4 import AutoscalingMode4OrStr
from .enums.compliance_type import ComplianceTypeOrStr
from .enums.provider import ProviderOrStr
from .enums.region import RegionOrStr
from .enums.release_channel import ReleaseChannelOrStr
from .enums.tier import TierOrStr
from .ip_access_list_entry import IpAccessListEntry, IpAccessListEntryDict
from .resource_tags_v1 import ResourceTagsV1, ResourceTagsV1Dict
from .service_endpoint_change import ServiceEndpointChange, ServiceEndpointChangeDict


class ServicePostRequest(SdkBaseModel):
    name: Optional[str] = UNSET
    """Name of the service. Alphanumerical string with whitespaces up to 50 characters."""

    provider: Optional[ProviderOrStr] = UNSET
    """Cloud provider"""

    region: Optional[RegionOrStr] = UNSET
    """Service region."""

    tier: Optional[TierOrStr] = UNSET
    """DEPRECATED for BASIC, SCALE and ENTERPRISE organization tiers. Use ``minReplicaMemoryGb``,
    ``maxReplicaMemoryGb``, and ``numReplicas`` instead. Tier of the service: 'development', 'production',
    'dedicated_high_mem', 'dedicated_high_cpu', 'dedicated_standard', 'dedicated_standard_n2d_standard_4',
    'dedicated_standard_n2d_standard_8', 'dedicated_standard_n2d_standard_32', 'dedicated_standard_n2d_standard_128',
    'dedicated_standard_n2d_standard_32_16SSD', 'dedicated_standard_n2d_standard_64_24SSD'. Production services scale,
    Development are fixed size. Azure services don't support Development tier"""

    ip_access_list: Optional[list[IpAccessListEntry]] = Field(default=UNSET, alias="ipAccessList")
    """List of IP addresses allowed to access the service"""

    min_total_memory_gb: Optional[float] = Field(default=UNSET, alias="minTotalMemoryGb")
    """DEPRECATED - inaccurate for services with non-default numbers of replicas. Use ``minReplicaMemoryGb`` instead.
    Minimum memory of three workers during auto-scaling in Gb. Available only for 'production' services. Must be a
    multiple of 12 and greater than or equal to 24. Always absent for horizontal-autoscaling services (replica count is
    variable)."""

    max_total_memory_gb: Optional[float] = Field(default=UNSET, alias="maxTotalMemoryGb")
    """DEPRECATED - inaccurate for services with non-default numbers of replicas. Use ``maxReplicaMemoryGb`` instead.
    Maximum memory of three workers during auto-scaling in Gb. Available only for 'production' services. Must be a
    multiple of 12 and lower than or equal to 360 for non paid services or 1068 for paid services. Always absent for
    horizontal-autoscaling services (replica count is variable)."""

    autoscaling_mode: Optional[AutoscalingMode4OrStr] = Field(default=UNSET, alias="autoscalingMode")
    """Autoscaling mode. "vertical" (the default when omitted) runs a fixed replica count while memory scales between
    minReplicaMemoryGb and maxReplicaMemoryGb; "horizontal" scales the replica count between minReplicas and maxReplicas
    at a fixed per-replica memory (minReplicaMemoryGb equal to maxReplicaMemoryGb). Horizontal requires the feature to
    be enabled for the organization."""

    min_replica_memory_gb: Optional[float] = Field(default=UNSET, alias="minReplicaMemoryGb")
    """Minimum total memory of each replica during auto-scaling in Gb. A range in vertical autoscaling; equal to
    maxReplicaMemoryGb in horizontal (memory is fixed while the replica count scales). Must be a multiple of 4 and
    greater than or equal to 8."""

    max_replica_memory_gb: Optional[float] = Field(default=UNSET, alias="maxReplicaMemoryGb")
    """Maximum total memory of each replica during auto-scaling in Gb. A range in vertical autoscaling; equal to
    minReplicaMemoryGb in horizontal (memory is fixed while the replica count scales). Must be a multiple of 4 and lower
    than or equal to 120* for non paid services or 356* for paid services.* - maximum replica size subject to cloud
    provider hardware availability in your selected region."""

    num_replicas: Optional[int] = Field(default=UNSET, alias="numReplicas")
    """Fixed replica count for vertical autoscaling (autoscalingMode "vertical" or omitted). Mutually exclusive with
    minReplicas/maxReplicas."""

    min_replicas: Optional[int] = Field(default=UNSET, alias="minReplicas")
    """Minimum number of replicas. A minReplicas/maxReplicas band scales the replica count in horizontal autoscaling
    (autoscalingMode "horizontal"). Must be provided together with maxReplicas. Mutually exclusive with numReplicas.
    Requires horizontal autoscaling to be enabled for the organization, unless autoscalingMode is omitted or "vertical"
    and minReplicas equals maxReplicas (an equal band is then an accepted vertical fixed count and needs no horizontal
    entitlement)."""

    max_replicas: Optional[int] = Field(default=UNSET, alias="maxReplicas")
    """Maximum number of replicas. A minReplicas/maxReplicas band scales the replica count in horizontal autoscaling
    (autoscalingMode "horizontal"). Must be provided together with minReplicas. Mutually exclusive with numReplicas.
    Requires horizontal autoscaling to be enabled for the organization, unless autoscalingMode is omitted or "vertical"
    and minReplicas equals maxReplicas (an equal band is then an accepted vertical fixed count and needs no horizontal
    entitlement)."""

    idle_scaling: Optional[bool] = Field(default=UNSET, alias="idleScaling")
    """When set to true the service is allowed to scale down to zero when idle. True by default."""

    idle_timeout_minutes: Optional[float] = Field(default=UNSET, alias="idleTimeoutMinutes")
    """Set minimum idling timeout (in minutes). Must be >= 5 minutes."""

    is_readonly: Optional[bool] = Field(default=UNSET, alias="isReadonly")
    """True if this service is read-only. It can only be read-only if a dataWarehouseId is provided."""

    data_warehouse_id: Optional[str] = Field(default=UNSET, alias="dataWarehouseId")
    """Data warehouse containing this service"""

    backup_id: Optional[UUID] = Field(default=UNSET, alias="backupId")
    """Optional backup ID used as an initial state for the new service. When used the region and the tier of the new
    instance must be the same as the values of the original instance."""

    encryption_key: Optional[str] = Field(default=UNSET, alias="encryptionKey")
    """Optional customer provided disk encryption key"""

    encryption_assumed_role_identifier: Optional[str] = Field(default=UNSET, alias="encryptionAssumedRoleIdentifier")
    """Optional role to use for disk encryption"""

    private_endpoint_ids: Optional[list[str]] = Field(default=UNSET, alias="privateEndpointIds")
    """DEPRECATED. To associate the service with private endpoints, first create the service, then use the ``Update
    Service Basic Details`` endpoint with the ``privateEndpointIds`` field to modify private endpoints."""

    private_preview_terms_checked: Optional[bool] = Field(default=UNSET, alias="privatePreviewTermsChecked")
    """Accept the private preview terms and conditions. It is only needed when creating the first service in the
    organization in case of a private preview"""

    release_channel: Optional[ReleaseChannelOrStr] = Field(default=UNSET, alias="releaseChannel")
    """Select fast if you want to get new ClickHouse releases as soon as they are available. You'll get new features
    faster, but with a higher risk of bugs. Select slow if you would like to defer releases to give yourself more time
    to test. This feature is only available for production services. default is the regular release channel."""

    byoc_id: Optional[str] = Field(default=UNSET, alias="byocId")
    """This is the ID returned after setting up a region for Bring Your Own Cloud (BYOC). When the byocId parameter is
    specified, the minReplicaMemoryGb and the maxReplicaGb parameters are required too, with values included among the
    following sizes: 48, 116, 172, 232."""

    has_transparent_data_encryption: Optional[bool] = Field(default=UNSET, alias="hasTransparentDataEncryption")
    """True if the service should have the Transparent Data Encryption (TDE) enabled. TDE is only available for
    ENTERPRISE organizations tiers and can only be enabled at service creation."""

    endpoints: Optional[list[ServiceEndpointChange]] = UNSET
    """List of service endpoints to enable or disable"""

    profile: Optional[str] = UNSET
    """Custom instance profile. Only available for ENTERPRISE and BYOC organization tiers. Standard values:
    'v1-default', 'v1-highmem-xs', 'v1-highmem-s', 'v1-highmem-m', 'v1-highmem-l', 'v1-highmem-xl'. BYOC services may
    instead use a dynamic BYOC profile configured for their infrastructure (e.g. 'v1-standard-byoc-4'); it requires
    byocId, and minReplicaMemoryGb and maxReplicaMemoryGb must both equal the profile's memory size. Use the
    serviceProfiles endpoint to list the profiles available to the organization."""

    compliance_type: Optional[ComplianceTypeOrStr] = Field(default=UNSET, alias="complianceType")
    """Type of regulatory compliance for service."""

    tags: Optional[list[ResourceTagsV1]] = UNSET
    """Tags associated with the service."""

    enable_core_dumps: Optional[bool] = Field(default=UNSET, alias="enableCoreDumps")
    """Enables the underlying infra for collecting core dumps. Default is enabled."""


class ServicePostRequestDict(TypedDict):
    name: NotRequired[str]
    provider: NotRequired[ProviderOrStr]
    region: NotRequired[RegionOrStr]
    tier: NotRequired[TierOrStr]
    ip_access_list: NotRequired[list[IpAccessListEntryDict]]
    min_total_memory_gb: NotRequired[float]
    max_total_memory_gb: NotRequired[float]
    autoscaling_mode: NotRequired[AutoscalingMode4OrStr]
    min_replica_memory_gb: NotRequired[float]
    max_replica_memory_gb: NotRequired[float]
    num_replicas: NotRequired[int]
    min_replicas: NotRequired[int]
    max_replicas: NotRequired[int]
    idle_scaling: NotRequired[bool]
    idle_timeout_minutes: NotRequired[float]
    is_readonly: NotRequired[bool]
    data_warehouse_id: NotRequired[str]
    backup_id: NotRequired[UUID]
    encryption_key: NotRequired[str]
    encryption_assumed_role_identifier: NotRequired[str]
    private_endpoint_ids: NotRequired[list[str]]
    private_preview_terms_checked: NotRequired[bool]
    release_channel: NotRequired[ReleaseChannelOrStr]
    byoc_id: NotRequired[str]
    has_transparent_data_encryption: NotRequired[bool]
    endpoints: NotRequired[list[ServiceEndpointChangeDict]]
    profile: NotRequired[str]
    compliance_type: NotRequired[ComplianceTypeOrStr]
    tags: NotRequired[list[ResourceTagsV1Dict]]
    enable_core_dumps: NotRequired[bool]
