
# V1 Organizations Quotas Response 1

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsQuotasResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`OrganizationQuota`](../../doc/models/organization-quota.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.organization_quota import OrganizationQuota
from openapispecforclickhousecloud.models.quota_code import QuotaCode
from openapispecforclickhousecloud.models.scope import Scope
from openapispecforclickhousecloud.models.v_1_organizations_quotas_response_1 import V1OrganizationsQuotasResponse1

v_1_organizations_quotas_response_1 = V1OrganizationsQuotasResponse1(
    status=200,
    request_id='00000d36-0000-0000-0000-000000000000',
    result=OrganizationQuota(
        quota_code=QuotaCode.SERVICESPERORGANIZATION,
        name='name6',
        description='description6',
        scope=Scope.ORGANIZATION,
        value=216,
        adjustable=False,
        usage=190,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

