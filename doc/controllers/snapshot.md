# Snapshot

```python
snapshot_api = client.snapshot
```

## Class Name

`SnapshotApi`

## Methods

* [Snapshot Get List](../../doc/controllers/snapshot.md#snapshot-get-list)
* [Snapshot Get](../../doc/controllers/snapshot.md#snapshot-get)
* [Snapshot Configuration Get](../../doc/controllers/snapshot.md#snapshot-configuration-get)
* [Snapshot Configuration Update](../../doc/controllers/snapshot.md#snapshot-configuration-update)


# Snapshot Get List

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns a list of all snapshots for the service. The most recent snapshots come first in the list.

```python
def snapshot_get_list(self,
                     organization_id,
                     service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the snapshot. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service the snapshot was created from. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesSnapshotsResponse`](../../doc/models/v1-organizations-services-snapshots-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = snapshot_api.snapshot_get_list(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesSnapshots400ErrorException`](../../doc/models/v1-organizations-services-snapshots-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesSnapshots500ErrorException`](../../doc/models/v1-organizations-services-snapshots-500-error-exception.md) |


# Snapshot Get

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns a single snapshot info.

```python
def snapshot_get(self,
                organization_id,
                service_id,
                snapshot_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the snapshot. |
| `service_id` | `uuid\|str` | Template, Required | ID of the service the snapshot was created from. |
| `snapshot_id` | `uuid\|str` | Template, Required | ID of the requested snapshot. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesSnapshotsSnapshotIdResponse`](../../doc/models/v1-organizations-services-snapshots-snapshot-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

snapshot_id = '0000088e-0000-0000-0000-000000000000'

result = snapshot_api.snapshot_get(
    organization_id,
    service_id,
    snapshot_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesSnapshotsSnapshotId400ErrorException`](../../doc/models/v1-organizations-services-snapshots-snapshot-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesSnapshotsSnapshotId500ErrorException`](../../doc/models/v1-organizations-services-snapshots-snapshot-id-500-error-exception.md) |


# Snapshot Configuration Get

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Returns the service snapshot configuration.

```python
def snapshot_configuration_get(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesSnapshotConfigurationResponse`](../../doc/models/v1-organizations-services-snapshot-configuration-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = snapshot_api.snapshot_configuration_get(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesSnapshotConfiguration400ErrorException`](../../doc/models/v1-organizations-services-snapshot-configuration-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesSnapshotConfiguration500ErrorException`](../../doc/models/v1-organizations-services-snapshot-configuration-500-error-exception.md) |


# Snapshot Configuration Update

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> Updates the service snapshot configuration. Requires ADMIN auth key role. Enables or disables scheduled snapshots and sets the cadence; when enabled, gap and timeFrame (in minutes) must together be one of the supported (gap, timeFrame) pairs: (30, 1440), (60, 2880). Provide at least one of enabled, gap, timeFrame; omit a field to leave it unchanged (null is not accepted).

```python
def snapshot_configuration_update(self,
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
| `body` | [`SnapshotConfigurationPatchRequest`](../../doc/models/snapshot-configuration-patch-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesSnapshotConfigurationResponse`](../../doc/models/v1-organizations-services-snapshot-configuration-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = snapshot_api.snapshot_configuration_update(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesSnapshotConfiguration400ErrorException`](../../doc/models/v1-organizations-services-snapshot-configuration-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesSnapshotConfiguration500ErrorException`](../../doc/models/v1-organizations-services-snapshot-configuration-500-error-exception.md) |

