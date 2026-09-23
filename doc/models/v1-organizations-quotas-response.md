
# V1 Organizations Quotas Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsQuotasResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`List[OrganizationQuota]`](../../doc/models/organization-quota.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.organization_quota import OrganizationQuota
from openapispecforclickhousecloud.models.quota_code import QuotaCode
from openapispecforclickhousecloud.models.scope import Scope
from openapispecforclickhousecloud.models.v_1_organizations_quotas_response import V1OrganizationsQuotasResponse

v_1_organizations_quotas_response = V1OrganizationsQuotasResponse(
    status=200,
    request_id='00001612-0000-0000-0000-000000000000',
    result=[
        OrganizationQuota(
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
        OrganizationQuota(
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
        OrganizationQuota(
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
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

