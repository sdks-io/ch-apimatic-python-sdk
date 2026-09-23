<!-- Generated file — do not edit; regenerated with the SDK. -->

# ClickStack — operations

Accessor: `client.click_stack` · Source: `open_api_spec_for_click_house_cloud/apis/click_stack.py` · 30 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.click_stack.click_stack_create_alert

- **Route**: `POST /v1/organizations/{organizationId}/services/{serviceId}/clickstack/alerts`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_create_alert(organization_id: UUID, service_id: UUID, *, body: ClickStackCreateAlertRequest | ClickStackCreateAlertRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickstackAlertsResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackAlertsResponse1, ClickStackCreateAlertErrorBody]`
- **Error**: `ClickStackCreateAlertErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackAlerts400Error1` [400] · `V1OrganizationsServicesClickstackAlerts500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickStackCreateAlertRequest` | `open_api_spec_for_click_house_cloud/models/click_stack_create_alert_request.py` |
| `ClickStackCreateAlertRequestDict` | `open_api_spec_for_click_house_cloud/models/click_stack_create_alert_request.py` |
| `V1OrganizationsServicesClickstackAlertsResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_response1.py` |
| `ClickStackCreateAlertErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_create_alert_error.py` |
| `V1OrganizationsServicesClickstackAlerts400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts400_error1.py` |
| `V1OrganizationsServicesClickstackAlerts500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts500_error1.py` |

### client.click_stack.click_stack_create_dashboard

- **Route**: `POST /v1/organizations/{organizationId}/services/{serviceId}/clickstack/dashboards`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_create_dashboard(organization_id: UUID, service_id: UUID, *, body: ClickStackCreateDashboardRequest | ClickStackCreateDashboardRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickstackDashboardsResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackDashboardsResponse1, ClickStackCreateDashboardErrorBody]`
- **Error**: `ClickStackCreateDashboardErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackDashboards400Error1` [400] · `V1OrganizationsServicesClickstackDashboards500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickStackCreateDashboardRequest` | `open_api_spec_for_click_house_cloud/models/click_stack_create_dashboard_request.py` |
| `ClickStackCreateDashboardRequestDict` | `open_api_spec_for_click_house_cloud/models/click_stack_create_dashboard_request.py` |
| `V1OrganizationsServicesClickstackDashboardsResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_response1.py` |
| `ClickStackCreateDashboardErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_create_dashboard_error.py` |
| `V1OrganizationsServicesClickstackDashboards400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards400_error1.py` |
| `V1OrganizationsServicesClickstackDashboards500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards500_error1.py` |

### client.click_stack.click_stack_create_role

- **Route**: `POST /v1/organizations/{organizationId}/services/{serviceId}/clickstack/roles`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_create_role(organization_id: UUID, service_id: UUID, *, body: ClickStackCreateRoleRequest | ClickStackCreateRoleRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickstackRolesResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackRolesResponse1, ClickStackCreateRoleErrorBody]`
- **Error**: `ClickStackCreateRoleErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackRoles400Error1` [400] · `V1OrganizationsServicesClickstackRoles500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickStackCreateRoleRequest` | `open_api_spec_for_click_house_cloud/models/click_stack_create_role_request.py` |
| `ClickStackCreateRoleRequestDict` | `open_api_spec_for_click_house_cloud/models/click_stack_create_role_request.py` |
| `V1OrganizationsServicesClickstackRolesResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_response1.py` |
| `ClickStackCreateRoleErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_create_role_error.py` |
| `V1OrganizationsServicesClickstackRoles400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles400_error1.py` |
| `V1OrganizationsServicesClickstackRoles500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles500_error1.py` |

### client.click_stack.click_stack_create_saved_search

- **Route**: `POST /v1/organizations/{organizationId}/services/{serviceId}/clickstack/saved-searches`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_create_saved_search(organization_id: UUID, service_id: UUID, *, body: ClickStackSavedSearchInput | ClickStackSavedSearchInputDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickstackSavedSearchesResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackSavedSearchesResponse1, ClickStackCreateSavedSearchErrorBody]`
- **Error**: `ClickStackCreateSavedSearchErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackSavedSearches400Error1` [400] · `V1OrganizationsServicesClickstackSavedSearches500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickStackSavedSearchInput` | `open_api_spec_for_click_house_cloud/models/click_stack_saved_search_input.py` |
| `ClickStackSavedSearchInputDict` | `open_api_spec_for_click_house_cloud/models/click_stack_saved_search_input.py` |
| `V1OrganizationsServicesClickstackSavedSearchesResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_response1.py` |
| `ClickStackCreateSavedSearchErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_create_saved_search_error.py` |
| `V1OrganizationsServicesClickstackSavedSearches400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches400_error1.py` |
| `V1OrganizationsServicesClickstackSavedSearches500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches500_error1.py` |

### client.click_stack.click_stack_create_source

- **Route**: `POST /v1/organizations/{organizationId}/services/{serviceId}/clickstack/sources`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_create_source(organization_id: UUID, service_id: UUID, *, body: ClickStackSource | ClickStackSourceDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickstackSourcesResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackSourcesResponse1, ClickStackCreateSourceErrorBody]`
- **Error**: `ClickStackCreateSourceErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackSources400Error1` [400] · `V1OrganizationsServicesClickstackSources500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickStackSource` | `open_api_spec_for_click_house_cloud/models/unions/click_stack_source.py` |
| `ClickStackSourceDict` | `open_api_spec_for_click_house_cloud/models/unions/click_stack_source.py` |
| `V1OrganizationsServicesClickstackSourcesResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_response1.py` |
| `ClickStackCreateSourceErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_create_source_error.py` |
| `V1OrganizationsServicesClickstackSources400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources400_error1.py` |
| `V1OrganizationsServicesClickstackSources500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources500_error1.py` |

### client.click_stack.click_stack_create_webhook

- **Route**: `POST /v1/organizations/{organizationId}/services/{serviceId}/clickstack/webhooks`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_create_webhook(organization_id: UUID, service_id: UUID, *, body: ClickStackWebhookInput | ClickStackWebhookInputDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickstackWebhooksResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackWebhooksResponse1, ClickStackCreateWebhookErrorBody]`
- **Error**: `ClickStackCreateWebhookErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackWebhooks400Error1` [400] · `V1OrganizationsServicesClickstackWebhooks500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickStackWebhookInput` | `open_api_spec_for_click_house_cloud/models/click_stack_webhook_input.py` |
| `ClickStackWebhookInputDict` | `open_api_spec_for_click_house_cloud/models/click_stack_webhook_input.py` |
| `V1OrganizationsServicesClickstackWebhooksResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_response1.py` |
| `ClickStackCreateWebhookErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_create_webhook_error.py` |
| `V1OrganizationsServicesClickstackWebhooks400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks400_error1.py` |
| `V1OrganizationsServicesClickstackWebhooks500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks500_error1.py` |

### client.click_stack.click_stack_delete_alert

- **Route**: `DELETE /v1/organizations/{organizationId}/services/{serviceId}/clickstack/alerts/{clickStackAlertId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_delete_alert(organization_id: UUID, service_id: UUID, click_stack_alert_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_stack_alert_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_stack_alert_id` — path `clickStackAlertId`
- **Returns (parsed)**: `V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2, ClickStackDeleteAlertErrorBody]`
- **Error**: `ClickStackDeleteAlertErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackAlertsClickStackAlertId400Error1` [400] · `V1OrganizationsServicesClickstackAlertsClickStackAlertId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse2` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id_response2.py` |
| `ClickStackDeleteAlertErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_delete_alert_error.py` |
| `V1OrganizationsServicesClickstackAlertsClickStackAlertId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id400_error1.py` |
| `V1OrganizationsServicesClickstackAlertsClickStackAlertId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id500_error1.py` |

### client.click_stack.click_stack_delete_dashboard

- **Route**: `DELETE /v1/organizations/{organizationId}/services/{serviceId}/clickstack/dashboards/{clickStackDashboardId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_delete_dashboard(organization_id: UUID, service_id: UUID, click_stack_dashboard_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_stack_dashboard_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_stack_dashboard_id` — path `clickStackDashboardId`
- **Returns (parsed)**: `V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2, ClickStackDeleteDashboardErrorBody]`
- **Error**: `ClickStackDeleteDashboardErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400Error1` [400] · `V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse2` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id_response2.py` |
| `ClickStackDeleteDashboardErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_delete_dashboard_error.py` |
| `V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id400_error1.py` |
| `V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id500_error1.py` |

### client.click_stack.click_stack_delete_role

- **Route**: `DELETE /v1/organizations/{organizationId}/services/{serviceId}/clickstack/roles/{clickStackRoleId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_delete_role(organization_id: UUID, service_id: UUID, click_stack_role_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_stack_role_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_stack_role_id` — path `clickStackRoleId`
- **Returns (parsed)**: `V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2, ClickStackDeleteRoleErrorBody]`
- **Error**: `ClickStackDeleteRoleErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackRolesClickStackRoleId400Error1` [400] · `V1OrganizationsServicesClickstackRolesClickStackRoleId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse2` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id_response2.py` |
| `ClickStackDeleteRoleErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_delete_role_error.py` |
| `V1OrganizationsServicesClickstackRolesClickStackRoleId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id400_error1.py` |
| `V1OrganizationsServicesClickstackRolesClickStackRoleId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id500_error1.py` |

### client.click_stack.click_stack_delete_saved_search

- **Route**: `DELETE /v1/organizations/{organizationId}/services/{serviceId}/clickstack/saved-searches/{clickStackSavedSearchId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_delete_saved_search(organization_id: UUID, service_id: UUID, click_stack_saved_search_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_stack_saved_search_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_stack_saved_search_id` — path `clickStackSavedSearchId`
- **Returns (parsed)**: `V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2, ClickStackDeleteSavedSearchErrorBody]`
- **Error**: `ClickStackDeleteSavedSearchErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400Error1` [400] · `V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse2` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id_response2.py` |
| `ClickStackDeleteSavedSearchErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_delete_saved_search_error.py` |
| `V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id400_error1.py` |
| `V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id500_error1.py` |

### client.click_stack.click_stack_delete_source

- **Route**: `DELETE /v1/organizations/{organizationId}/services/{serviceId}/clickstack/sources/{clickStackSourceId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_delete_source(organization_id: UUID, service_id: UUID, click_stack_source_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_stack_source_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_stack_source_id` — path `clickStackSourceId`
- **Returns (parsed)**: `V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2, ClickStackDeleteSourceErrorBody]`
- **Error**: `ClickStackDeleteSourceErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackSourcesClickStackSourceId400Error1` [400] · `V1OrganizationsServicesClickstackSourcesClickStackSourceId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse2` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id_response2.py` |
| `ClickStackDeleteSourceErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_delete_source_error.py` |
| `V1OrganizationsServicesClickstackSourcesClickStackSourceId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id400_error1.py` |
| `V1OrganizationsServicesClickstackSourcesClickStackSourceId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id500_error1.py` |

### client.click_stack.click_stack_delete_webhook

- **Route**: `DELETE /v1/organizations/{organizationId}/services/{serviceId}/clickstack/webhooks/{clickStackWebhookId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_delete_webhook(organization_id: UUID, service_id: UUID, click_stack_webhook_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_stack_webhook_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_stack_webhook_id` — path `clickStackWebhookId`
- **Returns (parsed)**: `V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1, ClickStackDeleteWebhookErrorBody]`
- **Error**: `ClickStackDeleteWebhookErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackWebhooksClickStackWebhookId400Error1` [400] · `V1OrganizationsServicesClickstackWebhooksClickStackWebhookId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_click_stack_webhook_id_response1.py` |
| `ClickStackDeleteWebhookErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_delete_webhook_error.py` |
| `V1OrganizationsServicesClickstackWebhooksClickStackWebhookId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_click_stack_webhook_id400_error1.py` |
| `V1OrganizationsServicesClickstackWebhooksClickStackWebhookId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_click_stack_webhook_id500_error1.py` |

### client.click_stack.click_stack_get_alert

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickstack/alerts/{clickStackAlertId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_get_alert(organization_id: UUID, service_id: UUID, click_stack_alert_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_stack_alert_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_stack_alert_id` — path `clickStackAlertId`
- **Returns (parsed)**: `V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse, ClickStackGetAlertErrorBody]`
- **Error**: `ClickStackGetAlertErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackAlertsClickStackAlertId400Error1` [400] · `V1OrganizationsServicesClickstackAlertsClickStackAlertId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id_response.py` |
| `ClickStackGetAlertErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_get_alert_error.py` |
| `V1OrganizationsServicesClickstackAlertsClickStackAlertId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id400_error1.py` |
| `V1OrganizationsServicesClickstackAlertsClickStackAlertId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id500_error1.py` |

### client.click_stack.click_stack_get_dashboard

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickstack/dashboards/{clickStackDashboardId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_get_dashboard(organization_id: UUID, service_id: UUID, click_stack_dashboard_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_stack_dashboard_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_stack_dashboard_id` — path `clickStackDashboardId`
- **Returns (parsed)**: `V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse, ClickStackGetDashboardErrorBody]`
- **Error**: `ClickStackGetDashboardErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400Error1` [400] · `V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id_response.py` |
| `ClickStackGetDashboardErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_get_dashboard_error.py` |
| `V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id400_error1.py` |
| `V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id500_error1.py` |

### client.click_stack.click_stack_get_role

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickstack/roles/{clickStackRoleId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_get_role(organization_id: UUID, service_id: UUID, click_stack_role_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_stack_role_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_stack_role_id` — path `clickStackRoleId`
- **Returns (parsed)**: `V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse, ClickStackGetRoleErrorBody]`
- **Error**: `ClickStackGetRoleErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackRolesClickStackRoleId400Error1` [400] · `V1OrganizationsServicesClickstackRolesClickStackRoleId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id_response.py` |
| `ClickStackGetRoleErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_get_role_error.py` |
| `V1OrganizationsServicesClickstackRolesClickStackRoleId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id400_error1.py` |
| `V1OrganizationsServicesClickstackRolesClickStackRoleId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id500_error1.py` |

### client.click_stack.click_stack_get_saved_search

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickstack/saved-searches/{clickStackSavedSearchId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_get_saved_search(organization_id: UUID, service_id: UUID, click_stack_saved_search_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_stack_saved_search_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_stack_saved_search_id` — path `clickStackSavedSearchId`
- **Returns (parsed)**: `V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse, ClickStackGetSavedSearchErrorBody]`
- **Error**: `ClickStackGetSavedSearchErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400Error1` [400] · `V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id_response.py` |
| `ClickStackGetSavedSearchErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_get_saved_search_error.py` |
| `V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id400_error1.py` |
| `V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id500_error1.py` |

### client.click_stack.click_stack_get_source

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickstack/sources/{clickStackSourceId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_get_source(organization_id: UUID, service_id: UUID, click_stack_source_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_stack_source_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_stack_source_id` — path `clickStackSourceId`
- **Returns (parsed)**: `V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse, ClickStackGetSourceErrorBody]`
- **Error**: `ClickStackGetSourceErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackSourcesClickStackSourceId400Error1` [400] · `V1OrganizationsServicesClickstackSourcesClickStackSourceId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id_response.py` |
| `ClickStackGetSourceErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_get_source_error.py` |
| `V1OrganizationsServicesClickstackSourcesClickStackSourceId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id400_error1.py` |
| `V1OrganizationsServicesClickstackSourcesClickStackSourceId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id500_error1.py` |

### client.click_stack.click_stack_list_alerts

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickstack/alerts`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_list_alerts(organization_id: UUID, service_id: UUID, *, limit: int | None = 1000, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `limit` — query · `offset` — query
- **Returns (parsed)**: `V1OrganizationsServicesClickstackAlertsResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackAlertsResponse, ClickStackListAlertsErrorBody]`
- **Error**: `ClickStackListAlertsErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackAlerts400Error1` [400] · `V1OrganizationsServicesClickstackAlerts500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickstackAlertsResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_response.py` |
| `ClickStackListAlertsErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_list_alerts_error.py` |
| `V1OrganizationsServicesClickstackAlerts400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts400_error1.py` |
| `V1OrganizationsServicesClickstackAlerts500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts500_error1.py` |

### client.click_stack.click_stack_list_dashboards

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickstack/dashboards`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_list_dashboards(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesClickstackDashboardsResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackDashboardsResponse, ClickStackListDashboardsErrorBody]`
- **Error**: `ClickStackListDashboardsErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackDashboards400Error1` [400] · `V1OrganizationsServicesClickstackDashboards500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickstackDashboardsResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_response.py` |
| `ClickStackListDashboardsErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_list_dashboards_error.py` |
| `V1OrganizationsServicesClickstackDashboards400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards400_error1.py` |
| `V1OrganizationsServicesClickstackDashboards500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards500_error1.py` |

### client.click_stack.click_stack_list_roles

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickstack/roles`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_list_roles(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesClickstackRolesResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackRolesResponse, ClickStackListRolesErrorBody]`
- **Error**: `ClickStackListRolesErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackRoles400Error1` [400] · `V1OrganizationsServicesClickstackRoles500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickstackRolesResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_response.py` |
| `ClickStackListRolesErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_list_roles_error.py` |
| `V1OrganizationsServicesClickstackRoles400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles400_error1.py` |
| `V1OrganizationsServicesClickstackRoles500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles500_error1.py` |

### client.click_stack.click_stack_list_saved_searches

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickstack/saved-searches`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_list_saved_searches(organization_id: UUID, service_id: UUID, *, limit: int | None = 1000, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `limit` — query · `offset` — query
- **Returns (parsed)**: `V1OrganizationsServicesClickstackSavedSearchesResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackSavedSearchesResponse, ClickStackListSavedSearchesErrorBody]`
- **Error**: `ClickStackListSavedSearchesErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackSavedSearches400Error1` [400] · `V1OrganizationsServicesClickstackSavedSearches500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickstackSavedSearchesResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_response.py` |
| `ClickStackListSavedSearchesErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_list_saved_searches_error.py` |
| `V1OrganizationsServicesClickstackSavedSearches400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches400_error1.py` |
| `V1OrganizationsServicesClickstackSavedSearches500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches500_error1.py` |

### client.click_stack.click_stack_list_sources

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickstack/sources`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_list_sources(organization_id: UUID, service_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId`
- **Returns (parsed)**: `V1OrganizationsServicesClickstackSourcesResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackSourcesResponse, ClickStackListSourcesErrorBody]`
- **Error**: `ClickStackListSourcesErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackSources400Error1` [400] · `V1OrganizationsServicesClickstackSources500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickstackSourcesResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_response.py` |
| `ClickStackListSourcesErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_list_sources_error.py` |
| `V1OrganizationsServicesClickstackSources400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources400_error1.py` |
| `V1OrganizationsServicesClickstackSources500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources500_error1.py` |

### client.click_stack.click_stack_list_webhooks

- **Route**: `GET /v1/organizations/{organizationId}/services/{serviceId}/clickstack/webhooks`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_list_webhooks(organization_id: UUID, service_id: UUID, *, limit: int | None = 1000, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `limit` — query · `offset` — query
- **Returns (parsed)**: `V1OrganizationsServicesClickstackWebhooksResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackWebhooksResponse, ClickStackListWebhooksErrorBody]`
- **Error**: `ClickStackListWebhooksErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackWebhooks400Error1` [400] · `V1OrganizationsServicesClickstackWebhooks500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsServicesClickstackWebhooksResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_response.py` |
| `ClickStackListWebhooksErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_list_webhooks_error.py` |
| `V1OrganizationsServicesClickstackWebhooks400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks400_error1.py` |
| `V1OrganizationsServicesClickstackWebhooks500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks500_error1.py` |

### client.click_stack.click_stack_update_alert

- **Route**: `PUT /v1/organizations/{organizationId}/services/{serviceId}/clickstack/alerts/{clickStackAlertId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_update_alert(organization_id: UUID, service_id: UUID, click_stack_alert_id: str, *, body: ClickStackUpdateAlertRequest | ClickStackUpdateAlertRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_stack_alert_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_stack_alert_id` — path `clickStackAlertId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse, ClickStackUpdateAlertErrorBody]`
- **Error**: `ClickStackUpdateAlertErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackAlertsClickStackAlertId400Error1` [400] · `V1OrganizationsServicesClickstackAlertsClickStackAlertId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickStackUpdateAlertRequest` | `open_api_spec_for_click_house_cloud/models/click_stack_update_alert_request.py` |
| `ClickStackUpdateAlertRequestDict` | `open_api_spec_for_click_house_cloud/models/click_stack_update_alert_request.py` |
| `V1OrganizationsServicesClickstackAlertsClickStackAlertIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id_response.py` |
| `ClickStackUpdateAlertErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_update_alert_error.py` |
| `V1OrganizationsServicesClickstackAlertsClickStackAlertId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id400_error1.py` |
| `V1OrganizationsServicesClickstackAlertsClickStackAlertId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_alerts_click_stack_alert_id500_error1.py` |

### client.click_stack.click_stack_update_dashboard

- **Route**: `PUT /v1/organizations/{organizationId}/services/{serviceId}/clickstack/dashboards/{clickStackDashboardId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_update_dashboard(organization_id: UUID, service_id: UUID, click_stack_dashboard_id: str, *, body: ClickStackUpdateDashboardRequest | ClickStackUpdateDashboardRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_stack_dashboard_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_stack_dashboard_id` — path `clickStackDashboardId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse, ClickStackUpdateDashboardErrorBody]`
- **Error**: `ClickStackUpdateDashboardErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400Error1` [400] · `V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickStackUpdateDashboardRequest` | `open_api_spec_for_click_house_cloud/models/click_stack_update_dashboard_request.py` |
| `ClickStackUpdateDashboardRequestDict` | `open_api_spec_for_click_house_cloud/models/click_stack_update_dashboard_request.py` |
| `V1OrganizationsServicesClickstackDashboardsClickStackDashboardIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id_response.py` |
| `ClickStackUpdateDashboardErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_update_dashboard_error.py` |
| `V1OrganizationsServicesClickstackDashboardsClickStackDashboardId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id400_error1.py` |
| `V1OrganizationsServicesClickstackDashboardsClickStackDashboardId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_click_stack_dashboard_id500_error1.py` |

### client.click_stack.click_stack_update_role

- **Route**: `PUT /v1/organizations/{organizationId}/services/{serviceId}/clickstack/roles/{clickStackRoleId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_update_role(organization_id: UUID, service_id: UUID, click_stack_role_id: str, *, body: ClickStackUpdateRoleRequest | ClickStackUpdateRoleRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_stack_role_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_stack_role_id` — path `clickStackRoleId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse, ClickStackUpdateRoleErrorBody]`
- **Error**: `ClickStackUpdateRoleErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackRolesClickStackRoleId400Error1` [400] · `V1OrganizationsServicesClickstackRolesClickStackRoleId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickStackUpdateRoleRequest` | `open_api_spec_for_click_house_cloud/models/click_stack_update_role_request.py` |
| `ClickStackUpdateRoleRequestDict` | `open_api_spec_for_click_house_cloud/models/click_stack_update_role_request.py` |
| `V1OrganizationsServicesClickstackRolesClickStackRoleIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id_response.py` |
| `ClickStackUpdateRoleErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_update_role_error.py` |
| `V1OrganizationsServicesClickstackRolesClickStackRoleId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id400_error1.py` |
| `V1OrganizationsServicesClickstackRolesClickStackRoleId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_roles_click_stack_role_id500_error1.py` |

### client.click_stack.click_stack_update_saved_search

- **Route**: `PUT /v1/organizations/{organizationId}/services/{serviceId}/clickstack/saved-searches/{clickStackSavedSearchId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_update_saved_search(organization_id: UUID, service_id: UUID, click_stack_saved_search_id: str, *, body: ClickStackSavedSearchInput | ClickStackSavedSearchInputDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_stack_saved_search_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_stack_saved_search_id` — path `clickStackSavedSearchId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse, ClickStackUpdateSavedSearchErrorBody]`
- **Error**: `ClickStackUpdateSavedSearchErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400Error1` [400] · `V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickStackSavedSearchInput` | `open_api_spec_for_click_house_cloud/models/click_stack_saved_search_input.py` |
| `ClickStackSavedSearchInputDict` | `open_api_spec_for_click_house_cloud/models/click_stack_saved_search_input.py` |
| `V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id_response.py` |
| `ClickStackUpdateSavedSearchErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_update_saved_search_error.py` |
| `V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id400_error1.py` |
| `V1OrganizationsServicesClickstackSavedSearchesClickStackSavedSearchId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_saved_searches_click_stack_saved_search_id500_error1.py` |

### client.click_stack.click_stack_update_source

- **Route**: `PUT /v1/organizations/{organizationId}/services/{serviceId}/clickstack/sources/{clickStackSourceId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_update_source(organization_id: UUID, service_id: UUID, click_stack_source_id: str, *, body: ClickStackSource | ClickStackSourceDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_stack_source_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_stack_source_id` — path `clickStackSourceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse, ClickStackUpdateSourceErrorBody]`
- **Error**: `ClickStackUpdateSourceErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackSourcesClickStackSourceId400Error1` [400] · `V1OrganizationsServicesClickstackSourcesClickStackSourceId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickStackSource` | `open_api_spec_for_click_house_cloud/models/unions/click_stack_source.py` |
| `ClickStackSourceDict` | `open_api_spec_for_click_house_cloud/models/unions/click_stack_source.py` |
| `V1OrganizationsServicesClickstackSourcesClickStackSourceIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id_response.py` |
| `ClickStackUpdateSourceErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_update_source_error.py` |
| `V1OrganizationsServicesClickstackSourcesClickStackSourceId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id400_error1.py` |
| `V1OrganizationsServicesClickstackSourcesClickStackSourceId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_sources_click_stack_source_id500_error1.py` |

### client.click_stack.click_stack_update_webhook

- **Route**: `PUT /v1/organizations/{organizationId}/services/{serviceId}/clickstack/webhooks/{clickStackWebhookId}`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_update_webhook(organization_id: UUID, service_id: UUID, click_stack_webhook_id: str, *, body: ClickStackWebhookInput | ClickStackWebhookInputDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`, `click_stack_webhook_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `click_stack_webhook_id` — path `clickStackWebhookId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse, ClickStackUpdateWebhookErrorBody]`
- **Error**: `ClickStackUpdateWebhookErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackWebhooksClickStackWebhookId400Error1` [400] · `V1OrganizationsServicesClickstackWebhooksClickStackWebhookId500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickStackWebhookInput` | `open_api_spec_for_click_house_cloud/models/click_stack_webhook_input.py` |
| `ClickStackWebhookInputDict` | `open_api_spec_for_click_house_cloud/models/click_stack_webhook_input.py` |
| `V1OrganizationsServicesClickstackWebhooksClickStackWebhookIdResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_click_stack_webhook_id_response.py` |
| `ClickStackUpdateWebhookErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_update_webhook_error.py` |
| `V1OrganizationsServicesClickstackWebhooksClickStackWebhookId400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_click_stack_webhook_id400_error1.py` |
| `V1OrganizationsServicesClickstackWebhooksClickStackWebhookId500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_webhooks_click_stack_webhook_id500_error1.py` |

### client.click_stack.click_stack_validate_dashboard

- **Route**: `POST /v1/organizations/{organizationId}/services/{serviceId}/clickstack/dashboards/validate`
- **Auth**: `basic_auth`
- **Signature**: `def click_stack_validate_dashboard(organization_id: UUID, service_id: UUID, *, body: ClickStackCreateDashboardRequest | ClickStackCreateDashboardRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `service_id`
- **Params**: `organization_id` — path `organizationId` · `service_id` — path `serviceId` · `body` — JSON body
- **Returns (parsed)**: `V1OrganizationsServicesClickstackDashboardsValidateResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsServicesClickstackDashboardsValidateResponse, ClickStackValidateDashboardErrorBody]`
- **Error**: `ClickStackValidateDashboardErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsServicesClickstackDashboardsValidate400Error1` [400] · `V1OrganizationsServicesClickstackDashboardsValidate500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClickStackCreateDashboardRequest` | `open_api_spec_for_click_house_cloud/models/click_stack_create_dashboard_request.py` |
| `ClickStackCreateDashboardRequestDict` | `open_api_spec_for_click_house_cloud/models/click_stack_create_dashboard_request.py` |
| `V1OrganizationsServicesClickstackDashboardsValidateResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_validate_response.py` |
| `ClickStackValidateDashboardErrorBody` | `open_api_spec_for_click_house_cloud/errors/click_stack_validate_dashboard_error.py` |
| `V1OrganizationsServicesClickstackDashboardsValidate400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_validate400_error1.py` |
| `V1OrganizationsServicesClickstackDashboardsValidate500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_services_clickstack_dashboards_validate500_error1.py` |

