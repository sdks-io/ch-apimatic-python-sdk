# Click Stack

```python
click_stack_api = client.click_stack
```

## Class Name

`ClickStackApi`

## Methods

* [Click Stack List Dashboards](../../doc/controllers/click-stack.md#click-stack-list-dashboards)
* [Click Stack Create Dashboard](../../doc/controllers/click-stack.md#click-stack-create-dashboard)
* [Click Stack Get Dashboard](../../doc/controllers/click-stack.md#click-stack-get-dashboard)
* [Click Stack Update Dashboard](../../doc/controllers/click-stack.md#click-stack-update-dashboard)
* [Click Stack Delete Dashboard](../../doc/controllers/click-stack.md#click-stack-delete-dashboard)
* [Click Stack Validate Dashboard](../../doc/controllers/click-stack.md#click-stack-validate-dashboard)
* [Click Stack List Alerts](../../doc/controllers/click-stack.md#click-stack-list-alerts)
* [Click Stack Create Alert](../../doc/controllers/click-stack.md#click-stack-create-alert)
* [Click Stack List Sources](../../doc/controllers/click-stack.md#click-stack-list-sources)
* [Click Stack Create Source](../../doc/controllers/click-stack.md#click-stack-create-source)
* [Click Stack Get Source](../../doc/controllers/click-stack.md#click-stack-get-source)
* [Click Stack Update Source](../../doc/controllers/click-stack.md#click-stack-update-source)
* [Click Stack Delete Source](../../doc/controllers/click-stack.md#click-stack-delete-source)
* [Click Stack Get Alert](../../doc/controllers/click-stack.md#click-stack-get-alert)
* [Click Stack Update Alert](../../doc/controllers/click-stack.md#click-stack-update-alert)
* [Click Stack Delete Alert](../../doc/controllers/click-stack.md#click-stack-delete-alert)
* [Click Stack List Webhooks](../../doc/controllers/click-stack.md#click-stack-list-webhooks)
* [Click Stack Create Webhook](../../doc/controllers/click-stack.md#click-stack-create-webhook)
* [Click Stack Update Webhook](../../doc/controllers/click-stack.md#click-stack-update-webhook)
* [Click Stack Delete Webhook](../../doc/controllers/click-stack.md#click-stack-delete-webhook)
* [Click Stack List Roles](../../doc/controllers/click-stack.md#click-stack-list-roles)
* [Click Stack Create Role](../../doc/controllers/click-stack.md#click-stack-create-role)
* [Click Stack Get Role](../../doc/controllers/click-stack.md#click-stack-get-role)
* [Click Stack Update Role](../../doc/controllers/click-stack.md#click-stack-update-role)
* [Click Stack Delete Role](../../doc/controllers/click-stack.md#click-stack-delete-role)
* [Click Stack List Saved Searches](../../doc/controllers/click-stack.md#click-stack-list-saved-searches)
* [Click Stack Create Saved Search](../../doc/controllers/click-stack.md#click-stack-create-saved-search)
* [Click Stack Get Saved Search](../../doc/controllers/click-stack.md#click-stack-get-saved-search)
* [Click Stack Update Saved Search](../../doc/controllers/click-stack.md#click-stack-update-saved-search)
* [Click Stack Delete Saved Search](../../doc/controllers/click-stack.md#click-stack-delete-saved-search)


# Click Stack List Dashboards

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves a list of all dashboards for the authenticated team

```python
def click_stack_list_dashboards(self,
                               organization_id,
                               service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackDashboardsResponse`](../../doc/models/v1-organizations-services-clickstack-dashboards-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = click_stack_api.click_stack_list_dashboards(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackDashboards400ErrorException`](../../doc/models/v1-organizations-services-clickstack-dashboards-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackDashboards500ErrorException`](../../doc/models/v1-organizations-services-clickstack-dashboards-500-error-exception.md) |


# Click Stack Create Dashboard

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Creates a new dashboard

```python
def click_stack_create_dashboard(self,
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
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `body` | [`ClickStackCreateDashboardRequest`](../../doc/models/click-stack-create-dashboard-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackDashboardsResponse1`](../../doc/models/v1-organizations-services-clickstack-dashboards-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

body = ClickStackCreateDashboardRequest(
    name='New Dashboard',
    tiles=[
        ClickStackTileInput(
            name='Error Rate',
            x=0,
            y=0,
            w=6,
            h=3,
            container_id='service-health',
            tab_id='errors',
            id='65f5e4a3b9e77c001a901234',
            as_ratio=False
        )
    ],
    tags=[
        'development'
    ],
    saved_query='service.name = \'api\'',
    saved_query_language=SavedQueryLanguage.SQL
)

result = click_stack_api.click_stack_create_dashboard(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackDashboards400ErrorException`](../../doc/models/v1-organizations-services-clickstack-dashboards-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackDashboards500ErrorException`](../../doc/models/v1-organizations-services-clickstack-dashboards-500-error-exception.md) |


# Click Stack Get Dashboard

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves a specific dashboard by ID

```python
def click_stack_get_dashboard(self,
                             organization_id,
                             service_id,
                             click_stack_dashboard_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `click_stack_dashboard_id` | `str` | Template, Required | ClickStack Dashboard ID |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse`](../../doc/models/v1-organizations-services-clickstack-dashboards-click-stack-dashboard-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_stack_dashboard_id = 'clickStackDashboardId6'

result = click_stack_api.click_stack_get_dashboard(
    organization_id,
    service_id,
    click_stack_dashboard_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400ErrorException`](../../doc/models/v1-organizations-services-clickstack-dashboards-click-stack-dashboard-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500ErrorException`](../../doc/models/v1-organizations-services-clickstack-dashboards-click-stack-dashboard-id-500-error-exception.md) |


# Click Stack Update Dashboard

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Updates an existing dashboard.  **Concurrency:** This endpoint does not support optimistic concurrency control. Concurrent PUT requests for the same dashboard may silently overwrite each other, which can leave orphan tile-to-container references on layout-shape edits. Clients should serialize edits to a given dashboard.

```python
def click_stack_update_dashboard(self,
                                organization_id,
                                service_id,
                                click_stack_dashboard_id,
                                body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `click_stack_dashboard_id` | `str` | Template, Required | ClickStack Dashboard ID |
| `body` | [`ClickStackUpdateDashboardRequest`](../../doc/models/click-stack-update-dashboard-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse`](../../doc/models/v1-organizations-services-clickstack-dashboards-click-stack-dashboard-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_stack_dashboard_id = 'clickStackDashboardId6'

body = ClickStackUpdateDashboardRequest(
    name='Updated Dashboard Name',
    tiles=[
        ClickStackTileInput(
            name='Error Rate',
            x=0,
            y=0,
            w=6,
            h=3,
            container_id='service-health',
            tab_id='errors',
            id='65f5e4a3b9e77c001a901234',
            as_ratio=False
        )
    ],
    tags=[
        'production',
        'updated'
    ],
    saved_query='service.name = \'api\'',
    saved_query_language=SavedQueryLanguage.SQL
)

result = click_stack_api.click_stack_update_dashboard(
    organization_id,
    service_id,
    click_stack_dashboard_id,
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400ErrorException`](../../doc/models/v1-organizations-services-clickstack-dashboards-click-stack-dashboard-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500ErrorException`](../../doc/models/v1-organizations-services-clickstack-dashboards-click-stack-dashboard-id-500-error-exception.md) |


# Click Stack Delete Dashboard

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Deletes a dashboard

```python
def click_stack_delete_dashboard(self,
                                organization_id,
                                service_id,
                                click_stack_dashboard_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `click_stack_dashboard_id` | `str` | Template, Required | ClickStack Dashboard ID |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2`](../../doc/models/v1-organizations-services-clickstack-dashboards-click-stack-dashboard-id-response-2.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_stack_dashboard_id = 'clickStackDashboardId6'

result = click_stack_api.click_stack_delete_dashboard(
    organization_id,
    service_id,
    click_stack_dashboard_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400ErrorException`](../../doc/models/v1-organizations-services-clickstack-dashboards-click-stack-dashboard-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500ErrorException`](../../doc/models/v1-organizations-services-clickstack-dashboards-click-stack-dashboard-id-500-error-exception.md) |


# Click Stack Validate Dashboard

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Validates a dashboard body against the same schema and tile rules used by POST /api/v2/dashboards. The dashboard is **never persisted**. Use this endpoint at plan time (e.g. from a Terraform provider) to check that a dashboard configuration is valid before applying it.

```python
def click_stack_validate_dashboard(self,
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
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `body` | [`ClickStackCreateDashboardRequest`](../../doc/models/click-stack-create-dashboard-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackDashboardsValidateResponse`](../../doc/models/v1-organizations-services-clickstack-dashboards-validate-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

body = ClickStackCreateDashboardRequest(
    name='New Dashboard',
    tiles=[
        ClickStackTileInput(
            name='Error Rate',
            x=0,
            y=0,
            w=6,
            h=3,
            container_id='service-health',
            tab_id='errors',
            id='65f5e4a3b9e77c001a901234',
            as_ratio=False
        )
    ],
    tags=[
        'development'
    ],
    saved_query='service.name = \'api\'',
    saved_query_language=SavedQueryLanguage.SQL
)

result = click_stack_api.click_stack_validate_dashboard(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackDashboardsValidate400ErrorException`](../../doc/models/v1-organizations-services-clickstack-dashboards-validate-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackDashboardsValidate500ErrorException`](../../doc/models/v1-organizations-services-clickstack-dashboards-validate-500-error-exception.md) |


# Click Stack List Alerts

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves alerts for the authenticated team (paginated). Results are capped at `limit` (default and maximum 1000). When `totalCount` exceeds the number of returned items, page with `limit`/`offset` to retrieve them all.

```python
def click_stack_list_alerts(self,
                           organization_id,
                           service_id,
                           limit=1000,
                           offset=0)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `limit` | `int` | Query, Optional | Maximum number of results to return.<br><br>**Default**: `1000`<br><br>**Constraints**: `>= 1`, `<= 1000` |
| `offset` | `int` | Query, Optional | Number of results to skip before returning.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0` |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackAlertsResponse`](../../doc/models/v1-organizations-services-clickstack-alerts-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

limit = 1000

offset = 0

result = click_stack_api.click_stack_list_alerts(
    organization_id,
    service_id,
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackAlerts400ErrorException`](../../doc/models/v1-organizations-services-clickstack-alerts-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackAlerts500ErrorException`](../../doc/models/v1-organizations-services-clickstack-alerts-500-error-exception.md) |


# Click Stack Create Alert

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Creates a new alert

```python
def click_stack_create_alert(self,
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
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `body` | [`ClickStackCreateAlertRequest`](../../doc/models/click-stack-create-alert-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackAlertsResponse1`](../../doc/models/v1-organizations-services-clickstack-alerts-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

body = ClickStackCreateAlertRequest(
    dashboard_id='65f5e4a3b9e77c001a567890',
    tile_id='65f5e4a3b9e77c001a901234',
    saved_search_id='65f5e4a3b9e77c001a345678',
    group_by='ServiceName',
    threshold=100,
    threshold_max=500,
    interval=Interval.ENUM_1H,
    schedule_offset_minutes=2,
    schedule_start_at=dateutil.parser.parse('02/08/2026 10:00:00'),
    source=Source.TILE,
    threshold_type=ThresholdType.ABOVE,
    name='Test Alert',
    message='Test Alert Message',
    note='Threshold raised from 50 to 100 on 2026-01-15. See [runbook](https://wiki.example.com/runbook).',
    num_consecutive_windows=3
)

result = click_stack_api.click_stack_create_alert(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackAlerts400ErrorException`](../../doc/models/v1-organizations-services-clickstack-alerts-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackAlerts500ErrorException`](../../doc/models/v1-organizations-services-clickstack-alerts-500-error-exception.md) |


# Click Stack List Sources

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves a list of all sources for the authenticated team

```python
def click_stack_list_sources(self,
                            organization_id,
                            service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackSourcesResponse`](../../doc/models/v1-organizations-services-clickstack-sources-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = click_stack_api.click_stack_list_sources(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackSources400ErrorException`](../../doc/models/v1-organizations-services-clickstack-sources-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackSources500ErrorException`](../../doc/models/v1-organizations-services-clickstack-sources-500-error-exception.md) |


# Click Stack Create Source

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Creates a new source.  The request body is a source object without the `id` field. If an `id` is sent anyway it is silently ignored (stripped before validation — the request is never rejected because of it). Granularity fields (`materializedViews[].minGranularity` and `metadataMaterializedViews.granularity`) accept the same short format the API returns (e.g. `5m`, `15s`, `1h`, `1d`).

```python
def click_stack_create_source(self,
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
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `body` | [ClickStackLogSource](../../doc/models/click-stack-log-source.md) \| [ClickStackTraceSource](../../doc/models/click-stack-trace-source.md) \| [ClickStackMetricSource](../../doc/models/click-stack-metric-source.md) \| [ClickStackSessionSource](../../doc/models/click-stack-session-source.md) \| [ClickStackPromqlSource](../../doc/models/click-stack-promql-source.md) \| None | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackSourcesResponse1`](../../doc/models/v1-organizations-services-clickstack-sources-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

body = ClickStackLogSource(
    name='Logs',
    connection='507f1f77bcf86cd799439012',
    mfrom=ClickStackSourceFrom(
        database_name='otel',
        table_name='otel_logs'
    ),
    default_table_select_expression='Timestamp, ServiceName, SeverityText, Body',
    timestamp_value_expression='Timestamp',
    id='507f1f77bcf86cd799439011',
    section='Billing',
    disabled=False,
    service_name_expression='ServiceName',
    service_version_expression='ResourceAttributes[\'service.version\']',
    severity_text_expression='SeverityText',
    body_expression='Body',
    event_attributes_expression='LogAttributes',
    resource_attributes_expression='ResourceAttributes',
    displayed_timestamp_value_expression='TimestampTime',
    metric_source_id='507f1f77bcf86cd799439013',
    trace_source_id='507f1f77bcf86cd799439014',
    trace_id_expression='TraceId',
    span_id_expression='SpanId',
    implicit_column_expression='Body',
    known_columns_list_expression='Timestamp, Body, ServiceName',
    use_text_index_for_implicit_column=UseTextIndexForImplicitColumn.AUTO
)

result = click_stack_api.click_stack_create_source(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackSources400ErrorException`](../../doc/models/v1-organizations-services-clickstack-sources-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackSources500ErrorException`](../../doc/models/v1-organizations-services-clickstack-sources-500-error-exception.md) |


# Click Stack Get Source

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves a specific source by ID

```python
def click_stack_get_source(self,
                          organization_id,
                          service_id,
                          click_stack_source_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `click_stack_source_id` | `str` | Template, Required | Source ID |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse`](../../doc/models/v1-organizations-services-clickstack-sources-click-stack-source-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_stack_source_id = 'clickStackSourceId8'

result = click_stack_api.click_stack_get_source(
    organization_id,
    service_id,
    click_stack_source_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackSourcesClickStackSourceId400ErrorException`](../../doc/models/v1-organizations-services-clickstack-sources-click-stack-source-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackSourcesClickStackSourceId500ErrorException`](../../doc/models/v1-organizations-services-clickstack-sources-click-stack-source-id-500-error-exception.md) |


# Click Stack Update Source

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Updates an existing source. The full source object must be provided; this is a replace, not a patch.  The request body is a source object without the `id` field. If an `id` is sent anyway it is silently ignored (stripped before validation — never a 400); the path parameter alone identifies the source. Granularity fields (`materializedViews[].minGranularity` and `metadataMaterializedViews.granularity`) accept the same short format the API returns (e.g. `5m`, `15s`, `1h`, `1d`).

```python
def click_stack_update_source(self,
                             organization_id,
                             service_id,
                             click_stack_source_id,
                             body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `click_stack_source_id` | `str` | Template, Required | Source ID |
| `body` | [ClickStackLogSource](../../doc/models/click-stack-log-source.md) \| [ClickStackTraceSource](../../doc/models/click-stack-trace-source.md) \| [ClickStackMetricSource](../../doc/models/click-stack-metric-source.md) \| [ClickStackSessionSource](../../doc/models/click-stack-session-source.md) \| [ClickStackPromqlSource](../../doc/models/click-stack-promql-source.md) \| None | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse`](../../doc/models/v1-organizations-services-clickstack-sources-click-stack-source-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_stack_source_id = 'clickStackSourceId8'

body = ClickStackLogSource(
    name='Logs',
    connection='507f1f77bcf86cd799439012',
    mfrom=ClickStackSourceFrom(
        database_name='otel',
        table_name='otel_logs'
    ),
    default_table_select_expression='Timestamp, ServiceName, SeverityText, Body',
    timestamp_value_expression='Timestamp',
    id='507f1f77bcf86cd799439011',
    section='Billing',
    disabled=False,
    service_name_expression='ServiceName',
    service_version_expression='ResourceAttributes[\'service.version\']',
    severity_text_expression='SeverityText',
    body_expression='Body',
    event_attributes_expression='LogAttributes',
    resource_attributes_expression='ResourceAttributes',
    displayed_timestamp_value_expression='TimestampTime',
    metric_source_id='507f1f77bcf86cd799439013',
    trace_source_id='507f1f77bcf86cd799439014',
    trace_id_expression='TraceId',
    span_id_expression='SpanId',
    implicit_column_expression='Body',
    known_columns_list_expression='Timestamp, Body, ServiceName',
    use_text_index_for_implicit_column=UseTextIndexForImplicitColumn.AUTO
)

result = click_stack_api.click_stack_update_source(
    organization_id,
    service_id,
    click_stack_source_id,
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackSourcesClickStackSourceId400ErrorException`](../../doc/models/v1-organizations-services-clickstack-sources-click-stack-source-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackSourcesClickStackSourceId500ErrorException`](../../doc/models/v1-organizations-services-clickstack-sources-click-stack-source-id-500-error-exception.md) |


# Click Stack Delete Source

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Deletes a source

```python
def click_stack_delete_source(self,
                             organization_id,
                             service_id,
                             click_stack_source_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `click_stack_source_id` | `str` | Template, Required | Source ID |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2`](../../doc/models/v1-organizations-services-clickstack-sources-click-stack-source-id-response-2.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_stack_source_id = 'clickStackSourceId8'

result = click_stack_api.click_stack_delete_source(
    organization_id,
    service_id,
    click_stack_source_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackSourcesClickStackSourceId400ErrorException`](../../doc/models/v1-organizations-services-clickstack-sources-click-stack-source-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackSourcesClickStackSourceId500ErrorException`](../../doc/models/v1-organizations-services-clickstack-sources-click-stack-source-id-500-error-exception.md) |


# Click Stack Get Alert

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves a specific alert by ID

```python
def click_stack_get_alert(self,
                         organization_id,
                         service_id,
                         click_stack_alert_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `click_stack_alert_id` | `str` | Template, Required | ClickStack Alert ID |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse`](../../doc/models/v1-organizations-services-clickstack-alerts-click-stack-alert-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_stack_alert_id = 'clickStackAlertId2'

result = click_stack_api.click_stack_get_alert(
    organization_id,
    service_id,
    click_stack_alert_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackAlertsClickStackAlertId400ErrorException`](../../doc/models/v1-organizations-services-clickstack-alerts-click-stack-alert-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackAlertsClickStackAlertId500ErrorException`](../../doc/models/v1-organizations-services-clickstack-alerts-click-stack-alert-id-500-error-exception.md) |


# Click Stack Update Alert

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Updates an existing alert

```python
def click_stack_update_alert(self,
                            organization_id,
                            service_id,
                            click_stack_alert_id,
                            body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `click_stack_alert_id` | `str` | Template, Required | ClickStack Alert ID |
| `body` | [`ClickStackUpdateAlertRequest`](../../doc/models/click-stack-update-alert-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse`](../../doc/models/v1-organizations-services-clickstack-alerts-click-stack-alert-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_stack_alert_id = 'clickStackAlertId2'

body = ClickStackUpdateAlertRequest(
    dashboard_id='65f5e4a3b9e77c001a567890',
    tile_id='65f5e4a3b9e77c001a901234',
    saved_search_id='65f5e4a3b9e77c001a345678',
    group_by='ServiceName',
    threshold=100,
    threshold_max=500,
    interval=Interval.ENUM_1H,
    schedule_offset_minutes=2,
    schedule_start_at=dateutil.parser.parse('02/08/2026 10:00:00'),
    source=Source.TILE,
    threshold_type=ThresholdType.ABOVE,
    name='Test Alert',
    message='Test Alert Message',
    note='Threshold raised from 50 to 100 on 2026-01-15. See [runbook](https://wiki.example.com/runbook).',
    num_consecutive_windows=3
)

result = click_stack_api.click_stack_update_alert(
    organization_id,
    service_id,
    click_stack_alert_id,
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackAlertsClickStackAlertId400ErrorException`](../../doc/models/v1-organizations-services-clickstack-alerts-click-stack-alert-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackAlertsClickStackAlertId500ErrorException`](../../doc/models/v1-organizations-services-clickstack-alerts-click-stack-alert-id-500-error-exception.md) |


# Click Stack Delete Alert

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Deletes an alert

```python
def click_stack_delete_alert(self,
                            organization_id,
                            service_id,
                            click_stack_alert_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `click_stack_alert_id` | `str` | Template, Required | ClickStack Alert ID |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2`](../../doc/models/v1-organizations-services-clickstack-alerts-click-stack-alert-id-response-2.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_stack_alert_id = 'clickStackAlertId2'

result = click_stack_api.click_stack_delete_alert(
    organization_id,
    service_id,
    click_stack_alert_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackAlertsClickStackAlertId400ErrorException`](../../doc/models/v1-organizations-services-clickstack-alerts-click-stack-alert-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackAlertsClickStackAlertId500ErrorException`](../../doc/models/v1-organizations-services-clickstack-alerts-click-stack-alert-id-500-error-exception.md) |


# Click Stack List Webhooks

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves webhooks for the authenticated team (paginated). Results are capped at `limit` (default and maximum 1000). When `totalCount` exceeds the number of returned items, page with `limit`/`offset` to retrieve them all.

```python
def click_stack_list_webhooks(self,
                             organization_id,
                             service_id,
                             limit=1000,
                             offset=0)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `limit` | `int` | Query, Optional | Maximum number of results to return.<br><br>**Default**: `1000`<br><br>**Constraints**: `>= 1`, `<= 1000` |
| `offset` | `int` | Query, Optional | Number of results to skip before returning.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0` |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackWebhooksResponse`](../../doc/models/v1-organizations-services-clickstack-webhooks-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

limit = 1000

offset = 0

result = click_stack_api.click_stack_list_webhooks(
    organization_id,
    service_id,
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackWebhooks400ErrorException`](../../doc/models/v1-organizations-services-clickstack-webhooks-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackWebhooks500ErrorException`](../../doc/models/v1-organizations-services-clickstack-webhooks-500-error-exception.md) |


# Click Stack Create Webhook

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Creates a new webhook for the authenticated team.

```python
def click_stack_create_webhook(self,
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
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `body` | [`ClickStackWebhookInput`](../../doc/models/click-stack-webhook-input.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackWebhooksResponse1`](../../doc/models/v1-organizations-services-clickstack-webhooks-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

body = ClickStackWebhookInput(
    name='Production Alerts',
    service=Service1.SLACK,
    url='https://hooks.slack.com/services/EXAMPLE/WEBHOOK/URL',
    description='Sends critical alerts to the #incidents channel',
    body='{"alert": "{{title}}", "severity": "{{level}}"}'
)

result = click_stack_api.click_stack_create_webhook(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackWebhooks400ErrorException`](../../doc/models/v1-organizations-services-clickstack-webhooks-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackWebhooks500ErrorException`](../../doc/models/v1-organizations-services-clickstack-webhooks-500-error-exception.md) |


# Click Stack Update Webhook

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Replaces an existing webhook. Readable optional fields (`description`, `body`) are a full replace: omitting them clears them. The write-only fields `headers` and `queryParams` are never returned on read, so omitting them preserves the stored values; send an explicit empty object (`{}`) to clear them. Exception: if the destination (`url` or `service`) changes, omitted `headers`/ `queryParams` are cleared rather than preserved so stored secrets are never forwarded to a new destination.

```python
def click_stack_update_webhook(self,
                              organization_id,
                              service_id,
                              click_stack_webhook_id,
                              body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `click_stack_webhook_id` | `str` | Template, Required | Webhook ID |
| `body` | [`ClickStackWebhookInput`](../../doc/models/click-stack-webhook-input.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse`](../../doc/models/v1-organizations-services-clickstack-webhooks-click-stack-webhook-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_stack_webhook_id = 'clickStackWebhookId2'

body = ClickStackWebhookInput(
    name='Production Alerts',
    service=Service1.SLACK,
    url='https://hooks.slack.com/services/EXAMPLE/WEBHOOK/URL',
    description='Sends critical alerts to the #incidents channel',
    body='{"alert": "{{title}}", "severity": "{{level}}"}'
)

result = click_stack_api.click_stack_update_webhook(
    organization_id,
    service_id,
    click_stack_webhook_id,
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackWebhooksClickStackWebhookId400ErrorException`](../../doc/models/v1-organizations-services-clickstack-webhooks-click-stack-webhook-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackWebhooksClickStackWebhookId500ErrorException`](../../doc/models/v1-organizations-services-clickstack-webhooks-click-stack-webhook-id-500-error-exception.md) |


# Click Stack Delete Webhook

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Deletes a webhook. Blocked with a 409 while any alert still references it — reassign or remove those alerts first — so deletion never leaves an alert pointing at a missing webhook (which would silently drop notifications). Mirrors the internal webhook delete guard.

```python
def click_stack_delete_webhook(self,
                              organization_id,
                              service_id,
                              click_stack_webhook_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `click_stack_webhook_id` | `str` | Template, Required | Webhook ID |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1`](../../doc/models/v1-organizations-services-clickstack-webhooks-click-stack-webhook-id-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_stack_webhook_id = 'clickStackWebhookId2'

result = click_stack_api.click_stack_delete_webhook(
    organization_id,
    service_id,
    click_stack_webhook_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackWebhooksClickStackWebhookId400ErrorException`](../../doc/models/v1-organizations-services-clickstack-webhooks-click-stack-webhook-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackWebhooksClickStackWebhookId500ErrorException`](../../doc/models/v1-organizations-services-clickstack-webhooks-click-stack-webhook-id-500-error-exception.md) |


# Click Stack List Roles

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves all roles for the authenticated team, including predefined roles.

```python
def click_stack_list_roles(self,
                          organization_id,
                          service_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackRolesResponse`](../../doc/models/v1-organizations-services-clickstack-roles-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = click_stack_api.click_stack_list_roles(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackRoles400ErrorException`](../../doc/models/v1-organizations-services-clickstack-roles-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackRoles500ErrorException`](../../doc/models/v1-organizations-services-clickstack-roles-500-error-exception.md) |


# Click Stack Create Role

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Creates a new custom role for the team.

```python
def click_stack_create_role(self,
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
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `body` | [`ClickStackCreateRoleRequest`](../../doc/models/click-stack-create-role-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackRolesResponse1`](../../doc/models/v1-organizations-services-clickstack-roles-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

body = ClickStackCreateRoleRequest(
    name='Deploy Bot',
    permissions=[
        ClickStackCaslPermission(
            action='read',
            subject='dashboard',
            inverted=False,
            integration='mongodb'
        )
    ],
    description='Manages dashboards via Terraform'
)

result = click_stack_api.click_stack_create_role(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackRoles400ErrorException`](../../doc/models/v1-organizations-services-clickstack-roles-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackRoles500ErrorException`](../../doc/models/v1-organizations-services-clickstack-roles-500-error-exception.md) |


# Click Stack Get Role

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves a specific role by ID.

```python
def click_stack_get_role(self,
                        organization_id,
                        service_id,
                        click_stack_role_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `click_stack_role_id` | `str` | Template, Required | id parameter |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse`](../../doc/models/v1-organizations-services-clickstack-roles-click-stack-role-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_stack_role_id = 'clickStackRoleId6'

result = click_stack_api.click_stack_get_role(
    organization_id,
    service_id,
    click_stack_role_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackRolesClickStackRoleId400ErrorException`](../../doc/models/v1-organizations-services-clickstack-roles-click-stack-role-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackRolesClickStackRoleId500ErrorException`](../../doc/models/v1-organizations-services-clickstack-roles-click-stack-role-id-500-error-exception.md) |


# Click Stack Update Role

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Updates a custom role's permissions, name, and description. Predefined roles cannot be modified.

```python
def click_stack_update_role(self,
                           organization_id,
                           service_id,
                           click_stack_role_id,
                           body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `click_stack_role_id` | `str` | Template, Required | id parameter |
| `body` | [`ClickStackUpdateRoleRequest`](../../doc/models/click-stack-update-role-request.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse`](../../doc/models/v1-organizations-services-clickstack-roles-click-stack-role-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_stack_role_id = 'clickStackRoleId6'

body = ClickStackUpdateRoleRequest(
    permissions=[
        ClickStackCaslPermission(
            action='read',
            subject='dashboard',
            inverted=False,
            integration='mongodb'
        )
    ],
    name='Deploy Bot',
    description='Manages dashboards via Terraform'
)

result = click_stack_api.click_stack_update_role(
    organization_id,
    service_id,
    click_stack_role_id,
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackRolesClickStackRoleId400ErrorException`](../../doc/models/v1-organizations-services-clickstack-roles-click-stack-role-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackRolesClickStackRoleId500ErrorException`](../../doc/models/v1-organizations-services-clickstack-roles-click-stack-role-id-500-error-exception.md) |


# Click Stack Delete Role

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Deletes a custom role. Predefined roles, the team default user role, and roles assigned to users cannot be deleted.

```python
def click_stack_delete_role(self,
                           organization_id,
                           service_id,
                           click_stack_role_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `click_stack_role_id` | `str` | Template, Required | id parameter |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2`](../../doc/models/v1-organizations-services-clickstack-roles-click-stack-role-id-response-2.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_stack_role_id = 'clickStackRoleId6'

result = click_stack_api.click_stack_delete_role(
    organization_id,
    service_id,
    click_stack_role_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackRolesClickStackRoleId400ErrorException`](../../doc/models/v1-organizations-services-clickstack-roles-click-stack-role-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackRolesClickStackRoleId500ErrorException`](../../doc/models/v1-organizations-services-clickstack-roles-click-stack-role-id-500-error-exception.md) |


# Click Stack List Saved Searches

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves saved searches for the authenticated team (paginated). Results are capped at `limit` (default and maximum 1000). When `totalCount` exceeds the number of returned items, page with `limit`/`offset` to retrieve them all.

```python
def click_stack_list_saved_searches(self,
                                   organization_id,
                                   service_id,
                                   limit=1000,
                                   offset=0)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `limit` | `int` | Query, Optional | Maximum number of results to return.<br><br>**Default**: `1000`<br><br>**Constraints**: `>= 1`, `<= 1000` |
| `offset` | `int` | Query, Optional | Number of results to skip before returning.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0` |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackSavedSearchesResponse`](../../doc/models/v1-organizations-services-clickstack-saved-searches-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

limit = 1000

offset = 0

result = click_stack_api.click_stack_list_saved_searches(
    organization_id,
    service_id,
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackSavedSearches400ErrorException`](../../doc/models/v1-organizations-services-clickstack-saved-searches-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackSavedSearches500ErrorException`](../../doc/models/v1-organizations-services-clickstack-saved-searches-500-error-exception.md) |


# Click Stack Create Saved Search

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Creates a new saved search.

```python
def click_stack_create_saved_search(self,
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
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `body` | [`ClickStackSavedSearchInput`](../../doc/models/click-stack-saved-search-input.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackSavedSearchesResponse1`](../../doc/models/v1-organizations-services-clickstack-saved-searches-response-1.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

body = ClickStackSavedSearchInput(
    name='Production Errors',
    source_id='507f1f77bcf86cd799439012',
    select='Timestamp, ServiceName, Body',
    where='SeverityText:ERROR',
    where_language=WhereLanguage12.LUCENE,
    order_by='Timestamp DESC',
    tags=[
        'production',
        'errors'
    ]
)

result = click_stack_api.click_stack_create_saved_search(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackSavedSearches400ErrorException`](../../doc/models/v1-organizations-services-clickstack-saved-searches-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackSavedSearches500ErrorException`](../../doc/models/v1-organizations-services-clickstack-saved-searches-500-error-exception.md) |


# Click Stack Get Saved Search

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Retrieves a specific saved search by ID.

```python
def click_stack_get_saved_search(self,
                                organization_id,
                                service_id,
                                click_stack_saved_search_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `click_stack_saved_search_id` | `str` | Template, Required | Saved search ID |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse`](../../doc/models/v1-organizations-services-clickstack-saved-searches-click-stack-saved-search-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_stack_saved_search_id = 'clickStackSavedSearchId8'

result = click_stack_api.click_stack_get_saved_search(
    organization_id,
    service_id,
    click_stack_saved_search_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400ErrorException`](../../doc/models/v1-organizations-services-clickstack-saved-searches-click-stack-saved-search-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500ErrorException`](../../doc/models/v1-organizations-services-clickstack-saved-searches-click-stack-saved-search-id-500-error-exception.md) |


# Click Stack Update Saved Search

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Updates an existing saved search. This is a full replace: send the full object. Every optional field (`select`, `where`, `whereLanguage`, `orderBy`, `tags`, `filters`) is always written and falls back to its default when omitted, so omitting a field resets it rather than preserving the stored value.

```python
def click_stack_update_saved_search(self,
                                   organization_id,
                                   service_id,
                                   click_stack_saved_search_id,
                                   body=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `click_stack_saved_search_id` | `str` | Template, Required | Saved search ID |
| `body` | [`ClickStackSavedSearchInput`](../../doc/models/click-stack-saved-search-input.md) | Body, Optional | - |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse`](../../doc/models/v1-organizations-services-clickstack-saved-searches-click-stack-saved-search-id-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_stack_saved_search_id = 'clickStackSavedSearchId8'

body = ClickStackSavedSearchInput(
    name='Production Errors',
    source_id='507f1f77bcf86cd799439012',
    select='Timestamp, ServiceName, Body',
    where='SeverityText:ERROR',
    where_language=WhereLanguage12.LUCENE,
    order_by='Timestamp DESC',
    tags=[
        'production',
        'errors'
    ]
)

result = click_stack_api.click_stack_update_saved_search(
    organization_id,
    service_id,
    click_stack_saved_search_id,
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400ErrorException`](../../doc/models/v1-organizations-services-clickstack-saved-searches-click-stack-saved-search-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500ErrorException`](../../doc/models/v1-organizations-services-clickstack-saved-searches-click-stack-saved-search-id-500-error-exception.md) |


# Click Stack Delete Saved Search

**This endpoint is in beta.** API contract is stable, and no breaking changes are expected in the future. <br /><br /> ClickStack: Deletes a saved search and any alerts attached to it.

```python
def click_stack_delete_saved_search(self,
                                   organization_id,
                                   service_id,
                                   click_stack_saved_search_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the ClickStack service. |
| `click_stack_saved_search_id` | `str` | Template, Required | Saved search ID |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2`](../../doc/models/v1-organizations-services-clickstack-saved-searches-click-stack-saved-search-id-response-2.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

click_stack_saved_search_id = 'clickStackSavedSearchId8'

result = click_stack_api.click_stack_delete_saved_search(
    organization_id,
    service_id,
    click_stack_saved_search_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400ErrorException`](../../doc/models/v1-organizations-services-clickstack-saved-searches-click-stack-saved-search-id-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500ErrorException`](../../doc/models/v1-organizations-services-clickstack-saved-searches-click-stack-saved-search-id-500-error-exception.md) |

