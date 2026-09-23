# Organization

```python
organization_api = client.organization
```

## Class Name

`OrganizationApi`

## Methods

* [Organization Get List](../../doc/controllers/organization.md#organization-get-list)
* [Organization Get](../../doc/controllers/organization.md#organization-get)
* [Organization Update](../../doc/controllers/organization.md#organization-update)
* [Organization Quotas Get List](../../doc/controllers/organization.md#organization-quotas-get-list)
* [Organization Quota Get](../../doc/controllers/organization.md#organization-quota-get)
* [Activity Get List](../../doc/controllers/organization.md#activity-get-list)
* [Activity Get](../../doc/controllers/organization.md#activity-get)
* [Organization Private Endpoint Config Get List](../../doc/controllers/organization.md#organization-private-endpoint-config-get-list)
* [Organization Byoc Infrastructure Create](../../doc/controllers/organization.md#organization-byoc-infrastructure-create)
* [Organization Byoc Infrastructure Delete](../../doc/controllers/organization.md#organization-byoc-infrastructure-delete)
* [Organization Byoc Infrastructure Update](../../doc/controllers/organization.md#organization-byoc-infrastructure-update)


# Organization Get List

Returns a list with a single organization associated with the API key in the request.

```python
def organization_get_list(self)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsResponse`](../../doc/models/v1-organizations-response.md).

## Example Usage

```python
result = organization_api.organization_get_list()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1Organizations400ErrorException`](../../doc/models/v1-organizations-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1Organizations500ErrorException`](../../doc/models/v1-organizations-500-error-exception.md) |


# Organization Get

Returns details of a single organization. In order to get the details, the auth key must belong to the organization.

```python
def organization_get(self,
                    organization_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsResponse1`](../../doc/models/v1-organizations-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

result = organization_api.organization_get(organization_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1Organizations400ErrorException`](../../doc/models/v1-organizations-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1Organizations500ErrorException`](../../doc/models/v1-organizations-500-error-exception.md) |


# Organization Update

Updates organization fields. Requires ADMIN auth key role.

```python
def organization_update(self,
                       organization_id,
                       body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization to update. |
| `body` | [`OrganizationPatchRequest`](../../doc/models/organization-patch-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsResponse1`](../../doc/models/v1-organizations-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

result = organization_api.organization_update(organization_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1Organizations400ErrorException`](../../doc/models/v1-organizations-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1Organizations500ErrorException`](../../doc/models/v1-organizations-500-error-exception.md) |


# Organization Quotas Get List

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the resource quotas enforced for the organization together with their current usage where available. Quotas that do not apply to the organization are omitted. Quota values reflect the limits currently enforced, so they can be polled to detect changes, for example after a billing status change. The response contains one entry per quota code; quotas enforced per resource may additionally appear under resource-scoped endpoints in the future.

```python
def organization_quotas_get_list(self,
                                organization_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsQuotasResponse`](../../doc/models/v1-organizations-quotas-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

result = organization_api.organization_quotas_get_list(organization_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsQuotas400ErrorException`](../../doc/models/v1-organizations-quotas-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsQuotas500ErrorException`](../../doc/models/v1-organizations-quotas-500-error-exception.md) |


# Organization Quota Get

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns a single organization quota identified by its quota code. Responds with a not found error when the quota code is unknown or the quota does not apply to the organization.

```python
def organization_quota_get(self,
                          organization_id,
                          quota_code)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `quota_code` | `str` | Template, Required | Code of the requested quota. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsQuotasResponse1`](../../doc/models/v1-organizations-quotas-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

quota_code = 'quotaCode2'

result = organization_api.organization_quota_get(
    organization_id,
    quota_code
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsQuotas400ErrorException`](../../doc/models/v1-organizations-quotas-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsQuotas500ErrorException`](../../doc/models/v1-organizations-quotas-500-error-exception.md) |


# Activity Get List

Returns a list of all organization activities.

```python
def activity_get_list(self,
                     organization_id,
                     from_date=None,
                     to_date=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `from_date` | `datetime` | Query, Optional | A starting date for a search |
| `to_date` | `datetime` | Query, Optional | An ending date for a search |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsActivitiesResponse`](../../doc/models/v1-organizations-activities-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

result = organization_api.activity_get_list(organization_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsActivities400ErrorException`](../../doc/models/v1-organizations-activities-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsActivities500ErrorException`](../../doc/models/v1-organizations-activities-500-error-exception.md) |


# Activity Get

Returns a single organization activity by ID.

```python
def activity_get(self,
                organization_id,
                activity_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `activity_id` | `str` | Template, Required | ID of the requested activity. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsActivitiesResponse1`](../../doc/models/v1-organizations-activities-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

activity_id = 'activityId2'

result = organization_api.activity_get(
    organization_id,
    activity_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsActivities400ErrorException`](../../doc/models/v1-organizations-activities-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsActivities500ErrorException`](../../doc/models/v1-organizations-activities-500-error-exception.md) |


# Organization Private Endpoint Config Get List

**This endpoint is deprecated.**

Deprecated. Please follow [documentation](https://clickhouse.com/docs/manage/security/aws-privatelink#add-endpoint-id-to-services-allow-list) for the updated process.

```python
def organization_private_endpoint_config_get_list(self,
                                                 organization_id,
                                                 cloud_provider,
                                                 region_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `cloud_provider` | `str` | Query, Required | Cloud provider identifier. One of aws, gcp, or azure. |
| `region_id` | `str` | Query, Required | Region identifier within specific cloud providers. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsPrivateEndpointConfigResponse`](../../doc/models/v1-organizations-private-endpoint-config-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

cloud_provider = 'cloud_provider6'

region_id = 'region_id6'

result = organization_api.organization_private_endpoint_config_get_list(
    organization_id,
    cloud_provider,
    region_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPrivateEndpointConfig400ErrorException`](../../doc/models/v1-organizations-private-endpoint-config-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPrivateEndpointConfig500ErrorException`](../../doc/models/v1-organizations-private-endpoint-config-500-error-exception.md) |


# Organization Byoc Infrastructure Create

Create a new BYOC Infrastructure in the organization. Returns the configuration of the newly created infrastructure

```python
def organization_byoc_infrastructure_create(self,
                                           organization_id,
                                           body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `body` | [`ByocInfrastructurePostRequest`](../../doc/models/byoc-infrastructure-post-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsByocInfrastructureResponse`](../../doc/models/v1-organizations-byoc-infrastructure-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

result = organization_api.organization_byoc_infrastructure_create(organization_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsByocInfrastructure400ErrorException`](../../doc/models/v1-organizations-byoc-infrastructure-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsByocInfrastructure500ErrorException`](../../doc/models/v1-organizations-byoc-infrastructure-500-error-exception.md) |


# Organization Byoc Infrastructure Delete

Removes a BYOC Infrastructure from the organization

```python
def organization_byoc_infrastructure_delete(self,
                                           organization_id,
                                           byoc_infrastructure_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `byoc_infrastructure_id` | `uuid\|str` | Template, Required | ID of the requested BYOC Infrastructure |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsByocInfrastructureResponse1`](../../doc/models/v1-organizations-byoc-infrastructure-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

byoc_infrastructure_id = '00000e02-0000-0000-0000-000000000000'

result = organization_api.organization_byoc_infrastructure_delete(
    organization_id,
    byoc_infrastructure_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsByocInfrastructure400ErrorException`](../../doc/models/v1-organizations-byoc-infrastructure-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsByocInfrastructure500ErrorException`](../../doc/models/v1-organizations-byoc-infrastructure-500-error-exception.md) |


# Organization Byoc Infrastructure Update

Update configuration of the BYOC infrastructure. Returns the modified infrastructure

```python
def organization_byoc_infrastructure_update(self,
                                           organization_id,
                                           byoc_infrastructure_id,
                                           body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `byoc_infrastructure_id` | `uuid\|str` | Template, Required | ID of the requested BYOC Infrastructure |
| `body` | [`ByocInfrastructurePatchRequest`](../../doc/models/byoc-infrastructure-patch-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsByocInfrastructureResponse`](../../doc/models/v1-organizations-byoc-infrastructure-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

byoc_infrastructure_id = '00000e02-0000-0000-0000-000000000000'

result = organization_api.organization_byoc_infrastructure_update(
    organization_id,
    byoc_infrastructure_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsByocInfrastructure400ErrorException`](../../doc/models/v1-organizations-byoc-infrastructure-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsByocInfrastructure500ErrorException`](../../doc/models/v1-organizations-byoc-infrastructure-500-error-exception.md) |

