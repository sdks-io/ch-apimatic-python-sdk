# Backup

```python
backup_api = client.backup
```

## Class Name

`BackupApi`

## Methods

* [Backup Get List](../../doc/controllers/backup.md#backup-get-list)
* [Backup Get](../../doc/controllers/backup.md#backup-get)
* [Backup Configuration Get](../../doc/controllers/backup.md#backup-configuration-get)
* [Backup Configuration Update](../../doc/controllers/backup.md#backup-configuration-update)
* [Backup Bucket Get](../../doc/controllers/backup.md#backup-bucket-get)
* [Backup Bucket Create](../../doc/controllers/backup.md#backup-bucket-create)
* [Backup Bucket Update](../../doc/controllers/backup.md#backup-bucket-update)
* [Backup Bucket Delete](../../doc/controllers/backup.md#backup-bucket-delete)


# Backup Get List

Returns a list of all backups for the service. The most recent backups comes first in the list.

```python
def backup_get_list(self,
                   organization_id,
                   service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the backup. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service the backup was created from. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesBackupsResponse`](../../doc/models/v1-organizations-services-backups-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = backup_api.backup_get_list(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesBackups400ErrorException`](../../doc/models/v1-organizations-services-backups-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesBackups500ErrorException`](../../doc/models/v1-organizations-services-backups-500-error-exception.md) |


# Backup Get

Returns a single backup info.

```python
def backup_get(self,
              organization_id,
              service_id,
              backup_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the backup. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service the backup was created from. |
| `backup_id` | `uuid\|str` | Template, Required | ID of the requested backup. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesBackupsBackupIdResponse`](../../doc/models/v1-organizations-services-backups-backup-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

backup_id = '00000c90-0000-0000-0000-000000000000'

result = backup_api.backup_get(
    organization_id,
    service_id,
    backup_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesBackupsBackupId400ErrorException`](../../doc/models/v1-organizations-services-backups-backup-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesBackupsBackupId500ErrorException`](../../doc/models/v1-organizations-services-backups-backup-id-500-error-exception.md) |


# Backup Configuration Get

Returns the service backup configuration.

```python
def backup_configuration_get(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesBackupConfigurationResponse`](../../doc/models/v1-organizations-services-backup-configuration-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = backup_api.backup_configuration_get(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesBackupConfiguration400ErrorException`](../../doc/models/v1-organizations-services-backup-configuration-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesBackupConfiguration500ErrorException`](../../doc/models/v1-organizations-services-backup-configuration-500-error-exception.md) |


# Backup Configuration Update

Updates service backup configuration. Requires ADMIN auth key role. Setting the properties with null value, will reset the properties to theirs default values.

```python
def backup_configuration_update(self,
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
| `body` | [`BackupConfigurationPatchRequest`](../../doc/models/backup-configuration-patch-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesBackupConfigurationResponse`](../../doc/models/v1-organizations-services-backup-configuration-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = backup_api.backup_configuration_update(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesBackupConfiguration400ErrorException`](../../doc/models/v1-organizations-services-backup-configuration-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesBackupConfiguration500ErrorException`](../../doc/models/v1-organizations-services-backup-configuration-500-error-exception.md) |


# Backup Bucket Get

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns the service backup bucket.

```python
def backup_bucket_get(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesBackupBucketResponse`](../../doc/models/v1-organizations-services-backup-bucket-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = backup_api.backup_bucket_get(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesBackupBucket400ErrorException`](../../doc/models/v1-organizations-services-backup-bucket-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesBackupBucket500ErrorException`](../../doc/models/v1-organizations-services-backup-bucket-500-error-exception.md) |


# Backup Bucket Create

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Create service backup bucket. Requires ADMIN auth key role.

```python
def backup_bucket_create(self,
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
| `body` | [AwsBackupBucketPostRequestV1](../../doc/models/aws-backup-bucket-post-request-v1.md) \| [GcpBackupBucketPostRequestV1](../../doc/models/gcp-backup-bucket-post-request-v1.md) \| [AzureBackupBucketPostRequestV1](../../doc/models/azure-backup-bucket-post-request-v1.md) \| None | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesBackupBucketResponse`](../../doc/models/v1-organizations-services-backup-bucket-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = backup_api.backup_bucket_create(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesBackupBucket400ErrorException`](../../doc/models/v1-organizations-services-backup-bucket-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesBackupBucket500ErrorException`](../../doc/models/v1-organizations-services-backup-bucket-500-error-exception.md) |


# Backup Bucket Update

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Update service backup bucket. Requires ADMIN auth key role. The secrets of the specified bucket provider are always required

```python
def backup_bucket_update(self,
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
| `body` | [AwsBackupBucketPatchRequestV1](../../doc/models/aws-backup-bucket-patch-request-v1.md) \| [GcpBackupBucketPatchRequestV1](../../doc/models/gcp-backup-bucket-patch-request-v1.md) \| [AzureBackupBucketPatchRequestV1](../../doc/models/azure-backup-bucket-patch-request-v1.md) \| None | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesBackupBucketResponse`](../../doc/models/v1-organizations-services-backup-bucket-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = backup_api.backup_bucket_update(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesBackupBucket400ErrorException`](../../doc/models/v1-organizations-services-backup-bucket-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesBackupBucket500ErrorException`](../../doc/models/v1-organizations-services-backup-bucket-500-error-exception.md) |


# Backup Bucket Delete

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Delete service backup bucket. Requires ADMIN auth key role.

```python
def backup_bucket_delete(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesBackupBucketResponse3`](../../doc/models/v1-organizations-services-backup-bucket-response-3.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = backup_api.backup_bucket_delete(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesBackupBucket400ErrorException`](../../doc/models/v1-organizations-services-backup-bucket-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesBackupBucket500ErrorException`](../../doc/models/v1-organizations-services-backup-bucket-500-error-exception.md) |

