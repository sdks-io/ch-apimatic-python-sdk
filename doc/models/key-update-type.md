
# Key Update Type

For 'openapi_key_update' activities: the type of update that was performed.

## Enumeration

`KeyUpdateType`

## Fields

| Name |
|  --- |
| `CREATED` |
| `DELETED` |
| `NAMECHANGED` |
| `ROLECHANGED` |
| `STATECHANGED` |
| `DATECHANGED` |
| `IPACCESSLISTCHANGED` |
| `ORGROLECHANGED` |
| `DEFAULTSERVICEROLECHANGED` |
| `SERVICEROLECHANGED` |
| `ROLESV2CHANGED` |

## Example

```python
from openapispecforclickhousecloud.models.key_update_type import KeyUpdateType

key_update_type = KeyUpdateType.STATECHANGED
```

