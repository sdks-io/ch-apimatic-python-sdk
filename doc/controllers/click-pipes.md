# Click Pipes

```python
click_pipes_api = client.click_pipes
```

## Class Name

`ClickPipesApi`

## Methods

* [Click Pipe Get List](../../doc/controllers/click-pipes.md#click-pipe-get-list)
* [Click Pipe Create](../../doc/controllers/click-pipes.md#click-pipe-create)
* [Click Pipes Service Context Get](../../doc/controllers/click-pipes.md#click-pipes-service-context-get)
* [Click Pipe Get](../../doc/controllers/click-pipes.md#click-pipe-get)
* [Click Pipe Update](../../doc/controllers/click-pipes.md#click-pipe-update)
* [Click Pipe Delete](../../doc/controllers/click-pipes.md#click-pipe-delete)
* [Click Pipe Settings Get](../../doc/controllers/click-pipes.md#click-pipe-settings-get)
* [Click Pipe Settings Update](../../doc/controllers/click-pipes.md#click-pipe-settings-update)
* [Click Pipe Schema Discovery](../../doc/controllers/click-pipes.md#click-pipe-schema-discovery)
* [Click Pipe Scaling Update](../../doc/controllers/click-pipes.md#click-pipe-scaling-update)
* [Click Pipe State Update](../../doc/controllers/click-pipes.md#click-pipe-state-update)
* [Click Pipe Cdc Scaling Get](../../doc/controllers/click-pipes.md#click-pipe-cdc-scaling-get)
* [Click Pipe Cdc Scaling Update](../../doc/controllers/click-pipes.md#click-pipe-cdc-scaling-update)
* [Click Pipe Reverse Private Endpoint Get List](../../doc/controllers/click-pipes.md#click-pipe-reverse-private-endpoint-get-list)
* [Click Pipe Reverse Private Endpoint Create](../../doc/controllers/click-pipes.md#click-pipe-reverse-private-endpoint-create)
* [Click Pipe Reverse Private Endpoint Get](../../doc/controllers/click-pipes.md#click-pipe-reverse-private-endpoint-get)
* [Click Pipe Reverse Private Endpoint Delete](../../doc/controllers/click-pipes.md#click-pipe-reverse-private-endpoint-delete)
* [Click Pipe Reverse Private Endpoint Update](../../doc/controllers/click-pipes.md#click-pipe-reverse-private-endpoint-update)


# Click Pipe Get List

Returns a list of ClickPipes.

```python
def click_pipe_get_list(self,
                       organization_id,
                       service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service that owns the ClickPipe. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickpipesResponse`](../../doc/models/v1-organizations-services-clickpipes-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = click_pipes_api.click_pipe_get_list(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickpipes400ErrorException`](../../doc/models/v1-organizations-services-clickpipes-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickpipes500ErrorException`](../../doc/models/v1-organizations-services-clickpipes-500-error-exception.md) |


# Click Pipe Create

Create a new ClickPipe.

```python
def click_pipe_create(self,
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
| `service_id` | `uuid\|str` | Template, Required | ID of the service to create the ClickPipe for. |
| `body` | [`ClickPipePostRequest`](../../doc/models/click-pipe-post-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickpipesResponse1`](../../doc/models/v1-organizations-services-clickpipes-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = click_pipes_api.click_pipe_create(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickpipes400ErrorException`](../../doc/models/v1-organizations-services-clickpipes-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickpipes500ErrorException`](../../doc/models/v1-organizations-services-clickpipes-500-error-exception.md) |


# Click Pipes Service Context Get

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns service-level ClickPipes capabilities and Private Preview workload identity context, including the GCP service account to grant access to customer source resources.

```python
def click_pipes_service_context_get(self,
                                   organization_id,
                                   service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service to get ClickPipes context for. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickpipesContextResponse`](../../doc/models/v1-organizations-services-clickpipes-context-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = click_pipes_api.click_pipes_service_context_get(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickpipesContext400ErrorException`](../../doc/models/v1-organizations-services-clickpipes-context-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickpipesContext500ErrorException`](../../doc/models/v1-organizations-services-clickpipes-context-500-error-exception.md) |


# Click Pipe Get

Returns the specified ClickPipe.

```python
def click_pipe_get(self,
                  organization_id,
                  service_id,
                  click_pipe_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service that owns the ClickPipe. |
| `click_pipe_id` | `uuid\|str` | Template, Required | ID of the requested ClickPipe. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickpipesClickPipeIdResponse`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_pipe_id = '000014a6-0000-0000-0000-000000000000'

result = click_pipes_api.click_pipe_get(
    organization_id,
    service_id,
    click_pipe_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickpipesClickPipeId400ErrorException`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickpipesClickPipeId500ErrorException`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-500-error-exception.md) |


# Click Pipe Update

Update the specified ClickPipe. Source fields not present in the per-source update schemas are immutable after creation. For Kafka sources, values submitted for immutable fields (type, format, brokers, topics, consumerGroup, offset, schemaRegistry, exactlyOnce) are not applied, except schema registry credentials, which are rejected.

```python
def click_pipe_update(self,
                     organization_id,
                     service_id,
                     click_pipe_id,
                     body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service to create the ClickPipe for. |
| `click_pipe_id` | `uuid\|str` | Template, Required | ID of the requested ClickPipe. |
| `body` | [`ClickPipePatchRequest`](../../doc/models/click-pipe-patch-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickpipesClickPipeIdResponse`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_pipe_id = '000014a6-0000-0000-0000-000000000000'

result = click_pipes_api.click_pipe_update(
    organization_id,
    service_id,
    click_pipe_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickpipesClickPipeId400ErrorException`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickpipesClickPipeId500ErrorException`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-500-error-exception.md) |


# Click Pipe Delete

Delete the specified ClickPipe.

```python
def click_pipe_delete(self,
                     organization_id,
                     service_id,
                     click_pipe_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service that owns the ClickPipe. |
| `click_pipe_id` | `uuid\|str` | Template, Required | ID of the ClickPipe to delete. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickpipesClickPipeIdResponse2`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-response-2.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_pipe_id = '000014a6-0000-0000-0000-000000000000'

result = click_pipes_api.click_pipe_delete(
    organization_id,
    service_id,
    click_pipe_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickpipesClickPipeId400ErrorException`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickpipesClickPipeId500ErrorException`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-500-error-exception.md) |


# Click Pipe Settings Get

Returns the advanced settings for the specified ClickPipe.

```python
def click_pipe_settings_get(self,
                           organization_id,
                           service_id,
                           click_pipe_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service that owns the ClickPipe. |
| `click_pipe_id` | `uuid\|str` | Template, Required | ID of the ClickPipe to get settings for. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-settings-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_pipe_id = '000014a6-0000-0000-0000-000000000000'

result = click_pipes_api.click_pipe_settings_get(
    organization_id,
    service_id,
    click_pipe_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickpipesClickPipeIdSettings400ErrorException`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-settings-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickpipesClickPipeIdSettings500ErrorException`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-settings-500-error-exception.md) |


# Click Pipe Settings Update

Update the advanced settings for the specified ClickPipe. Send key-value pairs where values can be strings, numbers, or booleans.

```python
def click_pipe_settings_update(self,
                              organization_id,
                              service_id,
                              click_pipe_id,
                              body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service that owns the ClickPipe. |
| `click_pipe_id` | `uuid\|str` | Template, Required | ID of the ClickPipe to update settings for. |
| `body` | [`ClickPipeSettingsPutRequest`](../../doc/models/click-pipe-settings-put-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-settings-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_pipe_id = '000014a6-0000-0000-0000-000000000000'

body = ClickPipeSettingsPutRequest(
    streaming_max_insert_wait_ms=5000,
    object_storage_concurrency=1,
    object_storage_polling_interval_ms=30000,
    object_storage_max_insert_bytes=10737418240,
    object_storage_max_file_count=100,
    clickhouse_max_threads=8,
    clickhouse_max_insert_threads=1,
    clickhouse_min_insert_block_size_bytes=1073741824,
    clickhouse_max_download_threads=4,
    clickhouse_parallel_distributed_insert_select=2,
    kafka_read_committed=False,
    object_storage_use_cluster_function=True,
    clickhouse_parallel_view_processing=False
)

result = click_pipes_api.click_pipe_settings_update(
    organization_id,
    service_id,
    click_pipe_id,
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickpipesClickPipeIdSettings400ErrorException`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-settings-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickpipesClickPipeIdSettings500ErrorException`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-settings-500-error-exception.md) |


# Click Pipe Schema Discovery

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Infers the schema (field names and ClickHouse data types) of a ClickPipe source without creating a pipe. Supported for Kafka, Kinesis, Pub/Sub, and object storage sources. Object storage inference runs on the destination service, which must be running.

```python
def click_pipe_schema_discovery(self,
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
| `service_id` | `uuid\|str` | Template, Required | ID of the service to run schema discovery against. |
| `body` | [`ClickPipeSchemaDiscoveryRequest`](../../doc/models/click-pipe-schema-discovery-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickpipesSchemaDiscoveryResponse`](../../doc/models/v1-organizations-services-clickpipes-schema-discovery-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = click_pipes_api.click_pipe_schema_discovery(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickpipesSchemaDiscovery400ErrorException`](../../doc/models/v1-organizations-services-clickpipes-schema-discovery-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickpipesSchemaDiscovery500ErrorException`](../../doc/models/v1-organizations-services-clickpipes-schema-discovery-500-error-exception.md) |


# Click Pipe Scaling Update

Change scaling settings for the specified ClickPipe. This endpoint supports Kafka, Kinesis, and object storage pipes (S3, GCS, Azure Blob).

**Note:** For database ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery), use the [Update CDC ClickPipes scaling](#tag/ClickPipes/operation/clickPipeCdcScalingUpdate) endpoint instead.

```python
def click_pipe_scaling_update(self,
                             organization_id,
                             service_id,
                             click_pipe_id,
                             body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service that owns the ClickPipe. |
| `click_pipe_id` | `uuid\|str` | Template, Required | ID of the ClickPipe to update scaling settings. |
| `body` | [`ClickPipeScalingPatchRequest`](../../doc/models/click-pipe-scaling-patch-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickpipesClickPipeIdScalingResponse`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-scaling-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_pipe_id = '000014a6-0000-0000-0000-000000000000'

result = click_pipes_api.click_pipe_scaling_update(
    organization_id,
    service_id,
    click_pipe_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickpipesClickPipeIdScaling400ErrorException`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-scaling-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickpipesClickPipeIdScaling500ErrorException`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-scaling-500-error-exception.md) |


# Click Pipe State Update

Start, stop or resync ClickPipe. Stopping a ClickPipe will stop the ingestion process from any state. Starting is allowed for ClickPipes in the "Stopped" state or with a "Failed" state. Resyncing is only for Postgres and MySQL pipes and can be done from any state.

```python
def click_pipe_state_update(self,
                           organization_id,
                           service_id,
                           click_pipe_id,
                           body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service that owns the ClickPipe. |
| `click_pipe_id` | `uuid\|str` | Template, Required | ID of the ClickPipe to update state. |
| `body` | [`ClickPipeStatePatchRequest`](../../doc/models/click-pipe-state-patch-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickpipesClickPipeIdStateResponse`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-state-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_pipe_id = '000014a6-0000-0000-0000-000000000000'

result = click_pipes_api.click_pipe_state_update(
    organization_id,
    service_id,
    click_pipe_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickpipesClickPipeIdState400ErrorException`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-state-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickpipesClickPipeIdState500ErrorException`](../../doc/models/v1-organizations-services-clickpipes-click-pipe-id-state-500-error-exception.md) |


# Click Pipe Cdc Scaling Get

Get scaling settings for database ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery).

The infrastructure is shared between all database ClickPipes in the service, both for initial load and CDC. For billing purposes, 2 CPU cores and 8 GB of RAM [correspond](https://clickhouse.com/docs/cloud/manage/billing/overview#clickpipes-for-postgres-cdc) to one compute unit.

**Note:** For Kafka, Kinesis, and object storage pipes (S3, GCS, Azure Blob), see [Get ClickPipe](#tag/ClickPipes/operation/clickPipeGet).

**This endpoint becomes available once at least one database ClickPipe was provisioned.**

```python
def click_pipe_cdc_scaling_get(self,
                              organization_id,
                              service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service that owns the ClickPipe. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickpipesCdcScalingResponse`](../../doc/models/v1-organizations-services-clickpipes-cdc-scaling-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = click_pipes_api.click_pipe_cdc_scaling_get(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickpipesCdcScaling400ErrorException`](../../doc/models/v1-organizations-services-clickpipes-cdc-scaling-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickpipesCdcScaling500ErrorException`](../../doc/models/v1-organizations-services-clickpipes-cdc-scaling-500-error-exception.md) |


# Click Pipe Cdc Scaling Update

Update scaling settings for database ClickPipes (PostgreSQL, MySQL, MongoDB, BigQuery).

The infrastructure is shared between all database ClickPipes in the service, both for initial load and CDC. Scaling settings may take a few minutes to fully propagate.

For billing purposes, 2 CPU cores and 8 GB of RAM [correspond](https://clickhouse.com/docs/cloud/manage/billing/overview#clickpipes-for-postgres-cdc) to one compute unit. If your organization tier changes, database ClickPipes will be [rescaled](https://clickhouse.com/docs/cloud/manage/billing/overview#compute) appropriately.

**Note:** For Kafka, Kinesis, and object storage pipes (S3, GCS, Azure Blob), see [Get ClickPipe](#tag/ClickPipes/operation/clickPipeGet).

**This endpoint becomes available once at least one database ClickPipe was provisioned.**

```python
def click_pipe_cdc_scaling_update(self,
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
| `service_id` | `uuid\|str` | Template, Required | ID of the service that owns the ClickPipe. |
| `body` | [`ClickPipesCdcScalingPatchRequest`](../../doc/models/click-pipes-cdc-scaling-patch-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickpipesCdcScalingResponse`](../../doc/models/v1-organizations-services-clickpipes-cdc-scaling-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

body = ClickPipesCdcScalingPatchRequest(
    replica_cpu_millicores=2000,
    replica_memory_gb=8
)

result = click_pipes_api.click_pipe_cdc_scaling_update(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickpipesCdcScaling400ErrorException`](../../doc/models/v1-organizations-services-clickpipes-cdc-scaling-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickpipesCdcScaling500ErrorException`](../../doc/models/v1-organizations-services-clickpipes-cdc-scaling-500-error-exception.md) |


# Click Pipe Reverse Private Endpoint Get List

Returns a list of reverse private endpoints for the specified service.

```python
def click_pipe_reverse_private_endpoint_get_list(self,
                                                organization_id,
                                                service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service that owns the Reverse Private Endpoint. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse`](../../doc/models/v1-organizations-services-clickpipes-reverse-private-endpoints-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = click_pipes_api.click_pipe_reverse_private_endpoint_get_list(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickpipesReversePrivateEndpoints400ErrorException`](../../doc/models/v1-organizations-services-clickpipes-reverse-private-endpoints-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickpipesReversePrivateEndpoints500ErrorException`](../../doc/models/v1-organizations-services-clickpipes-reverse-private-endpoints-500-error-exception.md) |


# Click Pipe Reverse Private Endpoint Create

Create a new reverse private endpoint.

```python
def click_pipe_reverse_private_endpoint_create(self,
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
| `service_id` | `uuid\|str` | Template, Required | ID of the service that owns the Reverse Private Endpoint. |
| `body` | [`CreateReversePrivateEndpoint`](../../doc/models/create-reverse-private-endpoint.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1`](../../doc/models/v1-organizations-services-clickpipes-reverse-private-endpoints-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

body = CreateReversePrivateEndpoint(
    description='My reverse private endpoint',
    mtype=Type1.VPC_ENDPOINT_SERVICE,
    vpc_endpoint_service_name='com.amazonaws.vpce.us-east-1.vpce-svc-12345678901234567',
    vpc_resource_configuration_id='rcfg-12345678901234567',
    vpc_resource_share_arn='arn:aws:ram:us-east-1:123456789012:resource-share/share-12345678901234567',
    msk_cluster_arn='arn:aws:kafka:us-east-1:123456789012:cluster/my-cluster',
    msk_authentication=MskAuthentication.SASL_IAM,
    gcp_service_attachment='projects/my-project/regions/us-central1/serviceAttachments/my-service',
    custom_private_dns_mappings=[
        CustomPrivateDnsMapping(
            private_dns_name='my-service.example.com'
        ),
        CustomPrivateDnsMapping(
            private_dns_name='*.example.com'
        )
    ]
)

result = click_pipes_api.click_pipe_reverse_private_endpoint_create(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickpipesReversePrivateEndpoints400ErrorException`](../../doc/models/v1-organizations-services-clickpipes-reverse-private-endpoints-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickpipesReversePrivateEndpoints500ErrorException`](../../doc/models/v1-organizations-services-clickpipes-reverse-private-endpoints-500-error-exception.md) |


# Click Pipe Reverse Private Endpoint Get

Returns the reverse private endpoint with the specified ID.

```python
def click_pipe_reverse_private_endpoint_get(self,
                                           organization_id,
                                           service_id,
                                           reverse_private_endpoint_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service that owns the Reverse Private Endpoint. |
| `reverse_private_endpoint_id` | `uuid\|str` | Template, Required | ID of the reverse private endpoint to get. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse`](../../doc/models/v1-organizations-services-clickpipes-reverse-private-endpoints-reverse-private-endpoint-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

reverse_private_endpoint_id = '00001af2-0000-0000-0000-000000000000'

result = click_pipes_api.click_pipe_reverse_private_endpoint_get(
    organization_id,
    service_id,
    reverse_private_endpoint_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400ErrorException`](../../doc/models/v1-organizations-services-clickpipes-reverse-private-endpoints-reverse-private-endpoint-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500ErrorException`](../../doc/models/v1-organizations-services-clickpipes-reverse-private-endpoints-reverse-private-endpoint-id-500-error-exception.md) |


# Click Pipe Reverse Private Endpoint Delete

Delete the reverse private endpoint with the specified ID.

```python
def click_pipe_reverse_private_endpoint_delete(self,
                                              organization_id,
                                              service_id,
                                              reverse_private_endpoint_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service that owns the Reverse Private Endpoint. |
| `reverse_private_endpoint_id` | `uuid\|str` | Template, Required | ID of the reverse private endpoint to delete. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1`](../../doc/models/v1-organizations-services-clickpipes-reverse-private-endpoints-reverse-private-endpoint-id-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

reverse_private_endpoint_id = '00001af2-0000-0000-0000-000000000000'

result = click_pipes_api.click_pipe_reverse_private_endpoint_delete(
    organization_id,
    service_id,
    reverse_private_endpoint_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400ErrorException`](../../doc/models/v1-organizations-services-clickpipes-reverse-private-endpoints-reverse-private-endpoint-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500ErrorException`](../../doc/models/v1-organizations-services-clickpipes-reverse-private-endpoints-reverse-private-endpoint-id-500-error-exception.md) |


# Click Pipe Reverse Private Endpoint Update

Update mutable fields for an existing reverse private endpoint. customPrivateDnsMappings is a full replacement list. Use an empty array to clear mappings.

```python
def click_pipe_reverse_private_endpoint_update(self,
                                              organization_id,
                                              service_id,
                                              reverse_private_endpoint_id,
                                              body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service that owns the Reverse Private Endpoint. |
| `reverse_private_endpoint_id` | `uuid\|str` | Template, Required | ID of the reverse private endpoint to update. |
| `body` | [`UpdateReversePrivateEndpoint`](../../doc/models/update-reverse-private-endpoint.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse`](../../doc/models/v1-organizations-services-clickpipes-reverse-private-endpoints-reverse-private-endpoint-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

reverse_private_endpoint_id = '00001af2-0000-0000-0000-000000000000'

body = UpdateReversePrivateEndpoint(
    custom_private_dns_mappings=[
        CustomPrivateDnsMapping(
            private_dns_name='my-service.example.com'
        ),
        CustomPrivateDnsMapping(
            private_dns_name='*.example.com'
        )
    ]
)

result = click_pipes_api.click_pipe_reverse_private_endpoint_update(
    organization_id,
    service_id,
    reverse_private_endpoint_id,
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400ErrorException`](../../doc/models/v1-organizations-services-clickpipes-reverse-private-endpoints-reverse-private-endpoint-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500ErrorException`](../../doc/models/v1-organizations-services-clickpipes-reverse-private-endpoints-reverse-private-endpoint-id-500-error-exception.md) |

