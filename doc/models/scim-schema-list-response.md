
# Scim Schema List Response

*This model accepts additional fields of type Any.*

## Structure

`ScimSchemaListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schemas` | `List[str]` | Required | SCIM schema URIs. |
| `total_results` | `int` | Required | Total number of schemas. |
| `items_per_page` | `int` | Required | Number of schemas per page. |
| `start_index` | `int` | Required | 1-based start index. |
| `resources` | [`List[ScimSchema]`](../../doc/models/scim-schema.md) | Required | Array of schema definitions. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_schema import ScimSchema
from openapispecforclickhousecloud.models.scim_schema_attribute import ScimSchemaAttribute
from openapispecforclickhousecloud.models.scim_schema_list_response import ScimSchemaListResponse
from openapispecforclickhousecloud.models.scim_schema_meta import ScimSchemaMeta
from openapispecforclickhousecloud.models.scim_schema_sub_attribute import ScimSchemaSubAttribute

scim_schema_list_response = ScimSchemaListResponse(
    schemas=[
        'schemas7',
        'schemas6'
    ],
    total_results=22,
    items_per_page=92,
    start_index=96,
    resources=[
        ScimSchema(
            schemas=[
                'schemas9',
                'schemas8'
            ],
            id='id6',
            name='name6',
            description='description6',
            attributes=[
                ScimSchemaAttribute(
                    name='name4',
                    mtype='type4',
                    multi_valued=False,
                    description='description4',
                    required=False,
                    mutability='mutability0',
                    returned='returned2',
                    sub_attributes=[
                        ScimSchemaSubAttribute(
                            name='name4',
                            mtype='type4',
                            multi_valued=False,
                            description='description4',
                            required=False,
                            mutability='mutability0',
                            returned='returned2',
                            case_exact=False,
                            uniqueness='uniqueness0',
                            reference_types=[
                                'referenceTypes0',
                                'referenceTypes1'
                            ],
                            canonical_values=[
                                'canonicalValues4'
                            ],
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        )
                    ],
                    case_exact=False,
                    uniqueness='uniqueness0',
                    reference_types=[
                        'referenceTypes0',
                        'referenceTypes1'
                    ],
                    canonical_values=[
                        'canonicalValues4'
                    ],
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            meta=ScimSchemaMeta(
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

