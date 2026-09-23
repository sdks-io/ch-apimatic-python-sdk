<!-- Generated file — do not edit; regenerated with the SDK. -->

# ServiceApi — operations

Accessor: `client.service_api` · Source: `open_api_spec_for_click_house_cloud/apis/service_api.py` · 26 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.service_api.instance_create

- **Route**: `POST /v1/organizations/{organizationId}/services`
- **Auth**: `basic_auth`
- **Signature**: `def instance_create(organization_id: UUID, *, body: ServicePostRequest | ServicePostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesResponse1, InstanceCreateErrorBody]`
- **Error**: `InstanceCreateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServices400Error1` [400] · `V1OrganizationsServices500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ServicePostRequest` | `open_api_spec_for_click_house_cloud/models/service_post_request.py` |
| `ServicePostRequestDict` | `open_api_spec_for_click_house_cloud/models/service_post_request.py` |
| `V1OrganizationsServicesResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_response1.py` |
| `InstanceCreateErrorBody` | `open_api_spec_for_click_house_cloud/errors/instance_create_error.py` |
| `V1OrganizationsServices400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services400_error1.py` |
| `V1OrganizationsServices500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services500_error1.py` |

### client.service_api.instance_delete

- **Route**: `DELETE /v1/organizations/{organizationId}/services/{serviceId}`
- **Auth**: `basic_auth`
- **Signature**: `def instance_delete(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesResponse4`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesResponse4, InstanceDeleteErrorBody]`
- **Error**: `InstanceDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServices400Error1` [400] · `V1OrganizationsServices500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesResponse4` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_response4.py` |
| `InstanceDeleteErrorBody` | `open_api_spec_for_click_house_cloud/errors/instance_delete_error.py` |
| `V1OrganizationsServices400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services400_error1.py` |
| `V1OrganizationsServices500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services500_error1.py` |

### client.service_api.instance_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}`
- **Auth**: `basic_auth`
- **Signature**: `def instance_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesResponse2`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesResponse2, InstanceGetErrorBody]`
- **Error**: `InstanceGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServices400Error1` [400] · `V1OrganizationsServices500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesResponse2` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_response2.py` |
| `InstanceGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/instance_get_error.py` |
| `V1OrganizationsServices400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services400_error1.py` |
| `V1OrganizationsServices500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services500_error1.py` |

### client.service_api.instance_get_list

- **Route**: `GET /v1/organizations/{organizationId}/services`
- **Auth**: `basic_auth`
- **Signature**: `def instance_get_list(organization_id: UUID, *, filter: list[str] | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId` · `filter` — query
- **Returns (parsed)**: `V1OrganizationsServicesResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesResponse, InstanceGetListErrorBody]`
- **Error**: `InstanceGetListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServices400Error1` [400] · `V1OrganizationsServices500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_response.py` |
| `InstanceGetListErrorBody` | `open_api_spec_for_click_house_cloud/errors/instance_get_list_error.py` |
| `V1OrganizationsServices400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services400_error1.py` |
| `V1OrganizationsServices500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services500_error1.py` |

### client.service_api.instance_password_update

- **Route**: `PATCH /v1/organizations/{organizationId}/services/{serviceId}/password`
- **Auth**: `basic_auth`
- **Signature**: `def instance_password_update(organization_id: UUID, service_id: UUID, *, body: ServicePasswordPatchRequest | ServicePasswordPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesPasswordResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesPasswordResponse, InstancePasswordUpdateErrorBody]`
- **Error**: `InstancePasswordUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesPassword400Error1` [400] · `V1OrganizationsServicesPassword500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ServicePasswordPatchRequest` | `open_api_spec_for_click_house_cloud/models/service_password_patch_request.py` |
| `ServicePasswordPatchRequestDict` | `open_api_spec_for_click_house_cloud/models/service_password_patch_request.py` |
| `V1OrganizationsServicesPasswordResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_password_response.py` |
| `InstancePasswordUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/instance_password_update_error.py` |
| `V1OrganizationsServicesPassword400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_password400_error1.py` |
| `V1OrganizationsServicesPassword500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_password500_error1.py` |

### client.service_api.instance_private_endpoint_config_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/privateEndpointConfig`
- **Auth**: `basic_auth`
- **Signature**: `def instance_private_endpoint_config_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesPrivateEndpointConfigResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesPrivateEndpointConfigResponse, InstancePrivateEndpointConfigGetErrorBody]`
- **Error**: `InstancePrivateEndpointConfigGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesPrivateEndpointConfig400Error1` [400] · `V1OrganizationsServicesPrivateEndpointConfig500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesPrivateEndpointConfigResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_private_endpoint_config_response.py` |
| `InstancePrivateEndpointConfigGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/instance_private_endpoint_config_get_error.py` |
| `V1OrganizationsServicesPrivateEndpointConfig400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_private_endpoint_config400_error1.py` |
| `V1OrganizationsServicesPrivateEndpointConfig500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_private_endpoint_config500_error1.py` |

### client.service_api.instance_private_endpoint_create

- **Route**: `POST /v1/organizations/{organizationId}/services/{serviceId}/privateEndpoint`
- **Auth**: `basic_auth`
- **Signature**: `def instance_private_endpoint_create(organization_id: UUID, service_id: UUID, *, body: ServicPrivateEndpointePostRequest | ServicPrivateEndpointePostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesPrivateEndpointResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesPrivateEndpointResponse, InstancePrivateEndpointCreateErrorBody]`
- **Error**: `InstancePrivateEndpointCreateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesPrivateEndpoint400Error1` [400] · `V1OrganizationsServicesPrivateEndpoint500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ServicPrivateEndpointePostRequest` | `open_api_spec_for_click_house_cloud/models/servic_private_endpointe_post_request.py` |
| `ServicPrivateEndpointePostRequestDict` | `open_api_spec_for_click_house_cloud/models/servic_private_endpointe_post_request.py` |
| `V1OrganizationsServicesPrivateEndpointResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_private_endpoint_response.py` |
| `InstancePrivateEndpointCreateErrorBody` | `open_api_spec_for_click_house_cloud/errors/instance_private_endpoint_create_error.py` |
| `V1OrganizationsServicesPrivateEndpoint400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_private_endpoint400_error1.py` |
| `V1OrganizationsServicesPrivateEndpoint500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_private_endpoint500_error1.py` |

### client.service_api.instance_query_endpoint_delete

- **Route**: `DELETE /v1/organizations/{organizationId}/services/{serviceId}/serviceQueryEndpoint`
- **Auth**: `basic_auth`
- **Signature**: `def instance_query_endpoint_delete(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesServiceQueryEndpointResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesServiceQueryEndpointResponse1, InstanceQueryEndpointDeleteErrorBody]`
- **Error**: `InstanceQueryEndpointDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesServiceQueryEndpoint400Error1` [400] · `V1OrganizationsServicesServiceQueryEndpoint500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesServiceQueryEndpointResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint_response1.py` |
| `InstanceQueryEndpointDeleteErrorBody` | `open_api_spec_for_click_house_cloud/errors/instance_query_endpoint_delete_error.py` |
| `V1OrganizationsServicesServiceQueryEndpoint400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint400_error1.py` |
| `V1OrganizationsServicesServiceQueryEndpoint500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint500_error1.py` |

### client.service_api.instance_query_endpoint_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/serviceQueryEndpoint`
- **Auth**: `basic_auth`
- **Signature**: `def instance_query_endpoint_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesServiceQueryEndpointResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesServiceQueryEndpointResponse, InstanceQueryEndpointGetErrorBody]`
- **Error**: `InstanceQueryEndpointGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesServiceQueryEndpoint400Error1` [400] · `V1OrganizationsServicesServiceQueryEndpoint500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesServiceQueryEndpointResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint_response.py` |
| `InstanceQueryEndpointGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/instance_query_endpoint_get_error.py` |
| `V1OrganizationsServicesServiceQueryEndpoint400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint400_error1.py` |
| `V1OrganizationsServicesServiceQueryEndpoint500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint500_error1.py` |

### client.service_api.instance_query_endpoint_upsert

- **Route**: `POST /v1/organizations/{organizationId}/services/{serviceId}/serviceQueryEndpoint`
- **Auth**: `basic_auth`
- **Signature**: `def instance_query_endpoint_upsert(organization_id: UUID, service_id: UUID, *, body: InstanceServiceQueryApiEndpointsPostRequest | InstanceServiceQueryApiEndpointsPostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesServiceQueryEndpointResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesServiceQueryEndpointResponse, InstanceQueryEndpointUpsertErrorBody]`
- **Error**: `InstanceQueryEndpointUpsertErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesServiceQueryEndpoint400Error1` [400] · `V1OrganizationsServicesServiceQueryEndpoint500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `InstanceServiceQueryApiEndpointsPostRequest` | `open_api_spec_for_click_house_cloud/models/instance_service_query_api_endpoints_post_request.py` |
| `InstanceServiceQueryApiEndpointsPostRequestDict` | `open_api_spec_for_click_house_cloud/models/instance_service_query_api_endpoints_post_request.py` |
| `V1OrganizationsServicesServiceQueryEndpointResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint_response.py` |
| `InstanceQueryEndpointUpsertErrorBody` | `open_api_spec_for_click_house_cloud/errors/instance_query_endpoint_upsert_error.py` |
| `V1OrganizationsServicesServiceQueryEndpoint400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint400_error1.py` |
| `V1OrganizationsServicesServiceQueryEndpoint500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_service_query_endpoint500_error1.py` |

### client.service_api.instance_replica_scaling_update

- **Route**: `PATCH /v1/organizations/{organizationId}/services/{serviceId}/replicaScaling`
- **Auth**: `basic_auth`
- **Signature**: `def instance_replica_scaling_update(organization_id: UUID, service_id: UUID, *, body: ServiceReplicaScalingPatchRequest | ServiceReplicaScalingPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesReplicaScalingResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesReplicaScalingResponse, InstanceReplicaScalingUpdateErrorBody]`
- **Error**: `InstanceReplicaScalingUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesReplicaScaling400Error1` [400] · `V1OrganizationsServicesReplicaScaling500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ServiceReplicaScalingPatchRequest` | `open_api_spec_for_click_house_cloud/models/service_replica_scaling_patch_request.py` |
| `ServiceReplicaScalingPatchRequestDict` | `open_api_spec_for_click_house_cloud/models/service_replica_scaling_patch_request.py` |
| `V1OrganizationsServicesReplicaScalingResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_replica_scaling_response.py` |
| `InstanceReplicaScalingUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/instance_replica_scaling_update_error.py` |
| `V1OrganizationsServicesReplicaScaling400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_replica_scaling400_error1.py` |
| `V1OrganizationsServicesReplicaScaling500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_replica_scaling500_error1.py` |

### client.service_api.instance_scaling_update

- **Route**: `PATCH /v1/organizations/{organizationId}/services/{serviceId}/scaling`
- **Auth**: `basic_auth`
- **Signature**: `def instance_scaling_update(organization_id: UUID, service_id: UUID, *, body: ServiceScalingPatchRequest | ServiceScalingPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesScalingResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesScalingResponse, InstanceScalingUpdateErrorBody]`
- **Error**: `InstanceScalingUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesScaling400Error1` [400] · `V1OrganizationsServicesScaling500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ServiceScalingPatchRequest` | `open_api_spec_for_click_house_cloud/models/service_scaling_patch_request.py` |
| `ServiceScalingPatchRequestDict` | `open_api_spec_for_click_house_cloud/models/service_scaling_patch_request.py` |
| `V1OrganizationsServicesScalingResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_response.py` |
| `InstanceScalingUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/instance_scaling_update_error.py` |
| `V1OrganizationsServicesScaling400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling400_error1.py` |
| `V1OrganizationsServicesScaling500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling500_error1.py` |

### client.service_api.instance_state_update

- **Route**: `PATCH /v1/organizations/{organizationId}/services/{serviceId}/state`
- **Auth**: `basic_auth`
- **Signature**: `def instance_state_update(organization_id: UUID, service_id: UUID, *, body: ServiceStatePatchRequest | ServiceStatePatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesStateResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesStateResponse, InstanceStateUpdateErrorBody]`
- **Error**: `InstanceStateUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesState400Error1` [400] · `V1OrganizationsServicesState500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ServiceStatePatchRequest` | `open_api_spec_for_click_house_cloud/models/service_state_patch_request.py` |
| `ServiceStatePatchRequestDict` | `open_api_spec_for_click_house_cloud/models/service_state_patch_request.py` |
| `V1OrganizationsServicesStateResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_state_response.py` |
| `InstanceStateUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/instance_state_update_error.py` |
| `V1OrganizationsServicesState400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_state400_error1.py` |
| `V1OrganizationsServicesState500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_state500_error1.py` |

### client.service_api.instance_update

- **Route**: `PATCH /v1/organizations/{organizationId}/services/{serviceId}`
- **Auth**: `basic_auth`
- **Signature**: `def instance_update(organization_id: UUID, service_id: UUID, *, body: ServicePatchRequest | ServicePatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesResponse2`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesResponse2, InstanceUpdateErrorBody]`
- **Error**: `InstanceUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServices400Error1` [400] · `V1OrganizationsServices500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ServicePatchRequest` | `open_api_spec_for_click_house_cloud/models/service_patch_request.py` |
| `ServicePatchRequestDict` | `open_api_spec_for_click_house_cloud/models/service_patch_request.py` |
| `V1OrganizationsServicesResponse2` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_response2.py` |
| `InstanceUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/instance_update_error.py` |
| `V1OrganizationsServices400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services400_error1.py` |
| `V1OrganizationsServices500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services500_error1.py` |

### client.service_api.scaling_schedule_delete

- **Route**: `DELETE /v1/organizations/{organizationId}/services/{serviceId}/scalingSchedule`
- **Auth**: `basic_auth`
- **Signature**: `def scaling_schedule_delete(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesScalingScheduleResponse2`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesScalingScheduleResponse2, ScalingScheduleDeleteErrorBody]`
- **Error**: `ScalingScheduleDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesScalingSchedule400Error1` [400] · `V1OrganizationsServicesScalingSchedule500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesScalingScheduleResponse2` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule_response2.py` |
| `ScalingScheduleDeleteErrorBody` | `open_api_spec_for_click_house_cloud/errors/scaling_schedule_delete_error.py` |
| `V1OrganizationsServicesScalingSchedule400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule400_error1.py` |
| `V1OrganizationsServicesScalingSchedule500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule500_error1.py` |

### client.service_api.scaling_schedule_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/scalingSchedule`
- **Auth**: `basic_auth`
- **Signature**: `def scaling_schedule_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesScalingScheduleResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesScalingScheduleResponse, ScalingScheduleGetErrorBody]`
- **Error**: `ScalingScheduleGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesScalingSchedule400Error1` [400] · `V1OrganizationsServicesScalingSchedule500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesScalingScheduleResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule_response.py` |
| `ScalingScheduleGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/scaling_schedule_get_error.py` |
| `V1OrganizationsServicesScalingSchedule400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule400_error1.py` |
| `V1OrganizationsServicesScalingSchedule500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule500_error1.py` |

### client.service_api.scaling_schedule_upsert

- **Route**: `POST /v1/organizations/{organizationId}/services/{serviceId}/scalingSchedule`
- **Auth**: `basic_auth`
- **Signature**: `def scaling_schedule_upsert(organization_id: UUID, service_id: UUID, *, body: ScalingSchedulePostRequest | ScalingSchedulePostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesScalingScheduleResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesScalingScheduleResponse, ScalingScheduleUpsertErrorBody]`
- **Error**: `ScalingScheduleUpsertErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesScalingSchedule400Error1` [400] · `V1OrganizationsServicesScalingSchedule500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ScalingSchedulePostRequest` | `open_api_spec_for_click_house_cloud/models/scaling_schedule_post_request.py` |
| `ScalingSchedulePostRequestDict` | `open_api_spec_for_click_house_cloud/models/scaling_schedule_post_request.py` |
| `V1OrganizationsServicesScalingScheduleResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule_response.py` |
| `ScalingScheduleUpsertErrorBody` | `open_api_spec_for_click_house_cloud/errors/scaling_schedule_upsert_error.py` |
| `V1OrganizationsServicesScalingSchedule400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule400_error1.py` |
| `V1OrganizationsServicesScalingSchedule500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_scaling_schedule500_error1.py` |

### client.service_api.service_clickhouse_setting_delete

- **Route**: `DELETE /v1/organizations/{organizationId}/services/{serviceId}/clickhouseSettings/{settingName}`
- **Auth**: `basic_auth`
- **Signature**: `def service_clickhouse_setting_delete(organization_id: UUID, service_id: UUID, setting_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `setting_name`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `setting_name` — path `settingName`
- **Returns (parsed)**: `V1OrganizationsServicesClickhouseSettingsSettingNameResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickhouseSettingsSettingNameResponse1, ServiceClickhouseSettingDeleteErrorBody]`
- **Error**: `ServiceClickhouseSettingDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickhouseSettingsSettingName400Error1` [400] · `V1OrganizationsServicesClickhouseSettingsSettingName500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickhouseSettingsSettingNameResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_setting_name_response1.py` |
| `ServiceClickhouseSettingDeleteErrorBody` | `open_api_spec_for_click_house_cloud/errors/service_clickhouse_setting_delete_error.py` |
| `V1OrganizationsServicesClickhouseSettingsSettingName400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_setting_name400_error1.py` |
| `V1OrganizationsServicesClickhouseSettingsSettingName500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_setting_name500_error1.py` |

### client.service_api.service_clickhouse_setting_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickhouseSettings/{settingName}`
- **Auth**: `basic_auth`
- **Signature**: `def service_clickhouse_setting_get(organization_id: UUID, service_id: UUID, setting_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `setting_name`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `setting_name` — path `settingName`
- **Returns (parsed)**: `V1OrganizationsServicesClickhouseSettingsSettingNameResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickhouseSettingsSettingNameResponse, ServiceClickhouseSettingGetErrorBody]`
- **Error**: `ServiceClickhouseSettingGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickhouseSettingsSettingName400Error1` [400] · `V1OrganizationsServicesClickhouseSettingsSettingName500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickhouseSettingsSettingNameResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_setting_name_response.py` |
| `ServiceClickhouseSettingGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/service_clickhouse_setting_get_error.py` |
| `V1OrganizationsServicesClickhouseSettingsSettingName400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_setting_name400_error1.py` |
| `V1OrganizationsServicesClickhouseSettingsSettingName500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_setting_name500_error1.py` |

### client.service_api.service_clickhouse_settings_list_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickhouseSettings`
- **Auth**: `basic_auth`
- **Signature**: `def service_clickhouse_settings_list_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesClickhouseSettingsResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickhouseSettingsResponse, ServiceClickhouseSettingsListGetErrorBody]`
- **Error**: `ServiceClickhouseSettingsListGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickhouseSettings400Error1` [400] · `V1OrganizationsServicesClickhouseSettings500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickhouseSettingsResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_response.py` |
| `ServiceClickhouseSettingsListGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/service_clickhouse_settings_list_get_error.py` |
| `V1OrganizationsServicesClickhouseSettings400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings400_error1.py` |
| `V1OrganizationsServicesClickhouseSettings500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings500_error1.py` |

### client.service_api.service_clickhouse_settings_schema_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickhouseSettings/schema`
- **Auth**: `basic_auth`
- **Signature**: `def service_clickhouse_settings_schema_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesClickhouseSettingsSchemaResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickhouseSettingsSchemaResponse, ServiceClickhouseSettingsSchemaGetErrorBody]`
- **Error**: `ServiceClickhouseSettingsSchemaGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickhouseSettingsSchema400Error1` [400] · `V1OrganizationsServicesClickhouseSettingsSchema500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickhouseSettingsSchemaResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_schema_response.py` |
| `ServiceClickhouseSettingsSchemaGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/service_clickhouse_settings_schema_get_error.py` |
| `V1OrganizationsServicesClickhouseSettingsSchema400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_schema400_error1.py` |
| `V1OrganizationsServicesClickhouseSettingsSchema500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_schema500_error1.py` |

### client.service_api.service_clickhouse_settings_update

- **Route**: `PATCH /v1/organizations/{organizationId}/services/{serviceId}/clickhouseSettings`
- **Auth**: `basic_auth`
- **Signature**: `def service_clickhouse_settings_update(organization_id: UUID, service_id: UUID, *, body: ServiceClickhouseSettingsPatchRequest | ServiceClickhouseSettingsPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickhouseSettingsResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickhouseSettingsResponse1, ServiceClickhouseSettingsUpdateErrorBody]`
- **Error**: `ServiceClickhouseSettingsUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickhouseSettings400Error1` [400] · `V1OrganizationsServicesClickhouseSettings500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ServiceClickhouseSettingsPatchRequest` | `open_api_spec_for_click_house_cloud/models/service_clickhouse_settings_patch_request.py` |
| `ServiceClickhouseSettingsPatchRequestDict` | `open_api_spec_for_click_house_cloud/models/service_clickhouse_settings_patch_request.py` |
| `V1OrganizationsServicesClickhouseSettingsResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings_response1.py` |
| `ServiceClickhouseSettingsUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/service_clickhouse_settings_update_error.py` |
| `V1OrganizationsServicesClickhouseSettings400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings400_error1.py` |
| `V1OrganizationsServicesClickhouseSettings500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickhouse_settings500_error1.py` |

### client.service_api.service_profiles_list

- **Route**: `GET /v1/organizations/{organizationId}/serviceProfiles`
- **Auth**: `basic_auth`
- **Signature**: `def service_profiles_list(organization_id: UUID, *, region_id: str | None = None, byoc_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId` · `region_id` — query · `byoc_id` — query
- **Returns (parsed)**: `V1OrganizationsServiceProfilesResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServiceProfilesResponse, ServiceProfilesListErrorBody]`
- **Error**: `ServiceProfilesListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServiceProfiles400Error1` [400] · `V1OrganizationsServiceProfiles500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServiceProfilesResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_service_profiles_response.py` |
| `ServiceProfilesListErrorBody` | `open_api_spec_for_click_house_cloud/errors/service_profiles_list_error.py` |
| `V1OrganizationsServiceProfiles400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_service_profiles400_error1.py` |
| `V1OrganizationsServiceProfiles500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_service_profiles500_error1.py` |

### client.service_api.upgrade_window_delete

- **Route**: `DELETE /v1/organizations/{organizationId}/services/{serviceId}/upgradeWindow`
- **Auth**: `basic_auth`
- **Signature**: `def upgrade_window_delete(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesUpgradeWindowResponse2`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesUpgradeWindowResponse2, UpgradeWindowDeleteErrorBody]`
- **Error**: `UpgradeWindowDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesUpgradeWindow400Error1` [400] · `V1OrganizationsServicesUpgradeWindow500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesUpgradeWindowResponse2` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window_response2.py` |
| `UpgradeWindowDeleteErrorBody` | `open_api_spec_for_click_house_cloud/errors/upgrade_window_delete_error.py` |
| `V1OrganizationsServicesUpgradeWindow400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window400_error1.py` |
| `V1OrganizationsServicesUpgradeWindow500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window500_error1.py` |

### client.service_api.upgrade_window_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/upgradeWindow`
- **Auth**: `basic_auth`
- **Signature**: `def upgrade_window_get(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesUpgradeWindowResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesUpgradeWindowResponse, UpgradeWindowGetErrorBody]`
- **Error**: `UpgradeWindowGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesUpgradeWindow400Error1` [400] · `V1OrganizationsServicesUpgradeWindow500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesUpgradeWindowResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window_response.py` |
| `UpgradeWindowGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/upgrade_window_get_error.py` |
| `V1OrganizationsServicesUpgradeWindow400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window400_error1.py` |
| `V1OrganizationsServicesUpgradeWindow500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window500_error1.py` |

### client.service_api.upgrade_window_update

- **Route**: `PUT /v1/organizations/{organizationId}/services/{serviceId}/upgradeWindow`
- **Auth**: `basic_auth`
- **Signature**: `def upgrade_window_update(organization_id: UUID, service_id: UUID, *, body: UpgradeWindowPutRequest | UpgradeWindowPutRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesUpgradeWindowResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesUpgradeWindowResponse, UpgradeWindowUpdateErrorBody]`
- **Error**: `UpgradeWindowUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesUpgradeWindow400Error1` [400] · `V1OrganizationsServicesUpgradeWindow500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpgradeWindowPutRequest` | `open_api_spec_for_click_house_cloud/models/upgrade_window_put_request.py` |
| `UpgradeWindowPutRequestDict` | `open_api_spec_for_click_house_cloud/models/upgrade_window_put_request.py` |
| `V1OrganizationsServicesUpgradeWindowResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window_response.py` |
| `UpgradeWindowUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/upgrade_window_update_error.py` |
| `V1OrganizationsServicesUpgradeWindow400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window400_error1.py` |
| `V1OrganizationsServicesUpgradeWindow500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_upgrade_window500_error1.py` |

