# Prometheus

```python
prometheus_api = client.prometheus
```

## Class Name

`PrometheusApi`

## Methods

* [Organization Prometheus Get](../../doc/controllers/prometheus.md#organization-prometheus-get)
* [Organization Prometheus Discovery Get](../../doc/controllers/prometheus.md#organization-prometheus-discovery-get)
* [Instance Prometheus Get](../../doc/controllers/prometheus.md#instance-prometheus-get)
* [Postgres Org Prometheus Get](../../doc/controllers/prometheus.md#postgres-org-prometheus-get)
* [Postgres Instance Prometheus Get](../../doc/controllers/prometheus.md#postgres-instance-prometheus-get)


# Organization Prometheus Get

**This endpoint is deprecated.**

Deprecated. Use the Prometheus service discovery endpoint (/v1/organizations/{organizationId}/prometheus/discovery) instead. This endpoint is not available for new organizations; contact ClickHouse support to request access. Returns Prometheus metrics for the services in an organization that the caller is authorized to view. Services the caller lacks view access to are omitted.

```python
def organization_prometheus_get(self,
                               organization_id,
                               filtered_metrics=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `filtered_metrics` | `str` | Query, Optional | Return a filtered list of Prometheus metrics. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `str`.

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

result = prometheus_api.organization_prometheus_get(organization_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPrometheus400ErrorException`](../../doc/models/v1-organizations-prometheus-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPrometheus500ErrorException`](../../doc/models/v1-organizations-prometheus-500-error-exception.md) |


# Organization Prometheus Discovery Get

Returns one Prometheus scrape target per service in the organization, in the [HTTP service discovery](https://prometheus.io/docs/prometheus/latest/http_sd/) (`http_sd`) format. Only services the API key is authorized to view are included; services that are being deleted or have been deleted are omitted.

Point an [`http_sd_configs`](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#http_sd_config) job at this endpoint to discover and scrape all services in the organization automatically. Prometheus refreshes the target list on every discovery poll, so newly created and deleted services are picked up without configuration changes.

Discovered targets scrape with `filtered_metrics=true` by default; pass `?filtered_metrics=false` to this endpoint to discover unfiltered targets. See the [Prometheus integration guide](https://clickhouse.com/docs/integrations/prometheus) for more on the exported metrics.

```python
def organization_prometheus_discovery_get(self,
                                         organization_id,
                                         filtered_metrics=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `filtered_metrics` | `str` | Query, Optional | Whether discovered targets scrape a filtered list of metrics. Sets the filtered_metrics parameter on each discovered target. Defaults to true. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[PrometheusDiscoveryTargetGroup]`](../../doc/models/prometheus-discovery-target-group.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

filtered_metrics = 'true'

result = prometheus_api.organization_prometheus_discovery_get(
    organization_id,
    filtered_metrics=filtered_metrics
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPrometheusDiscovery400ErrorException`](../../doc/models/v1-organizations-prometheus-discovery-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPrometheusDiscovery500ErrorException`](../../doc/models/v1-organizations-prometheus-discovery-500-error-exception.md) |


# Instance Prometheus Get

Returns prometheus metrics for a service.

```python
def instance_prometheus_get(self,
                           organization_id,
                           service_id,
                           filtered_metrics=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the organization that owns the service. |
| `service_id` | `uuid\|str` | Template, Required | ID of the requested service. |
| `filtered_metrics` | `str` | Query, Optional | Return a filtered list of Prometheus metrics. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `str`.

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

service_id = '00000060-0000-0000-0000-000000000000'

result = prometheus_api.instance_prometheus_get(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsServicesPrometheus400ErrorException`](../../doc/models/v1-organizations-services-prometheus-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsServicesPrometheus500ErrorException`](../../doc/models/v1-organizations-services-prometheus-500-error-exception.md) |


# Postgres Org Prometheus Get

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns Prometheus metrics for all PostgreSQL services in an organization. Maximum 100 services supported.

```python
def postgres_org_prometheus_get(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `str`.

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

result = prometheus_api.postgres_org_prometheus_get(organization_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPostgresPrometheus400ErrorException`](../../doc/models/v1-organizations-postgres-prometheus-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPostgresPrometheus500ErrorException`](../../doc/models/v1-organizations-postgres-prometheus-500-error-exception.md) |


# Postgres Instance Prometheus Get

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns Prometheus metrics for a PostgreSQL service.

```python
def postgres_instance_prometheus_get(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `str`.

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

postgres_id = '00000dcc-0000-0000-0000-000000000000'

result = prometheus_api.postgres_instance_prometheus_get(
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
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsPostgresPrometheus400ErrorException`](../../doc/models/v1-organizations-postgres-prometheus-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsPostgresPrometheus500ErrorException`](../../doc/models/v1-organizations-postgres-prometheus-500-error-exception.md) |

