
# Postgres Slow Query Pattern

*This model accepts additional fields of type Any.*

## Structure

`PostgresSlowQueryPattern`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query_id` | `str` | Required | Stable identifier for the query pattern (normalized SQL). |
| `query_text` | `str` | Required | Normalized query text with literals replaced by placeholders. |
| `db_name` | `str` | Required | Database the query ran in. |
| `db_user` | `str` | Required | Database user that executed the query. |
| `db_operation` | `str` | Required | Top-level SQL operation type (for example, SELECT, INSERT, UPDATE, DELETE, UTILITY). |
| `app` | `str` | Required | Value of the Postgres `application_name` for executions matching this pattern. |
| `call_count` | `int` | Required | Number of times the pattern executed in the window. |
| `error_count` | `int` | Required | Number of executions of the pattern that raised an error. |
| `total_duration_us` | `int` | Required | Total execution time across all calls, in microseconds. |
| `avg_duration_us` | `int` | Required | Average execution time per call, in microseconds. |
| `max_duration_us` | `int` | Required | Maximum execution time of any call, in microseconds. |
| `p_50_duration_us` | `int` | Required | 50th percentile execution time, in microseconds. |
| `p_95_duration_us` | `int` | Required | 95th percentile execution time, in microseconds. |
| `p_99_duration_us` | `int` | Required | 99th percentile execution time, in microseconds. |
| `total_rows` | `int` | Required | Total number of rows returned or affected across all calls. |
| `total_shared_blks_read` | `int` | Required | Total shared buffer blocks read from disk (cache misses) across all calls. |
| `total_shared_blks_hit` | `int` | Required | Total shared buffer blocks hit (cache hits) across all calls. |
| `total_cpu_time_us` | `int` | Required | Total CPU time across all calls, in microseconds. |
| `total_wal_bytes` | `int` | Required | Total WAL (write-ahead log) bytes generated across all calls. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.postgres_slow_query_pattern import PostgresSlowQueryPattern

postgres_slow_query_pattern = PostgresSlowQueryPattern(
    query_id='queryId6',
    query_text='queryText0',
    db_name='dbName8',
    db_user='dbUser2',
    db_operation='dbOperation2',
    app='app2',
    call_count=134,
    error_count=140,
    total_duration_us=192,
    avg_duration_us=238,
    max_duration_us=52,
    p_50_duration_us=188,
    p_95_duration_us=54,
    p_99_duration_us=128,
    total_rows=246,
    total_shared_blks_read=176,
    total_shared_blks_hit=226,
    total_cpu_time_us=224,
    total_wal_bytes=238,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

