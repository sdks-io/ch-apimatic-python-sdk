
# Scim Schema Extension

*This model accepts additional fields of type Any.*

## Structure

`ScimSchemaExtension`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schema` | `str` | Required | The URI of a schema extension. |
| `required` | `bool` | Required | Whether the schema extension is required. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_schema_extension import ScimSchemaExtension

scim_schema_extension = ScimSchemaExtension(
    schema='schema4',
    required=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

