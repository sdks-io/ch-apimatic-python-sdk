
# V1 Organizations Services Query Api Endpoints Response 1

## Structure

`V1OrganizationsServicesQueryApiEndpointsResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `int` | Required | HTTP status code. |
| `request_id` | `uuid\|str` | Required | Unique id assigned to every request. UUIDv4 |
| `result` | [`QueryApiEndpointListResponse`](../../doc/models/query-api-endpoint-list-response.md) | Required | - |

## Example

```python
from openapispecforclickhousecloud.models.owner_type import OwnerType
from openapispecforclickhousecloud.models.pagination import Pagination
from openapispecforclickhousecloud.models.public_query_api_endpoint_list_item import PublicQueryApiEndpointListItem
from openapispecforclickhousecloud.models.query_api_endpoint_list_response import QueryApiEndpointListResponse
from openapispecforclickhousecloud.models.v_1_organizations_services_query_api_endpoints_response_1 import V1OrganizationsServicesQueryApiEndpointsResponse1

v_1_organizations_services_query_api_endpoints_response_1 = V1OrganizationsServicesQueryApiEndpointsResponse1(
    status=200,
    request_id='00000b20-0000-0000-0000-000000000000',
    result=QueryApiEndpointListResponse(
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
)
```

