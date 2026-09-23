<!-- Generated file — do not edit; regenerated with the SDK. -->

# ApiKeys — operations

Accessor: `client.api_keys` · Source: `open_api_spec_for_click_house_cloud/apis/api_keys.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.api_keys.openapi_key_create

- **Route**: `POST /v1/organizations/{organizationId}/keys`
- **Auth**: `basic_auth`
- **Signature**: `def openapi_key_create(organization_id: UUID, *, body: ApiKeyPostRequest | ApiKeyPostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsKeysResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsKeysResponse1, OpenapiKeyCreateErrorBody]`
- **Error**: `OpenapiKeyCreateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsKeys400Error1` [400] · `V1OrganizationsKeys500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiKeyPostRequest` | `open_api_spec_for_click_house_cloud/models/api_key_post_request.py` |
| `ApiKeyPostRequestDict` | `open_api_spec_for_click_house_cloud/models/api_key_post_request.py` |
| `V1OrganizationsKeysResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response1.py` |
| `OpenapiKeyCreateErrorBody` | `open_api_spec_for_click_house_cloud/errors/openapi_key_create_error.py` |
| `V1OrganizationsKeys400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_keys400_error1.py` |
| `V1OrganizationsKeys500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_keys500_error1.py` |

### client.api_keys.openapi_key_delete

- **Route**: `DELETE /v1/organizations/{organizationId}/keys/{keyId}`
- **Auth**: `basic_auth`
- **Signature**: `def openapi_key_delete(organization_id: UUID, key_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `key_id`
- **Params**: `organization_id` — path `organizationId` · `key_id` — path `keyId`
- **Returns (parsed)**: `V1OrganizationsKeysResponse4`
- **Returns (raw)**: `ApiResult[V1OrganizationsKeysResponse4, OpenapiKeyDeleteErrorBody]`
- **Error**: `OpenapiKeyDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsKeys400Error1` [400] · `V1OrganizationsKeys500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsKeysResponse4` | `open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response4.py` |
| `OpenapiKeyDeleteErrorBody` | `open_api_spec_for_click_house_cloud/errors/openapi_key_delete_error.py` |
| `V1OrganizationsKeys400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_keys400_error1.py` |
| `V1OrganizationsKeys500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_keys500_error1.py` |

### client.api_keys.openapi_key_get

- **Route**: `GET /v1/organizations/{organizationId}/keys/{keyId}`
- **Auth**: `basic_auth`
- **Signature**: `def openapi_key_get(organization_id: UUID, key_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `key_id`
- **Params**: `organization_id` — path `organizationId` · `key_id` — path `keyId`
- **Returns (parsed)**: `V1OrganizationsKeysResponse2`
- **Returns (raw)**: `ApiResult[V1OrganizationsKeysResponse2, OpenapiKeyGetErrorBody]`
- **Error**: `OpenapiKeyGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsKeys400Error1` [400] · `V1OrganizationsKeys500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsKeysResponse2` | `open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response2.py` |
| `OpenapiKeyGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/openapi_key_get_error.py` |
| `V1OrganizationsKeys400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_keys400_error1.py` |
| `V1OrganizationsKeys500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_keys500_error1.py` |

### client.api_keys.openapi_key_get_list

- **Route**: `GET /v1/organizations/{organizationId}/keys`
- **Auth**: `basic_auth`
- **Signature**: `def openapi_key_get_list(organization_id: UUID, *, limit: int | None = 250, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId` · `limit` — query · `cursor` — query
- **Returns (parsed)**: `V1OrganizationsKeysResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsKeysResponse, OpenapiKeyGetListErrorBody]`
- **Error**: `OpenapiKeyGetListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsKeys400Error1` [400] · `V1OrganizationsKeys500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsKeysResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response.py` |
| `OpenapiKeyGetListErrorBody` | `open_api_spec_for_click_house_cloud/errors/openapi_key_get_list_error.py` |
| `V1OrganizationsKeys400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_keys400_error1.py` |
| `V1OrganizationsKeys500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_keys500_error1.py` |

### client.api_keys.openapi_key_update

- **Route**: `PATCH /v1/organizations/{organizationId}/keys/{keyId}`
- **Auth**: `basic_auth`
- **Signature**: `def openapi_key_update(organization_id: UUID, key_id: UUID, *, body: ApiKeyPatchRequest | ApiKeyPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `key_id`
- **Params**: `organization_id` — path `organizationId` · `key_id` — path `keyId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsKeysResponse2`
- **Returns (raw)**: `ApiResult[V1OrganizationsKeysResponse2, OpenapiKeyUpdateErrorBody]`
- **Error**: `OpenapiKeyUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsKeys400Error1` [400] · `V1OrganizationsKeys500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ApiKeyPatchRequest` | `open_api_spec_for_click_house_cloud/models/api_key_patch_request.py` |
| `ApiKeyPatchRequestDict` | `open_api_spec_for_click_house_cloud/models/api_key_patch_request.py` |
| `V1OrganizationsKeysResponse2` | `open_api_spec_for_click_house_cloud/models/v1_organizations_keys_response2.py` |
| `OpenapiKeyUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/openapi_key_update_error.py` |
| `V1OrganizationsKeys400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_keys400_error1.py` |
| `V1OrganizationsKeys500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_keys500_error1.py` |

