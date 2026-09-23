<!-- Generated file — do not edit; regenerated with the SDK. -->

# Billing — operations

Accessor: `client.billing` · Source: `open_api_spec_for_click_house_cloud/apis/billing.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.billing.active_balances_get

- **Route**: `GET /v1/organizations/{organizationId}/activeBalances`
- **Auth**: `basic_auth`
- **Signature**: `def active_balances_get(organization_id: UUID, *, limit: int | None = 100, offset: int | None = 0, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId` · `limit` — query · `offset` — query
- **Returns (parsed)**: `V1OrganizationsActiveBalancesResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsActiveBalancesResponse, ActiveBalancesGetErrorBody]`
- **Error**: `ActiveBalancesGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsActiveBalances400Error1` [400] · `V1OrganizationsActiveBalances500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsActiveBalancesResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_active_balances_response.py` |
| `ActiveBalancesGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/active_balances_get_error.py` |
| `V1OrganizationsActiveBalances400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_active_balances400_error1.py` |
| `V1OrganizationsActiveBalances500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_active_balances500_error1.py` |

### client.billing.credit_balances_get

- **Route**: `GET /v1/organizations/{organizationId}/creditBalances`
- **Auth**: `basic_auth`
- **Signature**: `def credit_balances_get(organization_id: UUID, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`
- **Params**: `organization_id` — path `organizationId`
- **Returns (parsed)**: `V1OrganizationsCreditBalancesResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsCreditBalancesResponse, CreditBalancesGetErrorBody]`
- **Error**: `CreditBalancesGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsCreditBalances400Error1` [400] · `V1OrganizationsCreditBalances500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsCreditBalancesResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_credit_balances_response.py` |
| `CreditBalancesGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/credit_balances_get_error.py` |
| `V1OrganizationsCreditBalances400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_credit_balances400_error1.py` |
| `V1OrganizationsCreditBalances500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_credit_balances500_error1.py` |

### client.billing.usage_cost_get

- **Route**: `GET /v1/organizations/{organizationId}/usageCost`
- **Auth**: `basic_auth`
- **Signature**: `def usage_cost_get(organization_id: UUID, from_date: Date, to_date: Date, *, filter: list[str] | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `organization_id`, `from_date`, `to_date`
- **Params**: `organization_id` — path `organizationId` · `from_date` — query · `to_date` — query · `filter` — query
- **Returns (parsed)**: `V1OrganizationsUsageCostResponse`
- **Returns (raw)**: `ApiResult[V1OrganizationsUsageCostResponse, UsageCostGetErrorBody]`
- **Error**: `UsageCostGetErrorBody` — **Case A (typed)**
- **Error arms**: `V1OrganizationsUsageCost400Error1` [400] · `V1OrganizationsUsageCost500Error1` [500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1OrganizationsUsageCostResponse` | `open_api_spec_for_click_house_cloud/models/v1_organizations_usage_cost_response.py` |
| `UsageCostGetErrorBody` | `open_api_spec_for_click_house_cloud/errors/usage_cost_get_error.py` |
| `V1OrganizationsUsageCost400Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_usage_cost400_error1.py` |
| `V1OrganizationsUsageCost500Error1` | `open_api_spec_for_click_house_cloud/models/v1_organizations_usage_cost500_error1.py` |

