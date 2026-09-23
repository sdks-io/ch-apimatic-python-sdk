<!-- Generated file — do not edit; regenerated with the SDK. -->

# ClickPipes — operations

Accessor: `client.click_pipes` · Source: `open_api_spec_for_click_house_cloud/apis/click_pipes.py` · 18 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.click_pipes.click_pipe_cdc_scaling_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickpipesCdcScaling`
- **Auth**: `basic_auth`
- **Signature**: `def click_pipe_cdc_scaling_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesClickpipesCdcScalingResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickpipesCdcScalingResponse, ClickPipeCdcScalingGetErrorBody]`
- **Error**: `ClickPipeCdcScalingGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickpipesCdcScaling400Error1` [400] · `V1OrganizationsServicesClickpipesCdcScaling500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickpipesCdcScalingResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_cdc_scaling_response.py` |
| `ClickPipeCdcScalingGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_pipe_cdc_scaling_get_error.py` |
| `V1OrganizationsServicesClickpipesCdcScaling400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_cdc_scaling400_error1.py` |
| `V1OrganizationsServicesClickpipesCdcScaling500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_cdc_scaling500_error1.py` |

### client.click_pipes.click_pipe_cdc_scaling_update

- **Route**: `PATCH /v1/organizations/{organizationId}/services/{serviceId}/clickpipesCdcScaling`
- **Auth**: `basic_auth`
- **Signature**: `def click_pipe_cdc_scaling_update(organization_id: UUID, service_id: UUID, *, body: ClickPipesCdcScalingPatchRequest | ClickPipesCdcScalingPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickpipesCdcScalingResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickpipesCdcScalingResponse, ClickPipeCdcScalingUpdateErrorBody]`
- **Error**: `ClickPipeCdcScalingUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickpipesCdcScaling400Error1` [400] · `V1OrganizationsServicesClickpipesCdcScaling500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickPipesCdcScalingPatchRequest` | `open_api_spec_for_click_house_cloud/models/click_pipes_cdc_scaling_patch_request.py` |
| `ClickPipesCdcScalingPatchRequestDict` | `open_api_spec_for_click_house_cloud/models/click_pipes_cdc_scaling_patch_request.py` |
| `V1OrganizationsServicesClickpipesCdcScalingResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_cdc_scaling_response.py` |
| `ClickPipeCdcScalingUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_pipe_cdc_scaling_update_error.py` |
| `V1OrganizationsServicesClickpipesCdcScaling400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_cdc_scaling400_error1.py` |
| `V1OrganizationsServicesClickpipesCdcScaling500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_cdc_scaling500_error1.py` |

### client.click_pipes.click_pipe_create

- **Route**: `POST /v1/organizations/{organizationId}/services/{serviceId}/clickpipes`
- **Auth**: `basic_auth`
- **Signature**: `def click_pipe_create(organization_id: UUID, service_id: UUID, *, body: ClickPipePostRequest | ClickPipePostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickpipesResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickpipesResponse1, ClickPipeCreateErrorBody]`
- **Error**: `ClickPipeCreateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickpipes400Error1` [400] · `V1OrganizationsServicesClickpipes500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickPipePostRequest` | `open_api_spec_for_click_house_cloud/models/click_pipe_post_request.py` |
| `ClickPipePostRequestDict` | `open_api_spec_for_click_house_cloud/models/click_pipe_post_request.py` |
| `V1OrganizationsServicesClickpipesResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_response1.py` |
| `ClickPipeCreateErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_pipe_create_error.py` |
| `V1OrganizationsServicesClickpipes400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes400_error1.py` |
| `V1OrganizationsServicesClickpipes500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes500_error1.py` |

### client.click_pipes.click_pipe_delete

- **Route**: `DELETE /v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_pipe_delete(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_pipe_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_pipe_id` — path `clickPipeId`
- **Returns (parsed)**: `V1OrganizationsServicesClickpipesClickPipeIdResponse2`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickpipesClickPipeIdResponse2, ClickPipeDeleteErrorBody]`
- **Error**: `ClickPipeDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickpipesClickPipeId400Error1` [400] · `V1OrganizationsServicesClickpipesClickPipeId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickpipesClickPipeIdResponse2` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_response2.py` |
| `ClickPipeDeleteErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_pipe_delete_error.py` |
| `V1OrganizationsServicesClickpipesClickPipeId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id400_error1.py` |
| `V1OrganizationsServicesClickpipesClickPipeId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id500_error1.py` |

### client.click_pipes.click_pipe_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_pipe_get(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_pipe_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_pipe_id` — path `clickPipeId`
- **Returns (parsed)**: `V1OrganizationsServicesClickpipesClickPipeIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickpipesClickPipeIdResponse, ClickPipeGetErrorBody]`
- **Error**: `ClickPipeGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickpipesClickPipeId400Error1` [400] · `V1OrganizationsServicesClickpipesClickPipeId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickpipesClickPipeIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_response.py` |
| `ClickPipeGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_pipe_get_error.py` |
| `V1OrganizationsServicesClickpipesClickPipeId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id400_error1.py` |
| `V1OrganizationsServicesClickpipesClickPipeId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id500_error1.py` |

### client.click_pipes.click_pipe_get_list

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickpipes`
- **Auth**: `basic_auth`
- **Signature**: `def click_pipe_get_list(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesClickpipesResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickpipesResponse, ClickPipeGetListErrorBody]`
- **Error**: `ClickPipeGetListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickpipes400Error1` [400] · `V1OrganizationsServicesClickpipes500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickpipesResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_response.py` |
| `ClickPipeGetListErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_pipe_get_list_error.py` |
| `V1OrganizationsServicesClickpipes400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes400_error1.py` |
| `V1OrganizationsServicesClickpipes500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes500_error1.py` |

### client.click_pipes.click_pipe_reverse_private_endpoint_create

- **Route**: `POST /v1/organizations/{organizationId}/services/{serviceId}/clickpipesReversePrivateEndpoints`
- **Auth**: `basic_auth`
- **Signature**: `def click_pipe_reverse_private_endpoint_create(organization_id: UUID, service_id: UUID, *, body: CreateReversePrivateEndpoint | CreateReversePrivateEndpointDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1, ClickPipeReversePrivateEndpointCreateErrorBody]`
- **Error**: `ClickPipeReversePrivateEndpointCreateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickpipesReversePrivateEndpoints400Error1` [400] · `V1OrganizationsServicesClickpipesReversePrivateEndpoints500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateReversePrivateEndpoint` | `open_api_spec_for_click_house_cloud/models/create_reverse_private_endpoint.py` |
| `CreateReversePrivateEndpointDict` | `open_api_spec_for_click_house_cloud/models/create_reverse_private_endpoint.py` |
| `V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_response1.py` |
| `ClickPipeReversePrivateEndpointCreateErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_create_error.py` |
| `V1OrganizationsServicesClickpipesReversePrivateEndpoints400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints400_error1.py` |
| `V1OrganizationsServicesClickpipesReversePrivateEndpoints500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints500_error1.py` |

### client.click_pipes.click_pipe_reverse_private_endpoint_delete

- **Route**: `DELETE /v1/organizations/{organizationId}/services/{serviceId}/clickpipesReversePrivateEndpoints/{reversePrivateEndpointId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_pipe_reverse_private_endpoint_delete(organization_id: UUID, service_id: UUID, reverse_private_endpoint_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `reverse_private_endpoint_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `reverse_private_endpoint_id` — path `reversePrivateEndpointId`
- **Returns (parsed)**: `V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1, ClickPipeReversePrivateEndpointDeleteErrorBody]`
- **Error**: `ClickPipeReversePrivateEndpointDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400Error1` [400] · `V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id_response1.py` |
| `ClickPipeReversePrivateEndpointDeleteErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_delete_error.py` |
| `V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id400_error1.py` |
| `V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id500_error1.py` |

### client.click_pipes.click_pipe_reverse_private_endpoint_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickpipesReversePrivateEndpoints/{reversePrivateEndpointId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_pipe_reverse_private_endpoint_get(organization_id: UUID, service_id: UUID, reverse_private_endpoint_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `reverse_private_endpoint_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `reverse_private_endpoint_id` — path `reversePrivateEndpointId`
- **Returns (parsed)**: `V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse, ClickPipeReversePrivateEndpointGetErrorBody]`
- **Error**: `ClickPipeReversePrivateEndpointGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400Error1` [400] · `V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id_response.py` |
| `ClickPipeReversePrivateEndpointGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_get_error.py` |
| `V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id400_error1.py` |
| `V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id500_error1.py` |

### client.click_pipes.click_pipe_reverse_private_endpoint_get_list

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickpipesReversePrivateEndpoints`
- **Auth**: `basic_auth`
- **Signature**: `def click_pipe_reverse_private_endpoint_get_list(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse, ClickPipeReversePrivateEndpointGetListErrorBody]`
- **Error**: `ClickPipeReversePrivateEndpointGetListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickpipesReversePrivateEndpoints400Error1` [400] · `V1OrganizationsServicesClickpipesReversePrivateEndpoints500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickpipesReversePrivateEndpointsResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_response.py` |
| `ClickPipeReversePrivateEndpointGetListErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_get_list_error.py` |
| `V1OrganizationsServicesClickpipesReversePrivateEndpoints400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints400_error1.py` |
| `V1OrganizationsServicesClickpipesReversePrivateEndpoints500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints500_error1.py` |

### client.click_pipes.click_pipe_reverse_private_endpoint_update

- **Route**: `PATCH /v1/organizations/{organizationId}/services/{serviceId}/clickpipesReversePrivateEndpoints/{reversePrivateEndpointId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_pipe_reverse_private_endpoint_update(organization_id: UUID, service_id: UUID, reverse_private_endpoint_id: UUID, *, body: UpdateReversePrivateEndpoint | UpdateReversePrivateEndpointDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `reverse_private_endpoint_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `reverse_private_endpoint_id` — path `reversePrivateEndpointId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse, ClickPipeReversePrivateEndpointUpdateErrorBody]`
- **Error**: `ClickPipeReversePrivateEndpointUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400Error1` [400] · `V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateReversePrivateEndpoint` | `open_api_spec_for_click_house_cloud/models/update_reverse_private_endpoint.py` |
| `UpdateReversePrivateEndpointDict` | `open_api_spec_for_click_house_cloud/models/update_reverse_private_endpoint.py` |
| `V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id_response.py` |
| `ClickPipeReversePrivateEndpointUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_pipe_reverse_private_endpoint_update_error.py` |
| `V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id400_error1.py` |
| `V1OrganizationsServicesClickpipesReversePrivateEndpointsReversePrivateEndpointId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_reverse_private_endpoints_reverse_private_endpoint_id500_error1.py` |

### client.click_pipes.click_pipe_scaling_update

- **Route**: `PATCH /v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}/scaling`
- **Auth**: `basic_auth`
- **Signature**: `def click_pipe_scaling_update(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, body: ClickPipeScalingPatchRequest | ClickPipeScalingPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_pipe_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_pipe_id` — path `clickPipeId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickpipesClickPipeIdScalingResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickpipesClickPipeIdScalingResponse, ClickPipeScalingUpdateErrorBody]`
- **Error**: `ClickPipeScalingUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickpipesClickPipeIdScaling400Error1` [400] · `V1OrganizationsServicesClickpipesClickPipeIdScaling500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickPipeScalingPatchRequest` | `open_api_spec_for_click_house_cloud/models/click_pipe_scaling_patch_request.py` |
| `ClickPipeScalingPatchRequestDict` | `open_api_spec_for_click_house_cloud/models/click_pipe_scaling_patch_request.py` |
| `V1OrganizationsServicesClickpipesClickPipeIdScalingResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_scaling_response.py` |
| `ClickPipeScalingUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_pipe_scaling_update_error.py` |
| `V1OrganizationsServicesClickpipesClickPipeIdScaling400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_scaling400_error1.py` |
| `V1OrganizationsServicesClickpipesClickPipeIdScaling500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_scaling500_error1.py` |

### client.click_pipes.click_pipe_schema_discovery

- **Route**: `POST /v1/organizations/{organizationId}/services/{serviceId}/clickpipes/schemaDiscovery`
- **Auth**: `basic_auth`
- **Signature**: `def click_pipe_schema_discovery(organization_id: UUID, service_id: UUID, *, body: ClickPipeSchemaDiscoveryRequest | ClickPipeSchemaDiscoveryRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickpipesSchemaDiscoveryResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickpipesSchemaDiscoveryResponse, ClickPipeSchemaDiscoveryErrorBody]`
- **Error**: `ClickPipeSchemaDiscoveryErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickpipesSchemaDiscovery400Error1` [400] · `V1OrganizationsServicesClickpipesSchemaDiscovery500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickPipeSchemaDiscoveryRequest` | `open_api_spec_for_click_house_cloud/models/click_pipe_schema_discovery_request.py` |
| `ClickPipeSchemaDiscoveryRequestDict` | `open_api_spec_for_click_house_cloud/models/click_pipe_schema_discovery_request.py` |
| `V1OrganizationsServicesClickpipesSchemaDiscoveryResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_schema_discovery_response.py` |
| `ClickPipeSchemaDiscoveryErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_pipe_schema_discovery_error.py` |
| `V1OrganizationsServicesClickpipesSchemaDiscovery400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_schema_discovery400_error1.py` |
| `V1OrganizationsServicesClickpipesSchemaDiscovery500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_schema_discovery500_error1.py` |

### client.click_pipes.click_pipe_settings_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}/settings`
- **Auth**: `basic_auth`
- **Signature**: `def click_pipe_settings_get(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_pipe_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_pipe_id` — path `clickPipeId`
- **Returns (parsed)**: `V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse, ClickPipeSettingsGetErrorBody]`
- **Error**: `ClickPipeSettingsGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickpipesClickPipeIdSettings400Error1` [400] · `V1OrganizationsServicesClickpipesClickPipeIdSettings500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_settings_response.py` |
| `ClickPipeSettingsGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_pipe_settings_get_error.py` |
| `V1OrganizationsServicesClickpipesClickPipeIdSettings400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_settings400_error1.py` |
| `V1OrganizationsServicesClickpipesClickPipeIdSettings500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_settings500_error1.py` |

### client.click_pipes.click_pipe_settings_update

- **Route**: `PUT /v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}/settings`
- **Auth**: `basic_auth`
- **Signature**: `def click_pipe_settings_update(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, body: ClickPipeSettingsPutRequest | ClickPipeSettingsPutRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_pipe_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_pipe_id` — path `clickPipeId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse, ClickPipeSettingsUpdateErrorBody]`
- **Error**: `ClickPipeSettingsUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickpipesClickPipeIdSettings400Error1` [400] · `V1OrganizationsServicesClickpipesClickPipeIdSettings500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickPipeSettingsPutRequest` | `open_api_spec_for_click_house_cloud/models/click_pipe_settings_put_request.py` |
| `ClickPipeSettingsPutRequestDict` | `open_api_spec_for_click_house_cloud/models/click_pipe_settings_put_request.py` |
| `V1OrganizationsServicesClickpipesClickPipeIdSettingsResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_settings_response.py` |
| `ClickPipeSettingsUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_pipe_settings_update_error.py` |
| `V1OrganizationsServicesClickpipesClickPipeIdSettings400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_settings400_error1.py` |
| `V1OrganizationsServicesClickpipesClickPipeIdSettings500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_settings500_error1.py` |

### client.click_pipes.click_pipe_state_update

- **Route**: `PATCH /v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}/state`
- **Auth**: `basic_auth`
- **Signature**: `def click_pipe_state_update(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, body: ClickPipeStatePatchRequest | ClickPipeStatePatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_pipe_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_pipe_id` — path `clickPipeId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickpipesClickPipeIdStateResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickpipesClickPipeIdStateResponse, ClickPipeStateUpdateErrorBody]`
- **Error**: `ClickPipeStateUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickpipesClickPipeIdState400Error1` [400] · `V1OrganizationsServicesClickpipesClickPipeIdState500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickPipeStatePatchRequest` | `open_api_spec_for_click_house_cloud/models/click_pipe_state_patch_request.py` |
| `ClickPipeStatePatchRequestDict` | `open_api_spec_for_click_house_cloud/models/click_pipe_state_patch_request.py` |
| `V1OrganizationsServicesClickpipesClickPipeIdStateResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_state_response.py` |
| `ClickPipeStateUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_pipe_state_update_error.py` |
| `V1OrganizationsServicesClickpipesClickPipeIdState400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_state400_error1.py` |
| `V1OrganizationsServicesClickpipesClickPipeIdState500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_state500_error1.py` |

### client.click_pipes.click_pipe_update

- **Route**: `PATCH /v1/organizations/{organizationId}/services/{serviceId}/clickpipes/{clickPipeId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_pipe_update(organization_id: UUID, service_id: UUID, click_pipe_id: UUID, *, body: ClickPipePatchRequest | ClickPipePatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_pipe_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_pipe_id` — path `clickPipeId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickpipesClickPipeIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickpipesClickPipeIdResponse, ClickPipeUpdateErrorBody]`
- **Error**: `ClickPipeUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickpipesClickPipeId400Error1` [400] · `V1OrganizationsServicesClickpipesClickPipeId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickPipePatchRequest` | `open_api_spec_for_click_house_cloud/models/click_pipe_patch_request.py` |
| `ClickPipePatchRequestDict` | `open_api_spec_for_click_house_cloud/models/click_pipe_patch_request.py` |
| `V1OrganizationsServicesClickpipesClickPipeIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id_response.py` |
| `ClickPipeUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_pipe_update_error.py` |
| `V1OrganizationsServicesClickpipesClickPipeId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id400_error1.py` |
| `V1OrganizationsServicesClickpipesClickPipeId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_click_pipe_id500_error1.py` |

### client.click_pipes.click_pipes_service_context_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickpipes/context`
- **Auth**: `basic_auth`
- **Signature**: `def click_pipes_service_context_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesClickpipesContextResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickpipesContextResponse, ClickPipesServiceContextGetErrorBody]`
- **Error**: `ClickPipesServiceContextGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickpipesContext400Error1` [400] · `V1OrganizationsServicesClickpipesContext500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickpipesContextResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_context_response.py` |
| `ClickPipesServiceContextGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_pipes_service_context_get_error.py` |
| `V1OrganizationsServicesClickpipesContext400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_context400_error1.py` |
| `V1OrganizationsServicesClickpipesContext500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickpipes_context500_error1.py` |

