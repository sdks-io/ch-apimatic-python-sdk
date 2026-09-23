<!-- Generated file — do not edit; regenerated with the SDK. -->

# Prometheus — operations

Accessor: `client.prometheus` · Source: `open_api_spec_for_click_house_cloud/apis/prometheus.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.prometheus.instance_prometheus_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/prometheus`
- **Auth**: `basic_auth`
- **Signature**: `def instance_prometheus_get(organization_id: UUID, service_id: UUID, *, filtered_metrics: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `filtered_metrics` — query
- **Returns (parsed)**: `str`
- **Returns (raw)**: `ApiResult[str, InstancePrometheusGetErrorBody]`
- **Error**: `InstancePrometheusGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesPrometheus400Error1` [400] · `V1OrganizationsServicesPrometheus500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `InstancePrometheusGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/instance_prometheus_get_error.py` |
| `V1OrganizationsServicesPrometheus400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_prometheus400_error1.py` |
| `V1OrganizationsServicesPrometheus500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_prometheus500_error1.py` |

### client.prometheus.organization_prometheus_discovery_get

- **Route**: `GET /v1/organizations/{organizationId}/prometheus/discovery`
- **Auth**: `basic_auth`
- **Signature**: `def organization_prometheus_discovery_get(organization_id: UUID, *, filtered_metrics: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId` · `filtered_metrics` — query
- **Returns (parsed)**: `list[PrometheusDiscoveryTargetGroup]`
- **Returns (raw)**: `ApiResult[list[PrometheusDiscoveryTargetGroup], OrganizationPrometheusDiscoveryGetErrorBody]`
- **Error**: `OrganizationPrometheusDiscoveryGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPrometheusDiscovery400Error1` [400] · `V1OrganizationsPrometheusDiscovery500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PrometheusDiscoveryTargetGroup` | `open_api_spec_for_click_house_cloud/models/prometheus_discovery_target_group.py` |
| `OrganizationPrometheusDiscoveryGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/organization_prometheus_discovery_get_error.py` |
| `V1OrganizationsPrometheusDiscovery400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_prometheus_discovery400_error1.py` |
| `V1OrganizationsPrometheusDiscovery500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_prometheus_discovery500_error1.py` |

### client.prometheus.organization_prometheus_get

- **Route**: `GET /v1/organizations/{organizationId}/prometheus`
- **Auth**: `basic_auth`
- **Signature**: `def organization_prometheus_get(organization_id: UUID, *, filtered_metrics: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId` · `filtered_metrics` — query
- **Returns (parsed)**: `str`
- **Returns (raw)**: `ApiResult[str, OrganizationPrometheusGetErrorBody]`
- **Error**: `OrganizationPrometheusGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPrometheus400Error1` [400] · `V1OrganizationsPrometheus500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OrganizationPrometheusGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/organization_prometheus_get_error.py` |
| `V1OrganizationsPrometheus400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_prometheus400_error1.py` |
| `V1OrganizationsPrometheus500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_prometheus500_error1.py` |

### client.prometheus.postgres_instance_prometheus_get

- **Route**: `GET /v1/organizations/{organizationId}/postgres/{postgresId}/prometheus`
- **Auth**: `basic_auth`
- **Signature**: `def postgres_instance_prometheus_get(organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `postgres_id`
- **Params**: `organization_id` — path `organizationId` · `postgres_id` — path `postgresId`
- **Returns (parsed)**: `str`
- **Returns (raw)**: `ApiResult[str, PostgresInstancePrometheusGetErrorBody]`
- **Error**: `PostgresInstancePrometheusGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPostgresPrometheus400Error1` [400] · `V1OrganizationsPostgresPrometheus500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PostgresInstancePrometheusGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/postgres_instance_prometheus_get_error.py` |
| `V1OrganizationsPostgresPrometheus400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_prometheus400_error1.py` |
| `V1OrganizationsPostgresPrometheus500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_prometheus500_error1.py` |

### client.prometheus.postgres_org_prometheus_get

- **Route**: `GET /v1/organizations/{organizationId}/postgres/prometheus`
- **Auth**: `basic_auth`
- **Signature**: `def postgres_org_prometheus_get(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId`
- **Returns (parsed)**: `str`
- **Returns (raw)**: `ApiResult[str, PostgresOrgPrometheusGetErrorBody]`
- **Error**: `PostgresOrgPrometheusGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPostgresPrometheus400Error1` [400] · `V1OrganizationsPostgresPrometheus500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PostgresOrgPrometheusGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/postgres_org_prometheus_get_error.py` |
| `V1OrganizationsPostgresPrometheus400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_prometheus400_error1.py` |
| `V1OrganizationsPostgresPrometheus500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_prometheus500_error1.py` |

