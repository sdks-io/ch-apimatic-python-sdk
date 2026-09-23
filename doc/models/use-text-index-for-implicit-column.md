
# Use Text Index for Implicit Column

Controls whether lucene rendering uses ClickHouse text indices via hasAllTokens() against the implicit column. "auto" detects a covering index at query time, "enabled" forces text index usage, "disabled" forces a LIKE/hasToken fallback.

## Enumeration

`UseTextIndexForImplicitColumn`

## Fields

| Name |
|  --- |
| `AUTO` |
| `ENABLED` |
| `DISABLED` |

## Example

```python
from openapispecforclickhousecloud.models.use_text_index_for_implicit_column import UseTextIndexForImplicitColumn

use_text_index_for_implicit_column = UseTextIndexForImplicitColumn.DISABLED
```

