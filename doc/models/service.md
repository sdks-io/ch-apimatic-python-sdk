
# Service

*This model accepts additional fields of type Any.*

## Structure

`Service`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Unique service ID. |
| `name` | `str` | Optional | Name of the service. Alphanumerical string with whitespaces up to 50 characters.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `50` |
| `provider` | [`Provider`](../../doc/models/provider.md) | Optional | Cloud provider |
| `region` | [`Region`](../../doc/models/region.md) | Optional | Service region. |
| `state` | [`State`](../../doc/models/state.md) | Optional | Current state of the service. |
| `clickhouse_version` | `str` | Optional | ClickHouse version of the service. |
| `endpoints` | [`List[ServiceEndpoint]`](../../doc/models/service-endpoint.md) | Optional | List of all service endpoints. |
| `tier` | [`Tier`](../../doc/models/tier.md) | Optional | DEPRECATED for BASIC, SCALE and ENTERPRISE organization tiers. Use `minReplicaMemoryGb`, `maxReplicaMemoryGb`, and `numReplicas` instead. Tier of the service: 'development', 'production', 'dedicated_high_mem', 'dedicated_high_cpu', 'dedicated_standard', 'dedicated_standard_n2d_standard_4', 'dedicated_standard_n2d_standard_8', 'dedicated_standard_n2d_standard_32', 'dedicated_standard_n2d_standard_128', 'dedicated_standard_n2d_standard_32_16SSD', 'dedicated_standard_n2d_standard_64_24SSD'. Production services scale, Development are fixed size. Azure services don't support Development tier |
| `min_total_memory_gb` | `float` | Optional | DEPRECATED - inaccurate for services with non-default numbers of replicas. Use `minReplicaMemoryGb` instead. Minimum memory of three workers during auto-scaling in Gb. Available only for 'production' services. Must be a multiple of 12 and greater than or equal to 24. Always absent for horizontal-autoscaling services (replica count is variable).<br><br>**Constraints**: `>= 24`, `<= 1068`, *Multiple Of*: `12` |
| `max_total_memory_gb` | `float` | Optional | DEPRECATED - inaccurate for services with non-default numbers of replicas. Use `maxReplicaMemoryGb` instead. Maximum memory of three workers during auto-scaling in Gb. Available only for 'production' services. Must be a multiple of 12 and lower than or equal to 360 for non paid services or 1068 for paid services. Always absent for horizontal-autoscaling services (replica count is variable).<br><br>**Constraints**: `>= 24`, `<= 1068`, *Multiple Of*: `12` |
| `min_replica_memory_gb` | `float` | Optional | Minimum total memory of each replica during auto-scaling in Gb. A range in vertical autoscaling; equal to maxReplicaMemoryGb in horizontal (memory is fixed while the replica count scales). Must be a multiple of 4 and greater than or equal to 8.<br><br>**Constraints**: `>= 8`, `<= 356`, *Multiple Of*: `4` |
| `max_replica_memory_gb` | `float` | Optional | Maximum total memory of each replica during auto-scaling in Gb. A range in vertical autoscaling; equal to minReplicaMemoryGb in horizontal (memory is fixed while the replica count scales). Must be a multiple of 4 and lower than or equal to 120* for non paid services or 356* for paid services.* - maximum replica size subject to cloud provider hardware availability in your selected region.<br><br>**Constraints**: `>= 8`, `<= 356`, *Multiple Of*: `4` |
| `num_replicas` | `int` | Optional | Number of replicas for the service. The number of replicas must be between 2 and 50 for the first service in a warehouse. Services that are created in an existing warehouse can have a number of replicas as low as 1. Further restrictions may apply based on your organization's tier and its per-warehouse replica limit. It defaults to 1 for the BASIC tier and 3 for the SCALE and ENTERPRISE tiers. Present only when the service uses vertical autoscaling. For horizontal autoscaling, use minReplicas and maxReplicas instead.<br><br>**Constraints**: `>= 1`, `<= 50` |
| `min_replicas` | `int` | Optional | Minimum number of replicas for horizontal autoscaling. Present only when the service uses horizontal autoscaling.<br><br>**Constraints**: `>= 1`, `<= 50` |
| `max_replicas` | `int` | Optional | Maximum number of replicas for horizontal autoscaling. Present only when the service uses horizontal autoscaling.<br><br>**Constraints**: `>= 1`, `<= 50` |
| `autoscaling_mode` | [`AutoscalingMode3`](../../doc/models/autoscaling-mode-3.md) | Required | Configured autoscaling mode. "vertical" runs a fixed replica count while memory scales between minReplicaMemoryGb and maxReplicaMemoryGb; "horizontal" scales the replica count between minReplicas and maxReplicas at a fixed per-replica memory. This is the baseline configuration; the mode currently applied (which may differ while a schedule entry is active) is currentScaling.effectiveAutoscalingMode. |
| `replica_memory_gb` | `float` | Optional | Fixed memory per replica in Gb for horizontal autoscaling. Present only when the service uses horizontal autoscaling. Must be a multiple of 4, at least 8 Gb, and at most 120 Gb for non paid services or 356 Gb for paid services.<br><br>**Constraints**: `>= 8`, `<= 356`, *Multiple Of*: `4` |
| `idle_scaling` | `bool` | Optional | When set to true the service is allowed to scale down to zero when idle. True by default. |
| `idle_timeout_minutes` | `float` | Optional | Set minimum idling timeout (in minutes). Must be >= 5 minutes. |
| `ip_access_list` | [`List[IpAccessListEntry]`](../../doc/models/ip-access-list-entry.md) | Optional | List of IP addresses allowed to access the service |
| `created_at` | `datetime` | Optional | Service creation timestamp. ISO-8601. |
| `encryption_key` | `str` | Optional | Optional customer provided disk encryption key |
| `encryption_assumed_role_identifier` | `str` | Optional | Optional role to use for disk encryption |
| `iam_role` | `str` | Optional | IAM role used for accessing objects in s3 |
| `private_endpoint_ids` | `List[str]` | Optional | List of private endpoints |
| `available_private_endpoint_ids` | `List[str]` | Optional | List of available private endpoints ids that can be attached to the service |
| `data_warehouse_id` | `str` | Optional | Data warehouse containing this service |
| `is_primary` | `bool` | Optional | True if this service is the primary service in the data warehouse |
| `is_readonly` | `bool` | Optional | True if this service is read-only. It can only be read-only if a dataWarehouseId is provided. |
| `release_channel` | [`ReleaseChannel`](../../doc/models/release-channel.md) | Optional | Select fast if you want to get new ClickHouse releases as soon as they are available. You'll get new features faster, but with a higher risk of bugs. Select slow if you would like to defer releases to give yourself more time to test. This feature is only available for production services. default is the regular release channel. |
| `byoc_id` | `str` | Optional | This is the ID returned after setting up a region for Bring Your Own Cloud (BYOC). When the byocId parameter is specified, the minReplicaMemoryGb and the maxReplicaGb parameters are required too, with values included among the following sizes: 48, 116, 172, 232. |
| `has_transparent_data_encryption` | `bool` | Optional | True if the service should have the Transparent Data Encryption (TDE) enabled. TDE is only available for ENTERPRISE organizations tiers and can only be enabled at service creation. |
| `profile` | `str` | Optional | Custom instance profile. Only available for ENTERPRISE and BYOC organization tiers. Standard values: 'v1-default', 'v1-highmem-xs', 'v1-highmem-s', 'v1-highmem-m', 'v1-highmem-l', 'v1-highmem-xl'. BYOC services may instead use a dynamic BYOC profile configured for their infrastructure (e.g. 'v1-standard-byoc-4'); it requires byocId, and minReplicaMemoryGb and maxReplicaMemoryGb must both equal the profile's memory size. Use the serviceProfiles endpoint to list the profiles available to the organization. |
| `transparent_data_encryption_key_id` | `str` | Optional | The ID of the Transparent Data Encryption key used for the service. This is only available if hasTransparentDataEncryption is true. |
| `encryption_role_id` | `str` | Optional | The ID of the IAM role used for encryption. This is only available if hasTransparentDataEncryption is true. |
| `compliance_type` | [`ComplianceType`](../../doc/models/compliance-type.md) | Optional | Type of regulatory compliance for service. |
| `tags` | [`List[ResourceTagsV1]`](../../doc/models/resource-tags-v1.md) | Optional | Tags associated with the service.<br><br>**Constraints**: *Maximum Items*: `50` |
| `enable_core_dumps` | `bool` | Optional | True if the service's underline infra is enabled for collecting core dumps. This is an experimental feature |
| `scaling_schedule` | [`ScalingSchedule`](../../doc/models/scaling-schedule.md) | Optional | - |
| `current_scaling` | [`CurrentScaling`](../../doc/models/current-scaling.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.autoscaling_mode_3 import AutoscalingMode3
from openapispecforclickhousecloud.models.current_scaling import CurrentScaling
from openapispecforclickhousecloud.models.effective_autoscaling_mode import EffectiveAutoscalingMode
from openapispecforclickhousecloud.models.provider import Provider
from openapispecforclickhousecloud.models.region import Region
from openapispecforclickhousecloud.models.service import Service
from openapispecforclickhousecloud.models.state import State

service = Service(
    autoscaling_mode=AutoscalingMode3.VERTICAL,
    current_scaling=CurrentScaling(
        effective_autoscaling_mode=EffectiveAutoscalingMode.VERTICAL,
        effective_min_replica_memory_gb=39.2,
        effective_max_replica_memory_gb=21.08,
        effective_min_replicas=124,
        effective_max_replicas=40,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    id='000023dc-0000-0000-0000-000000000000',
    name='name0',
    provider=Provider.AWS,
    region=Region.APNORTHEAST1,
    state=State.TERMINATING,
    min_total_memory_gb=48,
    max_total_memory_gb=360,
    min_replica_memory_gb=16,
    max_replica_memory_gb=120,
    num_replicas=3,
    min_replicas=1,
    max_replicas=5,
    replica_memory_gb=32,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

