
# Scim Resource Type List Response

*This model accepts additional fields of type Any.*

## Structure

`ScimResourceTypeListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schemas` | `List[str]` | Required | SCIM schema URIs. |
| `total_results` | `int` | Required | Total number of resource types. |
| `items_per_page` | `int` | Required | Number of resources per page. |
| `start_index` | `int` | Required | 1-based start index. |
| `resources` | [`List[ScimResourceType]`](../../doc/models/scim-resource-type.md) | Required | Array of resource type definitions. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_resource_type import ScimResourceType
from openapispecforclickhousecloud.models.scim_resource_type_list_response import ScimResourceTypeListResponse
from openapispecforclickhousecloud.models.scim_resource_type_meta import ScimResourceTypeMeta
from openapispecforclickhousecloud.models.scim_schema_extension import ScimSchemaExtension

scim_resource_type_list_response = ScimResourceTypeListResponse(
    schemas=[
        'schemas7'
    ],
    total_results=74,
    items_per_page=216,
    start_index=212,
    resources=[
        ScimResourceType(
            schemas=[
                'schemas9',
                'schemas8'
            ],
            id='id6',
            name='name6',
            endpoint='endpoint4',
            description='description6',
            schema='schema8',
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

