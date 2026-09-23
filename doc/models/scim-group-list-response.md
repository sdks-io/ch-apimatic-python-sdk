
# Scim Group List Response

*This model accepts additional fields of type Any.*

## Structure

`ScimGroupListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schemas` | `List[str]` | Required | Must be ["urn:ietf:params:scim:api:messages:2.0:ListResponse"]. |
| `total_results` | `int` | Required | Total number of Groups matching the query. |
| `start_index` | `int` | Required | 1-based index of the first result in the current set. |
| `items_per_page` | `int` | Required | Number of resources returned in this response. |
| `resources` | [`List[ScimGroup]`](../../doc/models/scim-group.md) | Required | Array of SCIM Group resources. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.scim_group import ScimGroup
from openapispecforclickhousecloud.models.scim_group_list_response import ScimGroupListResponse
from openapispecforclickhousecloud.models.scim_group_member import ScimGroupMember
from openapispecforclickhousecloud.models.scim_group_meta import ScimGroupMeta

scim_group_list_response = ScimGroupListResponse(
    schemas=[
        'schemas9'
    ],
    total_results=130,
    start_index=248,
    items_per_page=244,
    resources=[
        ScimGroup(
            schemas=[
                'urn:ietf:params:scim:schemas:core:2.0:Group'
            ],
            id='00000286-0000-0000-0000-000000000000',
            display_name='displayName6',
            meta=ScimGroupMeta(
                resource_type='resourceType6',
                created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                last_modified=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                location='location6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            external_id='externalId8',
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

