
# Scim Resource Type

*This model accepts additional fields of type Any.*

## Structure

`ScimResourceType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schemas` | `List[str]` | Required | SCIM schema URIs. |
| `id` | `str` | Required | The resource type ID. |
| `name` | `str` | Required | The resource type name. |
| `endpoint` | `str` | Required | The endpoint path for this resource type. |
| `description` | `str` | Required | A description of the resource type. |
| `schema` | `str` | Required | The primary schema URI for this resource type. |
| `schema_extensions` | [`List[ScimSchemaExtension]`](../../doc/models/scim-schema-extension.md) | Required | Optional schema extensions for this resource type. |
| `meta` | [`ScimResourceTypeMeta`](../../doc/models/scim-resource-type-meta.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_resource_type import ScimResourceType
from openapispecforclickhousecloud.models.scim_resource_type_meta import ScimResourceTypeMeta
from openapispecforclickhousecloud.models.scim_schema_extension import ScimSchemaExtension

scim_resource_type = ScimResourceType(
    schemas=[
        'schemas3',
        'schemas4'
    ],
    id='id4',
    name='name4',
    endpoint='endpoint2',
    description='description6',
    schema='schema6',
    schema_extensions=[
        ScimSchemaExtension(
            schema='schema0',
            required=False,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    meta=ScimResourceTypeMeta(
        resource_type='resourceType6',
        location='location6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

