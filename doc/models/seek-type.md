
# Seek Type

Starting position strategy for consuming the subscription. The seekTimestamp companion is required only when seekType is "timestamp"; setting it for a mismatched seek type is rejected.

## Enumeration

`SeekType`

## Fields

| Name |
|  --- |
| `LATEST` |
| `EARLIEST` |
| `TIMESTAMP` |

## Example

```python
from openapispecforclickhousecloud.models.seek_type import SeekType

seek_type = SeekType.EARLIEST
```

