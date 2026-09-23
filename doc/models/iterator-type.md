
# Iterator Type

Type of iterator to use when reading from the Kinesis stream. If AT_TIMESTAMP is used, the timestamp field must be provided.

## Enumeration

`IteratorType`

## Fields

| Name |
|  --- |
| `TRIM_HORIZON` |
| `LATEST` |
| `AT_TIMESTAMP` |

## Example

```python
from openapispecforclickhousecloud.models.iterator_type import IteratorType

iterator_type = IteratorType.AT_TIMESTAMP
```

