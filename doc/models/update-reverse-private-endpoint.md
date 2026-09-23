
# Update Reverse Private Endpoint

*This model accepts additional fields of type Any.*

## Structure

`UpdateReversePrivateEndpoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `custom_private_dns_mappings` | [`List[CustomPrivateDnsMapping]`](../../doc/models/custom-private-dns-mapping.md) | Optional | Optional private DNS names for Reverse Private Endpoint. Can be used as data source destination address. Must be unique across the ClickHouse service.<br>Generally available for Google Private Service Connect (PSC). For AWS PrivateLink (VPC endpoint service and VPC resource), available in Private Preview; contact ClickHouse support to enable it for your service. Not supported for MSK multi-VPC.<br>Supports exact names and leading wildcard names such as *.example.com |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.custom_private_dns_mapping import CustomPrivateDnsMapping
from openapispecforclickhousecloud.models.update_reverse_private_endpoint import UpdateReversePrivateEndpoint

update_reverse_private_endpoint = UpdateReversePrivateEndpoint(
    custom_private_dns_mappings=[
        CustomPrivateDnsMapping(
            private_dns_name='my-service.example.com',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        CustomPrivateDnsMapping(
            private_dns_name='*.example.com',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

