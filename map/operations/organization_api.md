<!-- Generated file — do not edit; regenerated with the SDK. -->

# OrganizationApi — operations

Accessor: `client.organization_api` · Source: `open_api_spec_for_click_house_cloud/apis/organization_api.py` · 11 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.organization_api.activity_get

- **Route**: `GET /v1/organizations/{organizationId}/activities/{activityId}`
- **Auth**: `basic_auth`
- **Signature**: `def activity_get(organization_id: UUID, activity_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `activity_id`
- **Params**: `organization_id` — path `organizationId` · `activity_id` — path `activityId`
- **Returns (parsed)**: `V1OrganizationsActivitiesResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsActivitiesResponse1, ActivityGetErrorBody]`
- **Error**: `ActivityGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsActivities400Error1` [400] · `V1OrganizationsActivities500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsActivitiesResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_activities_response1.py` |
| `ActivityGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/activity_get_error.py` |
| `V1OrganizationsActivities400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_activities400_error1.py` |
| `V1OrganizationsActivities500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_activities500_error1.py` |

### client.organization_api.activity_get_list

- **Route**: `GET /v1/organizations/{organizationId}/activities`
- **Auth**: `basic_auth`
- **Signature**: `def activity_get_list(organization_id: UUID, *, from_date: RFC3339DateTime | None = None, to_date: RFC3339DateTime | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId` · `from_date` — query · `to_date` — query
- **Returns (parsed)**: `V1OrganizationsActivitiesResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsActivitiesResponse, ActivityGetListErrorBody]`
- **Error**: `ActivityGetListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsActivities400Error1` [400] · `V1OrganizationsActivities500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsActivitiesResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_activities_response.py` |
| `ActivityGetListErrorBody` | `open_api_spec_for_click_house_cloud/errors/activity_get_list_error.py` |
| `V1OrganizationsActivities400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_activities400_error1.py` |
| `V1OrganizationsActivities500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_activities500_error1.py` |

### client.organization_api.organization_byoc_infrastructure_create

- **Route**: `POST /v1/organizations/{organizationId}/byocInfrastructure`
- **Auth**: `basic_auth`
- **Signature**: `def organization_byoc_infrastructure_create(organization_id: UUID, *, body: ByocInfrastructurePostRequest | ByocInfrastructurePostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsByocInfrastructureResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsByocInfrastructureResponse, OrganizationByocInfrastructureCreateErrorBody]`
- **Error**: `OrganizationByocInfrastructureCreateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsByocInfrastructure400Error1` [400] · `V1OrganizationsByocInfrastructure500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ByocInfrastructurePostRequest` | `open_api_spec_for_click_house_cloud/models/byoc_infrastructure_post_request.py` |
| `ByocInfrastructurePostRequestDict` | `open_api_spec_for_click_house_cloud/models/byoc_infrastructure_post_request.py` |
| `V1OrganizationsByocInfrastructureResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure_response.py` |
| `OrganizationByocInfrastructureCreateErrorBody` | `open_api_spec_for_click_house_cloud/errors/organization_byoc_infrastructure_create_error.py` |
| `V1OrganizationsByocInfrastructure400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure400_error1.py` |
| `V1OrganizationsByocInfrastructure500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure500_error1.py` |

### client.organization_api.organization_byoc_infrastructure_delete

- **Route**: `DELETE /v1/organizations/{organizationId}/byocInfrastructure/{byocInfrastructureId}`
- **Auth**: `basic_auth`
- **Signature**: `def organization_byoc_infrastructure_delete(organization_id: UUID, byoc_infrastructure_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `byoc_infrastructure_id`
- **Params**: `organization_id` — path `organizationId` · `byoc_infrastructure_id` — path `byocInfrastructureId`
- **Returns (parsed)**: `V1OrganizationsByocInfrastructureResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsByocInfrastructureResponse1, OrganizationByocInfrastructureDeleteErrorBody]`
- **Error**: `OrganizationByocInfrastructureDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsByocInfrastructure400Error1` [400] · `V1OrganizationsByocInfrastructure500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsByocInfrastructureResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure_response1.py` |
| `OrganizationByocInfrastructureDeleteErrorBody` | `open_api_spec_for_click_house_cloud/errors/organization_byoc_infrastructure_delete_error.py` |
| `V1OrganizationsByocInfrastructure400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure400_error1.py` |
| `V1OrganizationsByocInfrastructure500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure500_error1.py` |

### client.organization_api.organization_byoc_infrastructure_update

- **Route**: `PATCH /v1/organizations/{organizationId}/byocInfrastructure/{byocInfrastructureId}`
- **Auth**: `basic_auth`
- **Signature**: `def organization_byoc_infrastructure_update(organization_id: UUID, byoc_infrastructure_id: UUID, *, body: ByocInfrastructurePatchRequest | ByocInfrastructurePatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `byoc_infrastructure_id`
- **Params**: `organization_id` — path `organizationId` · `byoc_infrastructure_id` — path `byocInfrastructureId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsByocInfrastructureResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsByocInfrastructureResponse, OrganizationByocInfrastructureUpdateErrorBody]`
- **Error**: `OrganizationByocInfrastructureUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsByocInfrastructure400Error1` [400] · `V1OrganizationsByocInfrastructure500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ByocInfrastructurePatchRequest` | `open_api_spec_for_click_house_cloud/models/byoc_infrastructure_patch_request.py` |
| `ByocInfrastructurePatchRequestDict` | `open_api_spec_for_click_house_cloud/models/byoc_infrastructure_patch_request.py` |
| `V1OrganizationsByocInfrastructureResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure_response.py` |
| `OrganizationByocInfrastructureUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/organization_byoc_infrastructure_update_error.py` |
| `V1OrganizationsByocInfrastructure400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure400_error1.py` |
| `V1OrganizationsByocInfrastructure500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_byoc_infrastructure500_error1.py` |

### client.organization_api.organization_get

- **Route**: `GET /v1/organizations/{organizationId}`
- **Auth**: `basic_auth`
- **Signature**: `def organization_get(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId`
- **Returns (parsed)**: `V1OrganizationsResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsResponse1, OrganizationGetErrorBody]`
- **Error**: `OrganizationGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1Organizations400Error1` [400] · `V1Organizations500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_response1.py` |
| `OrganizationGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/organization_get_error.py` |
| `V1Organizations400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations400_error1.py` |
| `V1Organizations500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations500_error1.py` |

### client.organization_api.organization_get_list

- **Route**: `GET /v1/organizations`
- **Auth**: `basic_auth`
- **Signature**: `def organization_get_list(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `V1OrganizationsResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsResponse, OrganizationGetListErrorBody]`
- **Error**: `OrganizationGetListErrorBody` — **Case A (typed)**
- **Error arms**: `V1Organizations400Error1` [400] · `V1Organizations500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_response.py` |
| `OrganizationGetListErrorBody` | `open_api_spec_for_click_house_cloud/errors/organization_get_list_error.py` |
| `V1Organizations400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations400_error1.py` |
| `V1Organizations500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations500_error1.py` |

### client.organization_api.organization_private_endpoint_config_get_list

- **Route**: `GET /v1/organizations/{organizationId}/privateEndpointConfig`
- **Auth**: `basic_auth`
- **Signature**: `def organization_private_endpoint_config_get_list(organization_id: UUID, cloud_provider: str, region_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `cloud_provider`, `region_id`
- **Params**: `organization_id` — path `organizationId` · `cloud_provider` — query · `region_id` — query
- **Returns (parsed)**: `V1OrganizationsPrivateEndpointConfigResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsPrivateEndpointConfigResponse, OrganizationPrivateEndpointConfigGetListErrorBody]`
- **Error**: `OrganizationPrivateEndpointConfigGetListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsPrivateEndpointConfig400Error1` [400] · `V1OrganizationsPrivateEndpointConfig500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsPrivateEndpointConfigResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_private_endpoint_config_response.py` |
| `OrganizationPrivateEndpointConfigGetListErrorBody` | `open_api_spec_for_click_house_cloud/errors/organization_private_endpoint_config_get_list_error.py` |
| `V1OrganizationsPrivateEndpointConfig400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_private_endpoint_config400_error1.py` |
| `V1OrganizationsPrivateEndpointConfig500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_private_endpoint_config500_error1.py` |

### client.organization_api.organization_quota_get

- **Route**: `GET /v1/organizations/{organizationId}/quotas/{quotaCode}`
- **Auth**: `basic_auth`
- **Signature**: `def organization_quota_get(organization_id: UUID, quota_code: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `quota_code`
- **Params**: `organization_id` — path `organizationId` · `quota_code` — path `quotaCode`
- **Returns (parsed)**: `V1OrganizationsQuotasResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsQuotasResponse1, OrganizationQuotaGetErrorBody]`
- **Error**: `OrganizationQuotaGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsQuotas400Error1` [400] · `V1OrganizationsQuotas500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsQuotasResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_quotas_response1.py` |
| `OrganizationQuotaGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/organization_quota_get_error.py` |
| `V1OrganizationsQuotas400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_quotas400_error1.py` |
| `V1OrganizationsQuotas500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_quotas500_error1.py` |

### client.organization_api.organization_quotas_get_list

- **Route**: `GET /v1/organizations/{organizationId}/quotas`
- **Auth**: `basic_auth`
- **Signature**: `def organization_quotas_get_list(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId`
- **Returns (parsed)**: `V1OrganizationsQuotasResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsQuotasResponse, OrganizationQuotasGetListErrorBody]`
- **Error**: `OrganizationQuotasGetListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsQuotas400Error1` [400] · `V1OrganizationsQuotas500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsQuotasResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_quotas_response.py` |
| `OrganizationQuotasGetListErrorBody` | `open_api_spec_for_click_house_cloud/errors/organization_quotas_get_list_error.py` |
| `V1OrganizationsQuotas400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_quotas400_error1.py` |
| `V1OrganizationsQuotas500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_quotas500_error1.py` |

### client.organization_api.organization_update

- **Route**: `PATCH /v1/organizations/{organizationId}`
- **Auth**: `basic_auth`
- **Signature**: `def organization_update(organization_id: UUID, *, body: OrganizationPatchRequest | OrganizationPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsResponse1, OrganizationUpdateErrorBody]`
- **Error**: `OrganizationUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1Organizations400Error1` [400] · `V1Organizations500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OrganizationPatchRequest` | `open_api_spec_for_click_house_cloud/models/organization_patch_request.py` |
| `OrganizationPatchRequestDict` | `open_api_spec_for_click_house_cloud/models/organization_patch_request.py` |
| `V1OrganizationsResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_response1.py` |
| `OrganizationUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/organization_update_error.py` |
| `V1Organizations400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations400_error1.py` |
| `V1Organizations500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations500_error1.py` |

