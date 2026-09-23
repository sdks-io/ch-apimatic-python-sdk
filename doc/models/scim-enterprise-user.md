
# Scim Enterprise User

*This model accepts additional fields of type Any.*

## Structure

`ScimEnterpriseUser`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `employee_number` | `str` | Optional | Numeric or alphanumeric identifier assigned to a person, typically based on order of hire or association with an organization. |
| `cost_center` | `str` | Optional | Identifies the name of a cost center. |
| `organization` | `str` | Optional | Identifies the name of an organization. |
| `division` | `str` | Optional | Identifies the name of a division. |
| `department` | `str` | Optional | Identifies the name of a department. |
| `manager` | [`ScimEnterpriseManager`](../../doc/models/scim-enterprise-manager.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.scim_enterprise_user import ScimEnterpriseUser

scim_enterprise_user = ScimEnterpriseUser(
    employee_number='employeeNumber8',
    cost_center='costCenter6',
    organization='organization0',
    division='division4',
    department='department4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

