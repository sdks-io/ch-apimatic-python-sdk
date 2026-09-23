
# Postgres Query Execution

*This model accepts additional fields of type Any.*

## Structure

`PostgresQueryExecution`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timestamp` | `datetime` | Required | Execution timestamp (RFC 3339). |
| `query_id` | `str` | Required | Stable identifier for the query pattern. |
| `db_name` | `str` | Required | Database the query ran in. |
| `db_user` | `str` | Required | Database user that executed the query. |
| `db_operation` | `str` | Required | Top-level SQL operation type. |
| `app` | `str` | Required | Value of the Postgres `application_name` for this execution. |
| `query_text` | `str` | Required | Normalized query text for this execution. |
| `pid` | `str` | Required | Postgres backend process ID that executed the query. |
| `duration_us` | `int` | Required | Execution duration in microseconds. |
| `rows` | `int` | Required | Rows returned or affected. |
| `shared_blks_hit` | `int` | Required | Shared buffer blocks hit. |
| `shared_blks_read` | `int` | Required | Shared buffer blocks read from disk. |
| `shared_blks_written` | `int` | Required | Shared buffer blocks written. |
| `shared_blks_dirtied` | `int` | Required | Shared buffer blocks dirtied. |
| `shared_blk_read_time_us` | `int` | Required | Time spent reading shared blocks, in microseconds. |
| `shared_blk_write_time_us` | `int` | Required | Time spent writing shared blocks, in microseconds. |
| `local_blks_hit` | `int` | Required | Local buffer blocks hit (temp tables). |
| `local_blks_read` | `int` | Required | Local buffer blocks read (temp tables). |
| `local_blks_written` | `int` | Required | Local buffer blocks written (temp tables). |
| `local_blks_dirtied` | `int` | Required | Local buffer blocks dirtied (temp tables). |
| `temp_blks_read` | `int` | Required | Temp blocks read (spills to disk). |
| `temp_blks_written` | `int` | Required | Temp blocks written (spills to disk). |
| `temp_blk_read_time_us` | `int` | Required | Time spent reading temp blocks, in microseconds. |
| `temp_blk_write_time_us` | `int` | Required | Time spent writing temp blocks, in microseconds. |
| `wal_records` | `int` | Required | Number of WAL records produced. |
| `wal_bytes` | `int` | Required | Number of WAL bytes produced. |
| `wal_fpi` | `int` | Required | Number of WAL full-page images produced. |
| `cpu_user_time_us` | `int` | Required | CPU time spent in user mode, in microseconds. |
| `cpu_sys_time_us` | `int` | Required | CPU time spent in kernel mode, in microseconds. |
| `jit_functions` | `int` | Required | Number of JIT-compiled functions. |
| `jit_generation_time_us` | `int` | Required | JIT generation time, in microseconds. |
| `jit_inlining_time_us` | `int` | Required | JIT inlining time, in microseconds. |
| `jit_optimization_time_us` | `int` | Required | JIT optimization time, in microseconds. |
| `jit_emission_time_us` | `int` | Required | JIT emission time, in microseconds. |
| `jit_deform_time_us` | `int` | Required | JIT deform time, in microseconds. |
| `parallel_workers_planned` | `int` | Required | Parallel workers planned for this execution. |
| `parallel_workers_launched` | `int` | Required | Parallel workers actually launched for this execution. |
| `err_message` | `str` | Optional | Error message if the execution raised an error. |
| `err_sqlstate` | `str` | Optional | Postgres SQLSTATE code if the execution raised an error. |
| `err_elevel` | `int` | Optional | Postgres error severity level if the execution raised an error. |
| `server_role` | `str` | Required | Role of the server that executed the query (for example, primary or standby). |
| `trace_id` | `str` | Optional | OpenTelemetry trace ID associated with the execution. |
| `span_id` | `str` | Optional | OpenTelemetry span ID associated with the execution. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from openapispecforclickhousecloud.models.postgres_query_execution import PostgresQueryExecution

postgres_query_execution = PostgresQueryExecution(
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    query_id='queryId2',
    db_name='dbName4',
    db_user='dbUser8',
    db_operation='dbOperation8',
    app='app6',
    query_text='queryText6',
    pid='pid8',
    duration_us=208,
    rows=234,
    shared_blks_hit=186,
    shared_blks_read=168,
    shared_blks_written=184,
    shared_blks_dirtied=116,
    shared_blk_read_time_us=192,
    shared_blk_write_time_us=152,
    local_blks_hit=166,
    local_blks_read=76,
    local_blks_written=2,
    local_blks_dirtied=142,
    temp_blks_read=82,
    temp_blks_written=140,
    temp_blk_read_time_us=200,
    temp_blk_write_time_us=78,
    wal_records=254,
    wal_bytes=220,
    wal_fpi=138,
    cpu_user_time_us=88,
    cpu_sys_time_us=170,
    jit_functions=124,
    jit_generation_time_us=76,
    jit_inlining_time_us=34,
    jit_optimization_time_us=132,
    jit_emission_time_us=148,
    jit_deform_time_us=10,
    parallel_workers_planned=58,
    parallel_workers_launched=138,
    server_role='serverRole4',
    err_message='errMessage2',
    err_sqlstate='errSqlstate4',
    err_elevel=74,
    trace_id='traceId8',
    span_id='spanId0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

