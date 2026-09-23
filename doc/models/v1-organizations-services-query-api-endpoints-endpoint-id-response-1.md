
# V1 Organizations Services Query Api Endpoints Endpoint Id Response 1

## Structure

`V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1`

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
from openapispecforclickhousecloud.models.v_1_organizations_services_query_api_endpoints_endpoint_id_response_1 import V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1

v_1_organizations_services_query_api_endpoints_endpoint_id_response_1 = V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1(
    status=200,
    request_id='00001974-0000-0000-0000-000000000000',
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

