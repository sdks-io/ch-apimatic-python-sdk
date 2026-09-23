
# Scim Group

*This model accepts additional fields of type Any.*

## Structure

`ScimGroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schemas` | `List[str]` | Required | SCIM schema URIs. Must include "urn:ietf:params:scim:schemas:core:2.0:Group". |
| `id` | `uuid\|str` | Required | Unique identifier for this Group (corresponds to Role ID). |
| `external_id` | `str` | Optional | Identifier for the resource as defined by the provisioning client. |
| `display_name` | `str` | Required | Human-readable name for the Group. Maps to Role name. |
| `members` | [`List[ScimGroupMember]`](../../doc/models/scim-group-member.md) | Optional | Members of the Group. |
| `meta` | [`ScimGroupMeta`](../../doc/models/scim-group-meta.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.scim_group import ScimGroup
from openapispecforclickhousecloud.models.scim_group_member import ScimGroupMember
from openapispecforclickhousecloud.models.scim_group_meta import ScimGroupMeta

scim_group = ScimGroup(
    schemas=[
        'urn:ietf:params:scim:schemas:core:2.0:Group'
    ],
    id='00001c2e-0000-0000-0000-000000000000',
    display_name='displayName8',
    meta=ScimGroupMeta(
        resource_type='resourceType6',
        created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        last_modified=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        location='location6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    external_id='externalId0',
    members=[
        ScimGroupMember(
            value='value0',
            display='display0',
            mtype='type2',
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

