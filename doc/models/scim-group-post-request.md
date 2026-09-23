
# Scim Group Post Request

*This model accepts additional fields of type Any.*

## Structure

`ScimGroupPostRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schemas` | `List[str]` | Required | SCIM schema URIs. Must include "urn:ietf:params:scim:schemas:core:2.0:Group". |
| `external_id` | `str` | Optional | Identifier for the resource as defined by the provisioning client. |
| `display_name` | `str` | Required | Human-readable name for the Group. Maps to Role name. |
| `members` | [`List[ScimGroupMember]`](../../doc/models/scim-group-member.md) | Optional | Members of the Group. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_group_member import ScimGroupMember
from openapispecforclickhousecloud.models.scim_group_post_request import ScimGroupPostRequest

scim_group_post_request = ScimGroupPostRequest(
    schemas=[
        'urn:ietf:params:scim:schemas:core:2.0:Group'
    ],
    display_name='displayName4',
    external_id='externalId2',
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

