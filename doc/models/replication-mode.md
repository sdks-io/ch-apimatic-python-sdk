
# Replication Mode

Replication mode: "cdc" (change data capture with initial snapshot), "snapshot" (one-time snapshot only), or "cdc_only" (CDC without initial snapshot).

## Enumeration

`ReplicationMode`

## Fields

| Name |
|  --- |
| `CDC` |
| `SNAPSHOT` |
| `CDC_ONLY` |

## Example

```python
from openapispecforclickhousecloud.models.replication_mode import ReplicationMode

replication_mode = ReplicationMode.CDC_ONLY
```

