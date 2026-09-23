# Query AP Iendpoints

```python
query_ap_iendpoints_api = client.query_ap_iendpoints
```

## Class Name

`QueryApIendpointsApi`

## Methods

* [Query Api Endpoint Create](../../doc/controllers/query-ap-iendpoints.md#query-api-endpoint-create)
* [Query Api Endpoint List](../../doc/controllers/query-ap-iendpoints.md#query-api-endpoint-list)
* [Query Api Endpoint Delete](../../doc/controllers/query-ap-iendpoints.md#query-api-endpoint-delete)
* [Query Api Endpoint Get](../../doc/controllers/query-ap-iendpoints.md#query-api-endpoint-get)
* [Query Api Endpoint Update](../../doc/controllers/query-ap-iendpoints.md#query-api-endpoint-update)


# Query Api Endpoint Create

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates a Query API endpoint.

```python
def query_api_endpoint_create(self,
                             organization_id,
                             service_id,
                             body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `service_id` | `uuid\|str` | Template, Required | ID of the requested service. |
| `body` | [`PublicQueryApiEndpointRequest`](../../doc/models/public-query-api-endpoint-request.md) | Body, Optional | - |

## Response Type

**201**: The Query API endpoint was created.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesQueryApiEndpointsResponse`](../../doc/models/v1-organizations-services-query-api-endpoints-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = query_api_endpoints_api.query_api_endpoint_create(
    organization_id,
    service_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. | [`V1OrganizationsServicesQueryApiEndpoints400ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-400-error-exception.md) |
| 403 | The request is forbidden. | [`V1OrganizationsServicesQueryApiEndpoints403ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-403-error-exception.md) |
| 404 | Service not found. | [`V1OrganizationsServicesQueryApiEndpoints404ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-404-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesQueryApiEndpoints500ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-500-error-exception.md) |


# Query Api Endpoint List

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns all active Query API endpoints for the service.

```python
def query_api_endpoint_list(self,
                           organization_id,
                           service_id,
                           cursor=None,
                           limit=100)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `service_id` | `uuid\|str` | Template, Required | ID of the requested service. |
| `cursor` | `str` | Query, Optional | Cursor returned in `pagination.nextCursor` from the previous page. |
| `limit` | `int` | Query, Optional | Maximum number of records to return per page. Defaults to 100. Maximum is 100.<br><br>**Default**: `100`<br><br>**Constraints**: `>= 1`, `<= 100` |

## Response Type

**200**: Successful response.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesQueryApiEndpointsResponse1`](../../doc/models/v1-organizations-services-query-api-endpoints-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

limit = 100

result = query_api_endpoints_api.query_api_endpoint_list(
    organization_id,
    service_id,
    limit=limit
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. | [`V1OrganizationsServicesQueryApiEndpoints400ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-400-error-exception.md) |
| 403 | The request is forbidden. | [`V1OrganizationsServicesQueryApiEndpoints403ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-403-error-exception.md) |
| 404 | Service not found. | [`V1OrganizationsServicesQueryApiEndpoints404ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-404-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesQueryApiEndpoints500ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-500-error-exception.md) |


# Query Api Endpoint Delete

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes a Query API endpoint.

```python
def query_api_endpoint_delete(self,
                             organization_id,
                             service_id,
                             endpoint_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `service_id` | `uuid\|str` | Template, Required | ID of the requested service. |
| `endpoint_id` | `uuid\|str` | Template, Required | ID of the requested Query API endpoint. |

## Response Type

**200**: The Query API endpoint was deleted.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse`](../../doc/models/v1-organizations-services-query-api-endpoints-endpoint-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

endpoint_id = '00001c70-0000-0000-0000-000000000000'

result = query_api_endpoints_api.query_api_endpoint_delete(
    organization_id,
    service_id,
    endpoint_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesQueryApiEndpointsEndpointId400ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-endpoint-id-400-error-exception.md) |
| 403 | The request is forbidden. | [`V1OrganizationsServicesQueryApiEndpointsEndpointId403ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-endpoint-id-403-error-exception.md) |
| 404 | Query API endpoint not found. | [`V1OrganizationsServicesQueryApiEndpointsEndpointId404ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-endpoint-id-404-error-exception.md) |
| 409 | Query API endpoint can not be managed via this API. | [`V1OrganizationsServicesQueryApiEndpointsEndpointId409ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-endpoint-id-409-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesQueryApiEndpointsEndpointId500ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-endpoint-id-500-error-exception.md) |


# Query Api Endpoint Get

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns a Query API endpoint.

```python
def query_api_endpoint_get(self,
                          organization_id,
                          service_id,
                          endpoint_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `service_id` | `uuid\|str` | Template, Required | ID of the requested service. |
| `endpoint_id` | `uuid\|str` | Template, Required | ID of the requested Query API endpoint. |

## Response Type

**200**: Successful response.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1`](../../doc/models/v1-organizations-services-query-api-endpoints-endpoint-id-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

endpoint_id = '00001c70-0000-0000-0000-000000000000'

result = query_api_endpoints_api.query_api_endpoint_get(
    organization_id,
    service_id,
    endpoint_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesQueryApiEndpointsEndpointId400ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-endpoint-id-400-error-exception.md) |
| 403 | The request is forbidden. | [`V1OrganizationsServicesQueryApiEndpointsEndpointId403ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-endpoint-id-403-error-exception.md) |
| 404 | Query API endpoint not found. | [`V1OrganizationsServicesQueryApiEndpointsEndpointId404ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-endpoint-id-404-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesQueryApiEndpointsEndpointId500ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-endpoint-id-500-error-exception.md) |


# Query Api Endpoint Update

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Updates a Query API endpoint.

```python
def query_api_endpoint_update(self,
                             organization_id,
                             service_id,
                             endpoint_id,
                             body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `service_id` | `uuid\|str` | Template, Required | ID of the requested service. |
| `endpoint_id` | `uuid\|str` | Template, Required | ID of the requested Query API endpoint. |
| `body` | [`PublicQueryApiEndpointRequest`](../../doc/models/public-query-api-endpoint-request.md) | Body, Optional | - |

## Response Type

**200**: The Query API endpoint was updated.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1`](../../doc/models/v1-organizations-services-query-api-endpoints-endpoint-id-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

endpoint_id = '00001c70-0000-0000-0000-000000000000'

result = query_api_endpoints_api.query_api_endpoint_update(
    organization_id,
    service_id,
    endpoint_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. | [`V1OrganizationsServicesQueryApiEndpointsEndpointId400Error3Exception`](../../doc/models/v1-organizations-services-query-api-endpoints-endpoint-id-400-error-3-exception.md) |
| 403 | The request is forbidden. | [`V1OrganizationsServicesQueryApiEndpointsEndpointId403ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-endpoint-id-403-error-exception.md) |
| 404 | Query API endpoint not found. | [`V1OrganizationsServicesQueryApiEndpointsEndpointId404ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-endpoint-id-404-error-exception.md) |
| 409 | Query API endpoint can not be managed via this API. | [`V1OrganizationsServicesQueryApiEndpointsEndpointId409ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-endpoint-id-409-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesQueryApiEndpointsEndpointId500ErrorException`](../../doc/models/v1-organizations-services-query-api-endpoints-endpoint-id-500-error-exception.md) |

