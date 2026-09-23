<!-- Generated file — do not edit; regenerated with the SDK. -->

# Postgres — operations

Accessor: `client.postgres` · Source: `open_api_spec_for_click_house_cloud/apis/postgres.py` · 17 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.postgres.postgres_instance_config_get

- **Route**: `GET /v1/organizations/{organizationId}/postgres/{postgresId}/config`
- **Auth**: `basic_auth`
- **Signature**: `def postgres_instance_config_get(organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `postgres_id`
- **Params**: `organization_id` — path `organizationId` · `postgres_id` — path `postgresId`
- **Returns (parsed)**: `V1OrganizationsPostgresConfigResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsPostgresConfigResponse, PostgresInstanceConfigGetErrorBody]`
- **Error**: `PostgresInstanceConfigGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPostgresConfig400Error1` [400] · `V1OrganizationsPostgresConfig500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsPostgresConfigResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config_response.py` |
| `PostgresInstanceConfigGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/postgres_instance_config_get_error.py` |
| `V1OrganizationsPostgresConfig400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config400_error1.py` |
| `V1OrganizationsPostgresConfig500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config500_error1.py` |

### client.postgres.postgres_instance_config_patch

- **Route**: `PATCH /v1/organizations/{organizationId}/postgres/{postgresId}/config`
- **Auth**: `basic_auth`
- **Signature**: `def postgres_instance_config_patch(organization_id: UUID, postgres_id: UUID, *, body: PostgresInstanceConfig | PostgresInstanceConfigDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `postgres_id`
- **Params**: `organization_id` — path `organizationId` · `postgres_id` — path `postgresId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsPostgresConfigResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsPostgresConfigResponse1, PostgresInstanceConfigPatchErrorBody]`
- **Error**: `PostgresInstanceConfigPatchErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPostgresConfig400Error1` [400] · `V1OrganizationsPostgresConfig500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PostgresInstanceConfig` | `open_api_spec_for_click_house_cloud/models/postgres_instance_config.py` |
| `PostgresInstanceConfigDict` | `open_api_spec_for_click_house_cloud/models/postgres_instance_config.py` |
| `V1OrganizationsPostgresConfigResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config_response1.py` |
| `PostgresInstanceConfigPatchErrorBody` | `open_api_spec_for_click_house_cloud/errors/postgres_instance_config_patch_error.py` |
| `V1OrganizationsPostgresConfig400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config400_error1.py` |
| `V1OrganizationsPostgresConfig500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config500_error1.py` |

### client.postgres.postgres_instance_config_post

- **Route**: `POST /v1/organizations/{organizationId}/postgres/{postgresId}/config`
- **Auth**: `basic_auth`
- **Signature**: `def postgres_instance_config_post(organization_id: UUID, postgres_id: UUID, *, body: PostgresInstanceConfig | PostgresInstanceConfigDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `postgres_id`
- **Params**: `organization_id` — path `organizationId` · `postgres_id` — path `postgresId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsPostgresConfigResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsPostgresConfigResponse1, PostgresInstanceConfigPostErrorBody]`
- **Error**: `PostgresInstanceConfigPostErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPostgresConfig400Error1` [400] · `V1OrganizationsPostgresConfig500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PostgresInstanceConfig` | `open_api_spec_for_click_house_cloud/models/postgres_instance_config.py` |
| `PostgresInstanceConfigDict` | `open_api_spec_for_click_house_cloud/models/postgres_instance_config.py` |
| `V1OrganizationsPostgresConfigResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config_response1.py` |
| `PostgresInstanceConfigPostErrorBody` | `open_api_spec_for_click_house_cloud/errors/postgres_instance_config_post_error.py` |
| `V1OrganizationsPostgresConfig400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config400_error1.py` |
| `V1OrganizationsPostgresConfig500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_config500_error1.py` |

### client.postgres.postgres_instance_create_read_replica

- **Route**: `POST /v1/organizations/{organizationId}/postgres/{postgresId}/readReplica`
- **Auth**: `basic_auth`
- **Signature**: `def postgres_instance_create_read_replica(organization_id: UUID, postgres_id: UUID, *, body: PostgresServiceReadReplicaRequest | PostgresServiceReadReplicaRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `postgres_id`
- **Params**: `organization_id` — path `organizationId` · `postgres_id` — path `postgresId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsPostgresReadReplicaResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsPostgresReadReplicaResponse, PostgresInstanceCreateReadReplicaErrorBody]`
- **Error**: `PostgresInstanceCreateReadReplicaErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPostgresReadReplica400Error1` [400] · `V1OrganizationsPostgresReadReplica500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PostgresServiceReadReplicaRequest` | `open_api_spec_for_click_house_cloud/models/postgres_service_read_replica_request.py` |
| `PostgresServiceReadReplicaRequestDict` | `open_api_spec_for_click_house_cloud/models/postgres_service_read_replica_request.py` |
| `V1OrganizationsPostgresReadReplicaResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_read_replica_response.py` |
| `PostgresInstanceCreateReadReplicaErrorBody` | `open_api_spec_for_click_house_cloud/errors/postgres_instance_create_read_replica_error.py` |
| `V1OrganizationsPostgresReadReplica400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_read_replica400_error1.py` |
| `V1OrganizationsPostgresReadReplica500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_read_replica500_error1.py` |

### client.postgres.postgres_instance_metrics_get

- **Route**: `GET /v1/organizations/{organizationId}/postgres/{postgresId}/metrics`
- **Auth**: `basic_auth`
- **Signature**: `def postgres_instance_metrics_get(organization_id: UUID, postgres_id: UUID, from_date: RFC3339DateTime, to_date: RFC3339DateTime, *, bucket_size_seconds: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `postgres_id`, `from_date`, `to_date`
- **Params**: `organization_id` — path `organizationId` · `postgres_id` — path `postgresId` · `from_date` — query · `to_date` — query · `bucket_size_seconds` — query
- **Returns (parsed)**: `V1OrganizationsPostgresMetricsResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsPostgresMetricsResponse, PostgresInstanceMetricsGetErrorBody]`
- **Error**: `PostgresInstanceMetricsGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPostgresMetrics400Error1` [400] · `V1OrganizationsPostgresMetrics500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsPostgresMetricsResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_metrics_response.py` |
| `PostgresInstanceMetricsGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/postgres_instance_metrics_get_error.py` |
| `V1OrganizationsPostgresMetrics400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_metrics400_error1.py` |
| `V1OrganizationsPostgresMetrics500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_metrics500_error1.py` |

### client.postgres.postgres_instance_restore

- **Route**: `POST /v1/organizations/{organizationId}/postgres/{postgresId}/restoredService`
- **Auth**: `basic_auth`
- **Signature**: `def postgres_instance_restore(organization_id: UUID, postgres_id: UUID, *, body: PostgresServiceRestoreRequest | PostgresServiceRestoreRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `postgres_id`
- **Params**: `organization_id` — path `organizationId` · `postgres_id` — path `postgresId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsPostgresRestoredServiceResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsPostgresRestoredServiceResponse, PostgresInstanceRestoreErrorBody]`
- **Error**: `PostgresInstanceRestoreErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPostgresRestoredService400Error1` [400] · `V1OrganizationsPostgresRestoredService500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PostgresServiceRestoreRequest` | `open_api_spec_for_click_house_cloud/models/postgres_service_restore_request.py` |
| `PostgresServiceRestoreRequestDict` | `open_api_spec_for_click_house_cloud/models/postgres_service_restore_request.py` |
| `V1OrganizationsPostgresRestoredServiceResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_restored_service_response.py` |
| `PostgresInstanceRestoreErrorBody` | `open_api_spec_for_click_house_cloud/errors/postgres_instance_restore_error.py` |
| `V1OrganizationsPostgresRestoredService400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_restored_service400_error1.py` |
| `V1OrganizationsPostgresRestoredService500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_restored_service500_error1.py` |

### client.postgres.postgres_logs_get_list

- **Route**: `GET /v1/organizations/{organizationId}/postgres/{postgresId}/logs`
- **Auth**: `basic_auth`
- **Signature**: `def postgres_logs_get_list(organization_id: UUID, postgres_id: UUID, from_date: RFC3339DateTime, to_date: RFC3339DateTime, *, body_contains: str | None = None, severity: str | None = None, sort_order: SortOrder1OrStr | None = SortOrder1.DESC, limit: int | None = 50, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `postgres_id`, `from_date`, `to_date`
- **Params**: `organization_id` — path `organizationId` · `postgres_id` — path `postgresId` · `from_date` — query · `to_date` — query · `body_contains` — query · `severity` — query · `sort_order` — query · `limit` — query · `offset` — query
- **Returns (parsed)**: `V1OrganizationsPostgresLogsResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsPostgresLogsResponse, PostgresLogsGetListErrorBody]`
- **Error**: `PostgresLogsGetListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPostgresLogs400Error1` [400] · `V1OrganizationsPostgresLogs500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SortOrder1OrStr` | `open_api_spec_for_click_house_cloud/models/enums/sort_order1.py` |
| `V1OrganizationsPostgresLogsResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_logs_response.py` |
| `PostgresLogsGetListErrorBody` | `open_api_spec_for_click_house_cloud/errors/postgres_logs_get_list_error.py` |
| `V1OrganizationsPostgresLogs400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_logs400_error1.py` |
| `V1OrganizationsPostgresLogs500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_logs500_error1.py` |

### client.postgres.postgres_service_certs_get

- **Route**: `GET /v1/organizations/{organizationId}/postgres/{postgresId}/caCertificates`
- **Auth**: `basic_auth`
- **Signature**: `def postgres_service_certs_get(organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `postgres_id`
- **Params**: `organization_id` — path `organizationId` · `postgres_id` — path `postgresId`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, PostgresServiceCertsGetErrorBody]`
- **Error**: `PostgresServiceCertsGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPostgresCaCertificates400Error1` [400] · `V1OrganizationsPostgresCaCertificates500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PostgresServiceCertsGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/postgres_service_certs_get_error.py` |
| `V1OrganizationsPostgresCaCertificates400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_ca_certificates400_error1.py` |
| `V1OrganizationsPostgresCaCertificates500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_ca_certificates500_error1.py` |

### client.postgres.postgres_service_create

- **Route**: `POST /v1/organizations/{organizationId}/postgres`
- **Auth**: `basic_auth`
- **Signature**: `def postgres_service_create(organization_id: UUID, *, body: PostgresServicePostRequest | PostgresServicePostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsPostgresResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsPostgresResponse, PostgresServiceCreateErrorBody]`
- **Error**: `PostgresServiceCreateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPostgres400Error1` [400] · `V1OrganizationsPostgres500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PostgresServicePostRequest` | `open_api_spec_for_click_house_cloud/models/postgres_service_post_request.py` |
| `PostgresServicePostRequestDict` | `open_api_spec_for_click_house_cloud/models/postgres_service_post_request.py` |
| `V1OrganizationsPostgresResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response.py` |
| `PostgresServiceCreateErrorBody` | `open_api_spec_for_click_house_cloud/errors/postgres_service_create_error.py` |
| `V1OrganizationsPostgres400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres400_error1.py` |
| `V1OrganizationsPostgres500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres500_error1.py` |

### client.postgres.postgres_service_delete

- **Route**: `DELETE /v1/organizations/{organizationId}/postgres/{postgresId}`
- **Auth**: `basic_auth`
- **Signature**: `def postgres_service_delete(organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `postgres_id`
- **Params**: `organization_id` — path `organizationId` · `postgres_id` — path `postgresId`
- **Returns (parsed)**: `V1OrganizationsPostgresResponse3`
- **Returns (raw)**: `ApiResult[V1OrganizationsPostgresResponse3, PostgresServiceDeleteErrorBody]`
- **Error**: `PostgresServiceDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPostgres400Error1` [400] · `V1OrganizationsPostgres500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsPostgresResponse3` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response3.py` |
| `PostgresServiceDeleteErrorBody` | `open_api_spec_for_click_house_cloud/errors/postgres_service_delete_error.py` |
| `V1OrganizationsPostgres400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres400_error1.py` |
| `V1OrganizationsPostgres500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres500_error1.py` |

### client.postgres.postgres_service_get

- **Route**: `GET /v1/organizations/{organizationId}/postgres/{postgresId}`
- **Auth**: `basic_auth`
- **Signature**: `def postgres_service_get(organization_id: UUID, postgres_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `postgres_id`
- **Params**: `organization_id` — path `organizationId` · `postgres_id` — path `postgresId`
- **Returns (parsed)**: `V1OrganizationsPostgresResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsPostgresResponse, PostgresServiceGetErrorBody]`
- **Error**: `PostgresServiceGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPostgres400Error1` [400] · `V1OrganizationsPostgres500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsPostgresResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response.py` |
| `PostgresServiceGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/postgres_service_get_error.py` |
| `V1OrganizationsPostgres400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres400_error1.py` |
| `V1OrganizationsPostgres500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres500_error1.py` |

### client.postgres.postgres_service_get_list

- **Route**: `GET /v1/organizations/{organizationId}/postgres`
- **Auth**: `basic_auth`
- **Signature**: `def postgres_service_get_list(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId`
- **Returns (parsed)**: `V1OrganizationsPostgresResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsPostgresResponse1, PostgresServiceGetListErrorBody]`
- **Error**: `PostgresServiceGetListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPostgres400Error1` [400] · `V1OrganizationsPostgres500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsPostgresResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response1.py` |
| `PostgresServiceGetListErrorBody` | `open_api_spec_for_click_house_cloud/errors/postgres_service_get_list_error.py` |
| `V1OrganizationsPostgres400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres400_error1.py` |
| `V1OrganizationsPostgres500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres500_error1.py` |

### client.postgres.postgres_service_patch

- **Route**: `PATCH /v1/organizations/{organizationId}/postgres/{postgresId}`
- **Auth**: `basic_auth`
- **Signature**: `def postgres_service_patch(organization_id: UUID, postgres_id: UUID, *, body: PostgresServicePatchRequest | PostgresServicePatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `postgres_id`
- **Params**: `organization_id` — path `organizationId` · `postgres_id` — path `postgresId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsPostgresResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsPostgresResponse, PostgresServicePatchErrorBody]`
- **Error**: `PostgresServicePatchErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPostgres400Error1` [400] · `V1OrganizationsPostgres500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PostgresServicePatchRequest` | `open_api_spec_for_click_house_cloud/models/postgres_service_patch_request.py` |
| `PostgresServicePatchRequestDict` | `open_api_spec_for_click_house_cloud/models/postgres_service_patch_request.py` |
| `V1OrganizationsPostgresResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_response.py` |
| `PostgresServicePatchErrorBody` | `open_api_spec_for_click_house_cloud/errors/postgres_service_patch_error.py` |
| `V1OrganizationsPostgres400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres400_error1.py` |
| `V1OrganizationsPostgres500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres500_error1.py` |

### client.postgres.postgres_service_patch_state

- **Route**: `PATCH /v1/organizations/{organizationId}/postgres/{postgresId}/state`
- **Auth**: `basic_auth`
- **Signature**: `def postgres_service_patch_state(organization_id: UUID, postgres_id: UUID, *, body: PostgresServiceSetState | PostgresServiceSetStateDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `postgres_id`
- **Params**: `organization_id` — path `organizationId` · `postgres_id` — path `postgresId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsPostgresStateResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsPostgresStateResponse, PostgresServicePatchStateErrorBody]`
- **Error**: `PostgresServicePatchStateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPostgresState400Error1` [400] · `V1OrganizationsPostgresState500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PostgresServiceSetState` | `open_api_spec_for_click_house_cloud/models/postgres_service_set_state.py` |
| `PostgresServiceSetStateDict` | `open_api_spec_for_click_house_cloud/models/postgres_service_set_state.py` |
| `V1OrganizationsPostgresStateResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_state_response.py` |
| `PostgresServicePatchStateErrorBody` | `open_api_spec_for_click_house_cloud/errors/postgres_service_patch_state_error.py` |
| `V1OrganizationsPostgresState400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_state400_error1.py` |
| `V1OrganizationsPostgresState500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_state500_error1.py` |

### client.postgres.postgres_service_set_password

- **Route**: `PATCH /v1/organizations/{organizationId}/postgres/{postgresId}/password`
- **Auth**: `basic_auth`
- **Signature**: `def postgres_service_set_password(organization_id: UUID, postgres_id: UUID, *, body: PostgresServiceSetPassword | PostgresServiceSetPasswordDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `postgres_id`
- **Params**: `organization_id` — path `organizationId` · `postgres_id` — path `postgresId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsPostgresPasswordResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsPostgresPasswordResponse, PostgresServiceSetPasswordErrorBody]`
- **Error**: `PostgresServiceSetPasswordErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPostgresPassword400Error1` [400] · `V1OrganizationsPostgresPassword500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PostgresServiceSetPassword` | `open_api_spec_for_click_house_cloud/models/postgres_service_set_password.py` |
| `PostgresServiceSetPasswordDict` | `open_api_spec_for_click_house_cloud/models/postgres_service_set_password.py` |
| `V1OrganizationsPostgresPasswordResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_password_response.py` |
| `PostgresServiceSetPasswordErrorBody` | `open_api_spec_for_click_house_cloud/errors/postgres_service_set_password_error.py` |
| `V1OrganizationsPostgresPassword400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_password400_error1.py` |
| `V1OrganizationsPostgresPassword500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_password500_error1.py` |

### client.postgres.slow_query_pattern_get

- **Route**: `GET /v1/organizations/{organizationId}/postgres/{postgresId}/slowQueryPatterns/{queryId}`
- **Auth**: `basic_auth`
- **Signature**: `def slow_query_pattern_get(organization_id: UUID, postgres_id: UUID, query_id: str, db_name: str, db_user: str, db_operation: str, *, app: str | None = None, timestamp: RFC3339DateTime | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `postgres_id`, `query_id`, `db_name`, `db_user`, `db_operation`
- **Params**: `organization_id` — path `organizationId` · `postgres_id` — path `postgresId` · `query_id` — path `queryId` · `db_name` — query · `db_user` — query · `db_operation` — query · `app` — query · `timestamp` — query
- **Returns (parsed)**: `V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse, SlowQueryPatternGetErrorBody]`
- **Error**: `SlowQueryPatternGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPostgresSlowQueryPatternsQueryId400Error1` [400] · `V1OrganizationsPostgresSlowQueryPatternsQueryId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_slow_query_patterns_query_id_response.py` |
| `SlowQueryPatternGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/slow_query_pattern_get_error.py` |
| `V1OrganizationsPostgresSlowQueryPatternsQueryId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_slow_query_patterns_query_id400_error1.py` |
| `V1OrganizationsPostgresSlowQueryPatternsQueryId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_slow_query_patterns_query_id500_error1.py` |

### client.postgres.slow_query_patterns_get_list

- **Route**: `GET /v1/organizations/{organizationId}/postgres/{postgresId}/slowQueryPatterns`
- **Auth**: `basic_auth`
- **Signature**: `def slow_query_patterns_get_list(organization_id: UUID, postgres_id: UUID, from_date: RFC3339DateTime, to_date: RFC3339DateTime, *, db_name: str | None = None, db_user: str | None = None, db_operation: str | None = None, app: str | None = None, sort_by: SortByOrStr | None = SortBy.TOTAL_DURATION, sort_order: SortOrder1OrStr | None = SortOrder1.DESC, limit: int | None = 20, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `postgres_id`, `from_date`, `to_date`
- **Params**: `organization_id` — path `organizationId` · `postgres_id` — path `postgresId` · `from_date` — query · `to_date` — query · `db_name` — query · `db_user` — query · `db_operation` — query · `app` — query · `sort_by` — query · `sort_order` — query · `limit` — query · `offset` — query
- **Returns (parsed)**: `V1OrganizationsPostgresSlowQueryPatternsResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsPostgresSlowQueryPatternsResponse, SlowQueryPatternsGetListErrorBody]`
- **Error**: `SlowQueryPatternsGetListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPostgresSlowQueryPatterns400Error1` [400] · `V1OrganizationsPostgresSlowQueryPatterns500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SortByOrStr` | `open_api_spec_for_click_house_cloud/models/enums/sort_by.py` |
| `SortOrder1OrStr` | `open_api_spec_for_click_house_cloud/models/enums/sort_order1.py` |
| `V1OrganizationsPostgresSlowQueryPatternsResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_slow_query_patterns_response.py` |
| `SlowQueryPatternsGetListErrorBody` | `open_api_spec_for_click_house_cloud/errors/slow_query_patterns_get_list_error.py` |
| `V1OrganizationsPostgresSlowQueryPatterns400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_slow_query_patterns400_error1.py` |
| `V1OrganizationsPostgresSlowQueryPatterns500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_postgres_slow_query_patterns500_error1.py` |

