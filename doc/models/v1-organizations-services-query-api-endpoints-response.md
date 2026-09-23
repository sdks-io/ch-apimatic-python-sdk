
# V1 Organizations Services Query Api Endpoints Response

## Structure

`V1OrganizationsServicesQueryApiEndpointsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `int` | Required | HTTP status code. |
| `request_id` | `uuid\|str` | Required | Unique id assigned to every request. UUIDv4 |
| `result` | [`PublicQueryApiEndpoint`](../../doc/models/public-query-api-endpoint.md) | Required | - |

## Example

```python
from openapispecforclickhousecloud.models.owner_type import OwnerType
from openapispecforclickhousecloud.models.public_query_api_endpoint import PublicQueryApiEndpoint
from openapispecforclickhousecloud.models.v_1_organizations_services_query_api_endpoints_response import V1OrganizationsServicesQueryApiEndpointsResponse

v_1_organizations_services_query_api_endpoints_response = V1OrganizationsServicesQueryApiEndpointsResponse(
    status=201,
    request_id='00000adc-0000-0000-0000-000000000000',
    result=PublicQueryApiEndpoint(
        id='000002b8-0000-0000-0000-000000000000',
        name='name6',
        sql='sql4',
        database='database6',
        parameters={
            'key0': 'parameters2',
            'key1': 'parameters3',
            'key2': 'parameters4'
        },
        api_key_ids=[
            '00000332-0000-0000-0000-000000000000'
        ],
        roles=[
            'roles0',
            'roles9',
            'roles8'
        ],
        allowed_origins=[
            'allowedOrigins0',
            'allowedOrigins1'
        ],
        url='https://queries.clickhouse.cloud/run/00000000-0000-0000-0000-000000000000',
        owner_type=OwnerType.USER
    )
)
```

