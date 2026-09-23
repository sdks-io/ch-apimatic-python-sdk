
# Pg Ha Type

Type of high availability: “none” for no replication, “async” for asynchronous replication to a single standby, and “sync” for synchronous replication to two standbys.

## Enumeration

`PgHaType`

## Fields

| Name |
|  --- |
| `NONE` |
| `ENUM_ASYNC` |
| `SYNC` |

## Example

```python
from openapispecforclickhousecloud.models.pg_ha_type import PgHaType

pg_ha_type = PgHaType.SYNC
```

