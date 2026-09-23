<!-- Generated file — do not edit; regenerated with the SDK. -->

# SnapshotApi — operations

Accessor: `client.snapshot_api` · Source: `open_api_spec_for_click_house_cloud/apis/snapshot_api.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.snapshot_api.snapshot_configuration_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/snapshotConfiguration`
- **Auth**: `basic_auth`
- **Signature**: `def snapshot_configuration_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesSnapshotConfigurationResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesSnapshotConfigurationResponse, SnapshotConfigurationGetErrorBody]`
- **Error**: `SnapshotConfigurationGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesSnapshotConfiguration400Error1` [400] · `V1OrganizationsServicesSnapshotConfiguration500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesSnapshotConfigurationResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshot_configuration_response.py` |
| `SnapshotConfigurationGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/snapshot_configuration_get_error.py` |
| `V1OrganizationsServicesSnapshotConfiguration400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshot_configuration400_error1.py` |
| `V1OrganizationsServicesSnapshotConfiguration500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshot_configuration500_error1.py` |

### client.snapshot_api.snapshot_configuration_update

- **Route**: `PATCH /v1/organizations/{organizationId}/services/{serviceId}/snapshotConfiguration`
- **Auth**: `basic_auth`
- **Signature**: `def snapshot_configuration_update(organization_id: UUID, service_id: UUID, *, body: SnapshotConfigurationPatchRequest | SnapshotConfigurationPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesSnapshotConfigurationResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesSnapshotConfigurationResponse, SnapshotConfigurationUpdateErrorBody]`
- **Error**: `SnapshotConfigurationUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesSnapshotConfiguration400Error1` [400] · `V1OrganizationsServicesSnapshotConfiguration500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SnapshotConfigurationPatchRequest` | `open_api_spec_for_click_house_cloud/models/snapshot_configuration_patch_request.py` |
| `SnapshotConfigurationPatchRequestDict` | `open_api_spec_for_click_house_cloud/models/snapshot_configuration_patch_request.py` |
| `V1OrganizationsServicesSnapshotConfigurationResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshot_configuration_response.py` |
| `SnapshotConfigurationUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/snapshot_configuration_update_error.py` |
| `V1OrganizationsServicesSnapshotConfiguration400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshot_configuration400_error1.py` |
| `V1OrganizationsServicesSnapshotConfiguration500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshot_configuration500_error1.py` |

### client.snapshot_api.snapshot_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/snapshots/{snapshotId}`
- **Auth**: `basic_auth`
- **Signature**: `def snapshot_get(organization_id: UUID, service_id: UUID, snapshot_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `snapshot_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `snapshot_id` — path `snapshotId`
- **Returns (parsed)**: `V1OrganizationsServicesSnapshotsSnapshotIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesSnapshotsSnapshotIdResponse, SnapshotGetErrorBody]`
- **Error**: `SnapshotGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesSnapshotsSnapshotId400Error1` [400] · `V1OrganizationsServicesSnapshotsSnapshotId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesSnapshotsSnapshotIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshots_snapshot_id_response.py` |
| `SnapshotGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/snapshot_get_error.py` |
| `V1OrganizationsServicesSnapshotsSnapshotId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshots_snapshot_id400_error1.py` |
| `V1OrganizationsServicesSnapshotsSnapshotId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshots_snapshot_id500_error1.py` |

### client.snapshot_api.snapshot_get_list

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/snapshots`
- **Auth**: `basic_auth`
- **Signature**: `def snapshot_get_list(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesSnapshotsResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesSnapshotsResponse, SnapshotGetListErrorBody]`
- **Error**: `SnapshotGetListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesSnapshots400Error1` [400] · `V1OrganizationsServicesSnapshots500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesSnapshotsResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshots_response.py` |
| `SnapshotGetListErrorBody` | `open_api_spec_for_click_house_cloud/errors/snapshot_get_list_error.py` |
| `V1OrganizationsServicesSnapshots400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshots400_error1.py` |
| `V1OrganizationsServicesSnapshots500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_snapshots500_error1.py` |

