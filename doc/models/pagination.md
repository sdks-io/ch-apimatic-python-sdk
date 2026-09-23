
# Pagination

## Structure

`Pagination`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_records` | `int` | Required | Total number of records available. |
| `current_cursor` | str | Required | This is a container for any-of cases. |
| `next_cursor` | str | Required | This is a container for any-of cases. |
| `limit` | `int` | Required | Maximum number of records returned per page. |

## Example

```python
from openapispecforclickhousecloud.models.pagination import Pagination

pagination = Pagination(
    total_records=72,
    current_cursor='String5',
    next_cursor='String1',
    limit=80
)
```

