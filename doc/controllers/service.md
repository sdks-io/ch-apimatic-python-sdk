# Service

```python
service_api = client.service
```

## Class Name

`ServiceApi`

## Methods

* [Service Profiles List](../../doc/controllers/service.md#service-profiles-list)
* [Instance Get List](../../doc/controllers/service.md#instance-get-list)
* [Instance Create](../../doc/controllers/service.md#instance-create)
* [Instance Get](../../doc/controllers/service.md#instance-get)
* [Instance Update](../../doc/controllers/service.md#instance-update)
* [Instance Delete](../../doc/controllers/service.md#instance-delete)
* [Instance Private Endpoint Config Get](../../doc/controllers/service.md#instance-private-endpoint-config-get)
* [Instance Query Endpoint Get](../../doc/controllers/service.md#instance-query-endpoint-get)
* [Instance Query Endpoint Delete](../../doc/controllers/service.md#instance-query-endpoint-delete)
* [Instance Query Endpoint Upsert](../../doc/controllers/service.md#instance-query-endpoint-upsert)
* [Instance State Update](../../doc/controllers/service.md#instance-state-update)
* [Instance Scaling Update](../../doc/controllers/service.md#instance-scaling-update)
* [Instance Replica Scaling Update](../../doc/controllers/service.md#instance-replica-scaling-update)
* [Instance Password Update](../../doc/controllers/service.md#instance-password-update)
* [Instance Private Endpoint Create](../../doc/controllers/service.md#instance-private-endpoint-create)
* [Scaling Schedule Get](../../doc/controllers/service.md#scaling-schedule-get)
* [Scaling Schedule Upsert](../../doc/controllers/service.md#scaling-schedule-upsert)
* [Scaling Schedule Delete](../../doc/controllers/service.md#scaling-schedule-delete)
* [Upgrade Window Get](../../doc/controllers/service.md#upgrade-window-get)
* [Upgrade Window Update](../../doc/controllers/service.md#upgrade-window-update)
* [Upgrade Window Delete](../../doc/controllers/service.md#upgrade-window-delete)
* [Service Clickhouse Settings List Get](../../doc/controllers/service.md#service-clickhouse-settings-list-get)
* [Service Clickhouse Settings Update](../../doc/controllers/service.md#service-clickhouse-settings-update)
* [Service Clickhouse Settings Schema Get](../../doc/controllers/service.md#service-clickhouse-settings-schema-get)
* [Service Clickhouse Setting Get](../../doc/controllers/service.md#service-clickhouse-setting-get)
* [Service Clickhouse Setting Delete](../../doc/controllers/service.md#service-clickhouse-setting-delete)


# Service Profiles List

Returns the custom instance profiles the organization can use in a region. Pass byoc_id to list the profiles configured for a BYOC infrastructure; the region is then taken from the infrastructure and region_id may be omitted. The list is empty when the organization tier does not include custom hardware profiles.

```python
def service_profiles_list(self,
                         organization_id,
                         region_id=None,
                         byoc_id=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization to list available profiles for. |
| `region_id` | `str` | Query, Optional | Region to list profiles for, e.g. us-east-1. Required unless byoc_id is set; when both are set it must match the BYOC infrastructure's region. |
| `byoc_id` | `uuid\|str` | Query, Optional | ID of the BYOC infrastructure to list profiles for. BYOC profiles are only returned when this is set. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServiceProfilesResponse`](../../doc/models/v1-organizations-service-profiles-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

result = service_api.service_profiles_list(organization_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServiceProfiles400ErrorException`](../../doc/models/v1-organizations-service-profiles-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServiceProfiles500ErrorException`](../../doc/models/v1-organizations-service-profiles-500-error-exception.md) |


# Instance Get List

Returns a list of all services in the organization.

```python
def instance_get_list(self,
                     organization_id,
                     filter=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `filter` | `List[str]` | Query, Optional | Filter criteria to apply when retrieving the resource. Currently, only filtering by resource tags is supported. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesResponse`](../../doc/models/v1-organizations-services-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

filter = [
    'tag:Environment=Production',
    'tag:Department=Engineering',
    'tag:isActive'
]

result = service_api.instance_get_list(
    organization_id,
    filter=filter
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServices400ErrorException`](../../doc/models/v1-organizations-services-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServices500ErrorException`](../../doc/models/v1-organizations-services-500-error-exception.md) |


# Instance Create

Creates a new service in the organization, and returns the current service state and a password to access the service. The service is started asynchronously.

```python
def instance_create(self,
                   organization_id,
                   body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that will own the service. |
| `body` | [`ServicePostRequest`](../../doc/models/service-post-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesResponse1`](../../doc/models/v1-organizations-services-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

body = ServicePostRequest(
    min_total_memory_gb=48,
    max_total_memory_gb=360,
    autoscaling_mode=AutoscalingMode4.VERTICAL,
    min_replica_memory_gb=16,
    max_replica_memory_gb=120,
    num_replicas=3,
    min_replicas=1,
    max_replicas=5
)

result = service_api.instance_create(
    organization_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServices400ErrorException`](../../doc/models/v1-organizations-services-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServices500ErrorException`](../../doc/models/v1-organizations-services-500-error-exception.md) |


# Instance Get

Returns a service that belongs to the organization

```python
def instance_get(self,
                organization_id,
                service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the requested service. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesResponse2`](../../doc/models/v1-organizations-services-response-2.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = service_api.instance_get(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServices400ErrorException`](../../doc/models/v1-organizations-services-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServices500ErrorException`](../../doc/models/v1-organizations-services-500-error-exception.md) |


# Instance Update

Updates basic service details like service name or IP access list.

```python
def instance_update(self,
                   organization_id,
                   service_id,
                   body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service to update. |
| `body` | [`ServicePatchRequest`](../../doc/models/service-patch-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesResponse2`](../../doc/models/v1-organizations-services-response-2.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = service_api.instance_update(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServices400ErrorException`](../../doc/models/v1-organizations-services-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServices500ErrorException`](../../doc/models/v1-organizations-services-500-error-exception.md) |


# Instance Delete

Deletes the service. The service must be in stopped state and is deleted asynchronously after this method call.

```python
def instance_delete(self,
                   organization_id,
                   service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service to delete. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesResponse4`](../../doc/models/v1-organizations-services-response-4.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = service_api.instance_delete(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServices400ErrorException`](../../doc/models/v1-organizations-services-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServices500ErrorException`](../../doc/models/v1-organizations-services-500-error-exception.md) |


# Instance Private Endpoint Config Get

Information required to set up a private endpoint

```python
def instance_private_endpoint_config_get(self,
                                        organization_id,
                                        service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `service_id` | `uuid\|str` | Template, Required | ID of the requested service. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesPrivateEndpointConfigResponse`](../../doc/models/v1-organizations-services-private-endpoint-config-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = service_api.instance_private_endpoint_config_get(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesPrivateEndpointConfig400ErrorException`](../../doc/models/v1-organizations-services-private-endpoint-config-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesPrivateEndpointConfig500ErrorException`](../../doc/models/v1-organizations-services-private-endpoint-config-500-error-exception.md) |


# Instance Query Endpoint Get

Get the configuration for the service query endpoint that allows executing queries via API.

```python
def instance_query_endpoint_get(self,
                               organization_id,
                               service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `service_id` | `uuid\|str` | Template, Required | ID of the requested service. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesServiceQueryEndpointResponse`](../../doc/models/v1-organizations-services-service-query-endpoint-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = service_api.instance_query_endpoint_get(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesServiceQueryEndpoint400ErrorException`](../../doc/models/v1-organizations-services-service-query-endpoint-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesServiceQueryEndpoint500ErrorException`](../../doc/models/v1-organizations-services-service-query-endpoint-500-error-exception.md) |


# Instance Query Endpoint Delete

Removes the service query endpoint.

```python
def instance_query_endpoint_delete(self,
                                  organization_id,
                                  service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `service_id` | `uuid\|str` | Template, Required | ID of the requested service. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesServiceQueryEndpointResponse1`](../../doc/models/v1-organizations-services-service-query-endpoint-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = service_api.instance_query_endpoint_delete(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesServiceQueryEndpoint400ErrorException`](../../doc/models/v1-organizations-services-service-query-endpoint-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesServiceQueryEndpoint500ErrorException`](../../doc/models/v1-organizations-services-service-query-endpoint-500-error-exception.md) |


# Instance Query Endpoint Upsert

Create the service query endpoint that allows executing queries via API.

```python
def instance_query_endpoint_upsert(self,
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
| `body` | [`InstanceServiceQueryApiEndpointsPostRequest`](../../doc/models/instance-service-query-api-endpoints-post-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesServiceQueryEndpointResponse`](../../doc/models/v1-organizations-services-service-query-endpoint-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = service_api.instance_query_endpoint_upsert(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesServiceQueryEndpoint400ErrorException`](../../doc/models/v1-organizations-services-service-query-endpoint-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesServiceQueryEndpoint500ErrorException`](../../doc/models/v1-organizations-services-service-query-endpoint-500-error-exception.md) |


# Instance State Update

Starts, stops, or wakes a service. The `start` and `stop` commands require the `control-plane:service:manage` permission on the service. The `awake` command requires only `control-plane:service:view` and applies to an idle service; it does not start a stopped service.

```python
def instance_state_update(self,
                         organization_id,
                         service_id,
                         body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service to update state. |
| `body` | [`ServiceStatePatchRequest`](../../doc/models/service-state-patch-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesStateResponse`](../../doc/models/v1-organizations-services-state-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = service_api.instance_state_update(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesState400ErrorException`](../../doc/models/v1-organizations-services-state-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesState500ErrorException`](../../doc/models/v1-organizations-services-state-500-error-exception.md) |


# Instance Scaling Update

**This endpoint is deprecated.**

Updates minimum and maximum total memory limits and idle mode scaling behavior for the service. The memory settings are available only for "production" services and must be a multiple of 12 starting from 24GB. Please contact support to enable adjustment of numReplicas.

```python
def instance_scaling_update(self,
                           organization_id,
                           service_id,
                           body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service to update scaling parameters. |
| `body` | [`ServiceScalingPatchRequest`](../../doc/models/service-scaling-patch-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesScalingResponse`](../../doc/models/v1-organizations-services-scaling-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

body = ServiceScalingPatchRequest(
    min_total_memory_gb=48,
    max_total_memory_gb=360,
    num_replicas=3
)

result = service_api.instance_scaling_update(
    organization_id,
    service_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesScaling400ErrorException`](../../doc/models/v1-organizations-services-scaling-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesScaling500ErrorException`](../../doc/models/v1-organizations-services-scaling-500-error-exception.md) |


# Instance Replica Scaling Update

Updates minimum and maximum memory limits per replica and idle mode scaling behavior for the service. Supports both vertical autoscaling (fixed replica count, variable memory) and horizontal autoscaling (variable replica count, fixed memory). The memory settings are available only for "production" services and must be a multiple of 4 starting from 8GB. For vertical autoscaling, please contact support to enable adjustment of numReplicas. For horizontal autoscaling (autoscalingMode "horizontal" with minReplicas/maxReplicas), contact support to enable the feature for your organization.

```python
def instance_replica_scaling_update(self,
                                   organization_id,
                                   service_id,
                                   body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service to update scaling parameters. |
| `body` | [`ServiceReplicaScalingPatchRequest`](../../doc/models/service-replica-scaling-patch-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesReplicaScalingResponse`](../../doc/models/v1-organizations-services-replica-scaling-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

body = ServiceReplicaScalingPatchRequest(
    min_replica_memory_gb=16,
    max_replica_memory_gb=120,
    autoscaling_mode=AutoscalingMode6.VERTICAL,
    num_replicas=3,
    min_replicas=1,
    max_replicas=5
)

result = service_api.instance_replica_scaling_update(
    organization_id,
    service_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesReplicaScaling400ErrorException`](../../doc/models/v1-organizations-services-replica-scaling-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesReplicaScaling500ErrorException`](../../doc/models/v1-organizations-services-replica-scaling-500-error-exception.md) |


# Instance Password Update

Sets a new password for the service

```python
def instance_password_update(self,
                            organization_id,
                            service_id,
                            body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service to update password. |
| `body` | [`ServicePasswordPatchRequest`](../../doc/models/service-password-patch-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesPasswordResponse`](../../doc/models/v1-organizations-services-password-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = service_api.instance_password_update(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesPassword400ErrorException`](../../doc/models/v1-organizations-services-password-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesPassword500ErrorException`](../../doc/models/v1-organizations-services-password-500-error-exception.md) |


# Instance Private Endpoint Create

Create a new private endpoint. The private endpoint will be associated with this service and organization

```python
def instance_private_endpoint_create(self,
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
| `body` | [`ServicPrivateEndpointePostRequest`](../../doc/models/servic-private-endpointe-post-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesPrivateEndpointResponse`](../../doc/models/v1-organizations-services-private-endpoint-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = service_api.instance_private_endpoint_create(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesPrivateEndpoint400ErrorException`](../../doc/models/v1-organizations-services-private-endpoint-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesPrivateEndpoint500ErrorException`](../../doc/models/v1-organizations-services-private-endpoint-500-error-exception.md) |


# Scaling Schedule Get

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the autoscaling schedule for a service. Returns 404 if no schedule has been configured or if the schedule was cleared. Requires the scheduled autoscaling feature to be enabled for the organization.

```python
def scaling_schedule_get(self,
                        organization_id,
                        service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesScalingScheduleResponse`](../../doc/models/v1-organizations-services-scaling-schedule-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = service_api.scaling_schedule_get(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesScalingSchedule400ErrorException`](../../doc/models/v1-organizations-services-scaling-schedule-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesScalingSchedule500ErrorException`](../../doc/models/v1-organizations-services-scaling-schedule-500-error-exception.md) |


# Scaling Schedule Upsert

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Creates or fully replaces the autoscaling schedule for a service. Pass an empty `entries` array to clear the schedule — a subsequent GET will return 404, and the response will contain an empty `baseConfig` (all fields absent). The base scaling config (applied when no entry is active) is managed separately via the `replicaScaling` endpoint. Requires the scheduled autoscaling feature to be enabled for the organization.

```python
def scaling_schedule_upsert(self,
                           organization_id,
                           service_id,
                           body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service. |
| `body` | [`ScalingSchedulePostRequest`](../../doc/models/scaling-schedule-post-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesScalingScheduleResponse`](../../doc/models/v1-organizations-services-scaling-schedule-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

body = ScalingSchedulePostRequest(
    entries=[
        ScalingScheduleEntryRequest(
            name='Business hours',
            weekdays=[
                1,
                2,
                3,
                4,
                5
            ],
            start_hour_utc=9,
            end_hour_utc=17,
            autoscaling_mode=AutoscalingMode2.VERTICAL,
            min_replica_memory_gb=16,
            max_replica_memory_gb=16,
            num_replicas=3,
            min_replicas=2,
            max_replicas=3
        )
    ]
)

result = service_api.scaling_schedule_upsert(
    organization_id,
    service_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesScalingSchedule400ErrorException`](../../doc/models/v1-organizations-services-scaling-schedule-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesScalingSchedule500ErrorException`](../../doc/models/v1-organizations-services-scaling-schedule-500-error-exception.md) |


# Scaling Schedule Delete

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Deletes the autoscaling schedule for a service. If a schedule entry is currently active, the base scaling config is restored to the instance before the schedule is removed. Returns 404 if no schedule exists. Requires the scheduled autoscaling feature to be enabled for the organization.

```python
def scaling_schedule_delete(self,
                           organization_id,
                           service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesScalingScheduleResponse2`](../../doc/models/v1-organizations-services-scaling-schedule-response-2.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = service_api.scaling_schedule_delete(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesScalingSchedule400ErrorException`](../../doc/models/v1-organizations-services-scaling-schedule-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesScalingSchedule500ErrorException`](../../doc/models/v1-organizations-services-scaling-schedule-500-error-exception.md) |


# Upgrade Window Get

Returns the configured upgrade window for a service.

Errors:

- 401: missing, invalid, or disabled API key.
- 403: caller lacks `control-plane:service:view` on the service.
- 404: service does not exist, is not visible to the caller, or no upgrade window has been configured.

```python
def upgrade_window_get(self,
                      organization_id,
                      service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesUpgradeWindowResponse`](../../doc/models/v1-organizations-services-upgrade-window-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = service_api.upgrade_window_get(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesUpgradeWindow400ErrorException`](../../doc/models/v1-organizations-services-upgrade-window-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesUpgradeWindow500ErrorException`](../../doc/models/v1-organizations-services-upgrade-window-500-error-exception.md) |


# Upgrade Window Update

Creates or fully replaces the upgrade window for a service. The upgrade window currently lasts 6 hours from `startHourUtc`. The upgrade window can only be set on primary services; secondary services inherit the primary service window.

Errors:

- 400: invalid field values (`weekday` not in 0–6, `startHourUtc` not in {0, 6, 12, 18}), or the service is a secondary service.
- 401: missing, invalid, or disabled API key.
- 403: caller lacks `control-plane:service:manage` on the service, or the organization does not have the scheduled upgrades feature enabled.
- 404: service does not exist or is not visible to the caller.

```python
def upgrade_window_update(self,
                         organization_id,
                         service_id,
                         body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service. |
| `body` | [`UpgradeWindowPutRequest`](../../doc/models/upgrade-window-put-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesUpgradeWindowResponse`](../../doc/models/v1-organizations-services-upgrade-window-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

body = UpgradeWindowPutRequest(
    weekday=3,
    start_hour_utc=StartHourUtc1.HOUR12
)

result = service_api.upgrade_window_update(
    organization_id,
    service_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesUpgradeWindow400ErrorException`](../../doc/models/v1-organizations-services-upgrade-window-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesUpgradeWindow500ErrorException`](../../doc/models/v1-organizations-services-upgrade-window-500-error-exception.md) |


# Upgrade Window Delete

Deletes the upgrade window for a service, restoring the default scheduling behaviour. The upgrade window can only be deleted on primary services. Deletion succeeds even if the organization has lost the scheduled upgrades entitlement, so a window can be cleared after entitlement loss.

Errors:

- 400: the service is a secondary service.
- 401: missing, invalid, or disabled API key.
- 403: caller lacks `control-plane:service:manage` on the service.
- 404: service does not exist, is not visible to the caller, or no upgrade window is configured.

```python
def upgrade_window_delete(self,
                         organization_id,
                         service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesUpgradeWindowResponse2`](../../doc/models/v1-organizations-services-upgrade-window-response-2.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = service_api.upgrade_window_delete(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesUpgradeWindow400ErrorException`](../../doc/models/v1-organizations-services-upgrade-window-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesUpgradeWindow500ErrorException`](../../doc/models/v1-organizations-services-upgrade-window-500-error-exception.md) |


# Service Clickhouse Settings List Get

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the configured ClickHouse settings for the service. Only settings that have been explicitly set are included.

```python
def service_clickhouse_settings_list_get(self,
                                        organization_id,
                                        service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickhouseSettingsResponse`](../../doc/models/v1-organizations-services-clickhouse-settings-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = service_api.service_clickhouse_settings_list_get(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickhouseSettings400ErrorException`](../../doc/models/v1-organizations-services-clickhouse-settings-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickhouseSettings500ErrorException`](../../doc/models/v1-organizations-services-clickhouse-settings-500-error-exception.md) |


# Service Clickhouse Settings Update

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Updates one or more ClickHouse settings for the service. To reset a setting to its platform default, use the [DELETE single setting](#tag/Service/operation/serviceClickhouseSettingDelete) endpoint. Use the [schema endpoint](#tag/Service/operation/serviceClickhouseSettingsSchemaGet) to discover which settings are configurable.

```python
def service_clickhouse_settings_update(self,
                                      organization_id,
                                      service_id,
                                      body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service. |
| `body` | [`ServiceClickhouseSettingsPatchRequest`](../../doc/models/service-clickhouse-settings-patch-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickhouseSettingsResponse1`](../../doc/models/v1-organizations-services-clickhouse-settings-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

body = ServiceClickhouseSettingsPatchRequest(
    settings={
        'compatibility': '26.2',
        'max_query_size': 262144
    }
)

result = service_api.service_clickhouse_settings_update(
    organization_id,
    service_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickhouseSettings400ErrorException`](../../doc/models/v1-organizations-services-clickhouse-settings-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickhouseSettings500ErrorException`](../../doc/models/v1-organizations-services-clickhouse-settings-500-error-exception.md) |


# Service Clickhouse Settings Schema Get

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the schema of all configurable ClickHouse settings, including types, valid values, descriptions, and warnings.

```python
def service_clickhouse_settings_schema_get(self,
                                          organization_id,
                                          service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickhouseSettingsSchemaResponse`](../../doc/models/v1-organizations-services-clickhouse-settings-schema-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = service_api.service_clickhouse_settings_schema_get(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickhouseSettingsSchema400ErrorException`](../../doc/models/v1-organizations-services-clickhouse-settings-schema-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickhouseSettingsSchema500ErrorException`](../../doc/models/v1-organizations-services-clickhouse-settings-schema-500-error-exception.md) |


# Service Clickhouse Setting Get

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the current value of a ClickHouse setting for the service. Use the [schema endpoint](#tag/Service/operation/serviceClickhouseSettingsSchemaGet) to discover which settings are configurable.

```python
def service_clickhouse_setting_get(self,
                                  organization_id,
                                  service_id,
                                  setting_name)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service. |
| `setting_name` | `str` | Template, Required | Name of the setting to retrieve. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickhouseSettingsSettingNameResponse`](../../doc/models/v1-organizations-services-clickhouse-settings-setting-name-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

setting_name = 'settingName0'

result = service_api.service_clickhouse_setting_get(
    organization_id,
    service_id,
    setting_name
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickhouseSettingsSettingName400ErrorException`](../../doc/models/v1-organizations-services-clickhouse-settings-setting-name-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickhouseSettingsSettingName500ErrorException`](../../doc/models/v1-organizations-services-clickhouse-settings-setting-name-500-error-exception.md) |


# Service Clickhouse Setting Delete

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Removes a previously-configured ClickHouse setting, reverting its effective value to the platform default. Settings under `spec.extraConfig.server.*` (e.g. `keep_alive_timeout`, `shared_merge_tree_disable_merges_and_mutations_assignment`) trigger a ClickHouse server rollout restart; other settings propagate to all replicas after a short delay. Deleting a setting that was never configured is a no-op (200 OK).

```python
def service_clickhouse_setting_delete(self,
                                     organization_id,
                                     service_id,
                                     setting_name)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service. |
| `setting_name` | `str` | Template, Required | Name of the setting to reset. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickhouseSettingsSettingNameResponse1`](../../doc/models/v1-organizations-services-clickhouse-settings-setting-name-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

setting_name = 'settingName0'

result = service_api.service_clickhouse_setting_delete(
    organization_id,
    service_id,
    setting_name
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickhouseSettingsSettingName400ErrorException`](../../doc/models/v1-organizations-services-clickhouse-settings-setting-name-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickhouseSettingsSettingName500ErrorException`](../../doc/models/v1-organizations-services-clickhouse-settings-setting-name-500-error-exception.md) |

