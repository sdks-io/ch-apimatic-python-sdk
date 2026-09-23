
# Issue

## Structure

`Issue`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `path` | List[str \| float] | Required | This is List of a container for any-of cases. |
| `code` | `str` | Required | Validation issue code. |
| `message` | `str` | Required | Human-readable description of the issue. |

## Example

```python
from openapispecforclickhousecloud.models.issue import Issue

issue = Issue(
    path=[
        'String1',
        'String2'
    ],
    code='code2',
    message='message4'
)
```

