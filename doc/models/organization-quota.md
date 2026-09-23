
# Organization Quota

*This model accepts additional fields of type Any.*

## Structure

`OrganizationQuota`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `quota_code` | [`QuotaCode`](../../doc/models/quota-code.md) | Required | Stable identifier of the quota. Use it to request a single quota by code. |
| `name` | `str` | Required | Human-readable name of the quota. |
| `description` | `str` | Required | Explanation of the resource the quota limits and how the limit is applied. |
| `scope` | [`Scope`](../../doc/models/scope.md) | Required | Granularity at which the limit is applied. For example, `replicas-per-warehouse` is an organization-wide setting that limits each warehouse individually. |
| `value` | `int` | Required | Limit currently applied to the organization, including any adjustments made for the organization. The value can change when the billing status of the organization changes.<br><br>**Constraints**: `>= 0` |
| `usage` | `int` | Optional | Current consumption of the quota. Omitted for quotas that do not report usage. Usage can exceed `value` when a limit was lowered after resources were created; existing resources are not affected.<br><br>**Constraints**: `>= 0` |
| `adjustable` | `bool` | Required | Whether the limit can be raised for the organization by contacting ClickHouse support. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.organization_quota import OrganizationQuota
from openapispecforclickhousecloud.models.quota_code import QuotaCode
from openapispecforclickhousecloud.models.scope import Scope

organization_quota = OrganizationQuota(
    quota_code=QuotaCode.SERVICESPERORGANIZATION,
    name='Services per organization',
    description='description4',
    scope=Scope.ORGANIZATION,
    value=20,
    adjustable=False,
    usage=3,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

