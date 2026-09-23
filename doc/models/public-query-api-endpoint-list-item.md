
# Public Query Api Endpoint List Item

## Structure

`PublicQueryApiEndpointListItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Required | Unique ID of the Query API endpoint. |
| `name` | `str` | Required | Name of the Query API endpoint. |
| `database` | `str` | Required | Database used by the Query API endpoint. |
| `api_key_ids` | `List[uuid\|str]` | Required | API key IDs allowed to call the endpoint. |
| `roles` | `List[str]` | Required | Database roles used by the endpoint. |
| `allowed_origins` | `List[str]` | Required | Origins allowed by the endpoint CORS policy. |
| `url` | `str` | Required | Public URL used to execute the endpoint. |
| `owner_type` | [`OwnerType`](../../doc/models/owner-type.md) | Required | Owner type of the Query API endpoint. Endpoints with a user owned query cannot be updated or deleted through this API. |

## Example

```python
from openapispecforclickhousecloud.models.owner_type import OwnerType
from openapispecforclickhousecloud.models.public_query_api_endpoint_list_item import PublicQueryApiEndpointListItem

public_query_api_endpoint_list_item = PublicQueryApiEndpointListItem(
    id='0000142c-0000-0000-0000-000000000000',
    name='name4',
    database='database4',
    api_key_ids=[
        '0000126a-0000-0000-0000-000000000000',
        '0000126b-0000-0000-0000-000000000000',
        '0000126c-0000-0000-0000-000000000000'
    ],
    roles=[
        'roles2',
        'roles3'
    ],
    allowed_origins=[
        'allowedOrigins2',
        'allowedOrigins1'
    ],
    url='https://queries.clickhouse.cloud/run/00000000-0000-0000-0000-000000000000',
    owner_type=OwnerType.USER
)
```

