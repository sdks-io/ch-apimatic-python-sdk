
# Scim Group Meta

*This model accepts additional fields of type Any.*

## Structure

`ScimGroupMeta`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `resource_type` | `str` | Required | Always "Group". |
| `created` | `datetime` | Required | DateTime the Group was created. |
| `last_modified` | `datetime` | Required | DateTime the Group was last modified. |
| `location` | `str` | Optional | The URI of this Group resource. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.scim_group_meta import ScimGroupMeta

scim_group_meta = ScimGroupMeta(
    resource_type='resourceType6',
    created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    last_modified=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    location='location6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

