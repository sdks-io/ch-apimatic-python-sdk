
# Scim List Response

*This model accepts additional fields of type Any.*

## Structure

`ScimListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `schemas` | `List[str]` | Required | Must be ["urn:ietf:params:scim:api:messages:2.0:ListResponse"]. |
| `total_results` | `int` | Required | Total number of results matching the query. |
| `start_index` | `int` | Required | 1-based index of the first result in the current set. |
| `items_per_page` | `int` | Required | Number of resources returned in this response. |
| `resources` | [`List[ScimUser]`](../../doc/models/scim-user.md) | Required | Array of SCIM User resources. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.scim_list_response import ScimListResponse
from openapispecforclickhousecloud.models.scim_user import ScimUser
from openapispecforclickhousecloud.models.scim_user_email import ScimUserEmail
from openapispecforclickhousecloud.models.scim_user_meta import ScimUserMeta
from openapispecforclickhousecloud.models.scim_user_name import ScimUserName

scim_list_response = ScimListResponse(
    schemas=[
        'schemas3',
        'schemas4',
        'schemas5'
    ],
    total_results=8,
    start_index=146,
    items_per_page=150,
    resources=[
        ScimUser(
            schemas=[
                'urn:ietf:params:scim:schemas:core:2.0:User'
            ],
            id='samlp|b7a3c2d1-4e5f-6a7b-8c9d-0e1f2a3b4c5d|user@example.com',
            user_name='user@example.com',
            name=ScimUserName(
                formatted='formatted2',
                family_name='familyName8',
                given_name='givenName4',
                middle_name='middleName8',
                honorific_prefix='honorificPrefix4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            active=False,
            emails=[
                ScimUserEmail(
                    value='value8',
                    mtype='type6',
                    primary=False,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            meta=ScimUserMeta(
                resource_type='resourceType6',
                created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                last_modified=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                location='location6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            external_id='ext-user-001',
            display_name='displayName6',
            nick_name='nickName8',
            profile_url='profileUrl0',
            title='title2',
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

