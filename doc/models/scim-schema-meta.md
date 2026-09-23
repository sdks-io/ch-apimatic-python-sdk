
# Scim Schema Meta

*This model accepts additional fields of type Any.*

## Structure

`ScimSchemaMeta`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `resource_type` | `str` | Required | The resource type. |
| `location` | `str` | Required | The URI of this schema. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_schema_meta import ScimSchemaMeta

scim_schema_meta = ScimSchemaMeta(
    resource_type='resourceType8',
    location='location8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

