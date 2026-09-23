
# Scim Boolean Feature

*This model accepts additional fields of type Any.*

## Structure

`ScimBooleanFeature`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `supported` | `bool` | Required | Whether the feature is supported. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_boolean_feature import ScimBooleanFeature

scim_boolean_feature = ScimBooleanFeature(
    supported=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

