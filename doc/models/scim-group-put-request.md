
# Scim Group Put Request

*This model accepts additional fields of type Any.*

## Structure

`ScimGroupPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schemas` | `List[str]` | Required | SCIM schema URIs. Must include "urn:ietf:params:scim:schemas:core:2.0:Group". |
| `external_id` | `str` | Optional | Identifier for the resource as defined by the provisioning client. |
| `display_name` | `str` | Required | Human-readable name for the Group. Maps to Role name. |
| `members` | [`List[ScimGroupMember]`](../../doc/models/scim-group-member.md) | Optional | Members of the Group. |
| `id` | `str` | Optional | Server-assigned resource ID echoed back by the IdP. Ignored on write. |
| `meta` | [`ScimGroupMeta`](../../doc/models/scim-group-meta.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.scim_group_member import ScimGroupMember
from openapispecforclickhousecloud.models.scim_group_meta import ScimGroupMeta
from openapispecforclickhousecloud.models.scim_group_put_request import ScimGroupPutRequest

scim_group_put_request = ScimGroupPutRequest(
    schemas=[
        'urn:ietf:params:scim:schemas:core:2.0:Group'
    ],
    display_name='displayName0',
    external_id='externalId8',
    members=[
        ScimGroupMember(
            value='value0',
            display='display0',
            mtype='type2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ScimGroupMember(
            value='value0',
            display='display0',
            mtype='type2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    id='id2',
    meta=ScimGroupMeta(
        resource_type='resourceType6',
        created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        last_modified=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
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

