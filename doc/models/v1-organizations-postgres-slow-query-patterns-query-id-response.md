
# V1 Organizations Postgres Slow Query Patterns Query Id Response

*This model accepts additional fields of type Any.*

## Structure

`V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `float` | Optional | HTTP status code. |
| `request_id` | `uuid\|str` | Optional | Unique id assigned to every request. UUIDv4 |
| `result` | [`PostgresSlowQueryPatternDetail`](../../doc/models/postgres-slow-query-pattern-detail.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.postgres_query_execution import PostgresQueryExecution
from openapispecforclickhousecloud.models.postgres_slow_query_pattern import PostgresSlowQueryPattern
from openapispecforclickhousecloud.models.postgres_slow_query_pattern_detail import PostgresSlowQueryPatternDetail
from openapispecforclickhousecloud.models.v_1_organizations_postgres_slow_query_patterns_query_id_response import V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse

v_1_organizations_postgres_slow_query_patterns_query_id_response = V1OrganizationsPostgresSlowQueryPatternsQueryIdResponse(
    status=200,
    request_id='00001098-0000-0000-0000-000000000000',
    result=PostgresSlowQueryPatternDetail(
        recent_executions=[
            PostgresQueryExecution(
                timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                query_id='queryId0',
                db_name='dbName2',
                db_user='dbUser6',
                db_operation='dbOperation6',
                app='app8',
                query_text='queryText4',
                pid='pid6',
                duration_us=80,
                rows=106,
                shared_blks_hit=58,
                shared_blks_read=40,
                shared_blks_written=56,
                shared_blks_dirtied=244,
                shared_blk_read_time_us=64,
                shared_blk_write_time_us=24,
                local_blks_hit=38,
                local_blks_read=204,
                local_blks_written=130,
                local_blks_dirtied=14,
                temp_blks_read=210,
                temp_blks_written=12,
                temp_blk_read_time_us=72,
                temp_blk_write_time_us=206,
                wal_records=126,
                wal_bytes=92,
                wal_fpi=10,
                cpu_user_time_us=216,
                cpu_sys_time_us=42,
                jit_functions=252,
                jit_generation_time_us=204,
                jit_inlining_time_us=162,
                jit_optimization_time_us=4,
                jit_emission_time_us=20,
                jit_deform_time_us=138,
                parallel_workers_planned=186,
                parallel_workers_launched=10,
                server_role='serverRole6',
                err_message='errMessage0',
                err_sqlstate='errSqlstate6',
                err_elevel=202,
                trace_id='traceId6',
                span_id='spanId8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            PostgresQueryExecution(
                timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                query_id='queryId0',
                db_name='dbName2',
                db_user='dbUser6',
                db_operation='dbOperation6',
                app='app8',
                query_text='queryText4',
                pid='pid6',
                duration_us=80,
                rows=106,
                shared_blks_hit=58,
                shared_blks_read=40,
                shared_blks_written=56,
                shared_blks_dirtied=244,
                shared_blk_read_time_us=64,
                shared_blk_write_time_us=24,
                local_blks_hit=38,
                local_blks_read=204,
                local_blks_written=130,
                local_blks_dirtied=14,
                temp_blks_read=210,
                temp_blks_written=12,
                temp_blk_read_time_us=72,
                temp_blk_write_time_us=206,
                wal_records=126,
                wal_bytes=92,
                wal_fpi=10,
                cpu_user_time_us=216,
                cpu_sys_time_us=42,
                jit_functions=252,
                jit_generation_time_us=204,
                jit_inlining_time_us=162,
                jit_optimization_time_us=4,
                jit_emission_time_us=20,
                jit_deform_time_us=138,
                parallel_workers_planned=186,
                parallel_workers_launched=10,
                server_role='serverRole6',
                err_message='errMessage0',
                err_sqlstate='errSqlstate6',
                err_elevel=202,
                trace_id='traceId6',
                span_id='spanId8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        aggregate=PostgresSlowQueryPattern(
            query_id='queryId8',
            query_text='queryText2',
            db_name='dbName0',
            db_user='dbUser4',
            db_operation='dbOperation4',
            app='app0',
            call_count=40,
            error_count=46,
            total_duration_us=226,
            avg_duration_us=144,
            max_duration_us=146,
            p_50_duration_us=94,
            p_95_duration_us=216,
            p_99_duration_us=34,
            total_rows=152,
            total_shared_blks_read=14,
            total_shared_blks_hit=132,
            total_cpu_time_us=130,
            total_wal_bytes=144,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

