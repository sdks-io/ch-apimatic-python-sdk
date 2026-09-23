
# Scim Schema Attribute

*This model accepts additional fields of type Any.*

## Structure

`ScimSchemaAttribute`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | The attribute name. |
| `mtype` | `str` | Required | The attribute type (e.g., "string", "boolean", "complex"). |
| `sub_attributes` | [`List[ScimSchemaSubAttribute]`](../../doc/models/scim-schema-sub-attribute.md) | Optional | Sub-attributes for complex attributes. |
| `multi_valued` | `bool` | Required | Whether the attribute can have multiple values. |
| `description` | `str` | Required | A human-readable description of the attribute. |
| `required` | `bool` | Required | Whether the attribute is required. |
| `case_exact` | `bool` | Optional | Whether the string attribute is case sensitive. |
| `mutability` | `str` | Required | The circumstances under which the value of the attribute can be (re)defined. |
| `returned` | `str` | Required | The circumstances under which an attribute and associated values are returned. |
| `uniqueness` | `str` | Optional | How the service provider enforces uniqueness of attribute values. |
| `reference_types` | `List[str]` | Optional | A multi-valued array of JSON strings. |
| `canonical_values` | `List[str]` | Optional | A collection of suggested canonical values that MAY be used. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_schema_attribute import ScimSchemaAttribute
from openapispecforclickhousecloud.models.scim_schema_sub_attribute import ScimSchemaSubAttribute

scim_schema_attribute = ScimSchemaAttribute(
    name='name0',
    mtype='type0',
    multi_valued=False,
    description='description0',
    required=False,
    mutability='mutability6',
    returned='returned8',
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
        ),
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
    uniqueness='uniqueness6',
    reference_types=[
        'referenceTypes6',
        'referenceTypes7',
        'referenceTypes8'
    ],
    canonical_values=[
        'canonicalValues0',
        'canonicalValues1'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

