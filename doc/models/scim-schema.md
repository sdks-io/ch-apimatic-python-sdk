
# Scim Schema

*This model accepts additional fields of type Any.*

## Structure

`ScimSchema`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schemas` | `List[str]` | Required | SCIM schema URIs. |
| `id` | `str` | Required | The unique URI of the schema. |
| `name` | `str` | Required | The schema name. |
| `description` | `str` | Required | A description of the schema. |
| `attributes` | [`List[ScimSchemaAttribute]`](../../doc/models/scim-schema-attribute.md) | Required | Service provider attributes comprising the schema. |
| `meta` | [`ScimSchemaMeta`](../../doc/models/scim-schema-meta.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_schema import ScimSchema
from openapispecforclickhousecloud.models.scim_schema_attribute import ScimSchemaAttribute
from openapispecforclickhousecloud.models.scim_schema_meta import ScimSchemaMeta
from openapispecforclickhousecloud.models.scim_schema_sub_attribute import ScimSchemaSubAttribute

scim_schema = ScimSchema(
    schemas=[
        'schemas7',
        'schemas8'
    ],
    id='id8',
    name='name8',
    description='description8',
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
```

