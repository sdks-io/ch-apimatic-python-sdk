
# Query Api Endpoint List Response

## Structure

`QueryApiEndpointListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List[PublicQueryApiEndpointListItem]`](../../doc/models/public-query-api-endpoint-list-item.md) | Required | Active Query API endpoints for the service, including both owner types. |
| `pagination` | [`Pagination`](../../doc/models/pagination.md) | Required | - |

## Example

```python
from openapispecforclickhousecloud.models.owner_type import OwnerType
from openapispecforclickhousecloud.models.pagination import Pagination
from openapispecforclickhousecloud.models.public_query_api_endpoint_list_item import PublicQueryApiEndpointListItem
from openapispecforclickhousecloud.models.query_api_endpoint_list_response import QueryApiEndpointListResponse

query_api_endpoint_list_response = QueryApiEndpointListResponse(
    items=[
        PublicQueryApiEndpointListItem(
            id='00000422-0000-0000-0000-000000000000',
            name='name8',
            database='database2',
            api_key_ids=[
                '00002274-0000-0000-0000-000000000000',
                '00002275-0000-0000-0000-000000000000'
            ],
            roles=[
                'roles8'
            ],
            allowed_origins=[
                'allowedOrigins6'
            ],
            url='https://queries.clickhouse.cloud/run/00000000-0000-0000-0000-000000000000',
            owner_type=OwnerType.USER
        )
    ],
    pagination=Pagination(
        total_records=72,
        current_cursor='String5',
        next_cursor='String1',
        limit=80
    )
)
```

