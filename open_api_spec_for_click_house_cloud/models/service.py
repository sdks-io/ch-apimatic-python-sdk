from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .current_scaling import CurrentScaling, CurrentScalingDict
from .enums.autoscaling_mode3 import AutoscalingMode3OrStr
from .enums.compliance_type import ComplianceTypeOrStr
from .enums.provider import ProviderOrStr
from .enums.region import RegionOrStr
from .enums.release_channel import ReleaseChannelOrStr
from .enums.state import StateOrStr
from .enums.tier import TierOrStr
from .ip_access_list_entry import IpAccessListEntry, IpAccessListEntryDict
from .resource_tags_v1 import ResourceTagsV1, ResourceTagsV1Dict
from .scaling_schedule import ScalingSchedule, ScalingScheduleDict
from .service_endpoint import ServiceEndpoint, ServiceEndpointDict


class Service(SdkBaseModel):
    id: Optional[UUID] = UNSET
    """Unique service ID."""

    name: Optional[str] = UNSET
    """Name of the service. Alphanumerical string with whitespaces up to 50 characters."""

    provider: Optional[ProviderOrStr] = UNSET
    """Cloud provider"""

    region: Optional[RegionOrStr] = UNSET
    """Service region."""

    state: Optional[StateOrStr] = UNSET
    """Current state of the service."""

    clickhouse_version: Optional[str] = Field(default=UNSET, alias="clickhouseVersion")
    """ClickHouse version of the service."""

    endpoints: Optional[list[ServiceEndpoint]] = UNSET
    """List of all service endpoints."""

    tier: Optional[TierOrStr] = UNSET
    """DEPRECATED for BASIC, SCALE and ENTERPRISE organization tiers. Use ``minReplicaMemoryGb``,
    ``maxReplicaMemoryGb``, and ``numReplicas`` instead. Tier of the service: 'development', 'production',
    'dedicated_high_mem', 'dedicated_high_cpu', 'dedicated_standard', 'dedicated_standard_n2d_standard_4',
    'dedicated_standard_n2d_standard_8', 'dedicated_standard_n2d_standard_32', 'dedicated_standard_n2d_standard_128',
    'dedicated_standard_n2d_standard_32_16SSD', 'dedicated_standard_n2d_standard_64_24SSD'. Production services scale,
    Development are fixed size. Azure services don't support Development tier"""

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
    """Number of replicas for the service. The number of replicas must be between 2 and 50 for the first service in a
    warehouse. Services that are created in an existing warehouse can have a number of replicas as low as 1. Further
    restrictions may apply based on your organization's tier and its per-warehouse replica limit. It defaults to 1 for
    the BASIC tier and 3 for the SCALE and ENTERPRISE tiers. Present only when the service uses vertical autoscaling.
    For horizontal autoscaling, use minReplicas and maxReplicas instead."""

    min_replicas: Optional[int] = Field(default=UNSET, alias="minReplicas")
    """Minimum number of replicas for horizontal autoscaling. Present only when the service uses horizontal
    autoscaling."""

    max_replicas: Optional[int] = Field(default=UNSET, alias="maxReplicas")
    """Maximum number of replicas for horizontal autoscaling. Present only when the service uses horizontal
    autoscaling."""

    autoscaling_mode: AutoscalingMode3OrStr = Field(alias="autoscalingMode")
    """Configured autoscaling mode. "vertical" runs a fixed replica count while memory scales between minReplicaMemoryGb
    and maxReplicaMemoryGb; "horizontal" scales the replica count between minReplicas and maxReplicas at a fixed
    per-replica memory. This is the baseline configuration; the mode currently applied (which may differ while a
    schedule entry is active) is currentScaling.effectiveAutoscalingMode."""

    replica_memory_gb: Optional[float] = Field(default=UNSET, alias="replicaMemoryGb")
    """Fixed memory per replica in Gb for horizontal autoscaling. Present only when the service uses horizontal
    autoscaling. Must be a multiple of 4, at least 8 Gb, and at most 120 Gb for non paid services or 356 Gb for paid
    services."""

    idle_scaling: Optional[bool] = Field(default=UNSET, alias="idleScaling")
    """When set to true the service is allowed to scale down to zero when idle. True by default."""

    idle_timeout_minutes: Optional[float] = Field(default=UNSET, alias="idleTimeoutMinutes")
    """Set minimum idling timeout (in minutes). Must be >= 5 minutes."""

    ip_access_list: Optional[list[IpAccessListEntry]] = Field(default=UNSET, alias="ipAccessList")
    """List of IP addresses allowed to access the service"""

    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    """Service creation timestamp. ISO-8601."""

    encryption_key: Optional[str] = Field(default=UNSET, alias="encryptionKey")
    """Optional customer provided disk encryption key"""

    encryption_assumed_role_identifier: Optional[str] = Field(default=UNSET, alias="encryptionAssumedRoleIdentifier")
    """Optional role to use for disk encryption"""

    iam_role: Optional[str] = Field(default=UNSET, alias="iamRole")
    """IAM role used for accessing objects in s3"""

    private_endpoint_ids: Optional[list[str]] = Field(default=UNSET, alias="privateEndpointIds")
    """List of private endpoints"""

    available_private_endpoint_ids: Optional[list[str]] = Field(default=UNSET, alias="availablePrivateEndpointIds")
    """List of available private endpoints ids that can be attached to the service"""

    data_warehouse_id: Optional[str] = Field(default=UNSET, alias="dataWarehouseId")
    """Data warehouse containing this service"""

    is_primary: Optional[bool] = Field(default=UNSET, alias="isPrimary")
    """True if this service is the primary service in the data warehouse"""

    is_readonly: Optional[bool] = Field(default=UNSET, alias="isReadonly")
    """True if this service is read-only. It can only be read-only if a dataWarehouseId is provided."""

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

    profile: Optional[str] = UNSET
    """Custom instance profile. Only available for ENTERPRISE and BYOC organization tiers. Standard values:
    'v1-default', 'v1-highmem-xs', 'v1-highmem-s', 'v1-highmem-m', 'v1-highmem-l', 'v1-highmem-xl'. BYOC services may
    instead use a dynamic BYOC profile configured for their infrastructure (e.g. 'v1-standard-byoc-4'); it requires
    byocId, and minReplicaMemoryGb and maxReplicaMemoryGb must both equal the profile's memory size. Use the
    serviceProfiles endpoint to list the profiles available to the organization."""

    transparent_data_encryption_key_id: Optional[str] = Field(default=UNSET, alias="transparentDataEncryptionKeyId")
    """The ID of the Transparent Data Encryption key used for the service. This is only available if
    hasTransparentDataEncryption is true."""

    encryption_role_id: Optional[str] = Field(default=UNSET, alias="encryptionRoleId")
    """The ID of the IAM role used for encryption. This is only available if hasTransparentDataEncryption is true."""

    compliance_type: Optional[ComplianceTypeOrStr] = Field(default=UNSET, alias="complianceType")
    """Type of regulatory compliance for service."""

    tags: Optional[list[ResourceTagsV1]] = UNSET
    """Tags associated with the service."""

    enable_core_dumps: Optional[bool] = Field(default=UNSET, alias="enableCoreDumps")
    """True if the service's underline infra is enabled for collecting core dumps. This is an experimental feature"""

    scaling_schedule: Optional[ScalingSchedule] = Field(default=UNSET, alias="scalingSchedule")
    current_scaling: CurrentScaling = Field(alias="currentScaling")


class ServiceDict(TypedDict):
    id: NotRequired[UUID]
    name: NotRequired[str]
    provider: NotRequired[ProviderOrStr]
    region: NotRequired[RegionOrStr]
    state: NotRequired[StateOrStr]
    clickhouse_version: NotRequired[str]
    endpoints: NotRequired[list[ServiceEndpointDict]]
    tier: NotRequired[TierOrStr]
    min_total_memory_gb: NotRequired[float]
    max_total_memory_gb: NotRequired[float]
    min_replica_memory_gb: NotRequired[float]
    max_replica_memory_gb: NotRequired[float]
    num_replicas: NotRequired[int]
    min_replicas: NotRequired[int]
    max_replicas: NotRequired[int]
    autoscaling_mode: AutoscalingMode3OrStr
    replica_memory_gb: NotRequired[float]
    idle_scaling: NotRequired[bool]
    idle_timeout_minutes: NotRequired[float]
    ip_access_list: NotRequired[list[IpAccessListEntryDict]]
    created_at: NotRequired[RFC3339DateTime]
    encryption_key: NotRequired[str]
    encryption_assumed_role_identifier: NotRequired[str]
    iam_role: NotRequired[str]
    private_endpoint_ids: NotRequired[list[str]]
    available_private_endpoint_ids: NotRequired[list[str]]
    data_warehouse_id: NotRequired[str]
    is_primary: NotRequired[bool]
    is_readonly: NotRequired[bool]
    release_channel: NotRequired[ReleaseChannelOrStr]
    byoc_id: NotRequired[str]
    has_transparent_data_encryption: NotRequired[bool]
    profile: NotRequired[str]
    transparent_data_encryption_key_id: NotRequired[str]
    encryption_role_id: NotRequired[str]
    compliance_type: NotRequired[ComplianceTypeOrStr]
    tags: NotRequired[list[ResourceTagsV1Dict]]
    enable_core_dumps: NotRequired[bool]
    scaling_schedule: NotRequired[ScalingScheduleDict]
    current_scaling: CurrentScalingDict
