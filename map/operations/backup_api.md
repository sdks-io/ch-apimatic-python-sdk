<!-- Generated file — do not edit; regenerated with the SDK. -->

# BackupApi — operations

Accessor: `client.backup_api` · Source: `open_api_spec_for_click_house_cloud/apis/backup_api.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.backup_api.backup_bucket_create

- **Route**: `POST /v1/organizations/{organizationId}/services/{serviceId}/backupBucket`
- **Auth**: `basic_auth`
- **Signature**: `def backup_bucket_create(organization_id: UUID, service_id: UUID, *, body: BackupBucketPostRequest | BackupBucketPostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesBackupBucketResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesBackupBucketResponse, BackupBucketCreateErrorBody]`
- **Error**: `BackupBucketCreateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesBackupBucket400Error1` [400] · `V1OrganizationsServicesBackupBucket500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BackupBucketPostRequest` | `open_api_spec_for_click_house_cloud/models/unions/backup_bucket_post_request.py` |
| `BackupBucketPostRequestDict` | `open_api_spec_for_click_house_cloud/models/unions/backup_bucket_post_request.py` |
| `V1OrganizationsServicesBackupBucketResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket_response.py` |
| `BackupBucketCreateErrorBody` | `open_api_spec_for_click_house_cloud/errors/backup_bucket_create_error.py` |
| `V1OrganizationsServicesBackupBucket400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket400_error1.py` |
| `V1OrganizationsServicesBackupBucket500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket500_error1.py` |

### client.backup_api.backup_bucket_delete

- **Route**: `DELETE /v1/organizations/{organizationId}/services/{serviceId}/backupBucket`
- **Auth**: `basic_auth`
- **Signature**: `def backup_bucket_delete(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesBackupBucketResponse3`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesBackupBucketResponse3, BackupBucketDeleteErrorBody]`
- **Error**: `BackupBucketDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesBackupBucket400Error1` [400] · `V1OrganizationsServicesBackupBucket500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesBackupBucketResponse3` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket_response3.py` |
| `BackupBucketDeleteErrorBody` | `open_api_spec_for_click_house_cloud/errors/backup_bucket_delete_error.py` |
| `V1OrganizationsServicesBackupBucket400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket400_error1.py` |
| `V1OrganizationsServicesBackupBucket500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket500_error1.py` |

### client.backup_api.backup_bucket_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/backupBucket`
- **Auth**: `basic_auth`
- **Signature**: `def backup_bucket_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesBackupBucketResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesBackupBucketResponse, BackupBucketGetErrorBody]`
- **Error**: `BackupBucketGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesBackupBucket400Error1` [400] · `V1OrganizationsServicesBackupBucket500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesBackupBucketResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket_response.py` |
| `BackupBucketGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/backup_bucket_get_error.py` |
| `V1OrganizationsServicesBackupBucket400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket400_error1.py` |
| `V1OrganizationsServicesBackupBucket500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket500_error1.py` |

### client.backup_api.backup_bucket_update

- **Route**: `PATCH /v1/organizations/{organizationId}/services/{serviceId}/backupBucket`
- **Auth**: `basic_auth`
- **Signature**: `def backup_bucket_update(organization_id: UUID, service_id: UUID, *, body: BackupBucketPatchRequest | BackupBucketPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesBackupBucketResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesBackupBucketResponse, BackupBucketUpdateErrorBody]`
- **Error**: `BackupBucketUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesBackupBucket400Error1` [400] · `V1OrganizationsServicesBackupBucket500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BackupBucketPatchRequest` | `open_api_spec_for_click_house_cloud/models/unions/backup_bucket_patch_request.py` |
| `BackupBucketPatchRequestDict` | `open_api_spec_for_click_house_cloud/models/unions/backup_bucket_patch_request.py` |
| `V1OrganizationsServicesBackupBucketResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket_response.py` |
| `BackupBucketUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/backup_bucket_update_error.py` |
| `V1OrganizationsServicesBackupBucket400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket400_error1.py` |
| `V1OrganizationsServicesBackupBucket500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_bucket500_error1.py` |

### client.backup_api.backup_configuration_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/backupConfiguration`
- **Auth**: `basic_auth`
- **Signature**: `def backup_configuration_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesBackupConfigurationResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesBackupConfigurationResponse, BackupConfigurationGetErrorBody]`
- **Error**: `BackupConfigurationGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesBackupConfiguration400Error1` [400] · `V1OrganizationsServicesBackupConfiguration500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesBackupConfigurationResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_configuration_response.py` |
| `BackupConfigurationGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/backup_configuration_get_error.py` |
| `V1OrganizationsServicesBackupConfiguration400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_configuration400_error1.py` |
| `V1OrganizationsServicesBackupConfiguration500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_configuration500_error1.py` |

### client.backup_api.backup_configuration_update

- **Route**: `PATCH /v1/organizations/{organizationId}/services/{serviceId}/backupConfiguration`
- **Auth**: `basic_auth`
- **Signature**: `def backup_configuration_update(organization_id: UUID, service_id: UUID, *, body: BackupConfigurationPatchRequest | BackupConfigurationPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesBackupConfigurationResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesBackupConfigurationResponse, BackupConfigurationUpdateErrorBody]`
- **Error**: `BackupConfigurationUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesBackupConfiguration400Error1` [400] · `V1OrganizationsServicesBackupConfiguration500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BackupConfigurationPatchRequest` | `open_api_spec_for_click_house_cloud/models/backup_configuration_patch_request.py` |
| `BackupConfigurationPatchRequestDict` | `open_api_spec_for_click_house_cloud/models/backup_configuration_patch_request.py` |
| `V1OrganizationsServicesBackupConfigurationResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_configuration_response.py` |
| `BackupConfigurationUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/backup_configuration_update_error.py` |
| `V1OrganizationsServicesBackupConfiguration400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_configuration400_error1.py` |
| `V1OrganizationsServicesBackupConfiguration500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backup_configuration500_error1.py` |

### client.backup_api.backup_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/backups/{backupId}`
- **Auth**: `basic_auth`
- **Signature**: `def backup_get(organization_id: UUID, service_id: UUID, backup_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `backup_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `backup_id` — path `backupId`
- **Returns (parsed)**: `V1OrganizationsServicesBackupsBackupIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesBackupsBackupIdResponse, BackupGetErrorBody]`
- **Error**: `BackupGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesBackupsBackupId400Error1` [400] · `V1OrganizationsServicesBackupsBackupId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesBackupsBackupIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backups_backup_id_response.py` |
| `BackupGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/backup_get_error.py` |
| `V1OrganizationsServicesBackupsBackupId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backups_backup_id400_error1.py` |
| `V1OrganizationsServicesBackupsBackupId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backups_backup_id500_error1.py` |

### client.backup_api.backup_get_list

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/backups`
- **Auth**: `basic_auth`
- **Signature**: `def backup_get_list(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesBackupsResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesBackupsResponse, BackupGetListErrorBody]`
- **Error**: `BackupGetListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesBackups400Error1` [400] · `V1OrganizationsServicesBackups500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesBackupsResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backups_response.py` |
| `BackupGetListErrorBody` | `open_api_spec_for_click_house_cloud/errors/backup_get_list_error.py` |
| `V1OrganizationsServicesBackups400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backups400_error1.py` |
| `V1OrganizationsServicesBackups500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_backups500_error1.py` |

