
# V1 Organizations Services Query Api Endpoints Endpoint Id Response

## Structure

`V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `int` | Required | HTTP status code. |
| `request_id` | `uuid\|str` | Required | Unique id assigned to every request. UUIDv4 |

## Example

```python
from openapispecforclickhousecloud.models.v_1_organizations_services_query_api_endpoints_endpoint_id_response import V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse

v_1_organizations_services_query_api_endpoints_endpoint_id_response = V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse(
    status=200,
    request_id='000007cc-0000-0000-0000-000000000000'
)
```

