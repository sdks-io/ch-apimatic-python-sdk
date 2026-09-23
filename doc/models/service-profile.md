
# Service Profile

*This model accepts additional fields of type Any.*

## Structure

`ServiceProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `profile` | `str` | Optional | Profile name to pass as `profile` when creating a service (e.g. 'v1-standard-byoc-4'). |
| `cpu_cores` | `float` | Optional | Number of vCPUs per replica. |
| `memory_gi` | `float` | Optional | Memory per replica in GiB. When creating a BYOC service with this profile, minReplicaMemoryGb and maxReplicaMemoryGb must both equal this value. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.service_profile import ServiceProfile

service_profile = ServiceProfile(
    profile='profile6',
    cpu_cores=22.42,
    memory_gi=180.94,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

