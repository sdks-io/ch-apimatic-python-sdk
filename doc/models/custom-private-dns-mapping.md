
# Custom Private Dns Mapping

*This model accepts additional fields of type Any.*

## Structure

`CustomPrivateDnsMapping`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `private_dns_name` | `str` | Optional | Optional private DNS names for Reverse Private Endpoint. Can be used as data source destination address. Must be unique across the ClickHouse service.<br>Generally available for Google Private Service Connect (PSC). For AWS PrivateLink (VPC endpoint service and VPC resource), available in Private Preview; contact ClickHouse support to enable it for your service. Not supported for MSK multi-VPC.<br>Supports exact names and leading wildcard names such as *.example.com |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.custom_private_dns_mapping import CustomPrivateDnsMapping

custom_private_dns_mapping = CustomPrivateDnsMapping(
    private_dns_name='*.my-service.example.com',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

