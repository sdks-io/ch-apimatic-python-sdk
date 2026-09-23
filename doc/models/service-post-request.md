
# Service Post Request

*This model accepts additional fields of type Any.*

## Structure

`ServicePostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the service. Alphanumerical string with whitespaces up to 50 characters.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `50` |
| `provider` | [`Provider`](../../doc/models/provider.md) | Optional | Cloud provider |
| `region` | [`Region`](../../doc/models/region.md) | Optional | Service region. |
| `tier` | [`Tier`](../../doc/models/tier.md) | Optional | DEPRECATED for BASIC, SCALE and ENTERPRISE organization tiers. Use `minReplicaMemoryGb`, `maxReplicaMemoryGb`, and `numReplicas` instead. Tier of the service: 'development', 'production', 'dedicated_high_mem', 'dedicated_high_cpu', 'dedicated_standard', 'dedicated_standard_n2d_standard_4', 'dedicated_standard_n2d_standard_8', 'dedicated_standard_n2d_standard_32', 'dedicated_standard_n2d_standard_128', 'dedicated_standard_n2d_standard_32_16SSD', 'dedicated_standard_n2d_standard_64_24SSD'. Production services scale, Development are fixed size. Azure services don't support Development tier |
| `ip_access_list` | [`List[IpAccessListEntry]`](../../doc/models/ip-access-list-entry.md) | Optional | List of IP addresses allowed to access the service |
| `min_total_memory_gb` | `float` | Optional | DEPRECATED - inaccurate for services with non-default numbers of replicas. Use `minReplicaMemoryGb` instead. Minimum memory of three workers during auto-scaling in Gb. Available only for 'production' services. Must be a multiple of 12 and greater than or equal to 24. Always absent for horizontal-autoscaling services (replica count is variable).<br><br>**Constraints**: `>= 24`, `<= 1068`, *Multiple Of*: `12` |
| `max_total_memory_gb` | `float` | Optional | DEPRECATED - inaccurate for services with non-default numbers of replicas. Use `maxReplicaMemoryGb` instead. Maximum memory of three workers during auto-scaling in Gb. Available only for 'production' services. Must be a multiple of 12 and lower than or equal to 360 for non paid services or 1068 for paid services. Always absent for horizontal-autoscaling services (replica count is variable).<br><br>**Constraints**: `>= 24`, `<= 1068`, *Multiple Of*: `12` |
| `autoscaling_mode` | [`AutoscalingMode4`](../../doc/models/autoscaling-mode-4.md) | Optional | Autoscaling mode. "vertical" (the default when omitted) runs a fixed replica count while memory scales between minReplicaMemoryGb and maxReplicaMemoryGb; "horizontal" scales the replica count between minReplicas and maxReplicas at a fixed per-replica memory (minReplicaMemoryGb equal to maxReplicaMemoryGb). Horizontal requires the feature to be enabled for the organization. |
| `min_replica_memory_gb` | `float` | Optional | Minimum total memory of each replica during auto-scaling in Gb. A range in vertical autoscaling; equal to maxReplicaMemoryGb in horizontal (memory is fixed while the replica count scales). Must be a multiple of 4 and greater than or equal to 8.<br><br>**Constraints**: `>= 8`, `<= 356`, *Multiple Of*: `4` |
| `max_replica_memory_gb` | `float` | Optional | Maximum total memory of each replica during auto-scaling in Gb. A range in vertical autoscaling; equal to minReplicaMemoryGb in horizontal (memory is fixed while the replica count scales). Must be a multiple of 4 and lower than or equal to 120* for non paid services or 356* for paid services.* - maximum replica size subject to cloud provider hardware availability in your selected region.<br><br>**Constraints**: `>= 8`, `<= 356`, *Multiple Of*: `4` |
| `num_replicas` | `int` | Optional | Fixed replica count for vertical autoscaling (autoscalingMode "vertical" or omitted). Mutually exclusive with minReplicas/maxReplicas.<br><br>**Constraints**: `>= 1`, `<= 50` |
| `min_replicas` | `int` | Optional | Minimum number of replicas. A minReplicas/maxReplicas band scales the replica count in horizontal autoscaling (autoscalingMode "horizontal"). Must be provided together with maxReplicas. Mutually exclusive with numReplicas. Requires horizontal autoscaling to be enabled for the organization, unless autoscalingMode is omitted or "vertical" and minReplicas equals maxReplicas (an equal band is then an accepted vertical fixed count and needs no horizontal entitlement).<br><br>**Constraints**: `>= 1`, `<= 50` |
| `max_replicas` | `int` | Optional | Maximum number of replicas. A minReplicas/maxReplicas band scales the replica count in horizontal autoscaling (autoscalingMode "horizontal"). Must be provided together with minReplicas. Mutually exclusive with numReplicas. Requires horizontal autoscaling to be enabled for the organization, unless autoscalingMode is omitted or "vertical" and minReplicas equals maxReplicas (an equal band is then an accepted vertical fixed count and needs no horizontal entitlement).<br><br>**Constraints**: `>= 1`, `<= 50` |
| `idle_scaling` | `bool` | Optional | When set to true the service is allowed to scale down to zero when idle. True by default. |
| `idle_timeout_minutes` | `float` | Optional | Set minimum idling timeout (in minutes). Must be >= 5 minutes. |
| `is_readonly` | `bool` | Optional | True if this service is read-only. It can only be read-only if a dataWarehouseId is provided. |
| `data_warehouse_id` | `str` | Optional | Data warehouse containing this service |
| `backup_id` | `uuid\|str` | Optional | Optional backup ID used as an initial state for the new service. When used the region and the tier of the new instance must be the same as the values of the original instance. |
| `encryption_key` | `str` | Optional | Optional customer provided disk encryption key |
| `encryption_assumed_role_identifier` | `str` | Optional | Optional role to use for disk encryption |
| `private_endpoint_ids` | `List[str]` | Optional | DEPRECATED. To associate the service with private endpoints, first create the service, then use the `Update Service Basic Details` endpoint with the `privateEndpointIds` field to modify private endpoints. |
| `private_preview_terms_checked` | `bool` | Optional | Accept the private preview terms and conditions. It is only needed when creating the first service in the organization in case of a private preview |
| `release_channel` | [`ReleaseChannel`](../../doc/models/release-channel.md) | Optional | Select fast if you want to get new ClickHouse releases as soon as they are available. You'll get new features faster, but with a higher risk of bugs. Select slow if you would like to defer releases to give yourself more time to test. This feature is only available for production services. default is the regular release channel. |
| `byoc_id` | `str` | Optional | This is the ID returned after setting up a region for Bring Your Own Cloud (BYOC). When the byocId parameter is specified, the minReplicaMemoryGb and the maxReplicaGb parameters are required too, with values included among the following sizes: 48, 116, 172, 232. |
| `has_transparent_data_encryption` | `bool` | Optional | True if the service should have the Transparent Data Encryption (TDE) enabled. TDE is only available for ENTERPRISE organizations tiers and can only be enabled at service creation. |
| `endpoints` | [`List[ServiceEndpointChange]`](../../doc/models/service-endpoint-change.md) | Optional | List of service endpoints to enable or disable |
| `profile` | `str` | Optional | Custom instance profile. Only available for ENTERPRISE and BYOC organization tiers. Standard values: 'v1-default', 'v1-highmem-xs', 'v1-highmem-s', 'v1-highmem-m', 'v1-highmem-l', 'v1-highmem-xl'. BYOC services may instead use a dynamic BYOC profile configured for their infrastructure (e.g. 'v1-standard-byoc-4'); it requires byocId, and minReplicaMemoryGb and maxReplicaMemoryGb must both equal the profile's memory size. Use the serviceProfiles endpoint to list the profiles available to the organization. |
| `compliance_type` | [`ComplianceType`](../../doc/models/compliance-type.md) | Optional | Type of regulatory compliance for service. |
| `tags` | [`List[ResourceTagsV1]`](../../doc/models/resource-tags-v1.md) | Optional | Tags associated with the service.<br><br>**Constraints**: *Maximum Items*: `50` |
| `enable_core_dumps` | `bool` | Optional | Enables the underlying infra for collecting core dumps. Default is enabled. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.autoscaling_mode_4 import AutoscalingMode4
from openapispecforclickhousecloud.models.ip_access_list_entry import IpAccessListEntry
from openapispecforclickhousecloud.models.provider import Provider
from openapispecforclickhousecloud.models.region import Region
from openapispecforclickhousecloud.models.service_post_request import ServicePostRequest
from openapispecforclickhousecloud.models.tier import Tier

service_post_request = ServicePostRequest(
    name='name4',
    provider=Provider.AZURE,
    region=Region.USEAST1,
    tier=Tier.DEDICATED_STANDARD_N2D_STANDARD_128,
    ip_access_list=[
        IpAccessListEntry(
            source='source4',
            description='description8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        IpAccessListEntry(
            source='source4',
            description='description8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        IpAccessListEntry(
            source='source4',
            description='description8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    min_total_memory_gb=48,
    max_total_memory_gb=360,
    autoscaling_mode=AutoscalingMode4.VERTICAL,
    min_replica_memory_gb=16,
    max_replica_memory_gb=120,
    num_replicas=3,
    min_replicas=1,
    max_replicas=5,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

