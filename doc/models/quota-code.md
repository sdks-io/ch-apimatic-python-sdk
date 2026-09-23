
# Quota Code

Stable identifier of the quota. Use it to request a single quota by code.

## Enumeration

`QuotaCode`

## Fields

| Name |
|  --- |
| `SERVICESPERORGANIZATION` |
| `POSTGRESSERVICESPERORGANIZATION` |
| `REPLICASPERWAREHOUSE` |
| `APIKEYSPERORGANIZATION` |

## Example

```python
from openapispecforclickhousecloud.models.quota_code import QuotaCode

quota_code = QuotaCode.REPLICASPERWAREHOUSE
```

