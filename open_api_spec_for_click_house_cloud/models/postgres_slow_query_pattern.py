from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PostgresSlowQueryPattern(SdkBaseModel):
    query_id: str = Field(alias="queryId")
    """Stable identifier for the query pattern (normalized SQL)."""

    query_text: str = Field(alias="queryText")
    """Normalized query text with literals replaced by placeholders."""

    db_name: str = Field(alias="dbName")
    """Database the query ran in."""

    db_user: str = Field(alias="dbUser")
    """Database user that executed the query."""

    db_operation: str = Field(alias="dbOperation")
    """Top-level SQL operation type (for example, SELECT, INSERT, UPDATE, DELETE, UTILITY)."""

    app: str
    """Value of the Postgres ``application_name`` for executions matching this pattern."""

    call_count: int = Field(alias="callCount")
    """Number of times the pattern executed in the window."""

    error_count: int = Field(alias="errorCount")
    """Number of executions of the pattern that raised an error."""

    total_duration_us: int = Field(alias="totalDurationUs")
    """Total execution time across all calls, in microseconds."""

    avg_duration_us: int = Field(alias="avgDurationUs")
    """Average execution time per call, in microseconds."""

    max_duration_us: int = Field(alias="maxDurationUs")
    """Maximum execution time of any call, in microseconds."""

    p50_duration_us: int = Field(alias="p50DurationUs")
    """50th percentile execution time, in microseconds."""

    p95_duration_us: int = Field(alias="p95DurationUs")
    """95th percentile execution time, in microseconds."""

    p99_duration_us: int = Field(alias="p99DurationUs")
    """99th percentile execution time, in microseconds."""

    total_rows: int = Field(alias="totalRows")
    """Total number of rows returned or affected across all calls."""

    total_shared_blks_read: int = Field(alias="totalSharedBlksRead")
    """Total shared buffer blocks read from disk (cache misses) across all calls."""

    total_shared_blks_hit: int = Field(alias="totalSharedBlksHit")
    """Total shared buffer blocks hit (cache hits) across all calls."""

    total_cpu_time_us: int = Field(alias="totalCpuTimeUs")
    """Total CPU time across all calls, in microseconds."""

    total_wal_bytes: int = Field(alias="totalWalBytes")
    """Total WAL (write-ahead log) bytes generated across all calls."""


class PostgresSlowQueryPatternDict(TypedDict):
    query_id: str
    query_text: str
    db_name: str
    db_user: str
    db_operation: str
    app: str
    call_count: int
    error_count: int
    total_duration_us: int
    avg_duration_us: int
    max_duration_us: int
    p50_duration_us: int
    p95_duration_us: int
    p99_duration_us: int
    total_rows: int
    total_shared_blks_read: int
    total_shared_blks_hit: int
    total_cpu_time_us: int
    total_wal_bytes: int
