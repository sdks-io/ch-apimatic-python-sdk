
# Scim User Meta

*This model accepts additional fields of type Any.*

## Structure

`ScimUserMeta`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `resource_type` | `str` | Required | The name of the resource type of the resource. |
| `created` | `datetime` | Required | The DateTime the Resource was added to the Service Provider. |
| `last_modified` | `datetime` | Required | The most recent DateTime the details of this Resource were updated. |
| `location` | `str` | Optional | The URI of the resource being returned. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.scim_user_meta import ScimUserMeta

scim_user_meta = ScimUserMeta(
    resource_type='resourceType0',
    created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    last_modified=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    location='location0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

