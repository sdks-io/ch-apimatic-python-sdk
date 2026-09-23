
# Read Preference

MongoDB read preference for replica set reads.

## Enumeration

`ReadPreference`

## Fields

| Name |
|  --- |
| `PRIMARY` |
| `PRIMARYPREFERRED` |
| `SECONDARY` |
| `SECONDARYPREFERRED` |
| `NEAREST` |

## Example

```python
from openapispecforclickhousecloud.models.read_preference import ReadPreference

read_preference = ReadPreference.SECONDARYPREFERRED
```

