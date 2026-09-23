<!-- Generated file — do not edit; regenerated with the SDK. -->

# UserManagement — operations

Accessor: `client.user_management` · Source: `open_api_spec_for_click_house_cloud/apis/user_management.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.user_management.invitation_create

- **Route**: `POST /v1/organizations/{organizationId}/invitations`
- **Auth**: `basic_auth`
- **Signature**: `def invitation_create(organization_id: UUID, *, body: InvitationPostRequest | InvitationPostRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsInvitationsResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsInvitationsResponse1, InvitationCreateErrorBody]`
- **Error**: `InvitationCreateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsInvitations400Error1` [400] · `V1OrganizationsInvitations500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `InvitationPostRequest` | `open_api_spec_for_click_house_cloud/models/invitation_post_request.py` |
| `InvitationPostRequestDict` | `open_api_spec_for_click_house_cloud/models/invitation_post_request.py` |
| `V1OrganizationsInvitationsResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_invitations_response1.py` |
| `InvitationCreateErrorBody` | `open_api_spec_for_click_house_cloud/errors/invitation_create_error.py` |
| `V1OrganizationsInvitations400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_invitations400_error1.py` |
| `V1OrganizationsInvitations500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_invitations500_error1.py` |

### client.user_management.invitation_delete

- **Route**: `DELETE /v1/organizations/{organizationId}/invitations/{invitationId}`
- **Auth**: `basic_auth`
- **Signature**: `def invitation_delete(organization_id: UUID, invitation_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `invitation_id`
- **Params**: `organization_id` — path `organizationId` · `invitation_id` — path `invitationId`
- **Returns (parsed)**: `V1OrganizationsInvitationsResponse3`
- **Returns (raw)**: `ApiResult[V1OrganizationsInvitationsResponse3, InvitationDeleteErrorBody]`
- **Error**: `InvitationDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsInvitations400Error1` [400] · `V1OrganizationsInvitations500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsInvitationsResponse3` | `open_api_spec_for_click_house_cloud/models/v1_organizations_invitations_response3.py` |
| `InvitationDeleteErrorBody` | `open_api_spec_for_click_house_cloud/errors/invitation_delete_error.py` |
| `V1OrganizationsInvitations400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_invitations400_error1.py` |
| `V1OrganizationsInvitations500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_invitations500_error1.py` |

### client.user_management.invitation_get

- **Route**: `GET /v1/organizations/{organizationId}/invitations/{invitationId}`
- **Auth**: `basic_auth`
- **Signature**: `def invitation_get(organization_id: UUID, invitation_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `invitation_id`
- **Params**: `organization_id` — path `organizationId` · `invitation_id` — path `invitationId`
- **Returns (parsed)**: `V1OrganizationsInvitationsResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsInvitationsResponse1, InvitationGetErrorBody]`
- **Error**: `InvitationGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsInvitations400Error1` [400] · `V1OrganizationsInvitations500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsInvitationsResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_invitations_response1.py` |
| `InvitationGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/invitation_get_error.py` |
| `V1OrganizationsInvitations400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_invitations400_error1.py` |
| `V1OrganizationsInvitations500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_invitations500_error1.py` |

### client.user_management.invitation_get_list

- **Route**: `GET /v1/organizations/{organizationId}/invitations`
- **Auth**: `basic_auth`
- **Signature**: `def invitation_get_list(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId`
- **Returns (parsed)**: `V1OrganizationsInvitationsResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsInvitationsResponse, InvitationGetListErrorBody]`
- **Error**: `InvitationGetListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsInvitations400Error1` [400] · `V1OrganizationsInvitations500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsInvitationsResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_invitations_response.py` |
| `InvitationGetListErrorBody` | `open_api_spec_for_click_house_cloud/errors/invitation_get_list_error.py` |
| `V1OrganizationsInvitations400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_invitations400_error1.py` |
| `V1OrganizationsInvitations500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_invitations500_error1.py` |

### client.user_management.member_delete

- **Route**: `DELETE /v1/organizations/{organizationId}/members/{userId}`
- **Auth**: `basic_auth`
- **Signature**: `def member_delete(organization_id: UUID, user_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `user_id`
- **Params**: `organization_id` — path `organizationId` · `user_id` — path `userId`
- **Returns (parsed)**: `V1OrganizationsMembersResponse3`
- **Returns (raw)**: `ApiResult[V1OrganizationsMembersResponse3, MemberDeleteErrorBody]`
- **Error**: `MemberDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsMembers400Error1` [400] · `V1OrganizationsMembers500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsMembersResponse3` | `open_api_spec_for_click_house_cloud/models/v1_organizations_members_response3.py` |
| `MemberDeleteErrorBody` | `open_api_spec_for_click_house_cloud/errors/member_delete_error.py` |
| `V1OrganizationsMembers400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_members400_error1.py` |
| `V1OrganizationsMembers500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_members500_error1.py` |

### client.user_management.member_get

- **Route**: `GET /v1/organizations/{organizationId}/members/{userId}`
- **Auth**: `basic_auth`
- **Signature**: `def member_get(organization_id: UUID, user_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `user_id`
- **Params**: `organization_id` — path `organizationId` · `user_id` — path `userId`
- **Returns (parsed)**: `V1OrganizationsMembersResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsMembersResponse1, MemberGetErrorBody]`
- **Error**: `MemberGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsMembers400Error1` [400] · `V1OrganizationsMembers500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsMembersResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_members_response1.py` |
| `MemberGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/member_get_error.py` |
| `V1OrganizationsMembers400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_members400_error1.py` |
| `V1OrganizationsMembers500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_members500_error1.py` |

### client.user_management.member_get_list

- **Route**: `GET /v1/organizations/{organizationId}/members`
- **Auth**: `basic_auth`
- **Signature**: `def member_get_list(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId`
- **Returns (parsed)**: `V1OrganizationsMembersResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsMembersResponse, MemberGetListErrorBody]`
- **Error**: `MemberGetListErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsMembers400Error1` [400] · `V1OrganizationsMembers500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsMembersResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_members_response.py` |
| `MemberGetListErrorBody` | `open_api_spec_for_click_house_cloud/errors/member_get_list_error.py` |
| `V1OrganizationsMembers400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_members400_error1.py` |
| `V1OrganizationsMembers500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_members500_error1.py` |

### client.user_management.member_update

- **Route**: `PATCH /v1/organizations/{organizationId}/members/{userId}`
- **Auth**: `basic_auth`
- **Signature**: `def member_update(organization_id: UUID, user_id: UUID, *, body: MemberPatchRequest | MemberPatchRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `user_id`
- **Params**: `organization_id` — path `organizationId` · `user_id` — path `userId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsMembersResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsMembersResponse1, MemberUpdateErrorBody]`
- **Error**: `MemberUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsMembers400Error1` [400] · `V1OrganizationsMembers500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MemberPatchRequest` | `open_api_spec_for_click_house_cloud/models/member_patch_request.py` |
| `MemberPatchRequestDict` | `open_api_spec_for_click_house_cloud/models/member_patch_request.py` |
| `V1OrganizationsMembersResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_members_response1.py` |
| `MemberUpdateErrorBody` | `open_api_spec_for_click_house_cloud/errors/member_update_error.py` |
| `V1OrganizationsMembers400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_members400_error1.py` |
| `V1OrganizationsMembers500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_members500_error1.py` |

