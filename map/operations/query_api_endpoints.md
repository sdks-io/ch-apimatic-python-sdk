<!-- Generated file — do not edit; regenerated with the SDK. -->

# QueryApiEndpoints — operations

Accessor: `client.query_api_endpoints` · Source: `open_api_spec_for_click_house_cloud/apis/query_api_endpoints.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.query_api_endpoints.query_api_endpoint_create

- **Route**: `POST /v1/organizations/{organizationId}/services/{serviceId}/query-api-endpoints`
- **Auth**: `basic_auth`
- **Signature**: `def query_api_endpoint_create(organization_id: UUID, service_id: UUID, *, body: PublicQueryApiEndpointRequest | PublicQueryApiEndpointRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesQueryApiEndpointsResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesQueryApiEndpointsResponse, QueryApiEndpointCreateErrorBody]`
- **Error**: `QueryApiEndpointCreateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesQueryApiEndpoints400Error1` [400] · `V1OrganizationsServicesQueryApiEndpoints403Error1` [403] · `V1OrganizationsServicesQueryApiEndpoints404Error1` [404] · `V1OrganizationsServicesQueryApiEndpoints500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PublicQueryApiEndpointRequest` | `open_api_spec_for_click_house_cloud/models/public_query_api_endpoint_request.py` |
| `PublicQueryApiEndpointRequestDict` | `open_api_spec_for_click_house_cloud/models/public_query_api_endpoint_request.py` |
| `V1OrganizationsServicesQueryApiEndpointsResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_response.py` |
| `QueryApiEndpointCreateErrorBody` | `open_api_spec_for_click_house_cloud/errors/query_api_endpoint_create_error.py` |
| `V1OrganizationsServicesQueryApiEndpoints400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints400_error1.py` |
| `V1OrganizationsServicesQueryApiEndpoints403Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints403_error1.py` |
| `V1OrganizationsServicesQueryApiEndpoints404Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints404_error1.py` |
| `V1OrganizationsServicesQueryApiEndpoints500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints500_error1.py` |

### client.query_api_endpoints.query_api_endpoint_delete

- **Route**: `DELETE /v1/organizations/{organizationId}/services/{serviceId}/query-api-endpoints/{endpointId}`
- **Auth**: `basic_auth`
- **Signature**: `def query_api_endpoint_delete(organization_id: UUID, service_id: UUID, endpoint_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `endpoint_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `endpoint_id` — path `endpointId`
- **Returns (parsed)**: `V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse, QueryApiEndpointDeleteErrorBody]`
- **Error**: `QueryApiEndpointDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesQueryApiEndpointsEndpointId400Error1` [400] · `V1OrganizationsServicesQueryApiEndpointsEndpointId403Error1` [403] · `V1OrganizationsServicesQueryApiEndpointsEndpointId404Error1` [404] · `V1OrganizationsServicesQueryApiEndpointsEndpointId409Error1` [409] · `V1OrganizationsServicesQueryApiEndpointsEndpointId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id_response.py` |
| `QueryApiEndpointDeleteErrorBody` | `open_api_spec_for_click_house_cloud/errors/query_api_endpoint_delete_error.py` |
| `V1OrganizationsServicesQueryApiEndpointsEndpointId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id400_error1.py` |
| `V1OrganizationsServicesQueryApiEndpointsEndpointId403Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id403_error1.py` |
| `V1OrganizationsServicesQueryApiEndpointsEndpointId404Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id404_error1.py` |
| `V1OrganizationsServicesQueryApiEndpointsEndpointId409Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id409_error1.py` |
| `V1OrganizationsServicesQueryApiEndpointsEndpointId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id500_error1.py` |

### client.query_api_endpoints.query_api_endpoint_get

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/query-api-endpoints/{endpointId}`
- **Auth**: `basic_auth`
- **Signature**: `def query_api_endpoint_get(organization_id: UUID, service_id: UUID, endpoint_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `endpoint_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `endpoint_id` — path `endpointId`
- **Returns (parsed)**: `V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1, QueryApiEndpointGetErrorBody]`
- **Error**: `QueryApiEndpointGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesQueryApiEndpointsEndpointId400Error1` [400] · `V1OrganizationsServicesQueryApiEndpointsEndpointId403Error1` [403] · `V1OrganizationsServicesQueryApiEndpointsEndpointId404Error1` [404] · `V1OrganizationsServicesQueryApiEndpointsEndpointId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id_response1.py` |
| `QueryApiEndpointGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/query_api_endpoint_get_error.py` |
| `V1OrganizationsServicesQueryApiEndpointsEndpointId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id400_error1.py` |
| `V1OrganizationsServicesQueryApiEndpointsEndpointId403Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id403_error1.py` |
| `V1OrganizationsServicesQueryApiEndpointsEndpointId404Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id404_error1.py` |
| `V1OrganizationsServicesQueryApiEndpointsEndpointId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id500_error1.py` |

### client.query_api_endpoints.query_api_endpoint_list

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/query-api-endpoints`
- **Auth**: `basic_auth`
- **Signature**: `def query_api_endpoint_list(organization_id: UUID, service_id: UUID, *, cursor: str | None = None, limit: int | None = 100, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `cursor` — query · `limit` — query
- **Returns (parsed)**: `V1OrganizationsServicesQueryApiEndpointsResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesQueryApiEndpointsResponse1, QueryApiEndpointListErrorBody]`
- **Error**: `QueryApiEndpointListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesQueryApiEndpoints400Error1` [400] · `V1OrganizationsServicesQueryApiEndpoints403Error1` [403] · `V1OrganizationsServicesQueryApiEndpoints404Error1` [404] · `V1OrganizationsServicesQueryApiEndpoints500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesQueryApiEndpointsResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_response1.py` |
| `QueryApiEndpointListErrorBody` | `open_api_spec_for_click_house_cloud/errors/query_api_endpoint_list_error.py` |
| `V1OrganizationsServicesQueryApiEndpoints400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints400_error1.py` |
| `V1OrganizationsServicesQueryApiEndpoints403Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints403_error1.py` |
| `V1OrganizationsServicesQueryApiEndpoints404Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints404_error1.py` |
| `V1OrganizationsServicesQueryApiEndpoints500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints500_error1.py` |

### client.query_api_endpoints.query_api_endpoint_update

- **Route**: `PUT /v1/organizations/{organizationId}/services/{serviceId}/query-api-endpoints/{endpointId}`
- **Auth**: `basic_auth`
- **Signature**: `def query_api_endpoint_update(organization_id: UUID, service_id: UUID, endpoint_id: UUID, *, body: PublicQueryApiEndpointRequest | PublicQueryApiEndpointRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `endpoint_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `endpoint_id` — path `endpointId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1, QueryApiEndpointUpdateErrorBody]`
- **Error**: `QueryApiEndpointUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesQueryApiEndpointsEndpointId400Error31` [400] · `V1OrganizationsServicesQueryApiEndpointsEndpointId403Error1` [403] · `V1OrganizationsServicesQueryApiEndpointsEndpointId404Error1` [404] · `V1OrganizationsServicesQueryApiEndpointsEndpointId409Error1` [409] · `V1OrganizationsServicesQueryApiEndpointsEndpointId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PublicQueryApiEndpointRequest` | `open_api_spec_for_click_house_cloud/models/public_query_api_endpoint_request.py` |
| `PublicQueryApiEndpointRequestDict` | `open_api_spec_for_click_house_cloud/models/public_query_api_endpoint_request.py` |
| `V1OrganizationsServicesQueryApiEndpointsEndpointIdResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id_response1.py` |
| `QueryApiEndpointUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/query_api_endpoint_update_error.py` |
| `V1OrganizationsServicesQueryApiEndpointsEndpointId400Error31` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id400_error31.py` |
| `V1OrganizationsServicesQueryApiEndpointsEndpointId403Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id403_error1.py` |
| `V1OrganizationsServicesQueryApiEndpointsEndpointId404Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id404_error1.py` |
| `V1OrganizationsServicesQueryApiEndpointsEndpointId409Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id409_error1.py` |
| `V1OrganizationsServicesQueryApiEndpointsEndpointId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_query_api_endpoints_endpoint_id500_error1.py` |

