
# Ip Access List Entry

*This model accepts additional fields of type Any.*

## Structure

`IpAccessListEntry`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `source` | `str` | Optional | IP or CIDR |
| `description` | `str` | Optional | Optional description of IPv4 address or IPv4 CIDR to allow access from |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.ip_access_list_entry import IpAccessListEntry

ip_access_list_entry = IpAccessListEntry(
    source='source6',
    description='description2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

