from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.default_transaction_isolation import DefaultTransactionIsolationOrStr
from .enums.ssl_min_protocol_version import SslMinProtocolVersionOrStr
from .enums.wal_compression import WalCompressionOrStr
from .unions.autovacuum_analyze_scale_factor import AutovacuumAnalyzeScaleFactor, AutovacuumAnalyzeScaleFactorDict
from .unions.autovacuum_max_workers import AutovacuumMaxWorkers, AutovacuumMaxWorkersDict
from .unions.autovacuum_naptime import AutovacuumNaptime, AutovacuumNaptimeDict
from .unions.autovacuum_vacuum_cost_delay import AutovacuumVacuumCostDelay, AutovacuumVacuumCostDelayDict
from .unions.autovacuum_vacuum_cost_limit import AutovacuumVacuumCostLimit, AutovacuumVacuumCostLimitDict
from .unions.autovacuum_vacuum_insert_scale_factor import (
    AutovacuumVacuumInsertScaleFactor,
    AutovacuumVacuumInsertScaleFactorDict,
)
from .unions.autovacuum_vacuum_scale_factor import AutovacuumVacuumScaleFactor, AutovacuumVacuumScaleFactorDict
from .unions.autovacuum_work_mem import AutovacuumWorkMem, AutovacuumWorkMemDict
from .unions.effective_cache_size import EffectiveCacheSize, EffectiveCacheSizeDict
from .unions.effective_io_concurrency import EffectiveIoConcurrency, EffectiveIoConcurrencyDict
from .unions.idle_in_transaction_session_timeout import (
    IdleInTransactionSessionTimeout,
    IdleInTransactionSessionTimeoutDict,
)
from .unions.idle_session_timeout import IdleSessionTimeout, IdleSessionTimeoutDict
from .unions.lock_timeout import LockTimeout, LockTimeoutDict
from .unions.maintenance_work_mem import MaintenanceWorkMem, MaintenanceWorkMemDict
from .unions.max_connections import MaxConnections, MaxConnectionsDict
from .unions.max_parallel_maintenance_workers import MaxParallelMaintenanceWorkers, MaxParallelMaintenanceWorkersDict
from .unions.max_parallel_workers import MaxParallelWorkers, MaxParallelWorkersDict
from .unions.max_parallel_workers_per_gather import MaxParallelWorkersPerGather, MaxParallelWorkersPerGatherDict
from .unions.max_slot_wal_keep_size import MaxSlotWalKeepSize, MaxSlotWalKeepSizeDict
from .unions.max_wal_size import MaxWalSize, MaxWalSizeDict
from .unions.max_worker_processes import MaxWorkerProcesses, MaxWorkerProcessesDict
from .unions.min_wal_size import MinWalSize, MinWalSizeDict
from .unions.random_page_cost import RandomPageCost, RandomPageCostDict
from .unions.statement_timeout import StatementTimeout, StatementTimeoutDict
from .unions.transaction_timeout import TransactionTimeout, TransactionTimeoutDict
from .unions.wal_keep_size import WalKeepSize, WalKeepSizeDict
from .unions.wal_sender_timeout import WalSenderTimeout, WalSenderTimeoutDict
from .unions.work_mem import WorkMem, WorkMemDict


class PostgresConfiguration(SdkBaseModel):
    """Postgres `runtime configuration <https://www.postgresql.org/docs/current/runtime-config.html>`__
    configuration."""

    max_connections: Optional[MaxConnections] = UNSET
    """Sets the maximum number of concurrent connections to the database server."""

    default_transaction_isolation: Optional[DefaultTransactionIsolationOrStr] = UNSET
    """Sets the default transaction isolation level for new transactions."""

    ssl_min_protocol_version: Optional[SslMinProtocolVersionOrStr] = UNSET
    """Sets the minimum SSL/TLS protocol version allowed for client connections."""

    maintenance_work_mem: Optional[MaintenanceWorkMem] = UNSET
    """Sets the maximum memory to be used for maintenance operations."""

    work_mem: Optional[WorkMem] = UNSET
    """Sets the amount of memory Postgres will use for internal operations like sorting and hashing as part of executing
    a query."""

    effective_cache_size: Optional[EffectiveCacheSize] = UNSET
    """Sets the planner's assumption about the total size of data caches."""

    random_page_cost: Optional[RandomPageCost] = UNSET
    """Sets the planner's estimate of the cost of a non-sequentially-fetched disk page. Lower values (1.1-1.5) are
    better for SSDs."""

    effective_io_concurrency: Optional[EffectiveIoConcurrency] = UNSET
    """Number of concurrent disk I/O operations the planner expects. Higher values (100-200) benefit SSDs."""

    max_worker_processes: Optional[MaxWorkerProcesses] = UNSET
    """Maximum number of background processes the system can support. Includes parallel query workers, logical
    replication, and more."""

    max_parallel_workers: Optional[MaxParallelWorkers] = UNSET
    """Maximum number of workers that can be used for parallel operations. Cannot exceed max_worker_processes."""

    max_parallel_workers_per_gather: Optional[MaxParallelWorkersPerGather] = UNSET
    """Maximum number of parallel workers per executor node for parallel queries. Use 0 to disable parallel queries."""

    max_parallel_maintenance_workers: Optional[MaxParallelMaintenanceWorkers] = UNSET
    """Maximum number of parallel workers for maintenance operations like CREATE INDEX and VACUUM."""

    statement_timeout: Optional[StatementTimeout] = UNSET
    """Abort any statement that runs longer than the specified time. Use 0 to disable."""

    lock_timeout: Optional[LockTimeout] = UNSET
    """Abort any statement that waits longer than the specified time while attempting to acquire a lock. Use 0 to
    disable."""

    idle_session_timeout: Optional[IdleSessionTimeout] = UNSET
    """Terminate any session that has been idle for longer than the specified time. Use 0 to disable."""

    idle_in_transaction_session_timeout: Optional[IdleInTransactionSessionTimeout] = UNSET
    """Terminate any session that has been idle within an open transaction for longer than the specified time. Use 0 to
    disable."""

    transaction_timeout: Optional[TransactionTimeout] = UNSET
    """Terminate any statement that takes more than the specified time, even while active. Use 0 to disable."""

    wal_sender_timeout: Optional[WalSenderTimeout] = UNSET
    """Terminate replication connections that are inactive for longer than this time. Use 0 to disable."""

    wal_keep_size: Optional[WalKeepSize] = UNSET
    """Minimum size of past WAL files kept in pg_wal for standby servers. Use 0 to disable."""

    min_wal_size: Optional[MinWalSize] = UNSET
    """Minimum size to shrink the WAL to. WAL files are recycled rather than removed when below this size."""

    max_wal_size: Optional[MaxWalSize] = UNSET
    """Maximum size WAL can grow between checkpoints. Larger values improve write performance but increase crash
    recovery time."""

    max_slot_wal_keep_size: Optional[MaxSlotWalKeepSize] = UNSET
    """Specifies the maximum size of WAL files that replication slots are allowed to retain. Use -1 for unlimited."""

    wal_compression: Optional[WalCompressionOrStr] = UNSET
    """Compress full-page writes in WAL. Reduces I/O at the cost of CPU. Options vary by PostgreSQL version."""

    autovacuum_max_workers: Optional[AutovacuumMaxWorkers] = UNSET
    """Maximum number of autovacuum worker processes that can run at the same time. Workers share a single cost-limit
    budget, so raising this alone may not speed up vacuuming."""

    autovacuum_naptime: Optional[AutovacuumNaptime] = UNSET
    """Minimum delay between autovacuum runs. Lower values make autovacuum check for work more frequently."""

    autovacuum_work_mem: Optional[AutovacuumWorkMem] = UNSET
    """Maximum memory each autovacuum worker uses to track dead tuples. Higher values reduce repeated index-vacuum
    passes on large tables. Use -1 to fall back to maintenance_work_mem."""

    autovacuum_vacuum_scale_factor: Optional[AutovacuumVacuumScaleFactor] = UNSET
    """Fraction of a table's rows that must change before autovacuum runs. Lower values vacuum large tables more
    frequently."""

    autovacuum_analyze_scale_factor: Optional[AutovacuumAnalyzeScaleFactor] = UNSET
    """Fraction of a table's rows that must change before autovacuum runs ANALYZE to refresh planner statistics."""

    autovacuum_vacuum_insert_scale_factor: Optional[AutovacuumVacuumInsertScaleFactor] = UNSET
    """Fraction of a table's rows that must be inserted before autovacuum runs. Helps vacuum insert-heavy,
    rarely-updated tables."""

    autovacuum_vacuum_cost_limit: Optional[AutovacuumVacuumCostLimit] = UNSET
    """Cost-accounting limit shared across all autovacuum workers before they pause. Use -1 to inherit
    vacuum_cost_limit."""

    autovacuum_vacuum_cost_delay: Optional[AutovacuumVacuumCostDelay] = UNSET
    """Time autovacuum sleeps when the cost limit is reached. Lower values speed up vacuuming at the cost of more
    I/O."""


class PostgresConfigurationDict(TypedDict):
    max_connections: NotRequired[MaxConnectionsDict]
    default_transaction_isolation: NotRequired[DefaultTransactionIsolationOrStr]
    ssl_min_protocol_version: NotRequired[SslMinProtocolVersionOrStr]
    maintenance_work_mem: NotRequired[MaintenanceWorkMemDict]
    work_mem: NotRequired[WorkMemDict]
    effective_cache_size: NotRequired[EffectiveCacheSizeDict]
    random_page_cost: NotRequired[RandomPageCostDict]
    effective_io_concurrency: NotRequired[EffectiveIoConcurrencyDict]
    max_worker_processes: NotRequired[MaxWorkerProcessesDict]
    max_parallel_workers: NotRequired[MaxParallelWorkersDict]
    max_parallel_workers_per_gather: NotRequired[MaxParallelWorkersPerGatherDict]
    max_parallel_maintenance_workers: NotRequired[MaxParallelMaintenanceWorkersDict]
    statement_timeout: NotRequired[StatementTimeoutDict]
    lock_timeout: NotRequired[LockTimeoutDict]
    idle_session_timeout: NotRequired[IdleSessionTimeoutDict]
    idle_in_transaction_session_timeout: NotRequired[IdleInTransactionSessionTimeoutDict]
    transaction_timeout: NotRequired[TransactionTimeoutDict]
    wal_sender_timeout: NotRequired[WalSenderTimeoutDict]
    wal_keep_size: NotRequired[WalKeepSizeDict]
    min_wal_size: NotRequired[MinWalSizeDict]
    max_wal_size: NotRequired[MaxWalSizeDict]
    max_slot_wal_keep_size: NotRequired[MaxSlotWalKeepSizeDict]
    wal_compression: NotRequired[WalCompressionOrStr]
    autovacuum_max_workers: NotRequired[AutovacuumMaxWorkersDict]
    autovacuum_naptime: NotRequired[AutovacuumNaptimeDict]
    autovacuum_work_mem: NotRequired[AutovacuumWorkMemDict]
    autovacuum_vacuum_scale_factor: NotRequired[AutovacuumVacuumScaleFactorDict]
    autovacuum_analyze_scale_factor: NotRequired[AutovacuumAnalyzeScaleFactorDict]
    autovacuum_vacuum_insert_scale_factor: NotRequired[AutovacuumVacuumInsertScaleFactorDict]
    autovacuum_vacuum_cost_limit: NotRequired[AutovacuumVacuumCostLimitDict]
    autovacuum_vacuum_cost_delay: NotRequired[AutovacuumVacuumCostDelayDict]
