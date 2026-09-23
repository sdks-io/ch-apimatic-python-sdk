
# Postgres Log Entry

*This model accepts additional fields of type Any.*

## Structure

`PostgresLogEntry`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timestamp` | `datetime` | Required | Time the entry was logged (RFC 3339). |
| `severity` | `str` | Required | PostgreSQL severity of the entry (for example, LOG, WARNING, ERROR, FATAL, PANIC). |
| `body` | `str` | Required | Raw log entry body as emitted by PostgreSQL. Structured bodies are returned as a JSON-encoded string. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.postgres_log_entry import PostgresLogEntry

postgres_log_entry = PostgresLogEntry(
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    severity='severity4',
    body='body2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

