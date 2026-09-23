
# Table Engine

ClickHouse table engine: "ReplacingMergeTree" (handles updates/deletes), "MergeTree" (append-only), or "Null" (forward data to materialized views without storing it).

## Enumeration

`TableEngine`

## Fields

| Name |
|  --- |
| `MERGETREE` |
| `REPLACINGMERGETREE` |
| `NULL` |

## Example

```python
from openapispecforclickhousecloud.models.table_engine import TableEngine

table_engine = TableEngine.REPLACINGMERGETREE
```

