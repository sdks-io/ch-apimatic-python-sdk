<!-- Generated file — do not edit; regenerated with the SDK. -->

# RoleManagement — operations

Accessor: `client.role_management` · Source: `open_api_spec_for_click_house_cloud/apis/role_management.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.role_management.organization_role_delete

- **Route**: `DELETE /v1/organizations/{organizationId}/roles/{roleId}`
- **Auth**: `basic_auth`
- **Signature**: `def organization_role_delete(organization_id: UUID, role_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `role_id`
- **Params**: `organization_id` — path `organizationId` · `role_id` — path `roleId`
- **Returns (parsed)**: `V1OrganizationsRolesResponse4`
- **Returns (raw)**: `ApiResult[V1OrganizationsRolesResponse4, OrganizationRoleDeleteErrorBody]`
- **Error**: `OrganizationRoleDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsRoles400Error1` [400] · `V1OrganizationsRoles500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsRolesResponse4` | `open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response4.py` |
| `OrganizationRoleDeleteErrorBody` | `open_api_spec_for_click_house_cloud/errors/organization_role_delete_error.py` |
| `V1OrganizationsRoles400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_roles400_error1.py` |
| `V1OrganizationsRoles500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_roles500_error1.py` |

### client.role_management.organization_role_get

- **Route**: `GET /v1/organizations/{organizationId}/roles/{roleId}`
- **Auth**: `basic_auth`
- **Signature**: `def organization_role_get(organization_id: UUID, role_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `role_id`
- **Params**: `organization_id` — path `organizationId` · `role_id` — path `roleId`
- **Returns (parsed)**: `V1OrganizationsRolesResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsRolesResponse1, OrganizationRoleGetErrorBody]`
- **Error**: `OrganizationRoleGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsRoles400Error1` [400] · `V1OrganizationsRoles500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsRolesResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response1.py` |
| `OrganizationRoleGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/organization_role_get_error.py` |
| `V1OrganizationsRoles400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_roles400_error1.py` |
| `V1OrganizationsRoles500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_roles500_error1.py` |

### client.role_management.organization_role_patch

- **Route**: `PATCH /v1/organizations/{organizationId}/roles/{roleId}`
- **Auth**: `basic_auth`
- **Signature**: `def organization_role_patch(organization_id: UUID, role_id: UUID, *, body: RoleUpdateRequest | RoleUpdateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `role_id`
- **Params**: `organization_id` — path `organizationId` · `role_id` — path `roleId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsRolesResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsRolesResponse1, OrganizationRolePatchErrorBody]`
- **Error**: `OrganizationRolePatchErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsRoles400Error1` [400] · `V1OrganizationsRoles500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RoleUpdateRequest` | `open_api_spec_for_click_house_cloud/models/role_update_request.py` |
| `RoleUpdateRequestDict` | `open_api_spec_for_click_house_cloud/models/role_update_request.py` |
| `V1OrganizationsRolesResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response1.py` |
| `OrganizationRolePatchErrorBody` | `open_api_spec_for_click_house_cloud/errors/organization_role_patch_error.py` |
| `V1OrganizationsRoles400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_roles400_error1.py` |
| `V1OrganizationsRoles500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_roles500_error1.py` |

### client.role_management.organization_role_post

- **Route**: `POST /v1/organizations/{organizationId}/roles`
- **Auth**: `basic_auth`
- **Signature**: `def organization_role_post(organization_id: UUID, *, body: RoleCreateRequest | RoleCreateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsRolesResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsRolesResponse1, OrganizationRolePostErrorBody]`
- **Error**: `OrganizationRolePostErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsRoles400Error1` [400] · `V1OrganizationsRoles500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RoleCreateRequest` | `open_api_spec_for_click_house_cloud/models/role_create_request.py` |
| `RoleCreateRequestDict` | `open_api_spec_for_click_house_cloud/models/role_create_request.py` |
| `V1OrganizationsRolesResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response1.py` |
| `OrganizationRolePostErrorBody` | `open_api_spec_for_click_house_cloud/errors/organization_role_post_error.py` |
| `V1OrganizationsRoles400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_roles400_error1.py` |
| `V1OrganizationsRoles500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_roles500_error1.py` |

### client.role_management.organization_roles_get_list

- **Route**: `GET /v1/organizations/{organizationId}/roles`
- **Auth**: `basic_auth`
- **Signature**: `def organization_roles_get_list(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId`
- **Returns (parsed)**: `V1OrganizationsRolesResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsRolesResponse, OrganizationRolesGetListErrorBody]`
- **Error**: `OrganizationRolesGetListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsRoles400Error1` [400] · `V1OrganizationsRoles500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsRolesResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_roles_response.py` |
| `OrganizationRolesGetListErrorBody` | `open_api_spec_for_click_house_cloud/errors/organization_roles_get_list_error.py` |
| `V1OrganizationsRoles400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_roles400_error1.py` |
| `V1OrganizationsRoles500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_roles500_error1.py` |

