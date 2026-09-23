from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class PostgresQueryExecution(SdkBaseModel):
    timestamp: RFC3339DateTime
    """Execution timestamp (RFC 3339)."""

    query_id: str = Field(alias="queryId")
    """Stable identifier for the query pattern."""

    db_name: str = Field(alias="dbName")
    """Database the query ran in."""

    db_user: str = Field(alias="dbUser")
    """Database user that executed the query."""

    db_operation: str = Field(alias="dbOperation")
    """Top-level SQL operation type."""

    app: str
    """Value of the Postgres ``application_name`` for this execution."""

    query_text: str = Field(alias="queryText")
    """Normalized query text for this execution."""

    pid: str
    """Postgres backend process ID that executed the query."""

    duration_us: int = Field(alias="durationUs")
    """Execution duration in microseconds."""

    rows: int
    """Rows returned or affected."""

    shared_blks_hit: int = Field(alias="sharedBlksHit")
    """Shared buffer blocks hit."""

    shared_blks_read: int = Field(alias="sharedBlksRead")
    """Shared buffer blocks read from disk."""

    shared_blks_written: int = Field(alias="sharedBlksWritten")
    """Shared buffer blocks written."""

    shared_blks_dirtied: int = Field(alias="sharedBlksDirtied")
    """Shared buffer blocks dirtied."""

    shared_blk_read_time_us: int = Field(alias="sharedBlkReadTimeUs")
    """Time spent reading shared blocks, in microseconds."""

    shared_blk_write_time_us: int = Field(alias="sharedBlkWriteTimeUs")
    """Time spent writing shared blocks, in microseconds."""

    local_blks_hit: int = Field(alias="localBlksHit")
    """Local buffer blocks hit (temp tables)."""

    local_blks_read: int = Field(alias="localBlksRead")
    """Local buffer blocks read (temp tables)."""

    local_blks_written: int = Field(alias="localBlksWritten")
    """Local buffer blocks written (temp tables)."""

    local_blks_dirtied: int = Field(alias="localBlksDirtied")
    """Local buffer blocks dirtied (temp tables)."""

    temp_blks_read: int = Field(alias="tempBlksRead")
    """Temp blocks read (spills to disk)."""

    temp_blks_written: int = Field(alias="tempBlksWritten")
    """Temp blocks written (spills to disk)."""

    temp_blk_read_time_us: int = Field(alias="tempBlkReadTimeUs")
    """Time spent reading temp blocks, in microseconds."""

    temp_blk_write_time_us: int = Field(alias="tempBlkWriteTimeUs")
    """Time spent writing temp blocks, in microseconds."""

    wal_records: int = Field(alias="walRecords")
    """Number of WAL records produced."""

    wal_bytes: int = Field(alias="walBytes")
    """Number of WAL bytes produced."""

    wal_fpi: int = Field(alias="walFpi")
    """Number of WAL full-page images produced."""

    cpu_user_time_us: int = Field(alias="cpuUserTimeUs")
    """CPU time spent in user mode, in microseconds."""

    cpu_sys_time_us: int = Field(alias="cpuSysTimeUs")
    """CPU time spent in kernel mode, in microseconds."""

    jit_functions: int = Field(alias="jitFunctions")
    """Number of JIT-compiled functions."""

    jit_generation_time_us: int = Field(alias="jitGenerationTimeUs")
    """JIT generation time, in microseconds."""

    jit_inlining_time_us: int = Field(alias="jitInliningTimeUs")
    """JIT inlining time, in microseconds."""

    jit_optimization_time_us: int = Field(alias="jitOptimizationTimeUs")
    """JIT optimization time, in microseconds."""

    jit_emission_time_us: int = Field(alias="jitEmissionTimeUs")
    """JIT emission time, in microseconds."""

    jit_deform_time_us: int = Field(alias="jitDeformTimeUs")
    """JIT deform time, in microseconds."""

    parallel_workers_planned: int = Field(alias="parallelWorkersPlanned")
    """Parallel workers planned for this execution."""

    parallel_workers_launched: int = Field(alias="parallelWorkersLaunched")
    """Parallel workers actually launched for this execution."""

    err_message: Optional[str] = Field(default=UNSET, alias="errMessage")
    """Error message if the execution raised an error."""

    err_sqlstate: Optional[str] = Field(default=UNSET, alias="errSqlstate")
    """Postgres SQLSTATE code if the execution raised an error."""

    err_elevel: Optional[int] = Field(default=UNSET, alias="errElevel")
    """Postgres error severity level if the execution raised an error."""

    server_role: str = Field(alias="serverRole")
    """Role of the server that executed the query (for example, primary or standby)."""

    trace_id: Optional[str] = Field(default=UNSET, alias="traceId")
    """OpenTelemetry trace ID associated with the execution."""

    span_id: Optional[str] = Field(default=UNSET, alias="spanId")
    """OpenTelemetry span ID associated with the execution."""


class PostgresQueryExecutionDict(TypedDict):
    timestamp: RFC3339DateTime
    query_id: str
    db_name: str
    db_user: str
    db_operation: str
    app: str
    query_text: str
    pid: str
    duration_us: int
    rows: int
    shared_blks_hit: int
    shared_blks_read: int
    shared_blks_written: int
    shared_blks_dirtied: int
    shared_blk_read_time_us: int
    shared_blk_write_time_us: int
    local_blks_hit: int
    local_blks_read: int
    local_blks_written: int
    local_blks_dirtied: int
    temp_blks_read: int
    temp_blks_written: int
    temp_blk_read_time_us: int
    temp_blk_write_time_us: int
    wal_records: int
    wal_bytes: int
    wal_fpi: int
    cpu_user_time_us: int
    cpu_sys_time_us: int
    jit_functions: int
    jit_generation_time_us: int
    jit_inlining_time_us: int
    jit_optimization_time_us: int
    jit_emission_time_us: int
    jit_deform_time_us: int
    parallel_workers_planned: int
    parallel_workers_launched: int
    err_message: NotRequired[str]
    err_sqlstate: NotRequired[str]
    err_elevel: NotRequired[int]
    server_role: str
    trace_id: NotRequired[str]
    span_id: NotRequired[str]
