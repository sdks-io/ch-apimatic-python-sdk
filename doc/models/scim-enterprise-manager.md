
# Scim Enterprise Manager

*This model accepts additional fields of type Any.*

## Structure

`ScimEnterpriseManager`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `str` | Optional | The id of the SCIM resource representing the user's manager. |
| `display_name` | `str` | Optional | The displayName of the user's manager. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_enterprise_manager import ScimEnterpriseManager

scim_enterprise_manager = ScimEnterpriseManager(
    value='value2',
    display_name='displayName2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

