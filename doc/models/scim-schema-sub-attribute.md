
# Scim Schema Sub Attribute

A sub-attribute of a complex SCIM schema attribute. Per RFC 7643, sub-attributes cannot themselves have sub-attributes.

*This model accepts additional fields of type Any.*

## Structure

`ScimSchemaSubAttribute`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | The attribute name. |
| `mtype` | `str` | Required | The attribute type (e.g., "string", "boolean", "complex"). |
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

from openapispecforclickhousecloud.models.scim_schema_sub_attribute import ScimSchemaSubAttribute

scim_schema_sub_attribute = ScimSchemaSubAttribute(
    name='name2',
    mtype='type8',
    multi_valued=False,
    description='description8',
    required=False,
    mutability='mutability8',
    returned='returned0',
    case_exact=False,
    uniqueness='uniqueness8',
    reference_types=[
        'referenceTypes6'
    ],
    canonical_values=[
        'canonicalValues8',
        'canonicalValues9'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

