# Postgres

```python
postgres_api = client.postgres
```

## Class Name

`PostgresApi`

## Methods

* [Postgres Service Create](../../doc/controllers/postgres.md#postgres-service-create)
* [Postgres Service Get List](../../doc/controllers/postgres.md#postgres-service-get-list)
* [Postgres Service Get](../../doc/controllers/postgres.md#postgres-service-get)
* [Postgres Service Delete](../../doc/controllers/postgres.md#postgres-service-delete)
* [Postgres Service Patch](../../doc/controllers/postgres.md#postgres-service-patch)
* [Postgres Service Certs Get](../../doc/controllers/postgres.md#postgres-service-certs-get)
* [Postgres Instance Restore](../../doc/controllers/postgres.md#postgres-instance-restore)
* [Postgres Service Set Password](../../doc/controllers/postgres.md#postgres-service-set-password)
* [Postgres Service Patch State](../../doc/controllers/postgres.md#postgres-service-patch-state)
* [Postgres Instance Create Read Replica](../../doc/controllers/postgres.md#postgres-instance-create-read-replica)
* [Postgres Instance Config Get](../../doc/controllers/postgres.md#postgres-instance-config-get)
* [Postgres Instance Config Post](../../doc/controllers/postgres.md#postgres-instance-config-post)
* [Postgres Instance Config Patch](../../doc/controllers/postgres.md#postgres-instance-config-patch)
* [Postgres Instance Metrics Get](../../doc/controllers/postgres.md#postgres-instance-metrics-get)
* [Slow Query Patterns Get List](../../doc/controllers/postgres.md#slow-query-patterns-get-list)
* [Slow Query Pattern Get](../../doc/controllers/postgres.md#slow-query-pattern-get)
* [Postgres Logs Get List](../../doc/controllers/postgres.md#postgres-logs-get-list)


# Postgres Service Create

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Creates a new Postgres service in the organization and returns it. The service is started asynchronously.

```python
def postgres_service_create(self,
                           organization_id,
                           body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that will own the service. |
| `body` | [`PostgresServicePostRequest`](../../doc/models/postgres-service-post-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsPostgresResponse`](../../doc/models/v1-organizations-postgres-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

body = PostgresServicePostRequest(
    name='name6',
    provider=CloudProvider.AWS,
    region='region2',
    size=VmSize.ENUM_R6ID32XLARGE,
    pg_config=PostgresConfiguration(
        max_connections=100
    ),
    pg_bouncer_config={
        'default_pool_size': '16'
    }
)

result = postgres_api.postgres_service_create(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPostgres400ErrorException`](../../doc/models/v1-organizations-postgres-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPostgres500ErrorException`](../../doc/models/v1-organizations-postgres-500-error-exception.md) |


# Postgres Service Get List

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns a list of all Postgres services in the organization.

```python
def postgres_service_get_list(self,
                             organization_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the services. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsPostgresResponse1`](../../doc/models/v1-organizations-postgres-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

result = postgres_api.postgres_service_get_list(organization_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPostgres400ErrorException`](../../doc/models/v1-organizations-postgres-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPostgres500ErrorException`](../../doc/models/v1-organizations-postgres-500-error-exception.md) |


# Postgres Service Get

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns a Postgres service that belongs to the organization

```python
def postgres_service_get(self,
                        organization_id,
                        postgres_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the Postgres service. |
| `postgres_id` | `uuid\|str` | Template, Required | ID of the requested Postgres service. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsPostgresResponse`](../../doc/models/v1-organizations-postgres-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

postgres_id = '00000dcc-0000-0000-0000-000000000000'

result = postgres_api.postgres_service_get(
    organization_id,
    postgres_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPostgres400ErrorException`](../../doc/models/v1-organizations-postgres-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPostgres500ErrorException`](../../doc/models/v1-organizations-postgres-500-error-exception.md) |


# Postgres Service Delete

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Deletes a Postgres service that belongs to the organization

```python
def postgres_service_delete(self,
                           organization_id,
                           postgres_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the Postgres service. |
| `postgres_id` | `uuid\|str` | Template, Required | ID of the requested Postgres service. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsPostgresResponse3`](../../doc/models/v1-organizations-postgres-response-3.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

postgres_id = '00000dcc-0000-0000-0000-000000000000'

result = postgres_api.postgres_service_delete(
    organization_id,
    postgres_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPostgres400ErrorException`](../../doc/models/v1-organizations-postgres-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPostgres500ErrorException`](../../doc/models/v1-organizations-postgres-500-error-exception.md) |


# Postgres Service Patch

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Update a Postgres service that belongs to the organization. **WARNING:** Changing the name also updates the host name and certificates for the service.

```python
def postgres_service_patch(self,
                          organization_id,
                          postgres_id,
                          body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the Postgres service. |
| `postgres_id` | `uuid\|str` | Template, Required | ID of the requested Postgres service. |
| `body` | [`PostgresServicePatchRequest`](../../doc/models/postgres-service-patch-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsPostgresResponse`](../../doc/models/v1-organizations-postgres-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

postgres_id = '00000dcc-0000-0000-0000-000000000000'

result = postgres_api.postgres_service_patch(
    organization_id,
    postgres_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPostgres400ErrorException`](../../doc/models/v1-organizations-postgres-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPostgres500ErrorException`](../../doc/models/v1-organizations-postgres-500-error-exception.md) |


# Postgres Service Certs Get

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Download CA certificates for a PostgreSQL service

```python
def postgres_service_certs_get(self,
                              organization_id,
                              postgres_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the Postgres service. |
| `postgres_id` | `uuid\|str` | Template, Required | ID of the requested Postgres service. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

postgres_id = '00000dcc-0000-0000-0000-000000000000'

result = postgres_api.postgres_service_certs_get(
    organization_id,
    postgres_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPostgresCaCertificates400ErrorException`](../../doc/models/v1-organizations-postgres-ca-certificates-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPostgresCaCertificates500ErrorException`](../../doc/models/v1-organizations-postgres-ca-certificates-500-error-exception.md) |


# Postgres Instance Restore

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Restore a Postgres database from continuous backup, optionally at a specific point in time.

```python
def postgres_instance_restore(self,
                             organization_id,
                             postgres_id,
                             body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the Postgres service. |
| `postgres_id` | `uuid\|str` | Template, Required | ID of the requested Postgres service. |
| `body` | [`PostgresServiceRestoreRequest`](../../doc/models/postgres-service-restore-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsPostgresRestoredServiceResponse`](../../doc/models/v1-organizations-postgres-restored-service-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

postgres_id = '00000dcc-0000-0000-0000-000000000000'

body = PostgresServiceRestoreRequest(
    name='name6',
    restore_target=dateutil.parser.parse('03/31/2026 18:17:37'),
    pg_config=PostgresConfiguration(
        max_connections=100
    ),
    pg_bouncer_config={
        'default_pool_size': '16'
    }
)

result = postgres_api.postgres_instance_restore(
    organization_id,
    postgres_id,
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPostgresRestoredService400ErrorException`](../../doc/models/v1-organizations-postgres-restored-service-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPostgresRestoredService500ErrorException`](../../doc/models/v1-organizations-postgres-restored-service-500-error-exception.md) |


# Postgres Service Set Password

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Sets a new password for a Postgres service's superuser account.

```python
def postgres_service_set_password(self,
                                 organization_id,
                                 postgres_id,
                                 body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the Postgres service. |
| `postgres_id` | `uuid\|str` | Template, Required | ID of the requested Postgres service. |
| `body` | [`PostgresServiceSetPassword`](../../doc/models/postgres-service-set-password.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsPostgresPasswordResponse`](../../doc/models/v1-organizations-postgres-password-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

postgres_id = '00000dcc-0000-0000-0000-000000000000'

result = postgres_api.postgres_service_set_password(
    organization_id,
    postgres_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPostgresPassword400ErrorException`](../../doc/models/v1-organizations-postgres-password-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPostgresPassword500ErrorException`](../../doc/models/v1-organizations-postgres-password-500-error-exception.md) |


# Postgres Service Patch State

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Initiate a process for a Postgres service:

* restart: Initiates a service restart
* promote: Promotes a read replica to primary
* switchover: Switch a primary over to a standby

```python
def postgres_service_patch_state(self,
                                organization_id,
                                postgres_id,
                                body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the Postgres service. |
| `postgres_id` | `uuid\|str` | Template, Required | ID of the requested Postgres service. |
| `body` | [`PostgresServiceSetState`](../../doc/models/postgres-service-set-state.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsPostgresStateResponse`](../../doc/models/v1-organizations-postgres-state-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

postgres_id = '00000dcc-0000-0000-0000-000000000000'

result = postgres_api.postgres_service_patch_state(
    organization_id,
    postgres_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPostgresState400ErrorException`](../../doc/models/v1-organizations-postgres-state-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPostgresState500ErrorException`](../../doc/models/v1-organizations-postgres-state-500-error-exception.md) |


# Postgres Instance Create Read Replica

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Initiate the process to create a new read replica for a Postgres service.

```python
def postgres_instance_create_read_replica(self,
                                         organization_id,
                                         postgres_id,
                                         body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the Postgres service. |
| `postgres_id` | `uuid\|str` | Template, Required | ID of the requested Postgres service. |
| `body` | [`PostgresServiceReadReplicaRequest`](../../doc/models/postgres-service-read-replica-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsPostgresReadReplicaResponse`](../../doc/models/v1-organizations-postgres-read-replica-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

postgres_id = '00000dcc-0000-0000-0000-000000000000'

body = PostgresServiceReadReplicaRequest(
    name='name6',
    pg_config=PostgresConfiguration(
        max_connections=100
    ),
    pg_bouncer_config={
        'default_pool_size': '16'
    }
)

result = postgres_api.postgres_instance_create_read_replica(
    organization_id,
    postgres_id,
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPostgresReadReplica400ErrorException`](../../doc/models/v1-organizations-postgres-read-replica-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPostgresReadReplica500ErrorException`](../../doc/models/v1-organizations-postgres-read-replica-500-error-exception.md) |


# Postgres Instance Config Get

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns the configuration data for a Postgres service and its PgBouncer service.

```python
def postgres_instance_config_get(self,
                                organization_id,
                                postgres_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the Postgres service. |
| `postgres_id` | `uuid\|str` | Template, Required | ID of the requested Postgres service. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsPostgresConfigResponse`](../../doc/models/v1-organizations-postgres-config-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

postgres_id = '00000dcc-0000-0000-0000-000000000000'

result = postgres_api.postgres_instance_config_get(
    organization_id,
    postgres_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPostgresConfig400ErrorException`](../../doc/models/v1-organizations-postgres-config-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPostgresConfig500ErrorException`](../../doc/models/v1-organizations-postgres-config-500-error-exception.md) |


# Postgres Instance Config Post

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Replace the existing Postgres service and pgBouncer configuration.

```python
def postgres_instance_config_post(self,
                                 organization_id,
                                 postgres_id,
                                 body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the Postgres service. |
| `postgres_id` | `uuid\|str` | Template, Required | ID of the requested Postgres service. |
| `body` | [`PostgresInstanceConfig`](../../doc/models/postgres-instance-config.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsPostgresConfigResponse1`](../../doc/models/v1-organizations-postgres-config-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

postgres_id = '00000dcc-0000-0000-0000-000000000000'

body = PostgresInstanceConfig(
    pg_config=PostgresConfiguration(
        max_connections=100
    ),
    pg_bouncer_config={
        'default_pool_size': '16'
    }
)

result = postgres_api.postgres_instance_config_post(
    organization_id,
    postgres_id,
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPostgresConfig400ErrorException`](../../doc/models/v1-organizations-postgres-config-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPostgresConfig500ErrorException`](../../doc/models/v1-organizations-postgres-config-500-error-exception.md) |


# Postgres Instance Config Patch

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Update the existing Postgres service and pgBouncer configuration.

```python
def postgres_instance_config_patch(self,
                                  organization_id,
                                  postgres_id,
                                  body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the Postgres service. |
| `postgres_id` | `uuid\|str` | Template, Required | ID of the requested Postgres service. |
| `body` | [`PostgresInstanceConfig`](../../doc/models/postgres-instance-config.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsPostgresConfigResponse1`](../../doc/models/v1-organizations-postgres-config-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

postgres_id = '00000dcc-0000-0000-0000-000000000000'

body = PostgresInstanceConfig(
    pg_config=PostgresConfiguration(
        max_connections=100
    ),
    pg_bouncer_config={
        'default_pool_size': '16'
    }
)

result = postgres_api.postgres_instance_config_patch(
    organization_id,
    postgres_id,
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPostgresConfig400ErrorException`](../../doc/models/v1-organizations-postgres-config-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPostgresConfig500ErrorException`](../../doc/models/v1-organizations-postgres-config-500-error-exception.md) |


# Postgres Instance Metrics Get

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns bucketed time-series metrics for a PostgreSQL service over the requested window (CPU, memory, disk, network, connections, cache hit ratio, throughput, transactions, and more). Use this to chart or analyze how a service behaved over time.

```python
def postgres_instance_metrics_get(self,
                                 organization_id,
                                 postgres_id,
                                 from_date,
                                 to_date,
                                 bucket_size_seconds=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the Postgres service. |
| `postgres_id` | `uuid\|str` | Template, Required | ID of the Postgres service. |
| `from_date` | `datetime` | Query, Required | Inclusive start of the time window (RFC 3339 date-time). |
| `to_date` | `datetime` | Query, Required | Exclusive end of the time window (RFC 3339 date-time). |
| `bucket_size_seconds` | `int` | Query, Optional | Time-series bucket size in seconds. When omitted, a bucket size is derived from the requested window. Requests are capped at 250 data points.<br><br>**Constraints**: `>= 1` |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsPostgresMetricsResponse`](../../doc/models/v1-organizations-postgres-metrics-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

postgres_id = '00000dcc-0000-0000-0000-000000000000'

from_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

to_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = postgres_api.postgres_instance_metrics_get(
    organization_id,
    postgres_id,
    from_date,
    to_date
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPostgresMetrics400ErrorException`](../../doc/models/v1-organizations-postgres-metrics-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPostgresMetrics500ErrorException`](../../doc/models/v1-organizations-postgres-metrics-500-error-exception.md) |


# Slow Query Patterns Get List

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns aggregate metrics for the slowest query patterns observed on a Postgres service during the given time window. Use this to discover which queries dominate total execution time, CPU, I/O, or WAL generation.

```python
def slow_query_patterns_get_list(self,
                                organization_id,
                                postgres_id,
                                from_date,
                                to_date,
                                db_name=None,
                                db_user=None,
                                db_operation=None,
                                app=None,
                                sort_by="total_duration",
                                sort_order="desc",
                                limit=20,
                                offset=0)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the Postgres service. |
| `postgres_id` | `uuid\|str` | Template, Required | ID of the requested Postgres service. |
| `from_date` | `datetime` | Query, Required | Inclusive start of the time window (RFC 3339 date-time). |
| `to_date` | `datetime` | Query, Required | Exclusive end of the time window (RFC 3339 date-time). |
| `db_name` | `str` | Query, Optional | Database name filter. |
| `db_user` | `str` | Query, Optional | Database user filter. |
| `db_operation` | `str` | Query, Optional | Database operation filter (for example, SELECT, INSERT, UPDATE, DELETE, UTILITY). |
| `app` | `str` | Query, Optional | Application name filter. |
| `sort_by` | [`SortBy`](../../doc/models/sort-by.md) | Query, Optional | Field to sort results by.<br><br>**Default**: `"total_duration"` |
| `sort_order` | [`SortOrder1`](../../doc/models/sort-order-1.md) | Query, Optional | Sort order. One of `asc` or `desc`.<br><br>**Default**: `"desc"` |
| `limit` | `int` | Query, Optional | Maximum number of results to return.<br><br>**Default**: `20`<br><br>**Constraints**: `>= 1`, `<= 500` |
| `offset` | `int` | Query, Optional | Number of results to skip before returning.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0` |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsPostgresSlowQueryPatternsResponse`](../../doc/models/v1-organizations-postgres-slow-query-patterns-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

postgres_id = '00000dcc-0000-0000-0000-000000000000'

from_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

to_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

sort_by = SortBy.TOTAL_DURATION

sort_order = SortOrder1.DESC

limit = 20

offset = 0

result = postgres_api.slow_query_patterns_get_list(
    organization_id,
    postgres_id,
    from_date,
    to_date,
    sort_by=sort_by,
    sort_order=sort_order,
    limit=limit,
    offset=offset
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPostgresSlowQueryPatterns400ErrorException`](../../doc/models/v1-organizations-postgres-slow-query-patterns-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPostgresSlowQueryPatterns500ErrorException`](../../doc/models/v1-organizations-postgres-slow-query-patterns-500-error-exception.md) |


# Slow Query Pattern Get

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns aggregate metrics for a single slow query pattern together with its most recent individual executions.

```python
def slow_query_pattern_get(self,
                          organization_id,
                          postgres_id,
                          query_id,
                          db_name,
                          db_user,
                          db_operation,
                          app=None,
                          timestamp=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the Postgres service. |
| `postgres_id` | `uuid\|str` | Template, Required | ID of the requested Postgres service. |
| `query_id` | `str` | Template, Required | Stable identifier for the query pattern. |
| `db_name` | `str` | Query, Required | Database name filter. |
| `db_user` | `str` | Query, Required | Database user filter. |
| `db_operation` | `str` | Query, Required | Database operation filter (for example, SELECT, INSERT, UPDATE, DELETE, UTILITY). |
| `app` | `str` | Query, Optional | Application name filter. |
| `timestamp` | `datetime` | Query, Optional | Timestamp of a specific execution (RFC 3339). |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse`](../../doc/models/v1-organizations-postgres-slow-query-patterns-query-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

postgres_id = '00000dcc-0000-0000-0000-000000000000'

query_id = 'queryId6'

db_name = 'db_name6'

db_user = 'db_user2'

db_operation = 'db_operation2'

result = postgres_api.slow_query_pattern_get(
    organization_id,
    postgres_id,
    query_id,
    db_name,
    db_user,
    db_operation
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPostgresSlowQueryPatternsQueryId400ErrorException`](../../doc/models/v1-organizations-postgres-slow-query-patterns-query-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPostgresSlowQueryPatternsQueryId500ErrorException`](../../doc/models/v1-organizations-postgres-slow-query-patterns-query-id-500-error-exception.md) |


# Postgres Logs Get List

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns PostgreSQL server log entries for a Postgres service within the given time window, most recent first by default (override with `sort_order`). Results are paginated with `limit`/`offset`; advance `offset` until a page returns fewer than `limit` entries to read the full window. The time range must not exceed 30 days, and `to_date` must be after `from_date`.

```python
def postgres_logs_get_list(self,
                          organization_id,
                          postgres_id,
                          from_date,
                          to_date,
                          body_contains=None,
                          severity=None,
                          sort_order="desc",
                          limit=50,
                          offset=0)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the Postgres service. |
| `postgres_id` | `uuid\|str` | Template, Required | ID of the requested Postgres service. |
| `from_date` | `datetime` | Query, Required | Inclusive start of the time window (RFC 3339 date-time). |
| `to_date` | `datetime` | Query, Required | Inclusive end of the time window (RFC 3339 date-time). |
| `body_contains` | `str` | Query, Optional | Case-sensitive substring the log body must contain. |
| `severity` | `str` | Query, Optional | Filter to log entries with this PostgreSQL severity (for example, ERROR, WARNING, LOG). |
| `sort_order` | [`SortOrder1`](../../doc/models/sort-order-1.md) | Query, Optional | Sort order. One of `asc` or `desc`.<br><br>**Default**: `"desc"` |
| `limit` | `int` | Query, Optional | Maximum number of results to return.<br><br>**Default**: `50`<br><br>**Constraints**: `>= 1`, `<= 2000` |
| `offset` | `int` | Query, Optional | Number of results to skip before returning.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0` |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsPostgresLogsResponse`](../../doc/models/v1-organizations-postgres-logs-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

postgres_id = '00000dcc-0000-0000-0000-000000000000'

from_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

to_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

sort_order = SortOrder1.DESC

limit = 50

offset = 0

result = postgres_api.postgres_logs_get_list(
    organization_id,
    postgres_id,
    from_date,
    to_date,
    sort_order=sort_order,
    limit=limit,
    offset=offset
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPostgresLogs400ErrorException`](../../doc/models/v1-organizations-postgres-logs-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPostgresLogs500ErrorException`](../../doc/models/v1-organizations-postgres-logs-500-error-exception.md) |

