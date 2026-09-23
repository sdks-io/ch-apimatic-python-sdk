
# V1 Organizations Postgres Slow Query Patterns Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsPostgresSlowQueryPatternsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`List[PostgresSlowQueryPattern]`](../../doc/models/postgres-slow-query-pattern.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.postgres_slow_query_pattern import PostgresSlowQueryPattern
from openapispecforclickhousecloud.models.v_1_organizations_postgres_slow_query_patterns_response import V1OrganizationsPostgresSlowQueryPatternsResponse

v_1_organizations_postgres_slow_query_patterns_response = V1OrganizationsPostgresSlowQueryPatternsResponse(
    status=200,
    request_id='00002186-0000-0000-0000-000000000000',
    result=[
        PostgresSlowQueryPattern(
            query_id='queryId2',
            query_text='queryText6',
            db_name='dbName4',
            db_user='dbUser8',
            db_operation='dbOperation8',
            app='app6',
            call_count=50,
            error_count=56,
            total_duration_us=236,
            avg_duration_us=154,
            max_duration_us=120,
            p_50_duration_us=104,
            p_95_duration_us=226,
            p_99_duration_us=44,
            total_rows=162,
            total_shared_blks_read=4,
            total_shared_blks_hit=142,
            total_cpu_time_us=140,
            total_wal_bytes=154,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        PostgresSlowQueryPattern(
            query_id='queryId2',
            query_text='queryText6',
            db_name='dbName4',
            db_user='dbUser8',
            db_operation='dbOperation8',
            app='app6',
            call_count=50,
            error_count=56,
            total_duration_us=236,
            avg_duration_us=154,
            max_duration_us=120,
            p_50_duration_us=104,
            p_95_duration_us=226,
            p_99_duration_us=44,
            total_rows=162,
            total_shared_blks_read=4,
            total_shared_blks_hit=142,
            total_cpu_time_us=140,
            total_wal_bytes=154,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        PostgresSlowQueryPattern(
            query_id='queryId2',
            query_text='queryText6',
            db_name='dbName4',
            db_user='dbUser8',
            db_operation='dbOperation8',
            app='app6',
            call_count=50,
            error_count=56,
            total_duration_us=236,
            avg_duration_us=154,
            max_duration_us=120,
            p_50_duration_us=104,
            p_95_duration_us=226,
            p_99_duration_us=44,
            total_rows=162,
            total_shared_blks_read=4,
            total_shared_blks_hit=142,
            total_cpu_time_us=140,
            total_wal_bytes=154,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

