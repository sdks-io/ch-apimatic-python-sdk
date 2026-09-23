from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class SortBy(str, Enum):
    TOTAL_DURATION = "total_duration"
    AVG_DURATION = "avg_duration"
    CALL_COUNT = "call_count"
    TOTAL_BLKS_READ = "total_blks_read"
    TOTAL_CPU_TIME = "total_cpu_time"
    ERROR_COUNT = "error_count"
    MAX_DURATION = "max_duration"
    P50_DURATION = "p50_duration"
    P95_DURATION = "p95_duration"
    P99_DURATION = "p99_duration"
    TOTAL_ROWS = "total_rows"
    TOTAL_SHARED_BLKS_HIT = "total_shared_blks_hit"
    TOTAL_WAL_BYTES = "total_wal_bytes"

    __str__ = str.__str__


SortByOrStr: TypeAlias = Annotated[SortBy | str, open_enum_validator(SortBy)]
