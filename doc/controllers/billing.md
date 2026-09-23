# Billing

```python
billing_api = client.billing
```

## Class Name

`BillingApi`

## Methods

* [Usage Cost Get](../../doc/controllers/billing.md#usage-cost-get)
* [Active Balances Get](../../doc/controllers/billing.md#active-balances-get)
* [Credit Balances Get](../../doc/controllers/billing.md#credit-balances-get)


# Usage Cost Get

Returns a grand total and a list of daily, per-entity organization usage cost records for the organization in the queried time period (maximum 31 days). All days in both the request and the response are evaluated based on the UTC timezone.

```python
def usage_cost_get(self,
                  organization_id,
                  from_date,
                  to_date,
                  filter=None)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `from_date` | `date` | Query, Required | Start date for the report, e.g. 2024-12-19. |
| `to_date` | `date` | Query, Required | End date (inclusive) for the report, e.g. 2024-12-20. This date cannot be more than 30 days after from_date (for a maximum queried period of 31 days). |
| `filter` | `List[str]` | Query, Optional | Filter criteria to apply when retrieving the usage cost report. Currently, only filtering by resource tags is supported. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsUsageCostResponse`](../../doc/models/v1-organizations-usage-cost-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

from_date = dateutil.parser.parse('2016-03-13').date()

to_date = dateutil.parser.parse('2016-03-13').date()

filter = [
    'tag:Environment=Production',
    'tag:Department=Engineering',
    'tag:isActive'
]

result = billing_api.usage_cost_get(
    organization_id,
    from_date,
    to_date,
    filter=filter
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsUsageCost400ErrorException`](../../doc/models/v1-organizations-usage-cost-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsUsageCost500ErrorException`](../../doc/models/v1-organizations-usage-cost-500-error-exception.md) |


# Active Balances Get

**This endpoint is deprecated.**

DEPRECATED. Use the `/v1/organizations/{organizationId}/creditBalances` endpoint instead. <br /><br /> Returns the active prepaid credit balances for the organization, each with its own balance ID and remaining credits, along with the total remaining credits across all active balances. A balance is active when it has started, has not expired, and has credits remaining. Balances are ordered by expiration date, soonest first, and the returned page is capped at `limit` (default and maximum 100). When `totalCount` exceeds the number of returned balances, page with `limit`/`offset` to retrieve them all. `totalRemainingPrepaidCredits` always covers every active balance, not just the returned page.

```python
def active_balances_get(self,
                       organization_id,
                       limit=100,
                       offset=0)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |
| `limit` | `int` | Query, Optional | Maximum number of results to return.<br><br>**Default**: `100`<br><br>**Constraints**: `>= 1`, `<= 100` |
| `offset` | `int` | Query, Optional | Number of results to skip before returning.<br><br>**Default**: `0`<br><br>**Constraints**: `>= 0` |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsActiveBalancesResponse`](../../doc/models/v1-organizations-active-balances-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

limit = 100

offset = 0

result = billing_api.active_balances_get(
    organization_id,
    limit=limit,
    offset=offset
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsActiveBalances400ErrorException`](../../doc/models/v1-organizations-active-balances-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsActiveBalances500ErrorException`](../../doc/models/v1-organizations-active-balances-500-error-exception.md) |


# Credit Balances Get

**Disclaimer:** This beta endpoint is evolving; the API contract may change. <br /><br /> Returns the active credit balances for the organization, each with its own balance ID, type and remaining credits, along with the total remaining credits across all of them. A balance is active when it has started, has not expired, and has credits remaining. Balances are ordered by expiration date, soonest first. The list is always present and is empty when the organization has no active balances.

```python
def credit_balances_get(self,
                       organization_id)
```

## Authentication

This endpoint requires [basicAuth](../../doc/auth/basic-authentication.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `organization_id` | `uuid\|str` | Template, Required | ID of the requested organization. |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`V1OrganizationsCreditBalancesResponse`](../../doc/models/v1-organizations-credit-balances-response.md).

## Example Usage

```python
organization_id = '000023b8-0000-0000-0000-000000000000'

result = billing_api.credit_balances_get(organization_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be processed due to a client error. Please verify your request parameters and try again. | [`V1OrganizationsCreditBalances400ErrorException`](../../doc/models/v1-organizations-credit-balances-400-error-exception.md) |
| 500 | An internal server error has occurred. If this issue persists, please contact ClickHouse Cloud support for assistance. | [`V1OrganizationsCreditBalances500ErrorException`](../../doc/models/v1-organizations-credit-balances-500-error-exception.md) |

