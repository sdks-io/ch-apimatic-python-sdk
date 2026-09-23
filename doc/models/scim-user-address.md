
# Scim User Address

*This model accepts additional fields of type Any.*

## Structure

`ScimUserAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `formatted` | `str` | Optional | The full mailing address, formatted for display or use with a mailing label. |
| `street_address` | `str` | Optional | The full street address component. |
| `locality` | `str` | Optional | The city or locality component. |
| `region` | `str` | Optional | The state or region component. |
| `postal_code` | `str` | Optional | The zip code or postal code component. |
| `country` | `str` | Optional | The country name component. |
| `mtype` | `str` | Optional | Type of address (e.g., "work", "home", "other"). |
| `primary` | `bool` | Optional | A Boolean value indicating the preferred mailing address. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_user_address import ScimUserAddress

scim_user_address = ScimUserAddress(
    formatted='formatted0',
    street_address='streetAddress8',
    locality='locality8',
    region='region4',
    postal_code='postalCode0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

